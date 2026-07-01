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

- Total tracked papers: **612**
- Last generated: **2026-07-01**

## Papers by Source

- ACL Anthology: **4**
- arXiv: **517**
- OpenReview: **91**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-06-29 | arXiv | [Self-Evolving World Models for LLM Agent Planning](content/papers/self-evolving-world-models-for-llm-agent-planning.md) | agent, context, episodic |
| 2026-06-29 | OpenReview | [SHM-GATE: Structured Hierarchical Memory with Gated Admission for Multi-Agent LLM Hallucination Containment](content/papers/shm-gate-structured-hierarchical-memory-with-gated-admission-for-multi-agent-llm.md) | agent, benchmark, conversation |
| 2026-06-29 | arXiv | [Neural Subspace Reallocation: Continual Learning as Retrieval-Based Subspace Memory Management](content/papers/neural-subspace-reallocation-continual-learning-as-retrieval-based-subspace-memo.md) | benchmark, compression, retrieval |
| 2026-06-29 | arXiv | [Neural Procedural Memory: Empowering LLM Agents with Implicit Activation Steering](content/papers/neural-procedural-memory-empowering-llm-agents-with-implicit-activation-steering.md) | agent, benchmark, context |
| 2026-06-29 | arXiv | [MemLeak: Diagnosing Information Leaks in Multimodal Agent Memory](content/papers/memleak-diagnosing-information-leaks-in-multimodal-agent-memory.md) | agent, benchmark |
| 2026-06-29 | arXiv | [MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation](content/papers/memdelta-controlled-baselines-and-hidden-confounds-in-agent-memory-evaluation.md) | agent, context, retrieval |
| 2026-06-29 | arXiv | [ManimAgent: Self-Evolving Multimodal Agents for Visual Education](content/papers/manimagent-self-evolving-multimodal-agents-for-visual-education.md) | agent, episodic, retrieval |
| 2026-06-29 | arXiv | [Mandol: An Agglomerative Agent Memory System for Long-Term Conversations](content/papers/mandol-an-agglomerative-agent-memory-system-for-long-term-conversations.md) | agent, benchmark, context |
| 2026-06-29 | OpenReview | [MEMPLANNER: Governing Long-Horizon Agency via Dynamic Memory Management and Planning](content/papers/memplanner-governing-long-horizon-agency-via-dynamic-memory-management-and-plann.md) | agent, context |
| 2026-06-29 | arXiv | [LLM Agents Are Latent Context Managers: Eliciting Self-Managed Context via a Proprioceptive Dashboard](content/papers/llm-agents-are-latent-context-managers-eliciting-self-managed-context-via-a-prop.md) | agent, compression, context |
| 2026-06-29 | arXiv | [Forensic Trajectory Signatures for Agent Memory Poisoning Detection](content/papers/forensic-trajectory-signatures-for-agent-memory-poisoning-detection.md) | agent, retrieval |
| 2026-06-29 | arXiv | [DuoMem: Towards Capable On-Device Memory Agents via Dual-Space Distillation](content/papers/duomem-towards-capable-on-device-memory-agents-via-dual-space-distillation.md) | agent, benchmark, context |
| 2026-06-29 | arXiv | [Always-OnAgents:A Survey of Persistent Memory, State, and Governance in LLMAgents](content/papers/always-onagents-a-survey-of-persistent-memory-state-and-governance-in-llmagents.md) | agent |
| 2026-06-28 | arXiv | [Selective Memory Retention for Long-Horizon LLM Agents](content/papers/selective-memory-retention-for-long-horizon-llm-agents.md) | agent, benchmark |
| 2026-06-28 | arXiv | [From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents](content/papers/from-agent-traces-to-trust-a-survey-of-evidence-tracing-and-execution-provenance.md) | agent, benchmark, retrieval |
| 2026-06-27 | arXiv | [The Efficiency Frontier: A Unified Framework for Cost-Performance Optimization in LLM Context Management](content/papers/the-efficiency-frontier-a-unified-framework-for-cost-performance-optimization-in.md) | compression, context, retrieval |
| 2026-06-27 | arXiv | [Memory-Managed Long-Context Attention: A Preliminary Study of Editable Request-Local Memory](content/papers/memory-managed-long-context-attention-a-preliminary-study-of-editable-request-lo.md) | context, long-term |
| 2026-06-27 | arXiv | [MedEvoEval: Evaluating Continual Evolution of Doctor Agents through Simulated Clinical Episodes](content/papers/medevoeval-evaluating-continual-evolution-of-doctor-agents-through-simulated-cli.md) | agent, benchmark, retrieval |
| 2026-06-27 | arXiv | [HyphaeDB: A Living Knowledge Topology for Agent-First Memory](content/papers/hyphaedb-a-living-knowledge-topology-for-agent-first-memory.md) | agent |
| 2026-06-26 | arXiv | [The Power of Second Order Methods for Sequence Preconditioning](content/papers/the-power-of-second-order-methods-for-sequence-preconditioning.md) | compression |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
