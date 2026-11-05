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

- Total tracked papers: **1598**
- Last generated: **2026-11-05**

## Papers by Source

- ACL Anthology: **24**
- arXiv: **1428**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-11-03 | arXiv | [The Right Source Is Not Enough: Understanding History Interference in Speech-LLM Memory](content/papers/the-right-source-is-not-enough-understanding-history-interference-in-speech-llm-.md) | context, conversation, retrieval |
| 2026-11-03 | arXiv | [The Price of Scale in Proactive Memory Recall](content/papers/the-price-of-scale-in-proactive-memory-recall.md) | benchmark |
| 2026-11-03 | arXiv | [Sketchpad: certified exact arithmetic with a small vision-language model](content/papers/sketchpad-certified-exact-arithmetic-with-a-small-vision-language-model.md) | working memory |
| 2026-11-03 | arXiv | [One Assistant, Many Memories: Benchmarking Real-World Group Assistance When Recall Is Not Enough](content/papers/one-assistant-many-memories-benchmarking-real-world-group-assistance-when-recall.md) | agent, benchmark, context |
| 2026-11-03 | arXiv | [ModelBlaster: Closing the Performance Gap through Learning-Augmented Agents Across Models, Kernels and Hardware Backends](content/papers/modelblaster-closing-the-performance-gap-through-learning-augmented-agents-acros.md) | agent, context |
| 2026-11-03 | arXiv | [MINDSET: Energy-based Memory Evolution for Long Conversational Agents](content/papers/mindset-energy-based-memory-evolution-for-long-conversational-agents.md) | agent, context, conversation |
| 2026-11-03 | arXiv | [HARP: Training-Free Dual-Profile Agentic Communication for LLM-Based Recommendation](content/papers/harp-training-free-dual-profile-agentic-communication-for-llm-based-recommendati.md) | agent, benchmark, context |
| 2026-11-03 | arXiv | [From Autonomous Agents to Cognitive Symbionts: Toward AI-Augmented Human Intelligence](content/papers/from-autonomous-agents-to-cognitive-symbionts-toward-ai-augmented-human-intellig.md) | agent, context |
| 2026-11-03 | arXiv | [Drift No More: Spectral Locking for Long-Horizon Open-Weight Multi-Agent AI](content/papers/drift-no-more-spectral-locking-for-long-horizon-open-weight-multi-agent-ai.md) | agent, retrieval |
| 2026-11-03 | arXiv | [Clocks all the way down: does sequence-processing AI need endogenous temporal structure?](content/papers/clocks-all-the-way-down-does-sequence-processing-ai-need-endogenous-temporal-str.md) | retrieval |
| 2026-11-02 | arXiv | [When Prediction Shapes the Future: A BlueSky Agenda for Reflexive Time Series Analysis](content/papers/when-prediction-shapes-the-future-a-bluesky-agenda-for-reflexive-time-series-ana.md) | agent, context |
| 2026-11-02 | arXiv | [What Is This Memory Useful For? Measuring Task-Conditioned Utility in Long-Term Agent Memory](content/papers/what-is-this-memory-useful-for-measuring-task-conditioned-utility-in-long-term-a.md) | agent, benchmark, compression |
| 2026-11-02 | arXiv | [Top-$k$ Retrieval Leaves Memory Value Undetermined](content/papers/top-k-retrieval-leaves-memory-value-undetermined.md) | agent, benchmark, retrieval |
| 2026-11-02 | arXiv | [Rethinking Next-Visit Diagnosis Prediction Beyond Aggregate Metrics: Retrieval--Memory Multi-Agent Adjudication](content/papers/rethinking-next-visit-diagnosis-prediction-beyond-aggregate-metrics-retrieval-me.md) | agent, retrieval |
| 2026-11-02 | arXiv | [InteractionBench: Measuring Timing, Task Accuracy, Whisper and Volume, and Grounding in Real-Time Voice Systems](content/papers/interactionbench-measuring-timing-task-accuracy-whisper-and-volume-and-grounding.md) | benchmark, conversation |
| 2026-11-02 | arXiv | [EvoMemState: Evolving Memory State for Personal Agents](content/papers/evomemstate-evolving-memory-state-for-personal-agents.md) | agent, benchmark, long-term |
| 2026-11-02 | arXiv | [EvoGroup: A Self-Evolving Harness for Group Agents in Shared Contexts](content/papers/evogroup-a-self-evolving-harness-for-group-agents-in-shared-contexts.md) | agent, context, long-term |
| 2026-11-02 | arXiv | [Chain on Demand: Deferred Evidence Organization for Long-Term Conversational Memory](content/papers/chain-on-demand-deferred-evidence-organization-for-long-term-conversational-memo.md) | conversation, long-term, retrieval |
| 2026-11-02 | arXiv | [Agent Memory as Rate-Limited Filtering: Explicit State Outlasts Long Context Beyond a Reader-Dependent Horizon](content/papers/agent-memory-as-rate-limited-filtering-explicit-state-outlasts-long-context-beyo.md) | agent, benchmark, context |
| 2026-11-02 | arXiv | [A State Change Is Local, Its Consequences Are Not: Dependency-Aware State Revision for Long-Term Agent Memory](content/papers/a-state-change-is-local-its-consequences-are-not-dependency-aware-state-revision.md) | agent, benchmark, long-term |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
