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

- Total tracked papers: **361**
- Last generated: **2026-06-01**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **319**
- OpenReview: **41**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-05-31 | OpenReview | [REMem: Reasoning with Episodic Memory in Language Agent](content/papers/remem-reasoning-with-episodic-memory-in-language-agent.md) | agent, benchmark, context |
| 2026-05-30 | OpenReview | [Hello Again! LLM-powered Personalized Agent for Long-term Dialogue](content/papers/hello-again-llm-powered-personalized-agent-for-long-term-dialogue.md) | agent, benchmark, long-term |
| 2026-05-30 | OpenReview | [ER-MIA: Black-Box Adversarial Memory Injection Attacks on Long-Term Memory-Augmented Large Language Models](content/papers/er-mia-black-box-adversarial-memory-injection-attacks-on-long-term-memory-augmen.md) | context, long-term, retrieval |
| 2026-05-29 | arXiv | [VikingMem: A Memory Base Management System for Stateful LLM-based Applications](content/papers/vikingmem-a-memory-base-management-system-for-stateful-llm-based-applications.md) | agent, benchmark, compression |
| 2026-05-29 | arXiv | [TARIC: Memory-Augmented Traversability-Aware Outdoor VLN under Interrupted Semantic Cues](content/papers/taric-memory-augmented-traversability-aware-outdoor-vln-under-interrupted-semant.md) | agent |
| 2026-05-29 | arXiv | [SAGE: A Novelty Gate for Efficient Memory Evolution in Agentic LLMs](content/papers/sage-a-novelty-gate-for-efficient-memory-evolution-in-agentic-llms.md) | agent, long-term, retrieval |
| 2026-05-29 | arXiv | [Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models](content/papers/light-interaction-training-free-inference-acceleration-for-interactive-video-wor.md) | context |
| 2026-05-29 | arXiv | [ForecastCompass: Guiding Agentic Forecasting with Adaptive Factor Memory](content/papers/forecastcompass-guiding-agentic-forecasting-with-adaptive-factor-memory.md) | agent, retrieval |
| 2026-05-29 | arXiv | [Eywa: Provenance-Grounded Long-Term Memory for AI Agents](content/papers/eywa-provenance-grounded-long-term-memory-for-ai-agents.md) | agent, benchmark, context |
| 2026-05-29 | arXiv | [ElasticMem: Latent Memory as a Learnable Resource for LLM Agents](content/papers/elasticmem-latent-memory-as-a-learnable-resource-for-llm-agents.md) | agent, context, long-term |
| 2026-05-29 | arXiv | [Diagnosing Failure Modes of Shared-State Collaboration in Resource-Constrained Visual Agents](content/papers/diagnosing-failure-modes-of-shared-state-collaboration-in-resource-constrained-v.md) | agent, benchmark, context |
| 2026-05-29 | arXiv | [CoMem: Context Management with A Decoupled Long-Context Model](content/papers/comem-context-management-with-a-decoupled-long-context-model.md) | agent, compression, context |
| 2026-05-29 | arXiv | [Chain-of-Thought and Compressed Looped Transformers: A Memory-Budget Separation](content/papers/chain-of-thought-and-compressed-looped-transformers-a-memory-budget-separation.md) | context |
| 2026-05-29 | arXiv | [Beyond Static Dialogues: Benchmarking Realistic, Heterogeneous, and Evolving Long-Term Memory](content/papers/beyond-static-dialogues-benchmarking-realistic-heterogeneous-and-evolving-long-t.md) | benchmark, context, long-term |
| 2026-05-29 | arXiv | [AutoSci: A Memory-Centric Agentic System for the Full Scientific Research Lifecycle](content/papers/autosci-a-memory-centric-agentic-system-for-the-full-scientific-research-lifecyc.md) | agent, context, long-term |
| 2026-05-28 | arXiv | [WorldMemArena: Evaluating Multimodal Agent Memory Through Action-World Interaction](content/papers/worldmemarena-evaluating-multimodal-agent-memory-through-action-world-interactio.md) | agent, benchmark, context |
| 2026-05-28 | arXiv | [VikingMem: A Memory Base Management System for Stateful LLM-based Applications](content/papers/vikingmem-a-memory-base-management-system-for-stateful-llm-based-applications.md) | agent, benchmark, compression |
| 2026-05-28 | arXiv | [VLA-Pro: Cross-Task Procedural Memory Transfer for Vision-Language-Action Models](content/papers/vla-pro-cross-task-procedural-memory-transfer-for-vision-language-action-models.md) | context, retrieval |
| 2026-05-28 | arXiv | [Unlocking the Working Memory of Large Language Models for Latent Reasoning](content/papers/unlocking-the-working-memory-of-large-language-models-for-latent-reasoning.md) | benchmark |
| 2026-05-28 | arXiv | [Towards Verifiable Multimodal Deep Research: A Multi-Agent Harness for Interleaved Report Generation](content/papers/towards-verifiable-multimodal-deep-research-a-multi-agent-harness-for-interleave.md) | agent, benchmark |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
