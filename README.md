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

- Total tracked papers: **1484**
- Last generated: **2026-10-22**

## Papers by Source

- ACL Anthology: **6**
- arXiv: **1332**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-10-21 | arXiv | [Uni-Mem: Learning a Long-Horizon Agentic Memory Manager with Unified Online Policy Optimization](content/papers/uni-mem-learning-a-long-horizon-agentic-memory-manager-with-unified-online-polic.md) | agent, long-term, retrieval |
| 2026-10-21 | arXiv | [Remembering Through Change: Provenance-Preserving Hypergraph Memory for Multimodal Agents](content/papers/remembering-through-change-provenance-preserving-hypergraph-memory-for-multimoda.md) | agent, benchmark, long-term |
| 2026-10-21 | arXiv | [MemoryTax: The Bitter Lesson of Agent Memory](content/papers/memorytax-the-bitter-lesson-of-agent-memory.md) | agent, context, conversation |
| 2026-10-21 | arXiv | [Memory-Centric Continual Learning for AI Agents](content/papers/memory-centric-continual-learning-for-ai-agents.md) | agent, context, long-term |
| 2026-10-21 | arXiv | [MOSAIC: An Omni-Modal Benchmark for Long-Term Memory and Cross-Modal Reasoning in Conversational Agents](content/papers/mosaic-an-omni-modal-benchmark-for-long-term-memory-and-cross-modal-reasoning-in.md) | agent, benchmark, conversation |
| 2026-10-21 | arXiv | [ChronoSynth: Constraint-Aware Question Synthesis over Temporal Knowledge Graphs](content/papers/chronosynth-constraint-aware-question-synthesis-over-temporal-knowledge-graphs.md) | memory-augmented |
| 2026-10-20 | arXiv | [When Does Experience Memory Help Closed-Loop LLM Driving Agents? A Controlled Evaluation with Resampled Warmup Pools, Token-Matched Fillers, and Audited Baselines](content/papers/when-does-experience-memory-help-closed-loop-llm-driving-agents-a-controlled-eva.md) | agent, episodic, retrieval |
| 2026-10-20 | arXiv | [SAFE-Mem: Secure Agentic Memory with Fine-Grained Authority and Governance-Aware Retrieval](content/papers/safe-mem-secure-agentic-memory-with-fine-grained-authority-and-governance-aware-.md) | agent, long-term, retrieval |
| 2026-10-20 | arXiv | [Recast the Past: Stable Long Video Generation with Full Context Memory](content/papers/recast-the-past-stable-long-video-generation-with-full-context-memory.md) | context |
| 2026-10-20 | arXiv | [PerMIT: Securing Persistent Memory for LLM Agents via Machine-Checked Integrity Theorems and Scalable Community Trust](content/papers/permit-securing-persistent-memory-for-llm-agents-via-machine-checked-integrity-t.md) | agent |
| 2026-10-20 | arXiv | [Memory as Code: Declarative Retrieval over Codified Long-Term Memory](content/papers/memory-as-code-declarative-retrieval-over-codified-long-term-memory.md) | agent, long-term, retrieval |
| 2026-10-20 | arXiv | [Industrial ReMEmbR: Scaling Spatiotemporal Memory to Robot Fleets](content/papers/industrial-remembr-scaling-spatiotemporal-memory-to-robot-fleets.md) | agent, retrieval |
| 2026-10-20 | arXiv | [HABIT-Bench: Evaluating Habit Induction from Longitudinal Weak Evidence in Agent Memory](content/papers/habit-bench-evaluating-habit-induction-from-longitudinal-weak-evidence-in-agent-.md) | agent, conversation, long-term |
| 2026-10-20 | arXiv | [DuplexLedger: Benchmarking Transactional Memory in Full-Duplex Speech Agents](content/papers/duplexledger-benchmarking-transactional-memory-in-full-duplex-speech-agents.md) | agent, benchmark |
| 2026-10-20 | arXiv | [Disclosure Begets Disclosure: A Self-Reinforcing Privacy Loop in LLM Agents with Persistent Memory](content/papers/disclosure-begets-disclosure-a-self-reinforcing-privacy-loop-in-llm-agents-with-.md) | agent |
| 2026-10-20 | arXiv | [Combining Long-Term Memory and LLMs Comes at a High Cost: From Prompt Injection to Persistent Compromise](content/papers/combining-long-term-memory-and-llms-comes-at-a-high-cost-from-prompt-injection-t.md) | context, conversation, long-term |
| 2026-10-20 | arXiv | [ClawMMU: Protection-Coherent Virtual Memory for Stateful LLM Agents](content/papers/clawmmu-protection-coherent-virtual-memory-for-stateful-llm-agents.md) | agent, context, long-term |
| 2026-10-20 | arXiv | [A Radiation-Hardened, Fault-Aware Quantized Neural Network That Self-Heals](content/papers/a-radiation-hardened-fault-aware-quantized-neural-network-that-self-heals.md) | benchmark |
| 2026-10-19 | arXiv | [Whose Credential Is It? How Owner Attribution in Agent MemoryShapes Cross-User Account Misuse](content/papers/whose-credential-is-it-how-owner-attribution-in-agent-memoryshapes-cross-user-ac.md) | agent, long-term |
| 2026-10-19 | arXiv | [The Geometry of Agent Memory: Forecasting Retrieval-Bound Memory Failures, and Characterizing Its Limits](content/papers/the-geometry-of-agent-memory-forecasting-retrieval-bound-memory-failures-and-cha.md) | agent, context, conversation |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
