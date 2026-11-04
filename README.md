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

- Total tracked papers: **1577**
- Last generated: **2026-11-04**

## Papers by Source

- ACL Anthology: **17**
- arXiv: **1414**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-11-02 | arXiv | [When Prediction Shapes the Future: A BlueSky Agenda for Reflexive Time Series Analysis](content/papers/when-prediction-shapes-the-future-a-bluesky-agenda-for-reflexive-time-series-ana.md) | agent, context |
| 2026-11-02 | arXiv | [Top-$k$ Retrieval Leaves Memory Value Undetermined](content/papers/top-k-retrieval-leaves-memory-value-undetermined.md) | agent, benchmark, retrieval |
| 2026-11-02 | arXiv | [InteractionBench: Measuring Timing, Task Accuracy, Whisper and Volume, and Grounding in Real-Time Voice Systems](content/papers/interactionbench-measuring-timing-task-accuracy-whisper-and-volume-and-grounding.md) | benchmark, conversation |
| 2026-11-02 | arXiv | [Chain on Demand: Deferred Evidence Organization for Long-Term Conversational Memory](content/papers/chain-on-demand-deferred-evidence-organization-for-long-term-conversational-memo.md) | conversation, long-term, retrieval |
| 2026-11-02 | arXiv | [Agent Memory as Rate-Limited Filtering: Explicit State Outlasts Long Context Beyond a Reader-Dependent Horizon](content/papers/agent-memory-as-rate-limited-filtering-explicit-state-outlasts-long-context-beyo.md) | agent, benchmark, context |
| 2026-11-02 | arXiv | [A State Change Is Local, Its Consequences Are Not: Dependency-Aware State Revision for Long-Term Agent Memory](content/papers/a-state-change-is-local-its-consequences-are-not-dependency-aware-state-revision.md) | agent, benchmark, long-term |
| 2026-11-01 | arXiv | [SPAR: Experience-Driven Strategy Evolution in Multi-Session B2B Sales](content/papers/spar-experience-driven-strategy-evolution-in-multi-session-b2b-sales.md) | agent, context, episodic |
| 2026-11-01 | arXiv | [MemHarmBench: Evaluating Cross-Session Prompt Injection in Memory-Persistent AI Agents](content/papers/memharmbench-evaluating-cross-session-prompt-injection-in-memory-persistent-ai-a.md) | agent, benchmark |
| 2026-11-01 | arXiv | [Learning by Doing: Autonomously Compiling and Curating Agent Skills from Verified Traces](content/papers/learning-by-doing-autonomously-compiling-and-curating-agent-skills-from-verified.md) | agent, benchmark, episodic |
| 2026-11-01 | arXiv | [EvoRec: A Unified Self-Evolving Agentic Recommender with Dynamic Reflection Trees](content/papers/evorec-a-unified-self-evolving-agentic-recommender-with-dynamic-reflection-trees.md) | agent, long-term, retrieval |
| 2026-11-01 | arXiv | [Delivered, Not Used: Evaluating Agent Memory at Its Point of Use](content/papers/delivered-not-used-evaluating-agent-memory-at-its-point-of-use.md) | agent, retrieval |
| 2026-10-31 | arXiv | [Who Schedules Agent Memory? A Sidecar Approach to Long-Horizon Tasks](content/papers/who-schedules-agent-memory-a-sidecar-approach-to-long-horizon-tasks.md) | agent, retrieval |
| 2026-10-31 | arXiv | [Trail: Accurate Local Smart Home Control Using Decision Models](content/papers/trail-accurate-local-smart-home-control-using-decision-models.md) | conversation |
| 2026-10-31 | arXiv | [Pulse: Long-Horizon Tasks Need Streaming Personalization](content/papers/pulse-long-horizon-tasks-need-streaming-personalization.md) | agent, long-term |
| 2026-10-30 | arXiv | [When History Overrides Intent: Relational Schema Lock-In in Human-LLM Interaction](content/papers/when-history-overrides-intent-relational-schema-lock-in-in-human-llm-interaction.md) | context |
| 2026-10-30 | arXiv | [Unlimited OCR Works 2](content/papers/unlimited-ocr-works-2.md) | benchmark, context |
| 2026-10-30 | arXiv | [RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory](content/papers/roboarchitect-automating-the-design-of-robotic-agents-with-persistent-memory.md) | agent, benchmark |
| 2026-10-30 | arXiv | [RAMA: Retrieval-Augmented Multi-Agent Routing with Episodic Memory for LEO Satellite Networks](content/papers/rama-retrieval-augmented-multi-agent-routing-with-episodic-memory-for-leo-satell.md) | agent, episodic, retrieval |
| 2026-10-30 | arXiv | [Quantifying Local and Global Fidelity of Nonlinear Embeddings](content/papers/quantifying-local-and-global-fidelity-of-nonlinear-embeddings.md) | agent |
| 2026-10-30 | arXiv | [ORION: An Outcome-Driven LLM Advisor for RL-Based Multi-Domain 6G Slice Placement](content/papers/orion-an-outcome-driven-llm-advisor-for-rl-based-multi-domain-6g-slice-placement.md) | agent, episodic |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
