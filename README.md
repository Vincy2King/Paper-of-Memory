# Memory Papers Tracker

A GitHub-friendly tracker for memory-related papers with one page of introduction per paper.

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

- Total tracked papers: **1344**
- Last generated: **2026-10-08**

## Papers by Source

- ACL Anthology: **6**
- arXiv: **1192**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-10-07 | arXiv | [VideoEvolve: Co-Evolving Memory and Retrieval for Long Video Understanding](content/papers/videoevolve-co-evolving-memory-and-retrieval-for-long-video-understanding.md) | agent, benchmark, retrieval |
| 2026-10-07 | arXiv | [Stale, Misattributed, or Late: Where Personal Memory Fails Before Generation](content/papers/stale-misattributed-or-late-where-personal-memory-fails-before-generation.md) | agent, benchmark, retrieval |
| 2026-10-07 | arXiv | [SkillForge: Co-Evolving Skills and Agents via Dynamic Skill Lifecycles](content/papers/skillforge-co-evolving-skills-and-agents-via-dynamic-skill-lifecycles.md) | agent, benchmark |
| 2026-10-07 | arXiv | [Retrieval Is Not Enough: Refreshing Memory for Frozen Time-Series Forecasters](content/papers/retrieval-is-not-enough-refreshing-memory-for-frozen-time-series-forecasters.md) | benchmark, context, retrieval |
| 2026-10-07 | arXiv | [Relevance Is Not Sufficiency: What Actually Closes the Evidence Gap in Long-Term Memory QA](content/papers/relevance-is-not-sufficiency-what-actually-closes-the-evidence-gap-in-long-term-.md) | agent, context, long-term |
| 2026-10-07 | arXiv | [Madeleine: Learning Involuntary Recall for Conversational Memory from Simulated Lives](content/papers/madeleine-learning-involuntary-recall-for-conversational-memory-from-simulated-l.md) | context, conversation, long-term |
| 2026-10-07 | arXiv | [LiveMACE: Process-Aware Evaluation of LLM Agent Capabilities in Evolving Markets](content/papers/livemace-process-aware-evaluation-of-llm-agent-capabilities-in-evolving-markets.md) | agent, benchmark |
| 2026-10-07 | arXiv | [HGP:An on-device personalized agent memory via hybrid graph storage](content/papers/hgp-an-on-device-personalized-agent-memory-via-hybrid-graph-storage.md) | agent, benchmark, episodic |
| 2026-10-06 | arXiv | [Whose Memory Is It? Scope-Aware Commit Rules for Long-Term LLM Memory](content/papers/whose-memory-is-it-scope-aware-commit-rules-for-long-term-llm-memory.md) | agent, context, conversation |
| 2026-10-06 | arXiv | [Towards In-Parameter Memory Augmentation for Large Language Models](content/papers/towards-in-parameter-memory-augmentation-for-large-language-models.md) | agent, context |
| 2026-10-06 | arXiv | [STRUCTURALCOST: A controlled reading time dataset for modeling human sentence processing difficulty](content/papers/structuralcost-a-controlled-reading-time-dataset-for-modeling-human-sentence-pro.md) | working memory |
| 2026-10-06 | arXiv | [Retrieval Is Not Enough: Refreshing Memory for Frozen Time-Series Forecasters](content/papers/retrieval-is-not-enough-refreshing-memory-for-frozen-time-series-forecasters.md) | benchmark, context, retrieval |
| 2026-10-06 | arXiv | [Persistent Memory in Multi-Agent LLM Inference: What It Costs, What It Buys, and When You Can Tell](content/papers/persistent-memory-in-multi-agent-llm-inference-what-it-costs-what-it-buys-and-wh.md) | agent, benchmark, context |
| 2026-10-06 | arXiv | [PERSIST: Who-What-When Memory Across Sessions for Full-Duplex Spoken Dialogue](content/papers/persist-who-what-when-memory-across-sessions-for-full-duplex-spoken-dialogue.md) | benchmark, conversation, retrieval |
| 2026-10-06 | arXiv | [Memory Depth and Reconstructed Context Width: A Controlled Evaluation of Hierarchical Retrieval](content/papers/memory-depth-and-reconstructed-context-width-a-controlled-evaluation-of-hierarch.md) | context, conversation, long-term |
| 2026-10-06 | arXiv | [MINDSET: Energy-based Schema Evolution for Long Conversational Agent Memory](content/papers/mindset-energy-based-schema-evolution-for-long-conversational-agent-memory.md) | agent, context, conversation |
| 2026-10-06 | arXiv | [Harnessing LLMs as Agents: What Does It Cost?](content/papers/harnessing-llms-as-agents-what-does-it-cost.md) | agent, context |
| 2026-10-06 | arXiv | [Decoupling Memory from Context: Structured Memory for Token-Efficient Test-Time Continual Learning](content/papers/decoupling-memory-from-context-structured-memory-for-token-efficient-test-time-c.md) | agent, context, retrieval |
| 2026-10-06 | arXiv | [Decide Before You Look: Learning Which Retrieved Memories Deserve Pixels](content/papers/decide-before-you-look-learning-which-retrieved-memories-deserve-pixels.md) | long-term, retrieval |
| 2026-10-06 | arXiv | [DAEDALUS: Bootstrapping Agent Memory from Self-Generated Tasks](content/papers/daedalus-bootstrapping-agent-memory-from-self-generated-tasks.md) | agent, benchmark, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
