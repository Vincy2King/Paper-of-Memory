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

- Total tracked papers: **457**
- Last generated: **2026-06-07**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **377**
- OpenReview: **79**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-06-07 | OpenReview | [OP-Bench: Benchmarking Over-Personalization for Memory-Augmented Personalized Conversational Agents](content/papers/op-bench-benchmarking-over-personalization-for-memory-augmented-personalized-con.md) | agent, benchmark, conversation |
| 2026-06-07 | OpenReview | [MemMA: Coordinating the Memory Cycle through Multi-Agent Reasoning and In-Situ Self-Evolution](content/papers/memma-coordinating-the-memory-cycle-through-multi-agent-reasoning-and-in-situ-se.md) | agent, retrieval |
| 2026-06-07 | OpenReview | [LiCoMemory: Lightweight and Cognitive Agentic Memory for Efficient Long-Term Reasoning](content/papers/licomemory-lightweight-and-cognitive-agentic-memory-for-efficient-long-term-reas.md) | agent, benchmark, context |
| 2026-06-07 | OpenReview | [Knowledge Graph Enhanced Memory-Augmented Retrieval for Long Context Modeling](content/papers/knowledge-graph-enhanced-memory-augmented-retrieval-for-long-context-modeling.md) | context, retrieval |
| 2026-06-07 | OpenReview | [Knowledge Graph Enhanced Memory-Augmented Retrieval for Long Context Modeling](content/papers/knowledge-graph-enhanced-memory-augmented-retrieval-for-long-context-modeling.md) | context, retrieval |
| 2026-06-07 | OpenReview | [Injecting Context via Situation Working Memory for Logical Reasoning with LLMs](content/papers/injecting-context-via-situation-working-memory-for-logical-reasoning-with-llms.md) | context |
| 2026-06-07 | OpenReview | [From Retrieval to Reconstruction: Constructing Evolvable Cognitive Memory for Long-term Dialogue](content/papers/from-retrieval-to-reconstruction-constructing-evolvable-cognitive-memory-for-lon.md) | context, long-term, retrieval |
| 2026-06-07 | OpenReview | [EMemBench: Interactive Benchmarking of Episodic Memory for VLM Agents](content/papers/emembench-interactive-benchmarking-of-episodic-memory-for-vlm-agents.md) | agent, benchmark, context |
| 2026-06-07 | OpenReview | [EMemBench: Interactive Benchmarking of Episodic Memory for VLM Agents](content/papers/emembench-interactive-benchmarking-of-episodic-memory-for-vlm-agents.md) | agent, benchmark, context |
| 2026-06-07 | OpenReview | [AutoViewMem: Self-Configuring Orthogonal Views for Conversational Long-Term Memory](content/papers/autoviewmem-self-configuring-orthogonal-views-for-conversational-long-term-memor.md) | agent, benchmark, conversation |
| 2026-06-07 | OpenReview | [AtomMem : Learnable Dynamic Agentic Memory with Atomic Memory Operation](content/papers/atommem-learnable-dynamic-agentic-memory-with-atomic-memory-operation.md) | agent, benchmark, context |
| 2026-06-04 | arXiv | [When Should Memory Stay Silent: Measuring Memory-Use Boundaries in Memory-Augmented Conversational Agents](content/papers/when-should-memory-stay-silent-measuring-memory-use-boundaries-in-memory-augment.md) | agent, context, conversation |
| 2026-06-04 | arXiv | [Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills](content/papers/trace2skill-distill-trajectory-local-lessons-into-transferable-agent-skills.md) | agent, retrieval |
| 2026-06-04 | arXiv | [TOKI: A Bitemporal Operator Algebra for Contradiction Resolution in LLM-Agent Persistent Memory](content/papers/toki-a-bitemporal-operator-algebra-for-contradiction-resolution-in-llm-agent-per.md) | agent |
| 2026-06-04 | arXiv | [SubtleMemory: A Benchmark for Fine-Grained Relational Memory Discrimination in Long-Horizon AI Agents](content/papers/subtlememory-a-benchmark-for-fine-grained-relational-memory-discrimination-in-lo.md) | agent, benchmark, context |
| 2026-06-04 | arXiv | [Statistical Priors for Implicit Preferences: Decoupling Skill Selection as a Local Harness in Personal Agents](content/papers/statistical-priors-for-implicit-preferences-decoupling-skill-selection-as-a-loca.md) | agent |
| 2026-06-04 | arXiv | [QueryAgent-R1: Bridging Query Generation and Product Retrieval for E-Commerce Query Recommendation](content/papers/queryagent-r1-bridging-query-generation-and-product-retrieval-for-e-commerce-que.md) | agent, retrieval |
| 2026-06-04 | arXiv | [Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents](content/papers/memory-is-reconstructed-not-retrieved-graph-memory-for-llm-agents.md) | agent, benchmark, context |
| 2026-06-04 | arXiv | [FIDES: Faithful Inference via Deep Evidence Signals for Retrieval-Memory Conflict in RAG](content/papers/fides-faithful-inference-via-deep-evidence-signals-for-retrieval-memory-conflict.md) | benchmark, context, retrieval |
| 2026-06-04 | arXiv | [Enhancing Software Engineering Through Closed-Loop Memory Optimization](content/papers/enhancing-software-engineering-through-closed-loop-memory-optimization.md) | agent, benchmark, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
