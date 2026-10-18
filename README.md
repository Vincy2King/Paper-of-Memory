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

- Total tracked papers: **1421**
- Last generated: **2026-10-18**

## Papers by Source

- ACL Anthology: **6**
- arXiv: **1269**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-10-15 | arXiv | [TEM: Temporal State Tracking Memory for Large Language Model Agents](content/papers/tem-temporal-state-tracking-memory-for-large-language-model-agents.md) | agent, conversation, retrieval |
| 2026-10-15 | arXiv | [MemScope: Evolving Agent Memory Architectures through Localized Code Repair](content/papers/memscope-evolving-agent-memory-architectures-through-localized-code-repair.md) | agent |
| 2026-10-15 | arXiv | [MemCut: Every Secret Leaves a Trail in the Long-Term Memory of LLM Agents](content/papers/memcut-every-secret-leaves-a-trail-in-the-long-term-memory-of-llm-agents.md) | agent, benchmark, conversation |
| 2026-10-15 | arXiv | [MemComposer: Learning to Assemble Memories for LLM Agents via Reinforcement Learning](content/papers/memcomposer-learning-to-assemble-memories-for-llm-agents-via-reinforcement-learn.md) | agent, context |
| 2026-10-15 | arXiv | [Language Models Share a Readout Bottleneck in Working Memory](content/papers/language-models-share-a-readout-bottleneck-in-working-memory.md) | working memory |
| 2026-10-15 | arXiv | [LTM: Latent Transition Based In-Context Memory for Vision-Language-Action Models](content/papers/ltm-latent-transition-based-in-context-memory-for-vision-language-action-models.md) | compression, context |
| 2026-10-15 | arXiv | [Hy-Memory-30B-A3B: Attributed Reinforcement Learning for Long-Term Memory Writing](content/papers/hy-memory-30b-a3b-attributed-reinforcement-learning-for-long-term-memory-writing.md) | benchmark, context, long-term |
| 2026-10-15 | arXiv | [From Long Context to Selective Memory:A Survey of Memory-Centric Compression for Large Language Models](content/papers/from-long-context-to-selective-memory-a-survey-of-memory-centric-compression-for.md) | agent, benchmark, compression |
| 2026-10-15 | arXiv | [Compression Does Not End at Selection: Post-Selection Positional Geometry for Sparse KV Caches](content/papers/compression-does-not-end-at-selection-post-selection-positional-geometry-for-spa.md) | compression, context, long-term |
| 2026-10-15 | arXiv | [Co2In: a Bi-level Memory Incremental Learning Framework with Knowledge Encoding, Consolidation, and Integration](content/papers/co2in-a-bi-level-memory-incremental-learning-framework-with-knowledge-encoding-c.md) | long-term |
| 2026-10-15 | arXiv | [Beyond Downstream QA: Rethinking How We Evaluate Agent Memory](content/papers/beyond-downstream-qa-rethinking-how-we-evaluate-agent-memory.md) | agent, benchmark, conversation |
| 2026-10-15 | arXiv | [All-in-One Memory: Process-Rewarded Reinforcement Learning for Memory Agents](content/papers/all-in-one-memory-process-rewarded-reinforcement-learning-for-memory-agents.md) | agent, benchmark, context |
| 2026-10-14 | arXiv | [SkillForge: Co-Evolving Skills and Agents via Dynamic Skill Lifecycles](content/papers/skillforge-co-evolving-skills-and-agents-via-dynamic-skill-lifecycles.md) | agent, benchmark |
| 2026-10-14 | arXiv | [Seeing, Maintaining, and Learning: The Evolution of Multimodal Agent Memory](content/papers/seeing-maintaining-and-learning-the-evolution-of-multimodal-agent-memory.md) | agent |
| 2026-10-14 | arXiv | [STRATA: Self-Maintaining Structured Experience Graphs for Self-Evolving Language Agents](content/papers/strata-self-maintaining-structured-experience-graphs-for-self-evolving-language-.md) | agent, benchmark, context |
| 2026-10-14 | arXiv | [MemCode: Discrete Semantic Representations for Long-Term Agent Memory](content/papers/memcode-discrete-semantic-representations-for-long-term-agent-memory.md) | agent, context, long-term |
| 2026-10-14 | arXiv | [How Should a Camera-First AI Agent Work?](content/papers/how-should-a-camera-first-ai-agent-work.md) | agent |
| 2026-10-14 | arXiv | [HEM-Med: A Hierarchical Agentic Memory Framework for Safe Multi-Center Medication Recommendation](content/papers/hem-med-a-hierarchical-agentic-memory-framework-for-safe-multi-center-medication.md) | agent, context, retrieval |
| 2026-10-14 | arXiv | [EGCForest: Structured Agent Memory Organization for Enterprise Group Chats](content/papers/egcforest-structured-agent-memory-organization-for-enterprise-group-chats.md) | agent, benchmark, context |
| 2026-10-14 | arXiv | [Do LLMs Learn from Rewards in Context? : Rethinking the role of reward in In-Context RL](content/papers/do-llms-learn-from-rewards-in-context-rethinking-the-role-of-reward-in-in-contex.md) | agent, benchmark, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
