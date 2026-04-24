# Contributing

## Add a paper manually

Put a new JSON object into `data/manual_entries.json`:

```json
[
  {
    "title": "Your paper title",
    "source": "OpenReview",
    "venue": "ICLR 2026",
    "url": "https://openreview.net/forum?id=...",
    "published": "2026-04-24",
    "authors": ["Author A", "Author B"],
    "abstract": "Paper abstract here.",
    "tags": ["benchmark", "agent"],
    "intro": "Optional manual introduction in Chinese."
  }
]
```

## Narrow OpenReview scope

If global OpenReview keyword search is too broad, set explicit venue groups in `config/topics.json`:

```json
{
  "sources": {
    "openreview": {
      "group_ids": [
        "ICLR.cc/2026/Conference",
        "NeurIPS.cc/2025/Conference"
      ]
    }
  }
}
```

## Keep manual notes safe

Auto-updates preserve anything written between:

```text
<!-- MANUAL_NOTES_START -->
<!-- MANUAL_NOTES_END -->
```
