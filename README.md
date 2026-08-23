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

- Total tracked papers: **984**
- Last generated: **2026-08-23**

## Papers by Source

- ACL Anthology: **5**
- arXiv: **845**
- OpenReview: **134**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-08-22 | OpenReview | [Knowledge Graph Enhanced Memory-Augmented Retrieval for Long Context Modeling](content/papers/knowledge-graph-enhanced-memory-augmented-retrieval-for-long-context-modeling.md) | context, retrieval |
| 2026-08-21 | OpenReview | [Reason Before Remembering: An Entity-Centric Framework for Trustworthy Conversational Memory](content/papers/reason-before-remembering-an-entity-centric-framework-for-trustworthy-conversati.md) | context, conversation, retrieval |
| 2026-08-21 | OpenReview | [D-ACR: Dialogue-Aware Context Retrieval for Long-Term Conversational Memory](content/papers/d-acr-dialogue-aware-context-retrieval-for-long-term-conversational-memory.md) | benchmark, context, conversation |
| 2026-08-20 | arXiv | [SABET-QA: Temporal Knowledge Graph Question Answering](content/papers/sabet-qa-temporal-knowledge-graph-question-answering.md) | context |
| 2026-08-20 | arXiv | [Remember, Verify, or Ask? Cross-Family Evaluation of Memory Commitment in LLM Agents](content/papers/remember-verify-or-ask-cross-family-evaluation-of-memory-commitment-in-llm-agent.md) | agent, context |
| 2026-08-20 | arXiv | [MemTrapBench: Benchmarking Cognitive Traps in LLM Memory Use](content/papers/memtrapbench-benchmarking-cognitive-traps-in-llm-memory-use.md) | benchmark, long-term |
| 2026-08-20 | arXiv | [Compress and Forget: bitsandbytes Quantization Amplifies Proactive Interference in LLMs](content/papers/compress-and-forget-bitsandbytes-quantization-amplifies-proactive-interference-i.md) | benchmark, context, retrieval |
| 2026-08-20 | arXiv | [Can Agent Memory Systems Track Evolving State?](content/papers/can-agent-memory-systems-track-evolving-state.md) | agent, benchmark, context |
| 2026-08-20 | OpenReview | [CIRCUIT Memory: Confidence-Aware Multi-Axis Retrieval for Episodic Memory in LLM Agents](content/papers/circuit-memory-confidence-aware-multi-axis-retrieval-for-episodic-memory-in-llm-.md) | agent, episodic, retrieval |
| 2026-08-20 | arXiv | [Beyond Memory Majority: Latent-Source Reasoning for Multi-Agent Memory Arbitration](content/papers/beyond-memory-majority-latent-source-reasoning-for-multi-agent-memory-arbitratio.md) | agent, benchmark, long-term |
| 2026-08-19 | arXiv | [Report on The 1st Workshop on Human-Centered Proactive and Personalized Agents for Interactive Information Access at CHIIR 2026](content/papers/report-on-the-1st-workshop-on-human-centered-proactive-and-personalized-agents-f.md) | agent, context, long-term |
| 2026-08-19 | arXiv | [MemFuse: Multi-Source Memory Fusion from Fragmented Observations](content/papers/memfuse-multi-source-memory-fusion-from-fragmented-observations.md) | agent, benchmark, episodic |
| 2026-08-19 | arXiv | [DeltaMomentum: A Key-Value based Anisotropic Momentum Update via Delta Rule](content/papers/deltamomentum-a-key-value-based-anisotropic-momentum-update-via-delta-rule.md) | persistent memory |
| 2026-08-19 | arXiv | [D$^2$ACCI: A Dual-Loop Diagnostic Protocol for Evidence-Preserving Agent Memory](content/papers/d-2-acci-a-dual-loop-diagnostic-protocol-for-evidence-preserving-agent-memory.md) | agent, benchmark, retrieval |
| 2026-08-19 | arXiv | [Compress and Forget: bitsandbytes Quantization Amplifies Proactive Interference in LLMs](content/papers/compress-and-forget-bitsandbytes-quantization-amplifies-proactive-interference-i.md) | benchmark, context, retrieval |
| 2026-08-19 | arXiv | [Adaptive Memory and Reflection Multi-Agent System for Medical Question Answering](content/papers/adaptive-memory-and-reflection-multi-agent-system-for-medical-question-answering.md) | agent, retrieval |
| 2026-08-18 | arXiv | [On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification](content/papers/on-the-fragility-of-self-improving-agents-variance-task-order-and-underspecifica.md) | agent |
| 2026-08-18 | arXiv | [Multi-turn Conversational AI from Text to Multimodal Interaction: Data, Models, Evaluation, and Open Challenges](content/papers/multi-turn-conversational-ai-from-text-to-multimodal-interaction-data-models-eva.md) | agent, benchmark, context |
| 2026-08-18 | arXiv | [GraphWake: Group Polarization via Memory-Mediated Polarization Cascade in LLM-Agent Communities](content/papers/graphwake-group-polarization-via-memory-mediated-polarization-cascade-in-llm-age.md) | agent, retrieval |
| 2026-08-18 | arXiv | [EgoMemReason: A Memory-Driven Reasoning Benchmark for Long-Horizon Egocentric Video Understanding](content/papers/egomemreason-a-memory-driven-reasoning-benchmark-for-long-horizon-egocentric-vid.md) | agent, benchmark, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
