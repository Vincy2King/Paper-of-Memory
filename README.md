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

- Total tracked papers: **1315**
- Last generated: **2026-10-06**

## Papers by Source

- ACL Anthology: **6**
- arXiv: **1163**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-10-05 | arXiv | [ReMem: Streaming Video Understanding With Long Context Retention](content/papers/remem-streaming-video-understanding-with-long-context-retention.md) | benchmark, compression, context |
| 2026-10-05 | arXiv | [PACMI: Provenance-Aware Cascading Memory Invalidation for Long-Term LLM Agents](content/papers/pacmi-provenance-aware-cascading-memory-invalidation-for-long-term-llm-agents.md) | agent, benchmark, context |
| 2026-10-05 | arXiv | [MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents](content/papers/mempilot-orchestrating-on-demand-multimodal-memory-curation-for-llm-agents.md) | agent, benchmark |
| 2026-10-05 | arXiv | [MATE: Adaptive Long- and Short-Term User Memory for LLM-Based Recommendation](content/papers/mate-adaptive-long-and-short-term-user-memory-for-llm-based-recommendation.md) | context, long-term |
| 2026-10-05 | arXiv | [HLA-WM: Hybrid Linear Attention for Long-Horizon Video World Models](content/papers/hla-wm-hybrid-linear-attention-for-long-horizon-video-world-models.md) | context, retrieval |
| 2026-10-05 | arXiv | [Capability-Driven Self-Evolution of Agent Memory](content/papers/capability-driven-self-evolution-of-agent-memory.md) | agent |
| 2026-10-04 | arXiv | [StateWise: Diagnosing and Repairing Persistent Operational State Before Agent Actions](content/papers/statewise-diagnosing-and-repairing-persistent-operational-state-before-agent-act.md) | agent |
| 2026-10-04 | arXiv | [ReMAP: Restoring the Perceptual Cycle with Reasoning-Time Latent Visual Memory](content/papers/remap-restoring-the-perceptual-cycle-with-reasoning-time-latent-visual-memory.md) | benchmark, context, retrieval |
| 2026-10-04 | arXiv | [Memory Canonicalization: A Framework and Benchmark for Cross-Model Drift in Persistent LLM Memory](content/papers/memory-canonicalization-a-framework-and-benchmark-for-cross-model-drift-in-persi.md) | agent, benchmark, context |
| 2026-10-04 | arXiv | [Memadapter: Counterfactual Adaptation Against Memory-induced Sycophancy](content/papers/memadapter-counterfactual-adaptation-against-memory-induced-sycophancy.md) | agent, benchmark, context |
| 2026-10-04 | arXiv | [MemTrace: State-Consistent Memory for Long-Horizon Coding Agents](content/papers/memtrace-state-consistent-memory-for-long-horizon-coding-agents.md) | agent, benchmark, compression |
| 2026-10-04 | arXiv | [Have I Scene This Before? Spatially Grounded Conversational Memory for Complex Queries in Egocentric Assistants](content/papers/have-i-scene-this-before-spatially-grounded-conversational-memory-for-complex-qu.md) | benchmark, context, conversation |
| 2026-10-04 | arXiv | [GitSwarm: Decentralized Compounding Inference](content/papers/gitswarm-decentralized-compounding-inference.md) | agent |
| 2026-10-04 | arXiv | [From Memory to Guide: Spatio-Temporal Composer for Procedural Coding Memory](content/papers/from-memory-to-guide-spatio-temporal-composer-for-procedural-coding-memory.md) | agent, context |
| 2026-10-04 | arXiv | [Building LLM Agent Systems the Deep Learning Way: From Modular Design to Architecture Search](content/papers/building-llm-agent-systems-the-deep-learning-way-from-modular-design-to-architec.md) | agent, retrieval |
| 2026-10-04 | arXiv | [Agentic Trading: When LLM Agents Meet Financial Markets](content/papers/agentic-trading-when-llm-agents-meet-financial-markets.md) | agent, benchmark, context |
| 2026-10-04 | arXiv | [AgentDiscover: Autonomous Discovery with Minimal Search Scaffolding](content/papers/agentdiscover-autonomous-discovery-with-minimal-search-scaffolding.md) | agent, context, long-term |
| 2026-10-04 | arXiv | [ASCENT: Online Test-Time Training of Long-Horizon Agents via Self-Distillation of Verified Experience](content/papers/ascent-online-test-time-training-of-long-horizon-agents-via-self-distillation-of.md) | agent, context, retrieval |
| 2026-10-04 | arXiv | [AECG: Asymmetric Experience Consolidation and Governance In Multi-Agent Systems](content/papers/aecg-asymmetric-experience-consolidation-and-governance-in-multi-agent-systems.md) | agent, benchmark, retrieval |
| 2026-10-03 | arXiv | [StegoMemory: Agentic Memory Acts as Covert Steganographic Channel](content/papers/stegomemory-agentic-memory-acts-as-covert-steganographic-channel.md) | agent, retrieval |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
