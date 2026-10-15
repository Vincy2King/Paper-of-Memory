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

- Total tracked papers: **1398**
- Last generated: **2026-10-15**

## Papers by Source

- ACL Anthology: **6**
- arXiv: **1246**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-10-13 | arXiv | [TacitVLA: Reasoning Vision-Language-Action Models Without Reasoning Latency](content/papers/tacitvla-reasoning-vision-language-action-models-without-reasoning-latency.md) | benchmark, episodic |
| 2026-10-13 | arXiv | [Propose, Verify, Commit: Evidence-Grounded Memory for Long-Horizon Multi-Actor Conversations](content/papers/propose-verify-commit-evidence-grounded-memory-for-long-horizon-multi-actor-conv.md) | agent, benchmark, context |
| 2026-10-13 | arXiv | [MemoryVLN: From Ego-Aware Memory Representation to Cross-Context Memory Reuse in Vision-Language Navigation](content/papers/memoryvln-from-ego-aware-memory-representation-to-cross-context-memory-reuse-in-.md) | agent, compression, context |
| 2026-10-13 | arXiv | [Memory Echo in Single-Agent Long-Term Memory: Lifecycle Evaluation and Provenance-Guided Mitigation](content/papers/memory-echo-in-single-agent-long-term-memory-lifecycle-evaluation-and-provenance.md) | agent, benchmark, context |
| 2026-10-13 | arXiv | [Many Steps into One: Reasoning Contraction and the Limits of Safe Memory Reuse for LLM Agents](content/papers/many-steps-into-one-reasoning-contraction-and-the-limits-of-safe-memory-reuse-fo.md) | agent |
| 2026-10-13 | arXiv | [Learning How to Remember: Memory Modality Selection for GUI Agents](content/papers/learning-how-to-remember-memory-modality-selection-for-gui-agents.md) | agent, benchmark |
| 2026-10-13 | arXiv | [Kwai Summary Attention V2 Technical Report](content/papers/kwai-summary-attention-v2-technical-report.md) | compression, context |
| 2026-10-13 | arXiv | [Knowing the User Is Not Knowing What We Established: Grounding Awareness in Personal Agents](content/papers/knowing-the-user-is-not-knowing-what-we-established-grounding-awareness-in-perso.md) | agent, benchmark, retrieval |
| 2026-10-13 | arXiv | [Hybrid Reasoning Agents](content/papers/hybrid-reasoning-agents.md) | agent, benchmark, context |
| 2026-10-13 | arXiv | [CineMem: Attention-Aligned Fine-grained Memory Retrieval for Multi-Shot Long Video Generation](content/papers/cinemem-attention-aligned-fine-grained-memory-retrieval-for-multi-shot-long-vide.md) | context, long-term, retrieval |
| 2026-10-13 | arXiv | [Can Agents Truly Forget? Explore Machine Unlearning for LLM Agents](content/papers/can-agents-truly-forget-explore-machine-unlearning-for-llm-agents.md) | agent, benchmark |
| 2026-10-13 | arXiv | [Can Agents Forget When Asked? A Benchmark for Memory Unlearning in LLM Agents](content/papers/can-agents-forget-when-asked-a-benchmark-for-memory-unlearning-in-llm-agents.md) | agent, benchmark, context |
| 2026-10-12 | arXiv | [World-T3: Test-Time Training as Persistent Memory for Real-Time Video World Models](content/papers/world-t3-test-time-training-as-persistent-memory-for-real-time-video-world-model.md) | benchmark, context |
| 2026-10-12 | arXiv | [When Goals Leak Across Relationships: How Cached Goal Representations Shape Cross-Client Decisions](content/papers/when-goals-leak-across-relationships-how-cached-goal-representations-shape-cross.md) | agent, conversation |
| 2026-10-12 | arXiv | [REEL: Learning to Retrieve, Evaluate, and Evolve Visual Memory for Any Long-Horizon Multi-Shot Video Generation](content/papers/reel-learning-to-retrieve-evaluate-and-evolve-visual-memory-for-any-long-horizon.md) | agent |
| 2026-10-12 | arXiv | [Event Memory and Narrative Dynamics: A Large Language Model Framework for Multidimensional State Spaces](content/papers/event-memory-and-narrative-dynamics-a-large-language-model-framework-for-multidi.md) | context, episodic |
| 2026-10-12 | arXiv | [Do LLMs Learn from Rewards in Context? : Rethinking the role of reward in In-Context RL](content/papers/do-llms-learn-from-rewards-in-context-rethinking-the-role-of-reward-in-in-contex.md) | agent, benchmark, context |
| 2026-10-12 | arXiv | [Beyond the Remembered World: Predictive 4D Belief for Persistent Navigation in Evolving Worlds](content/papers/beyond-the-remembered-world-predictive-4d-belief-for-persistent-navigation-in-ev.md) | agent, benchmark, retrieval |
| 2026-10-11 | arXiv | [Suggested Is Not Superseded: A Pre-Registered Evaluation of a System-One Model as a Memory-Retirement Gate](content/papers/suggested-is-not-superseded-a-pre-registered-evaluation-of-a-system-one-model-as.md) | benchmark, conversation, long-term |
| 2026-10-11 | arXiv | [Recall What Is Missing: Composing Evidence from Long-Term Agent Memory](content/papers/recall-what-is-missing-composing-evidence-from-long-term-agent-memory.md) | agent, benchmark, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
