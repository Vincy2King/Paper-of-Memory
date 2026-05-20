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

- Total tracked papers: **262**
- Last generated: **2026-05-20**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **226**
- OpenReview: **35**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-05-20 | OpenReview | [Ontology-Guided Long-Term Agent Memory for Conversational RAG](content/papers/ontology-guided-long-term-agent-memory-for-conversational-rag.md) | agent, benchmark, context |
| 2026-05-18 | arXiv | [TinySAM 2: Extreme Memory Compression for Efficient Track Anything Model](content/papers/tinysam-2-extreme-memory-compression-for-efficient-track-anything-model.md) | compression |
| 2026-05-18 | arXiv | [SocialMemBench: Are AI Memory Systems Ready for Social Group Settings?](content/papers/socialmembench-are-ai-memory-systems-ready-for-social-group-settings.md) | agent, benchmark, context |
| 2026-05-18 | arXiv | [LongMINT: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems](content/papers/longmint-evaluating-memory-under-multi-target-interference-in-long-horizon-agent.md) | agent, benchmark, context |
| 2026-05-18 | arXiv | [Hidden in Memory: Sleeper Memory Poisoning in LLM Agents](content/papers/hidden-in-memory-sleeper-memory-poisoning-in-llm-agents.md) | agent, context, conversation |
| 2026-05-18 | arXiv | [EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective](content/papers/evomembench-benchmarking-agent-memory-from-a-self-evolving-perspective.md) | agent, benchmark, context |
| 2026-05-18 | arXiv | [DimMem: Dimensional Structuring for Efficient Long-Term Agent Memory](content/papers/dimmem-dimensional-structuring-for-efficient-long-term-agent-memory.md) | agent, benchmark, context |
| 2026-05-18 | arXiv | [CommitDistill: A Lightweight Knowledge-Centric Memory Layer for Software Repositories](content/papers/commitdistill-a-lightweight-knowledge-centric-memory-layer-for-software-reposito.md) | agent, benchmark, retrieval |
| 2026-05-18 | arXiv | [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](content/papers/agentic-harness-engineering-observability-driven-automatic-evolution-of-coding-a.md) | agent, benchmark, long-term |
| 2026-05-18 | arXiv | [AMARIS: A Memory-Augmented Rubric Improvement System for Rubric-Based Reinforcement Learning](content/papers/amaris-a-memory-augmented-rubric-improvement-system-for-rubric-based-reinforceme.md) | context, long-term, retrieval |
| 2026-05-17 | arXiv | [Taming "Zombie'' Agents: A Markov State-Aware Framework for Resilient Multi-Agent Evolution](content/papers/taming-zombie-agents-a-markov-state-aware-framework-for-resilient-multi-agent-ev.md) | agent |
| 2026-05-17 | arXiv | [OProver: A Unified Framework for Agentic Formal Theorem Proving](content/papers/oprover-a-unified-framework-for-agentic-formal-theorem-proving.md) | agent, benchmark, context |
| 2026-05-17 | arXiv | [NeuSymMS: A Hybrid Neuro-Symbolic Memory System for Persistent, Self-Curating LLM Agents](content/papers/neusymms-a-hybrid-neuro-symbolic-memory-system-for-persistent-self-curating-llm-.md) | agent, context, long-term |
| 2026-05-17 | arXiv | [MemRepair: Hierarchical Memory for Agentic Repository-Level Vulnerability Repair](content/papers/memrepair-hierarchical-memory-for-agentic-repository-level-vulnerability-repair.md) | agent, benchmark, context |
| 2026-05-17 | OpenReview | [MemGen: Weaving Generative Latent Memory for Self-Evolving Agents](content/papers/memgen-weaving-generative-latent-memory-for-self-evolving-agents.md) | agent, benchmark, retrieval |
| 2026-05-17 | arXiv | [Episodic-Semantic Memory Architecture for Long-Horizon Scientific Agents](content/papers/episodic-semantic-memory-architecture-for-long-horizon-scientific-agents.md) | agent, context, episodic |
| 2026-05-17 | arXiv | [Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents](content/papers/causal-intervention-based-memory-selection-for-long-horizon-llm-agents.md) | agent, benchmark, context |
| 2026-05-16 | arXiv | [When Robots Do the Chores: A Benchmark and Agent for Long-Horizon Household Task Execution](content/papers/when-robots-do-the-chores-a-benchmark-and-agent-for-long-horizon-household-task-.md) | agent, benchmark, episodic |
| 2026-05-16 | arXiv | [State Contamination in Memory-Augmented LLM Agents](content/papers/state-contamination-in-memory-augmented-llm-agents.md) | agent, context |
| 2026-05-16 | arXiv | [SE-GA: Memory-Augmented Self-Evolution for GUI Agents](content/papers/se-ga-memory-augmented-self-evolution-for-gui-agents.md) | agent, benchmark, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
