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

- Total tracked papers: **1530**
- Last generated: **2026-10-29**

## Papers by Source

- ACL Anthology: **17**
- arXiv: **1367**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-10-27 | arXiv | [TrawMem: Reframing Agent Memory as Task-Oriented Role-Adaptive Workspaces](content/papers/trawmem-reframing-agent-memory-as-task-oriented-role-adaptive-workspaces.md) | agent, context, long-term |
| 2026-10-27 | arXiv | [SEEK: Skill Extraction with Evolving Knowledge against Frontier Science Agents](content/papers/seek-skill-extraction-with-evolving-knowledge-against-frontier-science-agents.md) | agent, benchmark |
| 2026-10-27 | arXiv | [ReMCTS: Reflection-Enhanced Monte Carlo Tree Search for Code Generation](content/papers/remcts-reflection-enhanced-monte-carlo-tree-search-for-code-generation.md) | context |
| 2026-10-27 | arXiv | [From Voiceprints to User Entities: Online Speaker-Memory Construction for Multi-User Spoken Agents](content/papers/from-voiceprints-to-user-entities-online-speaker-memory-construction-for-multi-u.md) | agent, benchmark, retrieval |
| 2026-10-27 | arXiv | [ETAMem: Decoupling and Aligning Heterogeneous Memory for Long-Term Conversational Agents](content/papers/etamem-decoupling-and-aligning-heterogeneous-memory-for-long-term-conversational.md) | agent, conversation, long-term |
| 2026-10-27 | arXiv | [ACOR: incremental evidence accumulation towards real-time DNA storage reconstruction](content/papers/acor-incremental-evidence-accumulation-towards-real-time-dna-storage-reconstruct.md) | benchmark, context |
| 2026-10-26 | arXiv | [When Retrieval Is Not Enough: Obsolete Facts in Agent Memory](content/papers/when-retrieval-is-not-enough-obsolete-facts-in-agent-memory.md) | agent, benchmark, retrieval |
| 2026-10-26 | arXiv | [The Right Fact, the Wrong Decision: SciValidityBench for Scientific Agent Memory](content/papers/the-right-fact-the-wrong-decision-scivaliditybench-for-scientific-agent-memory.md) | agent, benchmark, long-term |
| 2026-10-26 | arXiv | [The Geometry of Agent Memory: Forecasting Retrieval-Bound Memory Failures, and Characterizing Its Limits](content/papers/the-geometry-of-agent-memory-forecasting-retrieval-bound-memory-failures-and-cha.md) | agent, context, conversation |
| 2026-10-26 | arXiv | [Learning to Remember: Advances in Memory Mechanisms for Large Language Models](content/papers/learning-to-remember-advances-in-memory-mechanisms-for-large-language-models.md) | agent, benchmark, context |
| 2026-10-26 | arXiv | [BehaviorMem: Building and Evaluating User Memory from Real-World E-Commerce Behavior Streams](content/papers/behaviormem-building-and-evaluating-user-memory-from-real-world-e-commerce-behav.md) | agent, benchmark, long-term |
| 2026-10-26 | arXiv | [Agent Memory as Recommendation: Recommender-System Design for Long-Term Memory of LLM Agents](content/papers/agent-memory-as-recommendation-recommender-system-design-for-long-term-memory-of.md) | agent, context, long-term |
| 2026-10-26 | arXiv | [Adaptive Memory Index Evolution for Agents](content/papers/adaptive-memory-index-evolution-for-agents.md) | agent, benchmark, retrieval |
| 2026-10-25 | arXiv | [Variational Cognitive Memory Abstraction for Long-Horizon Vision-Language-Action Models](content/papers/variational-cognitive-memory-abstraction-for-long-horizon-vision-language-action.md) | benchmark, compression, retrieval |
| 2026-10-25 | arXiv | [SEEK: Skill Extraction with Evolving Knowledge against Frontier Science Agents](content/papers/seek-skill-extraction-with-evolving-knowledge-against-frontier-science-agents.md) | agent, benchmark |
| 2026-10-25 | arXiv | [Memory Tax: Dissecting the Net Value of Agent Memory](content/papers/memory-tax-dissecting-the-net-value-of-agent-memory.md) | agent, benchmark, retrieval |
| 2026-10-25 | arXiv | [EvolveMAS: A Unified Self-Evolution Framework for Decentralized Multi-Agent Systems](content/papers/evolvemas-a-unified-self-evolution-framework-for-decentralized-multi-agent-syste.md) | agent, benchmark, context |
| 2026-10-25 | arXiv | [EMMA: Structured Episodic Memory for Multi-Agent Workflow Synthesis](content/papers/emma-structured-episodic-memory-for-multi-agent-workflow-synthesis.md) | agent, benchmark, context |
| 2026-10-25 | arXiv | [ClawMMU: Protection-Coherent Virtual Memory for Stateful LLM Agents](content/papers/clawmmu-protection-coherent-virtual-memory-for-stateful-llm-agents.md) | agent, context, long-term |
| 2026-10-25 | arXiv | [CaliMem: Search-Efficient Data Agent via Calibrated Memory](content/papers/calimem-search-efficient-data-agent-via-calibrated-memory.md) | agent |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
