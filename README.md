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

- Total tracked papers: **283**
- Last generated: **2026-05-23**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **247**
- OpenReview: **35**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-05-21 | arXiv | [The Log is the Agent: Event-Sourced Reactive Graphs for Auditable, Forkable Agentic Systems](content/papers/the-log-is-the-agent-event-sourced-reactive-graphs-for-auditable-forkable-agenti.md) | agent, conversation, retrieval |
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
| 2026-05-20 | arXiv | [Auto-Dreamer: Learning Offline Memory Consolidation for Language Agents](content/papers/auto-dreamer-learning-offline-memory-consolidation-for-language-agents.md) | agent, retrieval |
| 2026-05-19 | arXiv | [SimGym: A Framework for A/B Test Simulation in E-Commerce with Traffic-Grounded VLM Agents](content/papers/simgym-a-framework-for-a-b-test-simulation-in-e-commerce-with-traffic-grounded-v.md) | agent, episodic |
| 2026-05-19 | arXiv | [Rethinking How to Remember: Beyond Atomic Facts in Lifelong LLM Agent Memory](content/papers/rethinking-how-to-remember-beyond-atomic-facts-in-lifelong-llm-agent-memory.md) | agent, long-term, retrieval |
| 2026-05-19 | arXiv | [Mix-Quant: Quantized Prefilling, Precise Decoding for Agentic LLMs](content/papers/mix-quant-quantized-prefilling-precise-decoding-for-agentic-llms.md) | agent, benchmark, context |
| 2026-05-19 | arXiv | [Memory-Augmented Reinforcement Learning Agent for CAD Generation](content/papers/memory-augmented-reinforcement-learning-agent-for-cad-generation.md) | agent, retrieval |
| 2026-05-19 | arXiv | [MINTEval: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems](content/papers/minteval-evaluating-memory-under-multi-target-interference-in-long-horizon-agent.md) | agent, benchmark, context |
| 2026-05-19 | arXiv | [EngiAI: A Multi-Agent Framework and Benchmark Suite for LLM-Driven Engineering Design](content/papers/engiai-a-multi-agent-framework-and-benchmark-suite-for-llm-driven-engineering-de.md) | agent, benchmark, retrieval |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
