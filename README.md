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

- Total tracked papers: **677**
- Last generated: **2026-07-14**

## Papers by Source

- ACL Anthology: **4**
- arXiv: **567**
- OpenReview: **106**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-07-13 | OpenReview | [PersonaTree: Structured Lifecycle Memory for Person Understanding in LLM Agents](content/papers/personatree-structured-lifecycle-memory-for-person-understanding-in-llm-agents.md) | agent, benchmark, context |
| 2026-07-11 | OpenReview | [Basic Performance Measurements of the Intel Optane DC Persistent Memory Module](content/papers/basic-performance-measurements-of-the-intel-optane-dc-persistent-memory-module.md) | benchmark |
| 2026-07-11 | OpenReview | [A Memory-Augmented Extension of Random Forest: The Memory-Augmented Forest (MAF)](content/papers/a-memory-augmented-extension-of-random-forest-the-memory-augmented-forest-maf.md) | context |
| 2026-07-10 | arXiv | [Shared Selective Persistent Memory for Agentic LLM Systems](content/papers/shared-selective-persistent-memory-for-agentic-llm-systems.md) | agent, context, conversation |
| 2026-07-10 | arXiv | [SAGEAgent: A Self-Evolving Agent for Cost-Aware Modality Acquisition in Multimodal Survival Prediction](content/papers/sageagent-a-self-evolving-agent-for-cost-aware-modality-acquisition-in-multimoda.md) | agent, episodic |
| 2026-07-10 | arXiv | [LongMedBench: Benchmarking Medical Agents for Long-Horizon Clinical Decision-Making](content/papers/longmedbench-benchmarking-medical-agents-for-long-horizon-clinical-decision-maki.md) | agent, benchmark, context |
| 2026-07-10 | arXiv | [Beyond Fixed Representations: The Vocabulary and Verifier Gaps in Open-Ended AI](content/papers/beyond-fixed-representations-the-vocabulary-and-verifier-gaps-in-open-ended-ai.md) | persistent memory |
| 2026-07-09 | arXiv | [What to Keep, What to Forget: A Rate--Distortion View of Memory Compaction in LLMs and Agents](content/papers/what-to-keep-what-to-forget-a-rate-distortion-view-of-memory-compaction-in-llms-.md) | agent, benchmark, compression |
| 2026-07-09 | OpenReview | [EfficientNav: Towards On-Device Object-Goal Navigation with Navigation Map Caching and Retrieval](content/papers/efficientnav-towards-on-device-object-goal-navigation-with-navigation-map-cachin.md) | agent, benchmark, retrieval |
| 2026-07-09 | OpenReview | [Efficient Allocation of Working Memory Resource for Utility Maximization in Humans and Recurrent Neural Networks](content/papers/efficient-allocation-of-working-memory-resource-for-utility-maximization-in-huma.md) | context |
| 2026-07-09 | arXiv | [ContextSniper: AntTrail's Token-Efficient Code Memory for Repository-Level Program Repair](content/papers/contextsniper-anttrail-s-token-efficient-code-memory-for-repository-level-progra.md) | agent, context |
| 2026-07-09 | arXiv | [Cognitive-structured Multimodal Agent for Multimodal Understanding, Generation, and Editing](content/papers/cognitive-structured-multimodal-agent-for-multimodal-understanding-generation-an.md) | agent, benchmark, context |
| 2026-07-09 | arXiv | [Autonomous heterogeneous catalyst discovery with a self-evolving multi-agent digital twin](content/papers/autonomous-heterogeneous-catalyst-discovery-with-a-self-evolving-multi-agent-dig.md) | agent, benchmark |
| 2026-07-08 | arXiv | [A-TMA: Decoupling State-Aware Memory Failures in Long-Term Agent Memory](content/papers/a-tma-decoupling-state-aware-memory-failures-in-long-term-agent-memory.md) | agent, benchmark, conversation |
| 2026-07-07 | arXiv | [Rank-Order N-of-M Codes for Sparse Distributed Memory: Disentangling Representation and Learning Effects in Noise Robustness Against Contemporary Neuromorphic Architectures](content/papers/rank-order-n-of-m-codes-for-sparse-distributed-memory-disentangling-representati.md) | episodic |
| 2026-07-07 | arXiv | [Prompt-Adapter Context Routing for Parameter-Efficient Multi-Shot Long Video Extrapolation](content/papers/prompt-adapter-context-routing-for-parameter-efficient-multi-shot-long-video-ext.md) | benchmark, context |
| 2026-07-07 | arXiv | [Nested Episodic State Topology (NEST): A Graph-Theoretic Architecture of Cognitive States](content/papers/nested-episodic-state-topology-nest-a-graph-theoretic-architecture-of-cognitive-.md) | context, episodic |
| 2026-07-07 | arXiv | [MemDefrag: Latent Memory Defragmentation for Large Language Models](content/papers/memdefrag-latent-memory-defragmentation-for-large-language-models.md) | benchmark, context, long-term |
| 2026-07-06 | arXiv | [Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses](content/papers/your-agent-s-memories-are-not-its-own-forged-reasoning-attacks-on-llm-agent-memo.md) | agent, context |
| 2026-07-06 | arXiv | [When Claws Remember but Do Not Tell: Stealthy Memory Injection in Persistent Personal Agents](content/papers/when-claws-remember-but-do-not-tell-stealthy-memory-injection-in-persistent-pers.md) | agent, benchmark, conversation |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
