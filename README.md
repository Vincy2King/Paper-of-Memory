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

- Total tracked papers: **213**
- Last generated: **2026-05-14**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **178**
- OpenReview: **34**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-05-13 | arXiv | [Useful Memories Become Faulty When Continuously Updated by LLMs](content/papers/useful-memories-become-faulty-when-continuously-updated-by-llms.md) | agent, episodic |
| 2026-05-13 | arXiv | [RealICU: Do LLM Agents Understand Long-Context ICU Data? A Benchmark Beyond Behavior Imitation](content/papers/realicu-do-llm-agents-understand-long-context-icu-data-a-benchmark-beyond-behavi.md) | agent, benchmark, context |
| 2026-05-13 | arXiv | [ReTool-Video: Recursive Tool-Using Video Agents with Meta-Augmented Tool Grounding](content/papers/retool-video-recursive-tool-using-video-agents-with-meta-augmented-tool-groundin.md) | agent, retrieval |
| 2026-05-13 | arXiv | [NAACA: Training-Free NeuroAuditory Attentive Cognitive Architecture with Oscillatory Working Memory for Salience-Driven Attention Gating](content/papers/naaca-training-free-neuroauditory-attentive-cognitive-architecture-with-oscillat.md) | working memory |
| 2026-05-13 | arXiv | [Model-Agnostic Lifelong LLM Safety via Externalized Attack-Defense Co-Evolution](content/papers/model-agnostic-lifelong-llm-safety-via-externalized-attack-defense-co-evolution.md) | retrieval |
| 2026-05-13 | arXiv | [McCast: Memory-Guided Latent Drift Correction for Long-Horizon Precipitation Nowcasting](content/papers/mccast-memory-guided-latent-drift-correction-for-long-horizon-precipitation-nowc.md) | benchmark, retrieval |
| 2026-05-13 | arXiv | [Key-Value Means: Transformers with Expandable Block-Recurrent Compressed Memory](content/papers/key-value-means-transformers-with-expandable-block-recurrent-compressed-memory.md) | context |
| 2026-05-13 | arXiv | [Exploring Interaction Paradigms for LLM Agents in Scientific Visualization](content/papers/exploring-interaction-paradigms-for-llm-agents-in-scientific-visualization.md) | agent, benchmark, context |
| 2026-05-13 | arXiv | [Cognifold: Always-On Proactive Memory via Cognitive Folding](content/papers/cognifold-always-on-proactive-memory-via-cognitive-folding.md) | agent, benchmark, retrieval |
| 2026-05-13 | arXiv | [A Hierarchical Language Model with Predictable Scaling Laws and Provable Benefits of Reasoning](content/papers/a-hierarchical-language-model-with-predictable-scaling-laws-and-provable-benefit.md) | context |
| 2026-05-12 | arXiv | [SkillGraph: Skill-Augmented Reinforcement Learning for Agents via Evolving Skill Graphs](content/papers/skillgraph-skill-augmented-reinforcement-learning-for-agents-via-evolving-skill-.md) | agent |
| 2026-05-12 | arXiv | [SAGE: A Self-Evolving Agentic Graph-Memory Engine for Structure-Aware Associative Memory](content/papers/sage-a-self-evolving-agentic-graph-memory-engine-for-structure-aware-associative.md) | agent, benchmark, long-term |
| 2026-05-12 | arXiv | [Retrieve-then-Steer: Online Success Memory for Test-Time Adaptation of Generative VLAs](content/papers/retrieve-then-steer-online-success-memory-for-test-time-adaptation-of-generative.md) | long-term, retrieval |
| 2026-05-12 | arXiv | [Mitigating Context-Memory Conflicts in LLMs through Dynamic Cognitive Reconciliation Decoding](content/papers/mitigating-context-memory-conflicts-in-llms-through-dynamic-cognitive-reconcilia.md) | benchmark, context |
| 2026-05-12 | arXiv | [MemQ: Integrating Q-Learning into Self-Evolving Memory Agents over Provenance DAGs](content/papers/memq-integrating-q-learning-into-self-evolving-memory-agents-over-provenance-dag.md) | agent, benchmark, context |
| 2026-05-12 | arXiv | [MedMemoryBench: Benchmarking Agent Memory in Personalized Healthcare](content/papers/medmemorybench-benchmarking-agent-memory-in-personalized-healthcare.md) | agent, benchmark, conversation |
| 2026-05-12 | arXiv | [LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues](content/papers/longmemeval-v2-evaluating-long-term-agent-memory-toward-experienced-colleagues.md) | agent, benchmark, context |
| 2026-05-12 | arXiv | [Improving the Performance and Learning Stability of Parallelizable RNNs Designed for Ultra-Low Power Applications](content/papers/improving-the-performance-and-learning-stability-of-parallelizable-rnns-designed.md) | benchmark, long-term |
| 2026-05-12 | arXiv | [Goal-Oriented Reasoning for RAG-based Memory in Conversational Agentic LLM Systems](content/papers/goal-oriented-reasoning-for-rag-based-memory-in-conversational-agentic-llm-syste.md) | agent, context, conversation |
| 2026-05-12 | arXiv | [GRC: Unifying Reasoning-Driven Generation, Retrieval and Compression](content/papers/grc-unifying-reasoning-driven-generation-retrieval-and-compression.md) | agent, benchmark, compression |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
