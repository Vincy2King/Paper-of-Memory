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

- Total tracked papers: **1476**
- Last generated: **2026-10-21**

## Papers by Source

- ACL Anthology: **6**
- arXiv: **1324**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-10-20 | arXiv | [When Does Experience Memory Help Closed-Loop LLM Driving Agents? A Controlled Evaluation with Resampled Warmup Pools, Token-Matched Fillers, and Audited Baselines](content/papers/when-does-experience-memory-help-closed-loop-llm-driving-agents-a-controlled-eva.md) | agent, episodic, retrieval |
| 2026-10-20 | arXiv | [SAFE-Mem: Secure Agentic Memory with Fine-Grained Authority and Governance-Aware Retrieval](content/papers/safe-mem-secure-agentic-memory-with-fine-grained-authority-and-governance-aware-.md) | agent, long-term, retrieval |
| 2026-10-20 | arXiv | [Recast the Past: Stable Long Video Generation with Full Context Memory](content/papers/recast-the-past-stable-long-video-generation-with-full-context-memory.md) | context |
| 2026-10-20 | arXiv | [Memory as Code: Declarative Retrieval over Codified Long-Term Memory](content/papers/memory-as-code-declarative-retrieval-over-codified-long-term-memory.md) | agent, long-term, retrieval |
| 2026-10-20 | arXiv | [Industrial ReMEmbR: Scaling Spatiotemporal Memory to Robot Fleets](content/papers/industrial-remembr-scaling-spatiotemporal-memory-to-robot-fleets.md) | agent, retrieval |
| 2026-10-20 | arXiv | [HABIT-Bench: Evaluating Habit Induction from Longitudinal Weak Evidence in Agent Memory](content/papers/habit-bench-evaluating-habit-induction-from-longitudinal-weak-evidence-in-agent-.md) | agent, conversation, long-term |
| 2026-10-20 | arXiv | [DuplexLedger: Benchmarking Transactional Memory in Full-Duplex Speech Agents](content/papers/duplexledger-benchmarking-transactional-memory-in-full-duplex-speech-agents.md) | agent, benchmark |
| 2026-10-20 | arXiv | [Disclosure Begets Disclosure: A Self-Reinforcing Privacy Loop in LLM Agents with Persistent Memory](content/papers/disclosure-begets-disclosure-a-self-reinforcing-privacy-loop-in-llm-agents-with-.md) | agent |
| 2026-10-20 | arXiv | [ClawMMU: Protection-Coherent Virtual Memory for Stateful LLM Agents](content/papers/clawmmu-protection-coherent-virtual-memory-for-stateful-llm-agents.md) | agent, context, long-term |
| 2026-10-20 | arXiv | [A Radiation-Hardened, Fault-Aware Quantized Neural Network That Self-Heals](content/papers/a-radiation-hardened-fault-aware-quantized-neural-network-that-self-heals.md) | benchmark |
| 2026-10-19 | arXiv | [Whose Credential Is It? How Owner Attribution in Agent MemoryShapes Cross-User Account Misuse](content/papers/whose-credential-is-it-how-owner-attribution-in-agent-memoryshapes-cross-user-ac.md) | agent, long-term |
| 2026-10-19 | arXiv | [The Geometry of Agent Memory: Forecasting Retrieval-Bound Memory Failures, and Characterizing Its Limits](content/papers/the-geometry-of-agent-memory-forecasting-retrieval-bound-memory-failures-and-cha.md) | agent, context, conversation |
| 2026-10-19 | arXiv | [Remembering Has a Price: Learning Memory Worth under Resource Constraints](content/papers/remembering-has-a-price-learning-memory-worth-under-resource-constraints.md) | agent, context, retrieval |
| 2026-10-19 | arXiv | [REM: What to Store, When to Recall, What to Forget in Experience Memory for Coding Agents](content/papers/rem-what-to-store-when-to-recall-what-to-forget-in-experience-memory-for-coding-.md) | agent, context, retrieval |
| 2026-10-19 | arXiv | [Procedural Memory for Language Agents: A Neurosymbolic Perspective on Explicit Goal Structure](content/papers/procedural-memory-for-language-agents-a-neurosymbolic-perspective-on-explicit-go.md) | agent, episodic |
| 2026-10-19 | arXiv | [ProMemAgent: Long-Horizon Proactive Assistance with Context-Aware Prospective Memory from Sensory Perceptions](content/papers/promemagent-long-horizon-proactive-assistance-with-context-aware-prospective-mem.md) | agent, benchmark, context |
| 2026-10-19 | arXiv | [Magnolia: A Persistent-Memory Agent Framework for Computational Chemistry](content/papers/magnolia-a-persistent-memory-agent-framework-for-computational-chemistry.md) | agent |
| 2026-10-19 | arXiv | [M-Plan: Comprehensive Planning For LLM Agents with Memory Arrangement](content/papers/m-plan-comprehensive-planning-for-llm-agents-with-memory-arrangement.md) | agent, context, long-term |
| 2026-10-19 | arXiv | [Learning Complementary Agent Groups via Task Hypergraphs for Next-POI Recommendation with Missing Modalities](content/papers/learning-complementary-agent-groups-via-task-hypergraphs-for-next-poi-recommenda.md) | agent |
| 2026-10-19 | arXiv | [LSTMem: Hierarchical Long Short-Term Online Memory for Large Language Models](content/papers/lstmem-hierarchical-long-short-term-online-memory-for-large-language-models.md) | agent, benchmark |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
