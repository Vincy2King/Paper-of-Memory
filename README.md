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

- Total tracked papers: **949**
- Last generated: **2026-08-15**

## Papers by Source

- ACL Anthology: **5**
- arXiv: **810**
- OpenReview: **134**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-08-13 | arXiv | [When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](content/papers/when-your-agent-opens-the-chat-app-agent-controlled-search-over-raw-chat-logs-ri.md) | agent, context, conversation |
| 2026-08-13 | arXiv | [StateBridge: Training-free Hidden-state Alignment for Latent Communication in LLM Multi-Agent Systems](content/papers/statebridge-training-free-hidden-state-alignment-for-latent-communication-in-llm.md) | agent |
| 2026-08-13 | arXiv | [Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intelligence](content/papers/spatial-memory-agent-experience-grounded-procedure-memory-for-spatial-intelligen.md) | agent, benchmark, retrieval |
| 2026-08-13 | arXiv | [RippleMem: From Isolated Retrieval to Associative Recollection for Long-Term Agent Memory](content/papers/ripplemem-from-isolated-retrieval-to-associative-recollection-for-long-term-agen.md) | agent, context, episodic |
| 2026-08-13 | arXiv | [LycheeMemory V2: Efficient Long-Term Memory for LLM Agents via Semantic Segment-Level Consolidation](content/papers/lycheememory-v2-efficient-long-term-memory-for-llm-agents-via-semantic-segment-l.md) | agent, context, conversation |
| 2026-08-13 | arXiv | [Intern-S2-Preview: Scientific Agentic Foundation Model](content/papers/intern-s2-preview-scientific-agentic-foundation-model.md) | agent, benchmark |
| 2026-08-13 | arXiv | [Enhancing Virtual Agents through SLMs and Edge-Computing: An Exploratory Evaluation of Think and Memory Processes](content/papers/enhancing-virtual-agents-through-slms-and-edge-computing-an-exploratory-evaluati.md) | agent, context, conversation |
| 2026-08-13 | arXiv | [ERSkill: Evolving for Skill-Guided Adaptive Memory Retrieval](content/papers/erskill-evolving-for-skill-guided-adaptive-memory-retrieval.md) | agent, benchmark, long-term |
| 2026-08-13 | arXiv | [AQuA: Recursively Self-Improving Quantitative Trading Research Agents](content/papers/aqua-recursively-self-improving-quantitative-trading-research-agents.md) | agent |
| 2026-08-12 | arXiv | [Towards a Formal Definition of Agent Memory: Basis, Span, Optimality, and the Sequential Memory Problem](content/papers/towards-a-formal-definition-of-agent-memory-basis-span-optimality-and-the-sequen.md) | agent, compression |
| 2026-08-12 | arXiv | [Total Recall at What Cost? Benchmarking the Serving Cost of Agentic Memory Systems](content/papers/total-recall-at-what-cost-benchmarking-the-serving-cost-of-agentic-memory-system.md) | agent, benchmark, conversation |
| 2026-08-12 | arXiv | [The Sleeping Agent: What Gist-Based Context Compression Loses and Why](content/papers/the-sleeping-agent-what-gist-based-context-compression-loses-and-why.md) | agent, compression, context |
| 2026-08-12 | arXiv | [TELLME: Test-Enhanced Learning for Language Model Enrichment](content/papers/tellme-test-enhanced-learning-for-language-model-enrichment.md) | long-term |
| 2026-08-12 | arXiv | [LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation](content/papers/loongreflect-boosting-long-horizon-reflection-in-search-agents-via-global-perspe.md) | agent, benchmark, context |
| 2026-08-12 | arXiv | [LLMs Are Not Good Strategists, Yet Memory-Enhanced Agency Boosts Reasoning](content/papers/llms-are-not-good-strategists-yet-memory-enhanced-agency-boosts-reasoning.md) | agent, context, long-term |
| 2026-08-12 | arXiv | [Governed Persistent Memory: Source-Bound State Semantics and Fail-Closed Release for Long-Horizon Agents](content/papers/governed-persistent-memory-source-bound-state-semantics-and-fail-closed-release-.md) | agent, long-term, retrieval |
| 2026-08-12 | arXiv | [EgoCITE: Context-Augmented Indexing and Time-Aware Retrieval for Long-Horizon Egocentric Memory](content/papers/egocite-context-augmented-indexing-and-time-aware-retrieval-for-long-horizon-ego.md) | agent, context, conversation |
| 2026-08-12 | arXiv | [Consolidator: Learning Persistent Routed Memory Across Context Boundaries](content/papers/consolidator-learning-persistent-routed-memory-across-context-boundaries.md) | context, long-term |
| 2026-08-12 | arXiv | [$\varepsilon$-MemEvo: Adaptive Cross-Task Memory Transfer for LLM Program Evolution](content/papers/varepsilon-memevo-adaptive-cross-task-memory-transfer-for-llm-program-evolution.md) | benchmark |
| 2026-08-11 | arXiv | [TARL: Transaction-Aware Reliable Ledgers for Executable Memory Management in Long-Term Agents](content/papers/tarl-transaction-aware-reliable-ledgers-for-executable-memory-management-in-long.md) | agent, benchmark, long-term |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
