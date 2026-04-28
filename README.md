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

- Total tracked papers: **88**
- Last generated: **2026-04-28**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **56**
- OpenReview: **31**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-04-28 | OpenReview | [PlugMem: A Task-Agnostic Plugin Memory Module for LLM Agents](content/papers/plugmem-a-task-agnostic-plugin-memory-module-for-llm-agents.md) | agent, benchmark, context |
| 2026-04-27 | arXiv | [The AI Codebase Maturity Model: From Assisted Coding to Fully Autonomous Systems](content/papers/the-ai-codebase-maturity-model-from-assisted-coding-to-fully-autonomous-systems.md) | agent |
| 2026-04-27 | arXiv | [TSAssistant: A Human-in-the-Loop Agentic Framework for Automated Target Safety Assessment](content/papers/tsassistant-a-human-in-the-loop-agentic-framework-for-automated-target-safety-as.md) | agent, conversation |
| 2026-04-27 | arXiv | [Poster: ClawdGo: Endogenous Security Awareness Training for Autonomous AI Agents](content/papers/poster-clawdgo-endogenous-security-awareness-training-for-autonomous-ai-agents.md) | agent |
| 2026-04-26 | arXiv | [ZenBrain: A Neuroscience-Inspired 7-Layer Memory Architecture for Autonomous AI Systems](content/papers/zenbrain-a-neuroscience-inspired-7-layer-memory-architecture-for-autonomous-ai-s.md) | agent, context, episodic |
| 2026-04-26 | arXiv | [PRISM: Probing Reasoning, Instruction, and Source Memory in LLM Hallucinations](content/papers/prism-probing-reasoning-instruction-and-source-memory-in-llm-hallucinations.md) | agent, benchmark, conversation |
| 2026-04-26 | arXiv | [Masked by Consensus: Disentangling Privileged Knowledge in LLM Correctness](content/papers/masked-by-consensus-disentangling-privileged-knowledge-in-llm-correctness.md) | retrieval |
| 2026-04-26 | arXiv | [GraphPlanner: Graph Memory-Augmented Agentic Routing for Multi-Agent LLMs](content/papers/graphplanner-graph-memory-augmented-agentic-routing-for-multi-agent-llms.md) | agent |
| 2026-04-25 | OpenReview | [WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance](content/papers/webcoach-self-evolving-web-agents-with-cross-session-memory-guidance.md) | agent, benchmark, context |
| 2026-04-25 | OpenReview | [PROCED-MEM: BENCHMARKING PROCEDURAL MEMORY RETRIEVAL IN LANGUAGE AGENTS ACROSS DOMAINS](content/papers/proced-mem-benchmarking-procedural-memory-retrieval-in-language-agents-across-do.md) | agent, benchmark, context |
| 2026-04-25 | OpenReview | [MemoGraph: Augmenting LLMs with Explicit Episodic Memory for Multi-step Mathematical Reasoning](content/papers/memograph-augmenting-llms-with-explicit-episodic-memory-for-multi-step-mathemati.md) | agent, benchmark, context |
| 2026-04-25 | OpenReview | [MEMORY IS RECONSTRUCTED, NOT RETRIEVED: GRAPH MEMORY FOR LLM AGENTS](content/papers/memory-is-reconstructed-not-retrieved-graph-memory-for-llm-agents.md) | agent, benchmark, context |
| 2026-04-25 | OpenReview | [Learning Safe Robot Planning from Unsafe Experiences: An Episodic Memory Approach for LLM-based Agents](content/papers/learning-safe-robot-planning-from-unsafe-experiences-an-episodic-memory-approach.md) | agent, episodic, retrieval |
| 2026-04-25 | arXiv | [From Stateless Queries to Autonomous Actions: A Layered Security Framework for Agentic AI Systems](content/papers/from-stateless-queries-to-autonomous-actions-a-layered-security-framework-for-ag.md) | agent, benchmark, long-term |
| 2026-04-25 | OpenReview | [Episodic Memory from Compression Boundaries in Latent Representation Space](content/papers/episodic-memory-from-compression-boundaries-in-latent-representation-space.md) | agent, compression, context |
| 2026-04-25 | OpenReview | [ENGRAM: Effective, Lightweight Memory Orchestration for Conversational Agents](content/papers/engram-effective-lightweight-memory-orchestration-for-conversational-agents.md) | agent, benchmark, context |
| 2026-04-25 | OpenReview | [Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory](content/papers/diagnosing-retrieval-vs-utilization-bottlenecks-in-llm-agent-memory.md) | agent, context, retrieval |
| 2026-04-25 | OpenReview | [CloneMem: Benchmarking Long-Term Memory for AI Clones](content/papers/clonemem-benchmarking-long-term-memory-for-ai-clones.md) | agent, benchmark, conversation |
| 2026-04-25 | OpenReview | [AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications](content/papers/ama-bench-evaluating-long-horizon-memory-for-agentic-applications.md) | agent, benchmark, retrieval |
| 2026-04-25 | arXiv | [AI Identity: Standards, Gaps, and Research Directions for AI Agents](content/papers/ai-identity-standards-gaps-and-research-directions-for-ai-agents.md) | agent |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
