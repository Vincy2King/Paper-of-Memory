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

- Total tracked papers: **1155**
- Last generated: **2026-09-26**

## Papers by Source

- ACL Anthology: **6**
- arXiv: **1003**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-09-22 | OpenReview | [Temporal Context Reinstatement Drives Episodic-Like Order Memory in Long-Context Language Models](content/papers/temporal-context-reinstatement-drives-episodic-like-order-memory-in-long-context.md) | context, episodic, long-term |
| 2026-09-22 | OpenReview | [PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?](content/papers/persistbench-when-should-long-term-memories-be-forgotten-by-llms.md) | benchmark, context, conversation |
| 2026-09-22 | OpenReview | [MemEvolve: Meta-Evolution of Agent Memory Systems](content/papers/memevolve-meta-evolution-of-agent-memory-systems.md) | agent, benchmark, context |
| 2026-09-22 | OpenReview | [GAM-RAG: Gain-Adaptive Memory for Evolving Retrieval in Retrieval-Augmented Generation](content/papers/gam-rag-gain-adaptive-memory-for-evolving-retrieval-in-retrieval-augmented-gener.md) | retrieval |
| 2026-09-22 | OpenReview | [Episodic Memory-Guided Controllable Experience Synthesis for Reinforcement Learning](content/papers/episodic-memory-guided-controllable-experience-synthesis-for-reinforcement-learn.md) | episodic |
| 2026-09-22 | OpenReview | [Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks](content/papers/benchmarking-agent-memory-in-interdependent-multi-session-agentic-tasks.md) | agent, benchmark, context |
| 2026-09-22 | OpenReview | [AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications](content/papers/ama-bench-evaluating-long-horizon-memory-for-agentic-applications.md) | agent, benchmark, retrieval |
| 2026-09-21 | OpenReview | [MADrive: Memory-Augmented Driving Scene Modeling](content/papers/madrive-memory-augmented-driving-scene-modeling.md) | retrieval |
| 2026-09-20 | OpenReview | [Think-in-Memory: Metacognition-Augmented LLM with Long-Term Memory](content/papers/think-in-memory-metacognition-augmented-llm-with-long-term-memory.md) | agent, context, conversation |
| 2026-09-20 | OpenReview | [Preference-aware memory update for long-term llm agents](content/papers/preference-aware-memory-update-for-long-term-llm-agents.md) | agent, context, conversation |
| 2026-09-19 | OpenReview | [Revisiting Persistent Indexing Structures on Intel Optane DC Persistent Memory](content/papers/revisiting-persistent-indexing-structures-on-intel-optane-dc-persistent-memory.md) | persistent memory |
| 2026-09-15 | arXiv | [Smarter by the Moment: Environment-Driven Dynamic Policies for Continual LLM Improvement](content/papers/smarter-by-the-moment-environment-driven-dynamic-policies-for-continual-llm-impr.md) | benchmark, retrieval |
| 2026-09-15 | arXiv | [Persistent Recurrent Memory Between Transformer Layers - Improves Language Model Generalization](content/papers/persistent-recurrent-memory-between-transformer-layers-improves-language-model-g.md) | persistent memory |
| 2026-09-15 | arXiv | [LSREP: A Longitudinal State-Replay Protocol for Evaluating Conversational Memory, with ICE v2 as an Audited Local-First Architecture](content/papers/lsrep-a-longitudinal-state-replay-protocol-for-evaluating-conversational-memory-.md) | context, conversation, retrieval |
| 2026-09-14 | arXiv | [Where to Look and What to Use: Retrieve-Localize-Generate for Long-Term Conversational Memory Question Answering](content/papers/where-to-look-and-what-to-use-retrieve-localize-generate-for-long-term-conversat.md) | benchmark, context, conversation |
| 2026-09-14 | arXiv | [Semantic-TVM: Structure-Preserving Trustworthy Virtual Memory for Memory-Augmented and Tool-Using Agents](content/papers/semantic-tvm-structure-preserving-trustworthy-virtual-memory-for-memory-augmente.md) | agent, context |
| 2026-09-13 | arXiv | [The Immutable Past: Formalizing State Mutability and Conflict Resolution in Mutable RAG](content/papers/the-immutable-past-formalizing-state-mutability-and-conflict-resolution-in-mutab.md) | agent, benchmark, context |
| 2026-09-13 | arXiv | [Retrieval-Driven Memory Reconsolidation for Long-Term LLM Agents](content/papers/retrieval-driven-memory-reconsolidation-for-long-term-llm-agents.md) | agent, long-term, retrieval |
| 2026-09-13 | arXiv | [Pull: Lazy Materialization of Working Memory for Stateful LLM Conversations](content/papers/pull-lazy-materialization-of-working-memory-for-stateful-llm-conversations.md) | benchmark, compression, context |
| 2026-09-13 | arXiv | [Bioinfoysis Technical Report](content/papers/bioinfoysis-technical-report.md) | agent, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
