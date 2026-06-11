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

- Total tracked papers: **484**
- Last generated: **2026-06-11**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **404**
- OpenReview: **79**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-06-09 | arXiv | [What Spatial Memory Must Store: Occlusion as the Test for Language-Agent Memory](content/papers/what-spatial-memory-must-store-occlusion-as-the-test-for-language-agent-memory.md) | agent |
| 2026-06-09 | arXiv | [WebChallenger: A Reliable and Efficient Generalist Web Agent](content/papers/webchallenger-a-reliable-and-efficient-generalist-web-agent.md) | agent |
| 2026-06-09 | arXiv | [Trace Only What You Need: Structure-Aware On-Demand Hypergraph Memory for Long-Document Question Answering](content/papers/trace-only-what-you-need-structure-aware-on-demand-hypergraph-memory-for-long-do.md) | agent, context, retrieval |
| 2026-06-09 | arXiv | [Soul Computing: A Theoretical Framework and Technical Architecture for Intelligent Agents with Independent Consciousness](content/papers/soul-computing-a-theoretical-framework-and-technical-architecture-for-intelligen.md) | agent, long-term |
| 2026-06-09 | arXiv | [Recalling Too Well: Sycophancy Evaluation and Mitigation in Memory-Augmented Models](content/papers/recalling-too-well-sycophancy-evaluation-and-mitigation-in-memory-augmented-mode.md) | benchmark, compression, context |
| 2026-06-09 | arXiv | [REAL: A Reasoning-Enhanced Graph Framework for Long-Term Memory Management of LLMs](content/papers/real-a-reasoning-enhanced-graph-framework-for-long-term-memory-management-of-llm.md) | context, conversation, long-term |
| 2026-06-09 | arXiv | [Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory](content/papers/infini-memory-maintainable-topic-documents-for-long-term-llm-agent-memory.md) | agent, context, long-term |
| 2026-06-09 | arXiv | [ConvMemory v2: A Recall-Preserving Top-10 Evidence Reranker for Conversational Memory Retrieval](content/papers/convmemory-v2-a-recall-preserving-top-10-evidence-reranker-for-conversational-me.md) | benchmark, conversation, retrieval |
| 2026-06-09 | arXiv | [ActiveMem: Distributed Active Memory for Long-Horizon LLM Reasoning](content/papers/activemem-distributed-active-memory-for-long-horizon-llm-reasoning.md) | agent, context |
| 2026-06-08 | arXiv | [Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents](content/papers/memory-beyond-recall-a-dual-process-cognitive-memory-system-for-self-evolving-ll.md) | agent, benchmark, long-term |
| 2026-06-08 | arXiv | [MASS: Deep Research for Social Sciences with Memory-Augmented Social Simulation](content/papers/mass-deep-research-for-social-sciences-with-memory-augmented-social-simulation.md) | agent, retrieval |
| 2026-06-08 | arXiv | [H2HMem: A Multimodal Memory Benchmark for Agents in Human-Human Interactions](content/papers/h2hmem-a-multimodal-memory-benchmark-for-agents-in-human-human-interactions.md) | agent, benchmark, conversation |
| 2026-06-08 | arXiv | [Deployment-Time Memorization in Foundation-Model Agents](content/papers/deployment-time-memorization-in-foundation-model-agents.md) | agent, compression, retrieval |
| 2026-06-08 | arXiv | [A Survey on Large Language Model-Based Game Agents](content/papers/a-survey-on-large-language-model-based-game-agents.md) | agent, context |
| 2026-06-07 | OpenReview | [OP-Bench: Benchmarking Over-Personalization for Memory-Augmented Personalized Conversational Agents](content/papers/op-bench-benchmarking-over-personalization-for-memory-augmented-personalized-con.md) | agent, benchmark, conversation |
| 2026-06-07 | OpenReview | [MemMA: Coordinating the Memory Cycle through Multi-Agent Reasoning and In-Situ Self-Evolution](content/papers/memma-coordinating-the-memory-cycle-through-multi-agent-reasoning-and-in-situ-se.md) | agent, retrieval |
| 2026-06-07 | OpenReview | [LiCoMemory: Lightweight and Cognitive Agentic Memory for Efficient Long-Term Reasoning](content/papers/licomemory-lightweight-and-cognitive-agentic-memory-for-efficient-long-term-reas.md) | agent, benchmark, context |
| 2026-06-07 | OpenReview | [Knowledge Graph Enhanced Memory-Augmented Retrieval for Long Context Modeling](content/papers/knowledge-graph-enhanced-memory-augmented-retrieval-for-long-context-modeling.md) | context, retrieval |
| 2026-06-07 | OpenReview | [Knowledge Graph Enhanced Memory-Augmented Retrieval for Long Context Modeling](content/papers/knowledge-graph-enhanced-memory-augmented-retrieval-for-long-context-modeling.md) | context, retrieval |
| 2026-06-07 | OpenReview | [Injecting Context via Situation Working Memory for Logical Reasoning with LLMs](content/papers/injecting-context-via-situation-working-memory-for-logical-reasoning-with-llms.md) | context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
