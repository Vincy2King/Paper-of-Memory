#!/usr/bin/env python3
"""Fetch memory-related papers from multiple sources and build a Markdown tracker."""

from __future__ import annotations

import argparse
import datetime as dt
import email.utils
import gzip
import hashlib
import json
import re
import textwrap
import unicodedata
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Iterable


ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}
MODS_NS = {"mods": "http://www.loc.gov/mods/v3"}
ARXIV_API = "https://export.arxiv.org/api/query"
OPENREVIEW_SEARCH_API = "https://api2.openreview.net/notes/search"
MANUAL_NOTES_START = "<!-- MANUAL_NOTES_START -->"
MANUAL_NOTES_END = "<!-- MANUAL_NOTES_END -->"
DEFAULT_MANUAL_NOTES = "在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Update the memory paper tracker from remote sources and local manual entries."
    )
    parser.add_argument(
        "--config",
        default="config/topics.json",
        help="Path to the topic configuration JSON file.",
    )
    parser.add_argument(
        "--data",
        default="data/papers.json",
        help="Path to the paper metadata JSON file.",
    )
    parser.add_argument(
        "--manual",
        default="data/manual_entries.json",
        help="Path to manually curated papers JSON file.",
    )
    parser.add_argument(
        "--content-dir",
        default="content/papers",
        help="Directory where per-paper Markdown pages are written.",
    )
    parser.add_argument(
        "--readme",
        default="README.md",
        help="Path to the generated repository README file.",
    )
    parser.add_argument(
        "--build-only",
        action="store_true",
        help="Skip remote fetching and only rebuild Markdown pages and README.",
    )
    return parser.parse_args()


def read_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def split_sentences(text: str) -> list[str]:
    cleaned = normalize_space(text)
    if not cleaned:
        return []
    pieces = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'])", cleaned)
    return [piece.strip() for piece in pieces if piece.strip()]


def short_text(text: str, limit: int = 220) -> str:
    text = normalize_space(text)
    if len(text) <= limit:
        return text
    return textwrap.shorten(text, width=limit, placeholder="...")


def slugify(value: str, fallback: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_value.lower()).strip("-")
    if slug:
        return slug[:80]
    digest = hashlib.sha1(fallback.encode("utf-8")).hexdigest()[:12]
    return f"paper-{digest}"


def safe_date(date_text: str | None) -> str:
    if not date_text:
        return ""
    return date_text[:10]


def ms_to_date(value: Any) -> str:
    if value in (None, ""):
        return ""
    try:
        timestamp = int(value) / 1000.0
    except (TypeError, ValueError):
        return ""
    return dt.datetime.utcfromtimestamp(timestamp).date().isoformat()


def parse_rfc2822_date(value: str) -> str:
    if not value:
        return ""
    try:
        parsed = email.utils.parsedate_to_datetime(value)
    except (TypeError, ValueError, IndexError):
        return ""
    return parsed.date().isoformat()


def days_ago(date_text: str) -> int | None:
    if not date_text:
        return None
    try:
        paper_date = dt.date.fromisoformat(date_text[:10])
    except ValueError:
        return None
    return (dt.date.today() - paper_date).days


def contains_memory_signal(text: str, keywords: Iterable[str]) -> list[str]:
    lowered = normalize_space(text).lower()
    hits = []
    for keyword in keywords:
        if keyword.lower() in lowered:
            hits.append(keyword)
    return hits


def json_request(url: str, *, payload: dict | None = None, headers: dict | None = None):
    request_headers = {"User-Agent": "memory-paper-tracker/0.2"}
    if headers:
        request_headers.update(headers)
    data = None
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        request_headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=request_headers)
    with urllib.request.urlopen(request, timeout=45) as response:
        return json.loads(response.read().decode("utf-8"))


def text_request(url: str, *, headers: dict | None = None) -> str:
    request_headers = {"User-Agent": "memory-paper-tracker/0.2"}
    if headers:
        request_headers.update(headers)
    request = urllib.request.Request(url, headers=request_headers)
    with urllib.request.urlopen(request, timeout=45) as response:
        raw = response.read()
        encoding = response.headers.get_content_charset() or "utf-8"
        return raw.decode(encoding, errors="replace")


def bytes_request(url: str, *, headers: dict | None = None) -> bytes:
    request_headers = {"User-Agent": "memory-paper-tracker/0.2"}
    if headers:
        request_headers.update(headers)
    request = urllib.request.Request(url, headers=request_headers)
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.read()


def extract_arxiv_id(entry_id: str) -> str:
    return entry_id.rsplit("/", maxsplit=1)[-1]


def build_search_query(keyword: str, categories: list[str]) -> str:
    quoted = f'all:"{keyword}"'
    if not categories:
        return quoted
    category_part = " OR ".join(f"cat:{category}" for category in categories)
    return f"({quoted}) AND ({category_part})"


def fetch_arxiv_for_keyword(keyword: str, categories: list[str], max_results: int) -> list[dict]:
    query = build_search_query(keyword, categories)
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "memory-paper-tracker/0.2 (GitHub Actions updater)"},
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        raw = response.read()
    root = ET.fromstring(raw)
    records = []
    for entry in root.findall("atom:entry", ATOM_NS):
        title = normalize_space(entry.findtext("atom:title", default="", namespaces=ATOM_NS))
        summary = normalize_space(
            entry.findtext("atom:summary", default="", namespaces=ATOM_NS)
        )
        entry_id = normalize_space(entry.findtext("atom:id", default="", namespaces=ATOM_NS))
        authors = [
            normalize_space(author.findtext("atom:name", default="", namespaces=ATOM_NS))
            for author in entry.findall("atom:author", ATOM_NS)
        ]
        published = safe_date(
            entry.findtext("atom:published", default="", namespaces=ATOM_NS)
        )
        updated = safe_date(entry.findtext("atom:updated", default="", namespaces=ATOM_NS))
        categories_found = [
            category.attrib.get("term", "")
            for category in entry.findall("atom:category", ATOM_NS)
            if category.attrib.get("term")
        ]
        records.append(
            {
                "id": extract_arxiv_id(entry_id),
                "source": "arXiv",
                "source_key": entry_id,
                "title": title,
                "authors": authors,
                "url": entry_id,
                "published": published,
                "updated": updated,
                "abstract": summary,
                "matched_keywords": [keyword],
                "categories": categories_found,
                "venue": "",
            }
        )
    return records


def fetch_arxiv_records(config: dict) -> list[dict]:
    source_config = config.get("sources", {}).get("arxiv", {})
    if source_config is not None and not source_config.get("enabled", True):
        return []

    categories = source_config.get("categories", config.get("categories", []))
    max_results = source_config.get(
        "max_results_per_keyword", config.get("max_results_per_keyword", 25)
    )
    lookback_days = source_config.get("lookback_days", config.get("lookback_days", 7))

    collected: dict[str, dict] = {}
    for keyword in config.get("keywords", []):
        try:
            records = fetch_arxiv_for_keyword(
                keyword=keyword,
                categories=categories,
                max_results=max_results,
            )
        except Exception as exc:  # pragma: no cover - network path
            print(f"[warn] failed to fetch arXiv keyword '{keyword}': {exc}")
            continue

        for record in records:
            age = days_ago(record.get("updated") or record.get("published") or "")
            if age is not None and age > lookback_days:
                continue
            current = collected.get(record["id"])
            if current:
                current["matched_keywords"] = sorted(
                    set(current.get("matched_keywords", []))
                    | set(record.get("matched_keywords", []))
                )
                continue
            collected[record["id"]] = record
    return list(collected.values())


def get_openreview_content_value(note: dict, *field_names: str) -> Any:
    content = note.get("content", {})
    for field_name in field_names:
        if field_name not in content:
            continue
        value = content[field_name]
        if isinstance(value, dict) and "value" in value:
            return value["value"]
        return value
    return ""


def normalize_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [normalize_space(str(item)) for item in value if normalize_space(str(item))]
    text = normalize_space(str(value))
    return [text] if text else []


def search_openreview_for_keyword(
    keyword: str,
    *,
    group: str | None,
    limit: int,
) -> list[dict]:
    payload = {
        "query": keyword,
        "sort": "tmdate:desc",
        "limit": limit,
        "source": "forum",
    }
    if group:
        payload["group"] = group
    response = json_request(OPENREVIEW_SEARCH_API, payload=payload)
    return response.get("notes", [])


def note_is_top_level_forum(note: dict) -> bool:
    note_id = note.get("id", "")
    forum = note.get("forum", "")
    replyto = note.get("replyto")
    if replyto:
        return False
    if forum and note_id and forum != note_id:
        return False
    return True


def parse_openreview_note(note: dict, keyword: str) -> dict:
    title = normalize_space(str(get_openreview_content_value(note, "title")))
    abstract = normalize_space(str(get_openreview_content_value(note, "abstract")))
    authors = normalize_list(get_openreview_content_value(note, "authors"))
    venue = normalize_space(
        str(get_openreview_content_value(note, "venue", "venueid", "venue_id"))
    )
    note_id = note.get("id", "")
    published = (
        ms_to_date(note.get("pdate"))
        or ms_to_date(note.get("odate"))
        or ms_to_date(note.get("cdate"))
        or ms_to_date(note.get("tcdate"))
    )
    updated = ms_to_date(note.get("tmdate")) or ms_to_date(note.get("mdate")) or published
    invitation = ""
    invitations = note.get("invitations", [])
    if invitations:
        invitation = invitations[0]

    return {
        "id": f"openreview:{note_id}",
        "source": "OpenReview",
        "source_key": note_id,
        "title": title,
        "authors": authors,
        "url": f"https://openreview.net/forum?id={note_id}" if note_id else "",
        "published": published,
        "updated": updated,
        "abstract": abstract,
        "matched_keywords": [keyword],
        "categories": [invitation] if invitation else [],
        "venue": venue,
    }


def fetch_openreview_records(config: dict) -> list[dict]:
    source_config = config.get("sources", {}).get("openreview", {})
    if source_config is not None and not source_config.get("enabled", True):
        return []

    lookback_days = source_config.get("lookback_days", config.get("lookback_days", 7))
    max_results = source_config.get("max_results_per_keyword", 30)
    groups = source_config.get("group_ids", [])
    search_groups = groups if groups else [None]
    keywords = config.get("keywords", [])

    collected: dict[str, dict] = {}
    for keyword in config.get("keywords", []):
        for group in search_groups:
            try:
                notes = search_openreview_for_keyword(keyword, group=group, limit=max_results)
            except Exception as exc:  # pragma: no cover - network path
                scope = group or "global"
                print(f"[warn] failed to fetch OpenReview keyword '{keyword}' in {scope}: {exc}")
                continue

            for note in notes:
                if not note_is_top_level_forum(note):
                    continue
                record = parse_openreview_note(note, keyword)
                if not record["title"]:
                    continue
                actual_hits = contains_memory_signal(
                    f"{record.get('title', '')} {record.get('abstract', '')}",
                    keywords,
                )
                if not actual_hits:
                    continue
                record["matched_keywords"] = actual_hits
                age = days_ago(record.get("updated") or record.get("published") or "")
                if age is not None and age > lookback_days:
                    continue
                current = collected.get(record["id"])
                if current:
                    current["matched_keywords"] = sorted(
                        set(current.get("matched_keywords", []))
                        | set(record.get("matched_keywords", []))
                    )
                    continue
                collected[record["id"]] = record
    return list(collected.values())


def parse_acl_rss_items(feed_xml: str) -> list[dict]:
    root = ET.fromstring(feed_xml)
    channel = root.find("channel")
    if channel is None:
        return []

    items = []
    for item in channel.findall("item"):
        title = normalize_space(item.findtext("title", default=""))
        link = normalize_space(item.findtext("link", default=""))
        pub_date = parse_rfc2822_date(item.findtext("pubDate", default=""))
        description = normalize_space(item.findtext("description", default=""))
        items.append(
            {
                "title": title,
                "url": link,
                "published": pub_date,
                "updated": pub_date,
                "description": description,
            }
        )
    return items


def fetch_acl_mods_record(item: dict) -> dict | None:
    link = item.get("url", "").rstrip("/")
    if not link:
        return None
    mods_url = f"{link}.xml"
    raw = bytes_request(mods_url)
    root = ET.fromstring(raw)

    title = normalize_space(root.findtext(".//mods:titleInfo/mods:title", default="", namespaces=MODS_NS))
    abstract = normalize_space(root.findtext(".//mods:abstract", default="", namespaces=MODS_NS))
    date_issued = normalize_space(
        root.findtext(".//mods:originInfo/mods:dateIssued", default="", namespaces=MODS_NS)
    )
    venue = normalize_space(
        root.findtext(".//mods:relatedItem/mods:titleInfo/mods:title", default="", namespaces=MODS_NS)
    )

    authors = []
    for author in root.findall(".//mods:name", MODS_NS):
        given = normalize_space(
            author.findtext("mods:namePart[@type='given']", default="", namespaces=MODS_NS)
        )
        family = normalize_space(
            author.findtext("mods:namePart[@type='family']", default="", namespaces=MODS_NS)
        )
        name = normalize_space(f"{given} {family}")
        if name:
            authors.append(name)

    paper_id = link.rsplit("/", maxsplit=1)[-1]
    published = safe_date(date_issued) or item.get("published", "")
    return {
        "id": f"acl:{paper_id}",
        "source": "ACL Anthology",
        "source_key": paper_id,
        "title": title or item.get("title", ""),
        "authors": authors,
        "url": link,
        "published": published,
        "updated": item.get("updated", "") or published,
        "abstract": abstract,
        "matched_keywords": [],
        "categories": [],
        "venue": venue,
    }


def fetch_acl_anthology_records(config: dict) -> list[dict]:
    source_config = config.get("sources", {}).get("acl_anthology", {})
    if source_config is not None and not source_config.get("enabled", True):
        return []

    feed_url = source_config.get("feed_url", "https://aclanthology.org/papers/index.xml")
    lookback_days = source_config.get("lookback_days", config.get("lookback_days", 7))
    max_items = source_config.get("max_items", 1000)
    keywords = config.get("keywords", [])
    collected: dict[str, dict] = {}

    try:
        feed_xml = text_request(feed_url)
        items = parse_acl_rss_items(feed_xml)[:max_items]
    except Exception as exc:  # pragma: no cover - network path
        print(f"[warn] failed to fetch ACL Anthology RSS feed: {exc}")
        return []

    for item in items:
        age = days_ago(item.get("updated") or item.get("published") or "")
        if age is not None and age > lookback_days:
            continue
        combined = f"{item.get('title', '')} {item.get('description', '')}"
        hits = contains_memory_signal(combined, keywords)
        if not hits:
            continue
        try:
            record = fetch_acl_mods_record(item)
        except Exception as exc:  # pragma: no cover - network path
            print(f"[warn] failed to fetch ACL paper details for {item.get('url', '')}: {exc}")
            continue
        if not record:
            continue
        refined_hits = contains_memory_signal(
            f"{record.get('title', '')} {record.get('abstract', '')} {item.get('description', '')}",
            keywords,
        )
        record["matched_keywords"] = refined_hits or hits
        current = collected.get(record["id"])
        if current:
            current["matched_keywords"] = sorted(
                set(current.get("matched_keywords", [])) | set(record.get("matched_keywords", []))
            )
            continue
        collected[record["id"]] = record
    return list(collected.values())


def enrich_tags(record: dict, config: dict) -> list[str]:
    title_abstract = f"{record.get('title', '')} {record.get('abstract', '')}"
    hits = contains_memory_signal(title_abstract, config.get("highlight_keywords", []))
    if not hits:
        hits = contains_memory_signal(title_abstract, config.get("keywords", []))
    return sorted(set(hits))


def build_one_liner(record: dict) -> str:
    sentences = split_sentences(record.get("abstract", ""))
    if sentences:
        return short_text(sentences[0], limit=180)
    return "This paper is tracked as a memory-related work and awaits a fuller summary."


def build_intro(record: dict) -> str:
    sentences = split_sentences(record.get("abstract", ""))
    sentence_a = short_text(sentences[0], 220) if sentences else "The abstract is not available yet."
    sentence_b = short_text(sentences[1], 220) if len(sentences) > 1 else ""
    tags = ", ".join(record.get("tags", [])[:4]) or "memory research"
    source = record.get("source", "the literature")
    venue = record.get("venue", "")
    pieces = [
        f"这篇论文被纳入仓库，是因为它和 `{tags}` 这些主题直接相关。",
        f"它当前来自 `{source}`{f'，并与 `{venue}` 这个 venue 相关' if venue else ''}。",
        f"从摘要来看，作者主要关注的是：{sentence_a}",
    ]
    if sentence_b:
        pieces.append(f"进一步看，论文的核心做法或实验重点可以概括为：{sentence_b}")
    pieces.append(
        "如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。"
    )
    return "\n\n".join(pieces)


def build_relevance(record: dict) -> str:
    tags = record.get("tags", [])
    keywords = record.get("matched_keywords", [])
    reasons = []
    if record.get("source"):
        reasons.append(f"来源：{record['source']}")
    if record.get("venue"):
        reasons.append(f"Venue：{record['venue']}")
    if tags:
        reasons.append(f"高亮主题命中：{', '.join(tags[:6])}")
    if keywords:
        reasons.append(f"检索关键词命中：{', '.join(sorted(set(keywords))[:6])}")
    if record.get("categories"):
        reasons.append(f"来源分类信息：{', '.join(record['categories'][:4])}")
    return "\n".join(f"- {reason}" for reason in reasons) or "- 手工加入的条目，建议补充人工说明。"


def extract_manual_notes(page_path: Path) -> str:
    if not page_path.exists():
        return DEFAULT_MANUAL_NOTES
    content = page_path.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"{re.escape(MANUAL_NOTES_START)}\n?(.*?)\n?{re.escape(MANUAL_NOTES_END)}",
        re.S,
    )
    match = pattern.search(content)
    if not match:
        return DEFAULT_MANUAL_NOTES
    notes = match.group(1).strip()
    return notes or DEFAULT_MANUAL_NOTES


def render_paper_page(record: dict, manual_notes: str) -> str:
    authors = ", ".join(record.get("authors", [])) or "Unknown"
    tags = ", ".join(record.get("tags", [])) or "memory"
    categories = ", ".join(record.get("categories", [])) or "N/A"
    abstract = normalize_space(record.get("abstract", "")) or "Abstract not available."
    venue = record.get("venue", "") or "N/A"
    return f"""# {record['title']}

- Source: {record.get('source', 'Unknown')}
- Venue: {venue}
- Paper ID: {record.get('id', 'N/A')}
- Published: {record.get('published', 'N/A')}
- Updated: {record.get('updated', 'N/A')}
- Authors: {authors}
- Tags: {tags}
- Categories: {categories}
- URL: {record.get('url', '')}

## One-Sentence Summary
{record.get('one_liner', '')}

## Introduction
{record.get('intro', '')}

## Why It Was Included
{record.get('relevance', '')}

## Abstract Snapshot
{abstract}

## Manual Notes
{MANUAL_NOTES_START}
{manual_notes}
{MANUAL_NOTES_END}
"""


def render_readme(config: dict, papers: list[dict]) -> str:
    total = len(papers)
    today = dt.date.today().isoformat()
    counts: dict[str, int] = {}
    for paper in papers:
        counts[paper.get("source", "Unknown")] = counts.get(paper.get("source", "Unknown"), 0) + 1

    source_lines = "\n".join(
        f"- {name}: **{count}**"
        for name, count in sorted(counts.items(), key=lambda item: item[0].lower())
    ) or "- No papers yet"

    latest_rows = []
    for record in papers[:20]:
        title = record["title"].replace("|", "\\|")
        link = f"[{title}](content/papers/{record['slug']}.md)"
        tags = ", ".join(record.get("tags", [])[:3]).replace("|", "\\|") or "memory"
        source = record.get("source", "Unknown").replace("|", "\\|")
        latest_rows.append(
            f"| {record.get('updated') or record.get('published') or 'N/A'} | {source} | {link} | {tags} |"
        )
    table = "\n".join(latest_rows) if latest_rows else "| N/A | N/A | No papers yet | N/A |"

    return f"""# {config['project_name']}

{config['project_description']}

This repository is designed for one very specific maintenance goal: keep tracking new memory-related papers and make sure **every tracked paper has its own introduction page**.

## What This Repo Gives You

- A scheduled GitHub Action that pulls new papers from arXiv, OpenReview, and ACL Anthology.
- One Markdown page per paper under `content/papers/`.
- A generated intro for every paper, so new entries are never empty.
- A manual notes block that is preserved across automatic updates.
- A simple JSON config that you can edit without changing the code.

## Source Strategy

- `arXiv`: keyword search over recent submissions in configurable categories.
- `OpenReview`: keyword search over public forum notes, optionally narrowed by venue groups.
- `ACL Anthology`: scan the official RSS paper feed and enrich matched papers with per-paper XML metadata.

## Local Usage

```bash
python3 scripts/update_papers.py
```

Only rebuild pages and the index:

```bash
python3 scripts/update_papers.py --build-only
```

## Manual Curation

- Add non-indexed papers to `data/manual_entries.json`.
- Add your reading notes inside the `Manual Notes` block of any paper page.
- Edit `config/topics.json` when you want to tighten or broaden the notion of "memory-related".
- If you want OpenReview to focus on specific venues, fill `sources.openreview.group_ids`.

## Repository Snapshot

- Total tracked papers: **{total}**
- Last generated: **{today}**

## Papers by Source

{source_lines}

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
{table}

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
"""


def merge_records(existing: list[dict], incoming: list[dict], config: dict) -> list[dict]:
    merged = {}
    for record in existing:
        merged[record["id"]] = record

    for record in incoming:
        current = merged.get(record["id"], {})
        combined_keywords = sorted(
            set(current.get("matched_keywords", [])) | set(record.get("matched_keywords", []))
        )
        new_record = {**current, **record}
        new_record["matched_keywords"] = combined_keywords
        new_record["tags"] = sorted(
            set(current.get("tags", []))
            | set(record.get("tags", []))
            | set(enrich_tags(new_record, config))
        )
        new_record["slug"] = slugify(new_record["title"], new_record["id"])
        new_record["one_liner"] = (
            new_record.get("one_liner") or current.get("one_liner") or build_one_liner(new_record)
        )
        new_record["intro"] = new_record.get("intro") or current.get("intro") or build_intro(new_record)
        new_record["relevance"] = build_relevance(new_record)
        merged[new_record["id"]] = new_record

    papers = list(merged.values())
    papers.sort(
        key=lambda item: (item.get("updated") or item.get("published") or "", item["title"]),
        reverse=True,
    )
    return papers


def normalize_manual_entry(entry: dict, config: dict) -> dict:
    title = normalize_space(entry.get("title", "Untitled Paper"))
    paper_id = entry.get("id") or hashlib.sha1(title.encode("utf-8")).hexdigest()[:12]
    abstract = normalize_space(entry.get("abstract", ""))
    record = {
        "id": paper_id,
        "source": entry.get("source", "Manual"),
        "source_key": entry.get("source_key", paper_id),
        "title": title,
        "authors": entry.get("authors", []),
        "url": entry.get("url", ""),
        "published": safe_date(entry.get("published", "")),
        "updated": safe_date(entry.get("updated", entry.get("published", ""))),
        "abstract": abstract,
        "matched_keywords": entry.get("matched_keywords", []),
        "categories": entry.get("categories", []),
        "venue": entry.get("venue", ""),
    }
    record["tags"] = entry.get("tags") or enrich_tags(record, config)
    record["slug"] = slugify(record["title"], record["id"])
    record["one_liner"] = entry.get("one_liner") or build_one_liner(record)
    record["intro"] = entry.get("intro") or build_intro(record)
    record["relevance"] = build_relevance(record)
    return record


def fetch_records(config: dict) -> list[dict]:
    records = []
    records.extend(fetch_arxiv_records(config))
    records.extend(fetch_openreview_records(config))
    records.extend(fetch_acl_anthology_records(config))
    return records


def write_paper_pages(content_dir: Path, papers: list[dict]) -> None:
    content_dir.mkdir(parents=True, exist_ok=True)
    for record in papers:
        page_path = content_dir / f"{record['slug']}.md"
        manual_notes = extract_manual_notes(page_path)
        page_path.write_text(
            render_paper_page(record, manual_notes),
            encoding="utf-8",
        )


def main() -> None:
    args = parse_args()
    repo_root = Path.cwd()
    config_path = repo_root / args.config
    data_path = repo_root / args.data
    manual_path = repo_root / args.manual
    content_dir = repo_root / args.content_dir
    readme_path = repo_root / args.readme

    config = read_json(config_path, {})
    existing = read_json(data_path, [])
    manual_entries_raw = read_json(manual_path, [])
    manual_entries = [normalize_manual_entry(entry, config) for entry in manual_entries_raw]

    fetched = []
    if not args.build_only:
        fetched = fetch_records(config)

    papers = merge_records(existing=existing, incoming=fetched + manual_entries, config=config)
    write_json(data_path, papers)
    write_paper_pages(content_dir, papers)
    readme_path.write_text(render_readme(config, papers), encoding="utf-8")
    print(f"Tracked papers: {len(papers)}")
    print(f"README updated: {readme_path}")


if __name__ == "__main__":
    main()
