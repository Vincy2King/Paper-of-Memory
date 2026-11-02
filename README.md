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

- Total tracked papers: **1561**
- Last generated: **2026-11-02**

## Papers by Source

- ACL Anthology: **17**
- arXiv: **1398**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-10-30 | arXiv | [When History Overrides Intent: Relational Schema Lock-In in Human-LLM Interaction](content/papers/when-history-overrides-intent-relational-schema-lock-in-in-human-llm-interaction.md) | context |
| 2026-10-30 | arXiv | [Unlimited OCR Works 2](content/papers/unlimited-ocr-works-2.md) | benchmark, context |
| 2026-10-30 | arXiv | [RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory](content/papers/roboarchitect-automating-the-design-of-robotic-agents-with-persistent-memory.md) | agent, benchmark |
| 2026-10-30 | arXiv | [RAMA: Retrieval-Augmented Multi-Agent Routing with Episodic Memory for LEO Satellite Networks](content/papers/rama-retrieval-augmented-multi-agent-routing-with-episodic-memory-for-leo-satell.md) | agent, episodic, retrieval |
| 2026-10-30 | arXiv | [ORION: An Outcome-Driven LLM Advisor for RL-Based Multi-Domain 6G Slice Placement](content/papers/orion-an-outcome-driven-llm-advisor-for-rl-based-multi-domain-6g-slice-placement.md) | agent, episodic |
| 2026-10-30 | arXiv | [MUON-RT Reusing the Teacher's Trajectory for Momentum-Free Muon for LLM Self-Distillation](content/papers/muon-rt-reusing-the-teacher-s-trajectory-for-momentum-free-muon-for-llm-self-dis.md) | persistent memory |
| 2026-10-30 | arXiv | [MEMIG: Self-evolving Memory Construction for Antibody Optimization](content/papers/memig-self-evolving-memory-construction-for-antibody-optimization.md) | agent, context, retrieval |
| 2026-10-30 | arXiv | [KITE: Retrieval as a Decision Procedure for Long-Term Conversational Memory](content/papers/kite-retrieval-as-a-decision-procedure-for-long-term-conversational-memory.md) | agent, context, conversation |
| 2026-10-30 | arXiv | [GROME: GROunding Factorized MEmory into Video World Models](content/papers/grome-grounding-factorized-memory-into-video-world-models.md) | context, retrieval |
| 2026-10-29 | arXiv | [When Context Changes: Understanding Update Failures in LLMs](content/papers/when-context-changes-understanding-update-failures-in-llms.md) | agent, benchmark, context |
| 2026-10-29 | arXiv | [Unlimited OCR Works 2](content/papers/unlimited-ocr-works-2.md) | benchmark, context |
| 2026-10-29 | arXiv | [Topology Survives Shuffling: Robust Long-Context Memory Access Prediction for Graph Analytics](content/papers/topology-survives-shuffling-robust-long-context-memory-access-prediction-for-gra.md) | context |
| 2026-10-29 | arXiv | [The Price of Scale in Proactive Memory Recall](content/papers/the-price-of-scale-in-proactive-memory-recall.md) | benchmark |
| 2026-10-29 | arXiv | [The Cost of Working Memory in Streaming Mean Estimation](content/papers/the-cost-of-working-memory-in-streaming-mean-estimation.md) | compression |
| 2026-10-29 | arXiv | [MemSteer: Turning User Histories into Supervision for Agent Memory Optimization](content/papers/memsteer-turning-user-histories-into-supervision-for-agent-memory-optimization.md) | agent, context, retrieval |
| 2026-10-29 | arXiv | [Long-Term Agent Memory through Complementary Curation and Consolidation](content/papers/long-term-agent-memory-through-complementary-curation-and-consolidation.md) | agent, benchmark, episodic |
| 2026-10-29 | arXiv | [Judging Before Propagation: Task-Graph Contextual Integrity for Multi-Agent Privacy](content/papers/judging-before-propagation-task-graph-contextual-integrity-for-multi-agent-priva.md) | agent, benchmark, context |
| 2026-10-29 | arXiv | [HEMO: Harness Self-Evolution for Multi-Objective Combinatorial Optimization](content/papers/hemo-harness-self-evolution-for-multi-objective-combinatorial-optimization.md) | persistent memory |
| 2026-10-29 | arXiv | [GROME: GROunding Factorized MEmory into Video World Models](content/papers/grome-grounding-factorized-memory-into-video-world-models.md) | context, retrieval |
| 2026-10-29 | arXiv | [Finding Is Not Returning, Returning Is Not Reconstructing: A Multi-Dimensional Evaluation of Agent Social Re-entry](content/papers/finding-is-not-returning-returning-is-not-reconstructing-a-multi-dimensional-eva.md) | agent, context, conversation |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
