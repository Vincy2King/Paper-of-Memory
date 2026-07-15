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

- Total tracked papers: **693**
- Last generated: **2026-07-15**

## Papers by Source

- ACL Anthology: **4**
- arXiv: **581**
- OpenReview: **108**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-07-14 | OpenReview | [SMMBench: A Benchmark for Source-Distributed Multimodal Agent Memory](content/papers/smmbench-a-benchmark-for-source-distributed-multimodal-agent-memory.md) | agent, benchmark, context |
| 2026-07-14 | OpenReview | [OilSAM2: Memory-Augmented SAM2 for Scalable SAR Oil Spill Detection](content/papers/oilsam2-memory-augmented-sam2-for-scalable-sar-oil-spill-detection.md) | memory augmented, memory-augmented |
| 2026-07-13 | arXiv | [Vinci2: Providing Proactive Assistance in Continuous Egocentric Videos](content/papers/vinci2-providing-proactive-assistance-in-continuous-egocentric-videos.md) | agent, benchmark, context |
| 2026-07-13 | OpenReview | [PersonaTree: Structured Lifecycle Memory for Person Understanding in LLM Agents](content/papers/personatree-structured-lifecycle-memory-for-person-understanding-in-llm-agents.md) | agent, benchmark, context |
| 2026-07-13 | arXiv | [OpsMem: Dual-Memory Reasoning with Cross-Memory Resonance for Failure Diagnosis](content/papers/opsmem-dual-memory-reasoning-with-cross-memory-resonance-for-failure-diagnosis.md) | agent, long-term |
| 2026-07-13 | arXiv | [LongMedBench: Benchmarking Medical Agents for Long-Horizon Clinical Decision-Making](content/papers/longmedbench-benchmarking-medical-agents-for-long-horizon-clinical-decision-maki.md) | agent, benchmark, context |
| 2026-07-13 | arXiv | [Long-Memory Reservoir Computing for Data-Scarce Dengue Forecasting](content/papers/long-memory-reservoir-computing-for-data-scarce-dengue-forecasting.md) | long-term |
| 2026-07-13 | arXiv | [LightMem-Ego: Your AI Memory for Everyday Life](content/papers/lightmem-ego-your-ai-memory-for-everyday-life.md) | conversation, long-term, retrieval |
| 2026-07-13 | arXiv | [Forgetting Our Way to Shared Meaning: Effects of Forgetting on Conceptual Alignment in a Non-Partnership Coordination Game](content/papers/forgetting-our-way-to-shared-meaning-effects-of-forgetting-on-conceptual-alignme.md) | agent |
| 2026-07-13 | arXiv | [Bringing Back Rule Induction to Fluid Intelligence Research? An Initial Validation of the ARC-AGI Benchmark in Humans](content/papers/bringing-back-rule-induction-to-fluid-intelligence-research-an-initial-validatio.md) | benchmark |
| 2026-07-13 | arXiv | [A Glimpse into Long-term Physical Coexistence with Intelligent Robots](content/papers/a-glimpse-into-long-term-physical-coexistence-with-intelligent-robots.md) | agent, context, long-term |
| 2026-07-12 | arXiv | [When Context Dominates: Multimodal Signatures of Takeover Readiness Under Varying Hazard and Cognitive Load Conditions](content/papers/when-context-dominates-multimodal-signatures-of-takeover-readiness-under-varying.md) | context, conversation |
| 2026-07-12 | arXiv | [The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory](content/papers/the-compliance-trap-diagnosing-how-ai-agents-consume-conflicting-memory.md) | agent, benchmark, retrieval |
| 2026-07-12 | arXiv | [Agents Don't Just Agree, They Remember: Benchmarking Persistent Sycophancy in Stateful Personal Agents](content/papers/agents-don-t-just-agree-they-remember-benchmarking-persistent-sycophancy-in-stat.md) | agent, benchmark, conversation |
| 2026-07-11 | arXiv | [PhysMRV: Physical Memory Retrieval and Verification for Physics Plausibility Reasoning](content/papers/physmrv-physical-memory-retrieval-and-verification-for-physics-plausibility-reas.md) | benchmark, context, retrieval |
| 2026-07-11 | arXiv | [Context by Distinct Information: An Auditable Dirichlet-Process Working Memory for Long, Redundant Context Streams](content/papers/context-by-distinct-information-an-auditable-dirichlet-process-working-memory-fo.md) | context |
| 2026-07-11 | OpenReview | [Basic Performance Measurements of the Intel Optane DC Persistent Memory Module](content/papers/basic-performance-measurements-of-the-intel-optane-dc-persistent-memory-module.md) | benchmark |
| 2026-07-11 | arXiv | [ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory](content/papers/abot-agentos-a-general-robotic-agent-os-with-lifelong-multi-modal-memory.md) | agent, benchmark, context |
| 2026-07-11 | OpenReview | [A Memory-Augmented Extension of Random Forest: The Memory-Augmented Forest (MAF)](content/papers/a-memory-augmented-extension-of-random-forest-the-memory-augmented-forest-maf.md) | context |
| 2026-07-10 | arXiv | [Shared Selective Persistent Memory for Agentic LLM Systems](content/papers/shared-selective-persistent-memory-for-agentic-llm-systems.md) | agent, context, conversation |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
