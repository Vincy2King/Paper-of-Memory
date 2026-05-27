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

- Total tracked papers: **290**
- Last generated: **2026-05-27**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **251**
- OpenReview: **38**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-05-26 | OpenReview | [CADedup: High-performance Consistency-aware Deduplication Based on Persistent Memory](content/papers/cadedup-high-performance-consistency-aware-deduplication-based-on-persistent-mem.md) | benchmark |
| 2026-05-26 | OpenReview | [APEX-MEM: Agentic Semi-Structured Memory with Temporal Reasoning for Long-Term Conversational AI](content/papers/apex-mem-agentic-semi-structured-memory-with-temporal-reasoning-for-long-term-co.md) | agent, context, conversation |
| 2026-05-25 | OpenReview | [LatentMem: Customizing Latent Memory for Multi-Agent Systems](content/papers/latentmem-customizing-latent-memory-for-multi-agent-systems.md) | agent, benchmark, context |
| 2026-05-22 | arXiv | [Preisach Attention: A Hysteretic Model of Sequential Memory](content/papers/preisach-attention-a-hysteretic-model-of-sequential-memory.md) | episodic, retrieval |
| 2026-05-22 | arXiv | [MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection](content/papers/memaudit-post-hoc-auditing-of-poisoned-agent-memory-via-causal-attribution-and-s.md) | agent |
| 2026-05-21 | arXiv | [What Training Data Teaches RL Memory Agents: An Empirical Study of Curriculum Effects in Memory-Augmented QA](content/papers/what-training-data-teaches-rl-memory-agents-an-empirical-study-of-curriculum-eff.md) | agent, benchmark |
| 2026-05-21 | arXiv | [The Log is the Agent: Event-Sourced Reactive Graphs for Auditable, Forkable Agentic Systems](content/papers/the-log-is-the-agent-event-sourced-reactive-graphs-for-auditable-forkable-agenti.md) | agent, conversation, retrieval |
| 2026-05-21 | arXiv | [The Efficiency Frontier: A Unified Framework for Cost-Performance Optimization in LLM Context Management](content/papers/the-efficiency-frontier-a-unified-framework-for-cost-performance-optimization-in.md) | compression, context, retrieval |
| 2026-05-21 | arXiv | [Short-Term-to-Long-Term Memory Transfer for Knowledge Graphs under Partial Observability](content/papers/short-term-to-long-term-memory-transfer-for-knowledge-graphs-under-partial-obser.md) | agent, benchmark, long-term |
| 2026-05-21 | arXiv | [LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems](content/papers/lcguard-latent-communication-guard-for-safe-kv-sharing-in-multi-agent-systems.md) | agent, benchmark, context |
| 2026-05-21 | arXiv | [DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Memory QA](content/papers/defermem-query-time-evidence-distillation-via-reinforcement-learning-for-long-te.md) | agent, conversation, long-term |
| 2026-05-21 | arXiv | [AtelierEval: Agentic Evaluation of Humans & LLMs as Text-to-Image Prompters](content/papers/ateliereval-agentic-evaluation-of-humans-llms-as-text-to-image-prompters.md) | agent, benchmark |
| 2026-05-20 | OpenReview | [Ontology-Guided Long-Term Agent Memory for Conversational RAG](content/papers/ontology-guided-long-term-agent-memory-for-conversational-rag.md) | agent, benchmark, context |
| 2026-05-20 | arXiv | [NeuSymMS: A Hybrid Neuro-Symbolic Memory System for Persistent, Self-Curating LLM Agents](content/papers/neusymms-a-hybrid-neuro-symbolic-memory-system-for-persistent-self-curating-llm-.md) | agent, context, long-term |
| 2026-05-20 | arXiv | [Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents](content/papers/memory-r2-fair-credit-assignment-for-long-horizon-memory-augmented-llm-agents.md) | agent, context |
| 2026-05-20 | arXiv | [Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory](content/papers/memory-grafting-scaling-language-model-pre-training-via-offline-conditional-memo.md) | benchmark, context |
| 2026-05-20 | arXiv | [MemGym: a Long-Horizon Memory Environment for LLM Agents](content/papers/memgym-a-long-horizon-memory-environment-for-llm-agents.md) | agent, benchmark, compression |
| 2026-05-20 | arXiv | [MemConflict: Evaluating Long-Term Memory Systems Under Memory Conflicts](content/papers/memconflict-evaluating-long-term-memory-systems-under-memory-conflicts.md) | agent, benchmark, context |
| 2026-05-20 | arXiv | [Mem-$π$: Adaptive Memory through Learning When and What to Generate](content/papers/mem-adaptive-memory-through-learning-when-and-what-to-generate.md) | agent, benchmark, context |
| 2026-05-20 | arXiv | [CALMem : Application-Layer Dual Memory for Conversational AI](content/papers/calmem-application-layer-dual-memory-for-conversational-ai.md) | agent, context, conversation |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
