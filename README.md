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

- Total tracked papers: **810**
- Last generated: **2026-08-03**

## Papers by Source

- ACL Anthology: **5**
- arXiv: **683**
- OpenReview: **122**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-07-31 | OpenReview | [Trading Generalization for Working Memory Capacity in Neural Network Representations](content/papers/trading-generalization-for-working-memory-capacity-in-neural-network-representat.md) | working memory |
| 2026-07-31 | OpenReview | [Predictive Latent Simulation as a Memory Retrieval Mechanism](content/papers/predictive-latent-simulation-as-a-memory-retrieval-mechanism.md) | agent, retrieval |
| 2026-07-31 | OpenReview | [Inhibitory signals support working memory in sensory cortex](content/papers/inhibitory-signals-support-working-memory-in-sensory-cortex.md) | working memory |
| 2026-07-31 | OpenReview | [Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems](content/papers/caching-for-the-future-scrub-jay-episodic-memory-principles-for-agent-memory-sys.md) | agent, benchmark, context |
| 2026-07-30 | arXiv | [Understanding Is Done Early: A Depth Division of Labor in Large Language Models and Its Use for Unbounded-Context Memory](content/papers/understanding-is-done-early-a-depth-division-of-labor-in-large-language-models-a.md) | compression, context, conversation |
| 2026-07-30 | arXiv | [RRM: Experience-Driven Reflective Retrieval Memory for Long-Horizon Multimodal Reasoning](content/papers/rrm-experience-driven-reflective-retrieval-memory-for-long-horizon-multimodal-re.md) | agent, context, episodic |
| 2026-07-30 | arXiv | [Memory Decoder at Scale: A Pretrained, Parametric Long-Term Memory](content/papers/memory-decoder-at-scale-a-pretrained-parametric-long-term-memory.md) | benchmark, long-term, retrieval |
| 2026-07-30 | arXiv | [MemTxn: A Transaction Boundary for Source-Supported Updates and Complete-State Recovery in Agent Memory](content/papers/memtxn-a-transaction-boundary-for-source-supported-updates-and-complete-state-re.md) | agent, retrieval |
| 2026-07-30 | arXiv | [MemHarness: Memory Is Reconstructed, Not Replayed](content/papers/memharness-memory-is-reconstructed-not-replayed.md) | agent, context |
| 2026-07-30 | arXiv | [MIND: Lightweight and Effective Memory Injection Defense for LLM Agents via Intent-Aware Information Bottleneck](content/papers/mind-lightweight-and-effective-memory-injection-defense-for-llm-agents-via-inten.md) | agent, context |
| 2026-07-30 | arXiv | [LabEvolver: Training-Free Experience Evolution for Safe and Grounded Wet-Lab Agents](content/papers/labevolver-training-free-experience-evolution-for-safe-and-grounded-wet-lab-agen.md) | agent, episodic |
| 2026-07-30 | arXiv | [ChronoMem: Version Control and Semantic Rollback for Large Language Model Agent Memory](content/papers/chronomem-version-control-and-semantic-rollback-for-large-language-model-agent-m.md) | agent, benchmark, conversation |
| 2026-07-30 | arXiv | [ARES: Adaptive Reasoning-Effort Steering for PPA- and Cost-Aware RTL Optimization with LLM Agents](content/papers/ares-adaptive-reasoning-effort-steering-for-ppa-and-cost-aware-rtl-optimization-.md) | agent, long-term |
| 2026-07-29 | arXiv | [The Art of Not Forgetting A Local Learning Architecture for Continual Learning](content/papers/the-art-of-not-forgetting-a-local-learning-architecture-for-continual-learning.md) | benchmark |
| 2026-07-29 | arXiv | [Setoka: A Benchmark for Hierarchical User Understanding in Personalized Agents over Heterogeneous Data](content/papers/setoka-a-benchmark-for-hierarchical-user-understanding-in-personalized-agents-ov.md) | agent, benchmark, conversation |
| 2026-07-29 | arXiv | [NMKFR: A Robust Framework for Time-Aware Cold-Start Recommendation](content/papers/nmkfr-a-robust-framework-for-time-aware-cold-start-recommendation.md) | retrieval |
| 2026-07-29 | arXiv | [Metis: Memory Foundation Model](content/papers/metis-memory-foundation-model.md) | agent |
| 2026-07-29 | arXiv | [MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence and Repair](content/papers/memsecbench-tracking-agent-memory-poisoning-from-persistence-to-consequence-and-.md) | agent, benchmark, context |
| 2026-07-29 | arXiv | [Living-Harness Is an Interactive-Agent Evolver](content/papers/living-harness-is-an-interactive-agent-evolver.md) | agent, context, episodic |
| 2026-07-29 | arXiv | [Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability](content/papers/filesystem-based-memory-for-llm-agents-organization-evolution-and-sustainability.md) | agent, benchmark, conversation |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
