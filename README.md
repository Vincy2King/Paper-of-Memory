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

- Total tracked papers: **186**
- Last generated: **2026-05-12**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **151**
- OpenReview: **34**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-05-11 | arXiv | [Retrieve-then-Steer: Online Success Memory for Test-Time Adaptation of Generative VLAs](content/papers/retrieve-then-steer-online-success-memory-for-test-time-adaptation-of-generative.md) | long-term, retrieval |
| 2026-05-11 | arXiv | [Nautilus Compass: Black-box Persona Drift Detection for Production LLM Agents](content/papers/nautilus-compass-black-box-persona-drift-detection-for-production-llm-agents.md) | agent, conversation, retrieval |
| 2026-05-11 | arXiv | [MemReread: Enhancing Agentic Long-Context Reasoning via Memory-Guided Rereading](content/papers/memreread-enhancing-agentic-long-context-reasoning-via-memory-guided-rereading.md) | agent, context, retrieval |
| 2026-05-11 | arXiv | [MAGE: Multi-Agent Self-Evolution with Co-Evolutionary Knowledge Graphs](content/papers/mage-multi-agent-self-evolution-with-co-evolutionary-knowledge-graphs.md) | agent, benchmark, episodic |
| 2026-05-11 | arXiv | [Key-Value Means](content/papers/key-value-means.md) | context |
| 2026-05-11 | arXiv | [HAGE: Harnessing Agentic Memory via RL-Driven Weighted Graph Evolution](content/papers/hage-harnessing-agentic-memory-via-rl-driven-weighted-graph-evolution.md) | agent, retrieval |
| 2026-05-11 | arXiv | [H-MAPS: Hierarchical Memory-Augmented Proactive Search Assistant for Scientific Literature](content/papers/h-maps-hierarchical-memory-augmented-proactive-search-assistant-for-scientific-l.md) | context, retrieval |
| 2026-05-11 | arXiv | [EgoMemReason: A Memory-Driven Reasoning Benchmark for Long-Horizon Egocentric Video Understanding](content/papers/egomemreason-a-memory-driven-reasoning-benchmark-for-long-horizon-egocentric-vid.md) | agent, benchmark, context |
| 2026-05-11 | OpenReview | [ESSENTIAL: Episodic and Semantic Memory Integration for Video Class-Incremental Learning](content/papers/essential-episodic-and-semantic-memory-integration-for-video-class-incremental-l.md) | benchmark, episodic, retrieval |
| 2026-05-11 | arXiv | [Continual Harness: Online Adaptation for Self-Improving Foundation Agents](content/papers/continual-harness-online-adaptation-for-self-improving-foundation-agents.md) | agent, context |
| 2026-05-10 | arXiv | [The Trap of Trajectory: Towards Understanding and Mitigating Spurious Correlations in Agentic Memory](content/papers/the-trap-of-trajectory-towards-understanding-and-mitigating-spurious-correlation.md) | agent, benchmark, context |
| 2026-05-10 | arXiv | [Mem-W: Latent Memory-Native GUI Agents](content/papers/mem-w-latent-memory-native-gui-agents.md) | agent, benchmark, context |
| 2026-05-10 | arXiv | [EquiMem: Calibrating Shared Memory in Multi-Agent Debate via Game-Theoretic Equilibrium](content/papers/equimem-calibrating-shared-memory-in-multi-agent-debate-via-game-theoretic-equil.md) | agent, benchmark, retrieval |
| 2026-05-10 | arXiv | [Do Self-Evolving Agents Forget? Capability Degradation and Preservation in Lifelong LLM Agent Adaptation](content/papers/do-self-evolving-agents-forget-capability-degradation-and-preservation-in-lifelo.md) | agent |
| 2026-05-10 | arXiv | [Architecture Matters More Than Scale: A Comparative Study of Retrieval and Memory Augmentation for Financial QA Under SME Compute Constraints](content/papers/architecture-matters-more-than-scale-a-comparative-study-of-retrieval-and-memory.md) | benchmark, conversation, long-term |
| 2026-05-10 | arXiv | [A Cognitively Grounded Bayesian Framework for Misinformation Susceptibility](content/papers/a-cognitively-grounded-bayesian-framework-for-misinformation-susceptibility.md) | benchmark, compression |
| 2026-05-09 | arXiv | [The Echo Amplifies the Knowledge: Somatic Marker Analogues in Language Models via Emotion Vector Re-Injection](content/papers/the-echo-amplifies-the-knowledge-somatic-marker-analogues-in-language-models-via.md) | context, episodic |
| 2026-05-09 | arXiv | [ShadowMerge: A Novel Poisoning Attack on Graph-Based Agent Memory via Relation-Channel Conflicts](content/papers/shadowmerge-a-novel-poisoning-attack-on-graph-based-agent-memory-via-relation-ch.md) | agent, long-term |
| 2026-05-09 | arXiv | [GRC: Unifying Reasoning-Driven Generation, Retrieval and Compression](content/papers/grc-unifying-reasoning-driven-generation-retrieval-and-compression.md) | agent, benchmark, compression |
| 2026-05-09 | arXiv | [Bias by Necessity: Impossibility Theorems for Sequential Processing with Convergent AI and Human Validation](content/papers/bias-by-necessity-impossibility-theorems-for-sequential-processing-with-converge.md) | working memory |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
