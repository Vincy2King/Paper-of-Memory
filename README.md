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

- Total tracked papers: **472**
- Last generated: **2026-06-09**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **392**
- OpenReview: **79**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-06-08 | arXiv | [Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents](content/papers/memory-beyond-recall-a-dual-process-cognitive-memory-system-for-self-evolving-ll.md) | agent, benchmark, long-term |
| 2026-06-08 | arXiv | [MASS: Deep Research for Social Sciences with Memory-Augmented Social Simulation](content/papers/mass-deep-research-for-social-sciences-with-memory-augmented-social-simulation.md) | agent, retrieval |
| 2026-06-08 | arXiv | [H2HMem: A Multimodal Memory Benchmark for Agents in Human-Human Interactions](content/papers/h2hmem-a-multimodal-memory-benchmark-for-agents-in-human-human-interactions.md) | agent, benchmark, conversation |
| 2026-06-08 | arXiv | [A Survey on Large Language Model-Based Game Agents](content/papers/a-survey-on-large-language-model-based-game-agents.md) | agent, context |
| 2026-06-07 | OpenReview | [OP-Bench: Benchmarking Over-Personalization for Memory-Augmented Personalized Conversational Agents](content/papers/op-bench-benchmarking-over-personalization-for-memory-augmented-personalized-con.md) | agent, benchmark, conversation |
| 2026-06-07 | OpenReview | [MemMA: Coordinating the Memory Cycle through Multi-Agent Reasoning and In-Situ Self-Evolution](content/papers/memma-coordinating-the-memory-cycle-through-multi-agent-reasoning-and-in-situ-se.md) | agent, retrieval |
| 2026-06-07 | OpenReview | [LiCoMemory: Lightweight and Cognitive Agentic Memory for Efficient Long-Term Reasoning](content/papers/licomemory-lightweight-and-cognitive-agentic-memory-for-efficient-long-term-reas.md) | agent, benchmark, context |
| 2026-06-07 | OpenReview | [Knowledge Graph Enhanced Memory-Augmented Retrieval for Long Context Modeling](content/papers/knowledge-graph-enhanced-memory-augmented-retrieval-for-long-context-modeling.md) | context, retrieval |
| 2026-06-07 | OpenReview | [Knowledge Graph Enhanced Memory-Augmented Retrieval for Long Context Modeling](content/papers/knowledge-graph-enhanced-memory-augmented-retrieval-for-long-context-modeling.md) | context, retrieval |
| 2026-06-07 | OpenReview | [Injecting Context via Situation Working Memory for Logical Reasoning with LLMs](content/papers/injecting-context-via-situation-working-memory-for-logical-reasoning-with-llms.md) | context |
| 2026-06-07 | arXiv | [Harnessing Streaming Video in the Wild](content/papers/harnessing-streaming-video-in-the-wild.md) | benchmark, context, long-term |
| 2026-06-07 | arXiv | [Goal-Oriented Reasoning for RAG-based Memory in Conversational Agentic LLM Systems](content/papers/goal-oriented-reasoning-for-rag-based-memory-in-conversational-agentic-llm-syste.md) | agent, context, conversation |
| 2026-06-07 | OpenReview | [From Retrieval to Reconstruction: Constructing Evolvable Cognitive Memory for Long-term Dialogue](content/papers/from-retrieval-to-reconstruction-constructing-evolvable-cognitive-memory-for-lon.md) | context, long-term, retrieval |
| 2026-06-07 | OpenReview | [EMemBench: Interactive Benchmarking of Episodic Memory for VLM Agents](content/papers/emembench-interactive-benchmarking-of-episodic-memory-for-vlm-agents.md) | agent, benchmark, context |
| 2026-06-07 | OpenReview | [EMemBench: Interactive Benchmarking of Episodic Memory for VLM Agents](content/papers/emembench-interactive-benchmarking-of-episodic-memory-for-vlm-agents.md) | agent, benchmark, context |
| 2026-06-07 | OpenReview | [AutoViewMem: Self-Configuring Orthogonal Views for Conversational Long-Term Memory](content/papers/autoviewmem-self-configuring-orthogonal-views-for-conversational-long-term-memor.md) | agent, benchmark, conversation |
| 2026-06-07 | OpenReview | [AtomMem : Learnable Dynamic Agentic Memory with Atomic Memory Operation](content/papers/atommem-learnable-dynamic-agentic-memory-with-atomic-memory-operation.md) | agent, benchmark, context |
| 2026-06-06 | arXiv | [Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models](content/papers/light-interaction-training-free-inference-acceleration-for-interactive-video-wor.md) | context |
| 2026-06-06 | arXiv | [Improving the Performance and Learning Stability of Parallelizable RNNs Designed for Ultra-Low Power Applications](content/papers/improving-the-performance-and-learning-stability-of-parallelizable-rnns-designed.md) | benchmark, long-term |
| 2026-06-06 | arXiv | [Emergence World: A Platform for Evaluating Long-Horizon Multi-Agent Autonomy](content/papers/emergence-world-a-platform-for-evaluating-long-horizon-multi-agent-autonomy.md) | agent, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
