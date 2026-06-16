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

- Total tracked papers: **509**
- Last generated: **2026-06-16**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **428**
- OpenReview: **80**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-06-15 | OpenReview | [MEMPLANNER: Governing Long-Horizon Agency via Dynamic Memory Management and Planning](content/papers/memplanner-governing-long-horizon-agency-via-dynamic-memory-management-and-plann.md) | agent, context |
| 2026-06-15 | OpenReview | [GAMBIT: A Benchmark for Active Memory in Long-Horizon LLM Agents](content/papers/gambit-a-benchmark-for-active-memory-in-long-horizon-llm-agents.md) | agent, benchmark, context |
| 2026-06-15 | OpenReview | [Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems](content/papers/caching-for-the-future-scrub-jay-episodic-memory-principles-for-agent-memory-sys.md) | agent, benchmark, context |
| 2026-06-15 | OpenReview | [AgenticLOCI: A Multi-Agent Memory Framework for Conversational AI with Longitudinal Personalization](content/papers/agenticloci-a-multi-agent-memory-framework-for-conversational-ai-with-longitudin.md) | agent, benchmark, context |
| 2026-06-14 | OpenReview | [Renormalization Phenomenology in LLM Agent Memory Compression: Scaling Laws, Fixed Points, and Anomalous Summarization](content/papers/renormalization-phenomenology-in-llm-agent-memory-compression-scaling-laws-fixed.md) | agent, benchmark, compression |
| 2026-06-14 | OpenReview | [Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving Agent Memory](content/papers/memory-beyond-recall-a-dual-process-cognitive-memory-system-for-self-evolving-ag.md) | agent, benchmark, long-term |
| 2026-06-14 | arXiv | [Continuous Cross-Domain Traffic State Prediction via Memory-Augmented Graph Liquid Time-Constant Networks](content/papers/continuous-cross-domain-traffic-state-prediction-via-memory-augmented-graph-liqu.md) | memory-augmented |
| 2026-06-13 | OpenReview | [Schema-Mem: Structured and Evolving Memory for Long-term Conversational Knowledge](content/papers/schema-mem-structured-and-evolving-memory-for-long-term-conversational-knowledge.md) | agent, context, conversation |
| 2026-06-13 | OpenReview | [PersonaTree: Structured Lifecycle Memory for Person Understanding in LLM Agents](content/papers/personatree-structured-lifecycle-memory-for-person-understanding-in-llm-agents.md) | agent, benchmark, context |
| 2026-06-12 | arXiv | [VikingMem: A Memory Base Management System for Stateful LLM-based Applications](content/papers/vikingmem-a-memory-base-management-system-for-stateful-llm-based-applications.md) | agent, benchmark, compression |
| 2026-06-12 | arXiv | [StreamMemBench: Streaming Evaluation of Agent Memory for Future-Oriented Assistance](content/papers/streammembench-streaming-evaluation-of-agent-memory-for-future-oriented-assistan.md) | agent, benchmark |
| 2026-06-12 | OpenReview | [Reconstructing the Right Episode: Evaluating Interleaved Conversational Memory Beyond Long Context](content/papers/reconstructing-the-right-episode-evaluating-interleaved-conversational-memory-be.md) | benchmark, context, conversation |
| 2026-06-12 | arXiv | [Ontology Memory-Augmented ASR Correction for Long Text-Speech Interleaved Conversations](content/papers/ontology-memory-augmented-asr-correction-for-long-text-speech-interleaved-conver.md) | context, conversation |
| 2026-06-12 | arXiv | [Multi-Turn Reasoning When Context Arrives in Pieces: Scalable Sharding and Memory-Augmented RL](content/papers/multi-turn-reasoning-when-context-arrives-in-pieces-scalable-sharding-and-memory.md) | context, conversation |
| 2026-06-12 | arXiv | [MiniMax Sparse Attention](content/papers/minimax-sparse-attention.md) | agent, context, retrieval |
| 2026-06-12 | arXiv | [Knowledge Graph Enhanced Memory-Augmented Retrieval for Long Context Modeling](content/papers/knowledge-graph-enhanced-memory-augmented-retrieval-for-long-context-modeling.md) | context, retrieval |
| 2026-06-12 | arXiv | [GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge](content/papers/gitofthoughts-version-controlled-reasoning-and-agent-memory-you-can-replay-diff-.md) | agent, benchmark, context |
| 2026-06-12 | arXiv | [AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition](content/papers/agentspec-understanding-embodied-agent-scaffolds-through-controlled-composition.md) | agent |
| 2026-06-12 | OpenReview | [AIM: Constructing Adaptive Structured Memory via Agentic Information Management](content/papers/aim-constructing-adaptive-structured-memory-via-agentic-information-management.md) | agent, benchmark, long-term |
| 2026-06-11 | arXiv | [WISE: A Long-Horizon Agent in Minecraft with Why-Which Reasoning](content/papers/wise-a-long-horizon-agent-in-minecraft-with-why-which-reasoning.md) | agent, episodic, retrieval |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
