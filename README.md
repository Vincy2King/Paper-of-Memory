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

- Total tracked papers: **1550**
- Last generated: **2026-10-30**

## Papers by Source

- ACL Anthology: **17**
- arXiv: **1387**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
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
| 2026-10-29 | arXiv | [FIRME: Registry-Anchored Memory Graphs for Evolving, Heterogeneous Investor Knowledge](content/papers/firme-registry-anchored-memory-graphs-for-evolving-heterogeneous-investor-knowle.md) | context |
| 2026-10-29 | arXiv | [Don't Lose the Thread: Empowering Long-Horizon LLM Agents with Cognitive Resource Self-Allocation](content/papers/don-t-lose-the-thread-empowering-long-horizon-llm-agents-with-cognitive-resource.md) | agent, benchmark, context |
| 2026-10-29 | arXiv | [Cheap Retrieval and Observation Credit Assignment from One Quantity: The Value of Information](content/papers/cheap-retrieval-and-observation-credit-assignment-from-one-quantity-the-value-of.md) | context, retrieval |
| 2026-10-28 | arXiv | [Routed Continual Learning](content/papers/routed-continual-learning.md) | agent, context |
| 2026-10-28 | arXiv | [Multimodal Filesystem Memory For Long-Horizon Embodied Agents](content/papers/multimodal-filesystem-memory-for-long-horizon-embodied-agents.md) | agent, context, episodic |
| 2026-10-28 | arXiv | [Is it my preference? Role Grounding Attack against Agent's Memory via Social Interaction](content/papers/is-it-my-preference-role-grounding-attack-against-agent-s-memory-via-social-inte.md) | agent, context, conversation |
| 2026-10-28 | arXiv | [Episodic looking - using reinforcement learning to bias perception enhances few-shot and continual learning with protection from forgetting](content/papers/episodic-looking-using-reinforcement-learning-to-bias-perception-enhances-few-sh.md) | context, episodic, long-term |
| 2026-10-28 | arXiv | [CALM: Conflict-Aware Lifecycle Memory Governance for Long-Horizon Language Agents](content/papers/calm-conflict-aware-lifecycle-memory-governance-for-long-horizon-language-agents.md) | agent, retrieval |
| 2026-10-28 | arXiv | [Auditable Belief Updates as a Missing Safety Layer for LLM-Powered Multi-Agent Systems](content/papers/auditable-belief-updates-as-a-missing-safety-layer-for-llm-powered-multi-agent-s.md) | agent, retrieval |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
