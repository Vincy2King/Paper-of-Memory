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

- Total tracked papers: **345**
- Last generated: **2026-05-30**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **306**
- OpenReview: **38**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-05-28 | arXiv | [WorldMemArena: Evaluating Multimodal Agent Memory Through Action-World Interaction](content/papers/worldmemarena-evaluating-multimodal-agent-memory-through-action-world-interactio.md) | agent, benchmark, context |
| 2026-05-28 | arXiv | [VikingMem: A Memory Base Management System for Stateful LLM-based Applications](content/papers/vikingmem-a-memory-base-management-system-for-stateful-llm-based-applications.md) | agent, benchmark, compression |
| 2026-05-28 | arXiv | [VLA-Pro: Cross-Task Procedural Memory Transfer for Vision-Language-Action Models](content/papers/vla-pro-cross-task-procedural-memory-transfer-for-vision-language-action-models.md) | context, retrieval |
| 2026-05-28 | arXiv | [Unlocking the Working Memory of Large Language Models for Latent Reasoning](content/papers/unlocking-the-working-memory-of-large-language-models-for-latent-reasoning.md) | benchmark |
| 2026-05-28 | arXiv | [Towards Verifiable Multimodal Deep Research: A Multi-Agent Harness for Interleaved Report Generation](content/papers/towards-verifiable-multimodal-deep-research-a-multi-agent-harness-for-interleave.md) | agent, benchmark |
| 2026-05-28 | arXiv | [Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents](content/papers/skill-pro-learning-reusable-skills-from-experience-via-non-parametric-ppo-for-ll.md) | agent, compression, episodic |
| 2026-05-28 | arXiv | [Personalized Turn-Level User Conversation Satisfaction Benchmark](content/papers/personalized-turn-level-user-conversation-satisfaction-benchmark.md) | benchmark, context, conversation |
| 2026-05-28 | arXiv | [Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents](content/papers/meta-cognitive-memory-policy-optimization-for-long-horizon-llm-agents.md) | agent, context |
| 2026-05-28 | arXiv | [Hijacking Agent Memory: Stealthy Trojan Attacks Through Conversational Interaction](content/papers/hijacking-agent-memory-stealthy-trojan-attacks-through-conversational-interactio.md) | agent, conversation, long-term |
| 2026-05-28 | arXiv | [HEART-Bench: Do LLM Agents Exhibit Human-like Psychology?](content/papers/heart-bench-do-llm-agents-exhibit-human-like-psychology.md) | agent, benchmark, episodic |
| 2026-05-28 | arXiv | [Entity-Collision: A Stratified Protocol for Attributing Retrieval Lift in Agent Memory](content/papers/entity-collision-a-stratified-protocol-for-attributing-retrieval-lift-in-agent-m.md) | agent, benchmark, retrieval |
| 2026-05-27 | arXiv | [Structured Belief State and the First Precision-Aware Benchmark for LLM Memory Retrieval](content/papers/structured-belief-state-and-the-first-precision-aware-benchmark-for-llm-memory-r.md) | benchmark, retrieval |
| 2026-05-27 | arXiv | [Rethinking Memory as Continuously Evolving Connectivity](content/papers/rethinking-memory-as-continuously-evolving-connectivity.md) | agent, benchmark, long-term |
| 2026-05-27 | arXiv | [ProvMind: Provenance-grounded reasoning for materials synthesis](content/papers/provmind-provenance-grounded-reasoning-for-materials-synthesis.md) | benchmark, retrieval |
| 2026-05-27 | arXiv | [Plant, Persist, Trigger: Sleeper Attack on Large Language Model Agents](content/papers/plant-persist-trigger-sleeper-attack-on-large-language-model-agents.md) | agent, benchmark, context |
| 2026-05-27 | arXiv | [Personal Visual Memory from Explicit and Implicit Evidence](content/papers/personal-visual-memory-from-explicit-and-implicit-evidence.md) | agent, benchmark, context |
| 2026-05-27 | arXiv | [MemGuard: Preventing Memory Contamination in Long-Term Memory-Augmented Large Language Models](content/papers/memguard-preventing-memory-contamination-in-long-term-memory-augmented-large-lan.md) | benchmark, context, conversation |
| 2026-05-27 | arXiv | [MemCog: From Memory-as-Tool to Memory-as-Cognition in Conversational Agents](content/papers/memcog-from-memory-as-tool-to-memory-as-cognition-in-conversational-agents.md) | agent, benchmark, context |
| 2026-05-27 | arXiv | [MRMMIA: Membership Inference Attacks on Memory in Chat Agents](content/papers/mrmmia-membership-inference-attacks-on-memory-in-chat-agents.md) | agent, retrieval |
| 2026-05-27 | OpenReview | [LatentMem: Customizing Latent Memory for Multi-Agent Systems](content/papers/latentmem-customizing-latent-memory-for-multi-agent-systems.md) | agent, benchmark, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
