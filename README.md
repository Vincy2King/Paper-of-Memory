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

- Total tracked papers: **887**
- Last generated: **2026-08-07**

## Papers by Source

- ACL Anthology: **5**
- arXiv: **750**
- OpenReview: **132**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-08-06 | OpenReview | [Profile-Graph Memory for LLM Agents: Implicit Cross-Entity Traversal through Narrative Profiles](content/papers/profile-graph-memory-for-llm-agents-implicit-cross-entity-traversal-through-narr.md) | agent, benchmark, compression |
| 2026-08-06 | OpenReview | [MemTrace: Probing What Final Accuracy Misses in Long-Term Memory](content/papers/memtrace-probing-what-final-accuracy-misses-in-long-term-memory.md) | agent, benchmark, long-term |
| 2026-08-06 | OpenReview | [Long Context Modeling with Ranked Memory-Augmented Retrieval](content/papers/long-context-modeling-with-ranked-memory-augmented-retrieval.md) | benchmark, context, long-term |
| 2026-08-05 | arXiv | [When Memory Lies: An Empirical Study of Spatial Memory Staleness in VLM Agents](content/papers/when-memory-lies-an-empirical-study-of-spatial-memory-staleness-in-vlm-agents.md) | agent |
| 2026-08-05 | arXiv | [The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monitoring Misleads](content/papers/the-personalization-mirage-how-llms-fabricate-user-profiles-and-why-self-monitor.md) | persistent memory |
| 2026-08-05 | arXiv | [MemoryCPT: An End-to-End Agent Memory Framework for Cost-Performance Trade-off](content/papers/memorycpt-an-end-to-end-agent-memory-framework-for-cost-performance-trade-off.md) | agent, context, retrieval |
| 2026-08-05 | arXiv | [MemSIF: From Structured Interactions to Dual-Track Fact Memory for LLM Agents](content/papers/memsif-from-structured-interactions-to-dual-track-fact-memory-for-llm-agents.md) | agent, long-term |
| 2026-08-05 | arXiv | [Mamba with Hierarchical Memory: Solving Representation Bottleneck in Long Sequence Modeling](content/papers/mamba-with-hierarchical-memory-solving-representation-bottleneck-in-long-sequenc.md) | context, long-term, retrieval |
| 2026-08-05 | arXiv | [CogniFold: Always-On Proactive Memory via Cognitive Folding](content/papers/cognifold-always-on-proactive-memory-via-cognitive-folding.md) | agent, benchmark, conversation |
| 2026-08-05 | arXiv | [ChronoMem: Version Control and Semantic Rollback for Large Language Model Agent Memory](content/papers/chronomem-version-control-and-semantic-rollback-for-large-language-model-agent-m.md) | agent, benchmark, conversation |
| 2026-08-05 | OpenReview | [Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems](content/papers/caching-for-the-future-scrub-jay-episodic-memory-principles-for-agent-memory-sys.md) | agent, benchmark, context |
| 2026-08-05 | arXiv | [Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems](content/papers/caching-for-the-future-scrub-jay-episodic-memory-principles-for-agent-memory-sys.md) | agent, benchmark, context |
| 2026-08-05 | OpenReview | [Beyond Retrieval: Analytic Memory for Multimodal Agents](content/papers/beyond-retrieval-analytic-memory-for-multimodal-agents.md) | agent, benchmark, context |
| 2026-08-05 | arXiv | [Attention, Anomalies! Handling Attention Layers in Unsupervised Federated Outlier Detection](content/papers/attention-anomalies-handling-attention-layers-in-unsupervised-federated-outlier-.md) | context |
| 2026-08-04 | arXiv | [When Memory Becomes Authority: Benchmarking Authority Collapse at the Memory Consolidation Boundary](content/papers/when-memory-becomes-authority-benchmarking-authority-collapse-at-the-memory-cons.md) | agent, benchmark |
| 2026-08-04 | arXiv | [Verifiable Memory: Learning Unified Memory Management with Local and Global Verifiers for Large Language Model Agents](content/papers/verifiable-memory-learning-unified-memory-management-with-local-and-global-verif.md) | agent, benchmark, context |
| 2026-08-04 | arXiv | [TARL: Transaction-Aware Reliable Ledgers for Executable Memory Management in Long-Term Agents](content/papers/tarl-transaction-aware-reliable-ledgers-for-executable-memory-management-in-long.md) | agent, benchmark, long-term |
| 2026-08-04 | arXiv | [SafeCommit: Certifying When Memory-Grounded Agents May Safely Act](content/papers/safecommit-certifying-when-memory-grounded-agents-may-safely-act.md) | agent |
| 2026-08-04 | arXiv | [SPEAR: Code-Augmented Agentic Prompt Optimization](content/papers/spear-code-augmented-agentic-prompt-optimization.md) | agent, context, conversation |
| 2026-08-04 | arXiv | [RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States](content/papers/romerl-balancing-feedback-coverage-and-the-memory-reward-trap-in-self-evolving-a.md) | agent |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
