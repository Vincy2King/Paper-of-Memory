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

- Total tracked papers: **1093**
- Last generated: **2026-09-05**

## Papers by Source

- ACL Anthology: **6**
- arXiv: **945**
- OpenReview: **142**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-09-03 | arXiv | [When Users Don't Ask: Benchmarking Context-Driven Memory Retrieval in Conversational Agents](content/papers/when-users-don-t-ask-benchmarking-context-driven-memory-retrieval-in-conversatio.md) | agent, benchmark, context |
| 2026-09-03 | arXiv | [VideoHarness-RSI: Recursive Harness Self-Improvement for Long-Video Understanding with Frozen Vision-Language Models](content/papers/videoharness-rsi-recursive-harness-self-improvement-for-long-video-understanding.md) | agent, benchmark, context |
| 2026-09-03 | arXiv | [Rethinking World Models for Safety-Critical Embodied Systems](content/papers/rethinking-world-models-for-safety-critical-embodied-systems.md) | episodic |
| 2026-09-03 | OpenReview | [Reason Before Remembering: An Entity-Centric Framework for Trustworthy Conversational Memory](content/papers/reason-before-remembering-an-entity-centric-framework-for-trustworthy-conversati.md) | context, conversation, retrieval |
| 2026-09-03 | OpenReview | [Profile-Graph Memory for LLM Agents: Implicit Cross-Entity Traversal through Narrative Profiles](content/papers/profile-graph-memory-for-llm-agents-implicit-cross-entity-traversal-through-narr.md) | agent, benchmark, compression |
| 2026-09-03 | arXiv | [Proactive Service Agents: A Unified Decision Framework, Methods, and Evaluation](content/papers/proactive-service-agents-a-unified-decision-framework-methods-and-evaluation.md) | agent, long-term |
| 2026-09-03 | arXiv | [Plan Pointers and Record-Directive Form in Budgeted Verification of Inherited Agent Memory](content/papers/plan-pointers-and-record-directive-form-in-budgeted-verification-of-inherited-ag.md) | agent |
| 2026-09-03 | arXiv | [Learning What Not to Forget: Long-Horizon Agent Memory from a Few Kilobytes of Learning](content/papers/learning-what-not-to-forget-long-horizon-agent-memory-from-a-few-kilobytes-of-le.md) | agent, context, conversation |
| 2026-09-03 | arXiv | [Fresh Memory, Stale Plans: Dependency-Scoped Validation for Distributed LLM-Agent Memory](content/papers/fresh-memory-stale-plans-dependency-scoped-validation-for-distributed-llm-agent-.md) | agent |
| 2026-09-03 | arXiv | [Decoupled Analysis-Judging: An Automated Creativity Evaluator Using LLMs in Complex Multi-step Creativity Tasks](content/papers/decoupled-analysis-judging-an-automated-creativity-evaluator-using-llms-in-compl.md) | context |
| 2026-09-03 | arXiv | [Bioinfoysis Technical Report](content/papers/bioinfoysis-technical-report.md) | agent, context |
| 2026-09-03 | arXiv | [Activation-Keyed Momentum: An Anisotropic Momentum Update via the Delta Rule](content/papers/activation-keyed-momentum-an-anisotropic-momentum-update-via-the-delta-rule.md) | persistent memory |
| 2026-09-02 | arXiv | [TRACE: Spatiotemporal Contact Memory Graph Network Simulator for Granular Dynamics](content/papers/trace-spatiotemporal-contact-memory-graph-network-simulator-for-granular-dynamic.md) | benchmark |
| 2026-09-02 | arXiv | [PhoenixNest-Video: Evidence-Grounded Multimodal Agent Framework for Automated Video Interview Assessment](content/papers/phoenixnest-video-evidence-grounded-multimodal-agent-framework-for-automated-vid.md) | agent, retrieval |
| 2026-09-02 | arXiv | [NS-Copilot: An LLM-Driven Agent System for Autonomous Neuroscience Analysis](content/papers/ns-copilot-an-llm-driven-agent-system-for-autonomous-neuroscience-analysis.md) | agent, benchmark |
| 2026-09-02 | arXiv | [MemoryLACE: Memory Lifecycle-Aware Consolidation and Evidence Retrieval](content/papers/memorylace-memory-lifecycle-aware-consolidation-and-evidence-retrieval.md) | agent, long-term, retrieval |
| 2026-09-02 | arXiv | [InsightSeg: Reusing Correction Insights for Guideline-Consistent Segmentation](content/papers/insightseg-reusing-correction-insights-for-guideline-consistent-segmentation.md) | agent, episodic |
| 2026-09-02 | arXiv | [CAPTURE: Disentangling Preference Drift from Memory Poisoning in Personalized LLM Agents](content/papers/capture-disentangling-preference-drift-from-memory-poisoning-in-personalized-llm.md) | agent, benchmark, context |
| 2026-09-02 | arXiv | [APEx: Distillation of Agent Procedural Experience for Adaptive Deep Research Question Answering](content/papers/apex-distillation-of-agent-procedural-experience-for-adaptive-deep-research-ques.md) | agent, benchmark |
| 2026-09-02 | arXiv | [AGI Maze Prediction Datasets: A Compact Benchmark for Learning World Dynamics with Transformers](content/papers/agi-maze-prediction-datasets-a-compact-benchmark-for-learning-world-dynamics-wit.md) | benchmark |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
