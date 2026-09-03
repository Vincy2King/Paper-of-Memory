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

- Total tracked papers: **1080**
- Last generated: **2026-09-03**

## Papers by Source

- ACL Anthology: **5**
- arXiv: **933**
- OpenReview: **142**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-09-02 | arXiv | [PhoenixNest-Video: Evidence-Grounded Multimodal Agent Framework for Automated Video Interview Assessment](content/papers/phoenixnest-video-evidence-grounded-multimodal-agent-framework-for-automated-vid.md) | agent, retrieval |
| 2026-09-02 | arXiv | [NS-Copilot: An LLM-Driven Agent System for Autonomous Neuroscience Analysis](content/papers/ns-copilot-an-llm-driven-agent-system-for-autonomous-neuroscience-analysis.md) | agent, benchmark |
| 2026-09-02 | arXiv | [InsightSeg: Reusing Correction Insights for Guideline-Consistent Segmentation](content/papers/insightseg-reusing-correction-insights-for-guideline-consistent-segmentation.md) | agent, episodic |
| 2026-09-02 | arXiv | [CAPTURE: Disentangling Preference Drift from Memory Poisoning in Personalized LLM Agents](content/papers/capture-disentangling-preference-drift-from-memory-poisoning-in-personalized-llm.md) | agent, benchmark, context |
| 2026-09-02 | arXiv | [APEx: Distillation of Agent Procedural Experience for Adaptive Deep Research Question Answering](content/papers/apex-distillation-of-agent-procedural-experience-for-adaptive-deep-research-ques.md) | agent, benchmark |
| 2026-09-02 | arXiv | [AGI Maze Prediction Datasets: A Compact Benchmark for Learning World Dynamics with Transformers](content/papers/agi-maze-prediction-datasets-a-compact-benchmark-for-learning-world-dynamics-wit.md) | benchmark |
| 2026-09-01 | arXiv | [Zeta-Lite: A Concurrent, Branchable In-Browser SQL Database for Agentic Memory](content/papers/zeta-lite-a-concurrent-branchable-in-browser-sql-database-for-agentic-memory.md) | agent |
| 2026-09-01 | arXiv | [The Memory Trust Gap: Capability-Dependent Failures in Persistent-Memory Agents](content/papers/the-memory-trust-gap-capability-dependent-failures-in-persistent-memory-agents.md) | agent, benchmark |
| 2026-09-01 | arXiv | [Replacing Training with Memory: Listwise Selection for Text-to-SQL](content/papers/replacing-training-with-memory-listwise-selection-for-text-to-sql.md) | benchmark |
| 2026-09-01 | arXiv | [MutMem-V2: Cryptographically Authorized Mutation in Persistent Agent Memory Portable Verification and Reproducible Evidence](content/papers/mutmem-v2-cryptographically-authorized-mutation-in-persistent-agent-memory-porta.md) | agent |
| 2026-09-01 | arXiv | [ClinTraceBench: Source-Verifiable Longitudinal Clinical Reasoning over EHR-Derived Dialogues](content/papers/clintracebench-source-verifiable-longitudinal-clinical-reasoning-over-ehr-derive.md) | agent, compression, context |
| 2026-09-01 | OpenReview | [CIRCUIT Memory: Confidence-Aware Multi-Axis Retrieval for Episodic Memory in LLM Agents](content/papers/circuit-memory-confidence-aware-multi-axis-retrieval-for-episodic-memory-in-llm-.md) | agent, episodic, retrieval |
| 2026-09-01 | arXiv | [Agent Memory Is a Surface for Endogenous Authorization Laundering](content/papers/agent-memory-is-a-surface-for-endogenous-authorization-laundering.md) | agent |
| 2026-09-01 | arXiv | [ARISE-RL: Agentic Rubric-Grounded Iterative Self-Evolution with Reinforcement Learning](content/papers/arise-rl-agentic-rubric-grounded-iterative-self-evolution-with-reinforcement-lea.md) | agent, benchmark |
| 2026-08-31 | arXiv | [When Errors Become Memories: Causal Pathway Tracing in Multi-Turn Memory-Augmented LLMs](content/papers/when-errors-become-memories-causal-pathway-tracing-in-multi-turn-memory-augmente.md) | long-term |
| 2026-08-31 | arXiv | [UTILMEM: Benchmarking Evidence Utilization in Long-Term Conversational Memory](content/papers/utilmem-benchmarking-evidence-utilization-in-long-term-conversational-memory.md) | agent, benchmark, conversation |
| 2026-08-31 | arXiv | [The Optimizer Is the Agent: Reasoning-Driven Search across Prompts, Programs, and ML Workflows](content/papers/the-optimizer-is-the-agent-reasoning-driven-search-across-prompts-programs-and-m.md) | agent |
| 2026-08-31 | arXiv | [Strong Drafts Need Compact Memories: Long-Context Speculative Decoding with Compressed KV Cache](content/papers/strong-drafts-need-compact-memories-long-context-speculative-decoding-with-compr.md) | agent, context |
| 2026-08-31 | arXiv | [Slow to See, Slow to Suppress: Understanding the Effects of Modality in Context-Memory Conflicts](content/papers/slow-to-see-slow-to-suppress-understanding-the-effects-of-modality-in-context-me.md) | context, retrieval |
| 2026-08-31 | arXiv | [Measure Before You Manage: Evaluating Agent Working Memory in Coding Agents](content/papers/measure-before-you-manage-evaluating-agent-working-memory-in-coding-agents.md) | agent, compression, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
