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

- Total tracked papers: **1709**
- Last generated: **2026-11-19**

## Papers by Source

- ACL Anthology: **24**
- arXiv: **1539**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-11-18 | arXiv | [Twists and Turns: A Graph-Based Benchmark and Framework for Long-Term Memory in Exploration Tasks](content/papers/twists-and-turns-a-graph-based-benchmark-and-framework-for-long-term-memory-in-e.md) | benchmark, long-term, retrieval |
| 2026-11-18 | arXiv | [Resolution as Attention for Efficient Agent Memory Perception](content/papers/resolution-as-attention-for-efficient-agent-memory-perception.md) | agent |
| 2026-11-18 | arXiv | [On Agentic Manipulation Policies](content/papers/on-agentic-manipulation-policies.md) | agent, benchmark |
| 2026-11-18 | arXiv | [Multi-Agent Memory Inconsistency: Where Factual Conflicts Disappear in LLM Agents](content/papers/multi-agent-memory-inconsistency-where-factual-conflicts-disappear-in-llm-agents.md) | agent, benchmark, context |
| 2026-11-18 | arXiv | [MemoSync: Co-Managing Developer-Agent Metamemory Across Contexts](content/papers/memosync-co-managing-developer-agent-metamemory-across-contexts.md) | agent, context |
| 2026-11-18 | arXiv | [Jetriever: Shifting Agent Memory Retrieval from Similarity to Utility](content/papers/jetriever-shifting-agent-memory-retrieval-from-similarity-to-utility.md) | agent, retrieval |
| 2026-11-18 | arXiv | [Algorithmic Market Making Can Lead to Rough Volatility Through the Order Book](content/papers/algorithmic-market-making-can-lead-to-rough-volatility-through-the-order-book.md) | agent |
| 2026-11-17 | arXiv | [Variance Restoration over Covariance Rank: Memory-Budgeted Analytic Continual Learning](content/papers/variance-restoration-over-covariance-rank-memory-budgeted-analytic-continual-lea.md) | benchmark |
| 2026-11-17 | arXiv | [Surfacing Disagreement Beats Resolving It: A Gated Ablation Study of Provenance-Weighted Memory for Multi-Agent Debate](content/papers/surfacing-disagreement-beats-resolving-it-a-gated-ablation-study-of-provenance-w.md) | agent, retrieval |
| 2026-11-17 | arXiv | [RegimeCouncil: Paired-Evidence Routing For Memory Conflict Governance In LLM Agents](content/papers/regimecouncil-paired-evidence-routing-for-memory-conflict-governance-in-llm-agen.md) | agent, long-term |
| 2026-11-17 | arXiv | [RAG in a Trenchcoat: When Minimal Memory Is Enough for Agentic Systems, and When It Isn't](content/papers/rag-in-a-trenchcoat-when-minimal-memory-is-enough-for-agentic-systems-and-when-i.md) | agent, benchmark, retrieval |
| 2026-11-17 | arXiv | [PhysScope: Agentic Multimodal Physics Reasoning with Grounded Visual Memory](content/papers/physscope-agentic-multimodal-physics-reasoning-with-grounded-visual-memory.md) | agent, benchmark |
| 2026-11-17 | arXiv | [Network-Exposed Configuration Attacks on LLM-Controlled Social Robots](content/papers/network-exposed-configuration-attacks-on-llm-controlled-social-robots.md) | conversation |
| 2026-11-17 | arXiv | [Natural Language Programming: Rethinking Language, Memory, and Cognition in the Era of Generative AI](content/papers/natural-language-programming-rethinking-language-memory-and-cognition-in-the-era.md) | conversation, episodic |
| 2026-11-17 | arXiv | [Multi-Agent Memory Inconsistency: Where Factual Conflicts Disappear in LLM Agents](content/papers/multi-agent-memory-inconsistency-where-factual-conflicts-disappear-in-llm-agents.md) | agent, benchmark, context |
| 2026-11-17 | arXiv | [LMMR: Learned Multigranular Memory Retrieval for Small Language Model Agents](content/papers/lmmr-learned-multigranular-memory-retrieval-for-small-language-model-agents.md) | agent, retrieval |
| 2026-11-17 | arXiv | [Harnesses That Improve Themselves: A Unifying Framework for Self-Improving Agent Harnesses](content/papers/harnesses-that-improve-themselves-a-unifying-framework-for-self-improving-agent-.md) | agent, benchmark, context |
| 2026-11-17 | arXiv | [GuardAgent: A Memory-Augmented Agentic Framework for Adaptive Detection of Adversarial Promotions in LLM-Based Recommendation](content/papers/guardagent-a-memory-augmented-agentic-framework-for-adaptive-detection-of-advers.md) | agent |
| 2026-11-17 | arXiv | [EvoDisco: Strategy Discovery for Evolving Agent Memory](content/papers/evodisco-strategy-discovery-for-evolving-agent-memory.md) | agent, retrieval |
| 2026-11-17 | arXiv | [Déjà View: A Shared Working-Memory Model for Visual Tasks](content/papers/deja-view-a-shared-working-memory-model-for-visual-tasks.md) | working memory |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
