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

- Total tracked papers: **1683**
- Last generated: **2026-11-17**

## Papers by Source

- ACL Anthology: **24**
- arXiv: **1513**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-11-16 | arXiv | [We Are What We Remember: Mental-State-Driven Memory for Long-Term Character Dialogue](content/papers/we-are-what-we-remember-mental-state-driven-memory-for-long-term-character-dialo.md) | agent, benchmark, context |
| 2026-11-16 | arXiv | [Memadapter: Counterfactual Adaptation Against Memory-induced Sycophancy](content/papers/memadapter-counterfactual-adaptation-against-memory-induced-sycophancy.md) | agent, benchmark, context |
| 2026-11-16 | arXiv | [MemDoctor: Stage-wise Error Attribution and Repair for MLLM Agent Memory](content/papers/memdoctor-stage-wise-error-attribution-and-repair-for-mllm-agent-memory.md) | agent |
| 2026-11-16 | arXiv | [Jetriever: Shifting Agent Memory Retrieval from Similarity to Utility](content/papers/jetriever-shifting-agent-memory-retrieval-from-similarity-to-utility.md) | agent, retrieval |
| 2026-11-16 | arXiv | [Instant Weight-Space Consolidation for Long-Term Memory in LLMs](content/papers/instant-weight-space-consolidation-for-long-term-memory-in-llms.md) | agent, conversation, episodic |
| 2026-11-15 | arXiv | [When Facts Change, Which Decisions Break? Dependency-Aware Context Graphs for Agents](content/papers/when-facts-change-which-decisions-break-dependency-aware-context-graphs-for-agen.md) | agent, benchmark, context |
| 2026-11-15 | arXiv | [StaleBench: Isolating Stale Retrieval in Agent Memory, and Pricing the Fix](content/papers/stalebench-isolating-stale-retrieval-in-agent-memory-and-pricing-the-fix.md) | agent, retrieval |
| 2026-11-15 | arXiv | [Remember, Replay, Adapt: Learning from Past Experience in Online Vision-and-Language Navigation](content/papers/remember-replay-adapt-learning-from-past-experience-in-online-vision-and-languag.md) | benchmark, episodic |
| 2026-11-15 | arXiv | [MINDSET: Energy-based Memory Evolution for Long Conversational Agents](content/papers/mindset-energy-based-memory-evolution-for-long-conversational-agents.md) | agent, context, conversation |
| 2026-11-15 | arXiv | [HEAMS: Holistic Evaluation of Agent Memory Systems](content/papers/heams-holistic-evaluation-of-agent-memory-systems.md) | agent, benchmark, context |
| 2026-11-14 | arXiv | [What Moves a LoCoMo Score? Memory Context, Answer Prompts and Judges](content/papers/what-moves-a-locomo-score-memory-context-answer-prompts-and-judges.md) | agent, benchmark, context |
| 2026-11-14 | arXiv | [Personalized Memory Rubrics: Learning What to Remember per User via Rubric-Guided Credit Assignment](content/papers/personalized-memory-rubrics-learning-what-to-remember-per-user-via-rubric-guided.md) | agent, benchmark |
| 2026-11-14 | arXiv | [Omni-Workspace: Benchmarking Omni-Modal AI Assistants on Multimodal Workspace Tasks](content/papers/omni-workspace-benchmarking-omni-modal-ai-assistants-on-multimodal-workspace-tas.md) | agent, benchmark, context |
| 2026-11-14 | arXiv | [B2G-Agent: An LLM-Based Multi-Agent Tool for End-to-End Building-Grid Interactions](content/papers/b2g-agent-an-llm-based-multi-agent-tool-for-end-to-end-building-grid-interaction.md) | agent, retrieval |
| 2026-11-13 | arXiv | [Who Should Be on the Panel? Task-Conditioned Persona Selection for LLM Trading Agents](content/papers/who-should-be-on-the-panel-task-conditioned-persona-selection-for-llm-trading-ag.md) | agent |
| 2026-11-13 | arXiv | [RecMem: Recurrent Memory Compression for Long-Sequence Generative Recommendation](content/papers/recmem-recurrent-memory-compression-for-long-sequence-generative-recommendation.md) | compression, context, retrieval |
| 2026-11-13 | arXiv | [MIGRO: A Decoupled and Portable Long-Term Memory System for Language Models](content/papers/migro-a-decoupled-and-portable-long-term-memory-system-for-language-models.md) | context, long-term, retrieval |
| 2026-11-13 | arXiv | [Cheap Retrieval and Observation Credit Assignment from One Quantity: The Value of Information](content/papers/cheap-retrieval-and-observation-credit-assignment-from-one-quantity-the-value-of.md) | retrieval |
| 2026-11-12 | arXiv | [We Are What We Remember: Mental-State-Driven Memory for Long-Term Character Dialogue](content/papers/we-are-what-we-remember-mental-state-driven-memory-for-long-term-character-dialo.md) | agent, benchmark, context |
| 2026-11-12 | arXiv | [HeMeR: Heterogeneous Memory Reconciliation for Embodied Agents via Structured KV Reuse](content/papers/hemer-heterogeneous-memory-reconciliation-for-embodied-agents-via-structured-kv-.md) | agent, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
