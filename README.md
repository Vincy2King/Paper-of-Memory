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

- Total tracked papers: **228**
- Last generated: **2026-05-16**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **193**
- OpenReview: **34**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-05-14 | arXiv | [When Robots Do the Chores: A Benchmark and Agent for Long-Horizon Household Task Execution](content/papers/when-robots-do-the-chores-a-benchmark-and-agent-for-long-horizon-household-task-.md) | agent, benchmark, episodic |
| 2026-05-14 | arXiv | [Spontaneous symmetry breaking and Goldstone modes for deep information propagation](content/papers/spontaneous-symmetry-breaking-and-goldstone-modes-for-deep-information-propagati.md) | long-term |
| 2026-05-14 | arXiv | [ShadowMerge: A Novel Poisoning Attack on Graph-Based Agent Memory via Relation-Channel Conflicts](content/papers/shadowmerge-a-novel-poisoning-attack-on-graph-based-agent-memory-via-relation-ch.md) | agent, long-term |
| 2026-05-14 | arXiv | [MemReranker: Reasoning-Aware Reranking for Agent Memory Retrieval](content/papers/memreranker-reasoning-aware-reranking-for-agent-memory-retrieval.md) | agent, benchmark, context |
| 2026-05-14 | arXiv | [MemQ: Integrating Q-Learning into Self-Evolving Memory Agents over Provenance DAGs](content/papers/memq-integrating-q-learning-into-self-evolving-memory-agents-over-provenance-dag.md) | agent, benchmark, context |
| 2026-05-14 | arXiv | [MemLineage: Lineage-Guided Enforcement for LLM Agent Memory](content/papers/memlineage-lineage-guided-enforcement-for-llm-agent-memory.md) | agent |
| 2026-05-14 | arXiv | [MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory](content/papers/memeye-a-visual-centric-evaluation-framework-for-multimodal-agent-memory.md) | agent, benchmark, long-term |
| 2026-05-14 | arXiv | [GroupMemBench: Benchmarking LLM Agent Memory in Multi-Party Conversations](content/papers/groupmembench-benchmarking-llm-agent-memory-in-multi-party-conversations.md) | agent, benchmark, conversation |
| 2026-05-14 | arXiv | [EverAnimate: Minute-Scale Human Animation via Latent Flow Restoration](content/papers/everanimate-minute-scale-human-animation-via-latent-flow-restoration.md) | context |
| 2026-05-14 | arXiv | [EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation](content/papers/entitybench-towards-entity-consistent-long-range-multi-shot-video-generation.md) | benchmark |
| 2026-05-14 | arXiv | [Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination](content/papers/attractor-geometry-of-transformer-memory-from-conflict-arbitration-to-confident-.md) | context |
| 2026-05-14 | arXiv | [Agentic Recommender System with Hierarchical Belief-State Memory](content/papers/agentic-recommender-system-with-hierarchical-belief-state-memory.md) | agent, benchmark |
| 2026-05-14 | arXiv | [ASH: Agents that Self-Hone via Embodied Learning](content/papers/ash-agents-that-self-hone-via-embodied-learning.md) | agent, long-term, retrieval |
| 2026-05-13 | arXiv | [Useful Memories Become Faulty When Continuously Updated by LLMs](content/papers/useful-memories-become-faulty-when-continuously-updated-by-llms.md) | agent, episodic |
| 2026-05-13 | arXiv | [RealICU: Do LLM Agents Understand Long-Context ICU Data? A Benchmark Beyond Behavior Imitation](content/papers/realicu-do-llm-agents-understand-long-context-icu-data-a-benchmark-beyond-behavi.md) | agent, benchmark, context |
| 2026-05-13 | arXiv | [ReTool-Video: Recursive Tool-Using Video Agents with Meta-Augmented Tool Grounding](content/papers/retool-video-recursive-tool-using-video-agents-with-meta-augmented-tool-groundin.md) | agent, retrieval |
| 2026-05-13 | arXiv | [NAACA: Training-Free NeuroAuditory Attentive Cognitive Architecture with Oscillatory Working Memory for Salience-Driven Attention Gating](content/papers/naaca-training-free-neuroauditory-attentive-cognitive-architecture-with-oscillat.md) | working memory |
| 2026-05-13 | arXiv | [Model-Agnostic Lifelong LLM Safety via Externalized Attack-Defense Co-Evolution](content/papers/model-agnostic-lifelong-llm-safety-via-externalized-attack-defense-co-evolution.md) | retrieval |
| 2026-05-13 | arXiv | [McCast: Memory-Guided Latent Drift Correction for Long-Horizon Precipitation Nowcasting](content/papers/mccast-memory-guided-latent-drift-correction-for-long-horizon-precipitation-nowc.md) | benchmark, retrieval |
| 2026-05-13 | arXiv | [Key-Value Means: Transformers with Expandable Block-Recurrent Compressed Memory](content/papers/key-value-means-transformers-with-expandable-block-recurrent-compressed-memory.md) | context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
