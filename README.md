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

- Total tracked papers: **446**
- Last generated: **2026-06-06**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **377**
- OpenReview: **68**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-06-04 | arXiv | [When Should Memory Stay Silent: Measuring Memory-Use Boundaries in Memory-Augmented Conversational Agents](content/papers/when-should-memory-stay-silent-measuring-memory-use-boundaries-in-memory-augment.md) | agent, context, conversation |
| 2026-06-04 | arXiv | [Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills](content/papers/trace2skill-distill-trajectory-local-lessons-into-transferable-agent-skills.md) | agent, retrieval |
| 2026-06-04 | arXiv | [TOKI: A Bitemporal Operator Algebra for Contradiction Resolution in LLM-Agent Persistent Memory](content/papers/toki-a-bitemporal-operator-algebra-for-contradiction-resolution-in-llm-agent-per.md) | agent |
| 2026-06-04 | arXiv | [SubtleMemory: A Benchmark for Fine-Grained Relational Memory Discrimination in Long-Horizon AI Agents](content/papers/subtlememory-a-benchmark-for-fine-grained-relational-memory-discrimination-in-lo.md) | agent, benchmark, context |
| 2026-06-04 | arXiv | [Statistical Priors for Implicit Preferences: Decoupling Skill Selection as a Local Harness in Personal Agents](content/papers/statistical-priors-for-implicit-preferences-decoupling-skill-selection-as-a-loca.md) | agent |
| 2026-06-04 | arXiv | [QueryAgent-R1: Bridging Query Generation and Product Retrieval for E-Commerce Query Recommendation](content/papers/queryagent-r1-bridging-query-generation-and-product-retrieval-for-e-commerce-que.md) | agent, retrieval |
| 2026-06-04 | arXiv | [Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents](content/papers/memory-is-reconstructed-not-retrieved-graph-memory-for-llm-agents.md) | agent, benchmark, context |
| 2026-06-04 | arXiv | [FIDES: Faithful Inference via Deep Evidence Signals for Retrieval-Memory Conflict in RAG](content/papers/fides-faithful-inference-via-deep-evidence-signals-for-retrieval-memory-conflict.md) | benchmark, context, retrieval |
| 2026-06-04 | arXiv | [Enhancing Software Engineering Through Closed-Loop Memory Optimization](content/papers/enhancing-software-engineering-through-closed-loop-memory-optimization.md) | agent, benchmark, context |
| 2026-06-04 | arXiv | [Computational Modeling of Human Adaptation in Urban Infrastructure Management under Extreme Conditions: A Case Study of Subway Flood Scenarios](content/papers/computational-modeling-of-human-adaptation-in-urban-infrastructure-management-un.md) | retrieval |
| 2026-06-04 | arXiv | [Beyond Similarity: Trustworthy Memory Search for Personal AI Agents](content/papers/beyond-similarity-trustworthy-memory-search-for-personal-ai-agents.md) | agent, context, long-term |
| 2026-06-04 | arXiv | [Beyond Semantic Organization: Memory as Execution State Management for Long-Horizon Agents](content/papers/beyond-semantic-organization-memory-as-execution-state-management-for-long-horiz.md) | agent, context |
| 2026-06-04 | arXiv | [Ask Only When Needed: Proactive Retrieval from Memory and Skills for Experience-Driven Lifelong Agents](content/papers/ask-only-when-needed-proactive-retrieval-from-memory-and-skills-for-experience-d.md) | agent, episodic, retrieval |
| 2026-06-04 | arXiv | [Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads](content/papers/agent-memory-characterization-and-system-implications-of-stateful-long-horizon-w.md) | agent, benchmark, retrieval |
| 2026-06-04 | arXiv | [AdaMEM: Test-Time Adaptive Memory for Language Agents](content/papers/adamem-test-time-adaptive-memory-for-language-agents.md) | agent, long-term, retrieval |
| 2026-06-04 | arXiv | [AIS-Based Vessel Trajectory Prediction Using Memory-Augmented Neural Networks](content/papers/ais-based-vessel-trajectory-prediction-using-memory-augmented-neural-networks.md) | memory-augmented |
| 2026-06-03 | arXiv | [memorywire: A Vendor-Neutral Wire Format for Agent Memory Operations](content/papers/memorywire-a-vendor-neutral-wire-format-for-agent-memory-operations.md) | agent, benchmark, context |
| 2026-06-03 | arXiv | [Towards Verifiable Multimodal Deep Research: A Multi-Agent Harness for Interleaved Report Generation](content/papers/towards-verifiable-multimodal-deep-research-a-multi-agent-harness-for-interleave.md) | agent, benchmark |
| 2026-06-03 | arXiv | [Temporal Order Matters for Agentic Memory: Segment Trees for Long-Horizon Agents](content/papers/temporal-order-matters-for-agentic-memory-segment-trees-for-long-horizon-agents.md) | agent, benchmark, context |
| 2026-06-03 | arXiv | [Scaling Self-Evolving Agents via Parametric Memory](content/papers/scaling-self-evolving-agents-via-parametric-memory.md) | agent, context, retrieval |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
