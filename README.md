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

- Total tracked papers: **1508**
- Last generated: **2026-10-26**

## Papers by Source

- ACL Anthology: **17**
- arXiv: **1345**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-10-23 | arXiv | [When to Trust Memory: Retrieval-Guided Probabilistic Spatiotemporal Forecasting under Distribution Shift](content/papers/when-to-trust-memory-retrieval-guided-probabilistic-spatiotemporal-forecasting-u.md) | retrieval |
| 2026-10-23 | arXiv | [Lifelong Context Adaptation through Bidirectional Memory-Skill Learning](content/papers/lifelong-context-adaptation-through-bidirectional-memory-skill-learning.md) | agent, context, conversation |
| 2026-10-23 | arXiv | [Agentic Memory Management Is the Next Frontier of Information Retrieval](content/papers/agentic-memory-management-is-the-next-frontier-of-information-retrieval.md) | agent, benchmark, retrieval |
| 2026-10-23 | arXiv | [ActionRAG: Evidence-Refining Graph Diffusion for Long-Term Memory in LLM Agents](content/papers/actionrag-evidence-refining-graph-diffusion-for-long-term-memory-in-llm-agents.md) | agent, long-term, retrieval |
| 2026-10-22 | ACL Anthology | [Shared Selective Persistent Memory for Agentic LLM Systems](content/papers/shared-selective-persistent-memory-for-agentic-llm-systems.md) | agent |
| 2026-10-22 | ACL Anthology | [Retrieval is Enough: A Memory-Augmented Agent for Algorithm Selection](content/papers/retrieval-is-enough-a-memory-augmented-agent-for-algorithm-selection.md) | agent, retrieval |
| 2026-10-22 | arXiv | [Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation](content/papers/memory-before-goal-role-of-pre-history-memory-for-humanoid-loco-manipulation.md) | benchmark |
| 2026-10-22 | ACL Anthology | [MemTools: A Unified Research Framework for Interoperable Agent Memory](content/papers/memtools-a-unified-research-framework-for-interoperable-agent-memory.md) | agent |
| 2026-10-22 | arXiv | [Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought](content/papers/is-complex-agentic-memory-always-needed-naive-rag-is-stronger-than-we-thought.md) | agent, benchmark, conversation |
| 2026-10-22 | arXiv | [Governance-State Corruption in Long-Term Memory for LLM Agents: A Cross-Model Stress Test](content/papers/governance-state-corruption-in-long-term-memory-for-llm-agents-a-cross-model-str.md) | agent, benchmark, context |
| 2026-10-22 | arXiv | [Disclosure Begets Disclosure: A Self-Reinforcing Privacy Loop in LLM Agents with Persistent Memory](content/papers/disclosure-begets-disclosure-a-self-reinforcing-privacy-loop-in-llm-agents-with-.md) | agent |
| 2026-10-22 | ACL Anthology | [Causal Episodic Memory for Feedback-Driven Agent Repair](content/papers/causal-episodic-memory-for-feedback-driven-agent-repair.md) | agent, episodic |
| 2026-10-22 | ACL Anthology | [AgenticLOCI: A Multi-Agent Memory Framework for Conversational AI with Longitudinal Personalization](content/papers/agenticloci-a-multi-agent-memory-framework-for-conversational-ai-with-longitudin.md) | agent, conversation |
| 2026-10-22 | arXiv | [AfterDeleteBench: Auditing Post-Deletion Information Persistence in LLM Agents](content/papers/afterdeletebench-auditing-post-deletion-information-persistence-in-llm-agents.md) | agent |
| 2026-10-22 | arXiv | [A Mathematical Theory of the Jacobian Lens](content/papers/a-mathematical-theory-of-the-jacobian-lens.md) | context |
| 2026-10-21 | arXiv | [Why Bother Me Again? Benchmarking Personal Agent Memory for Interaction Preferences](content/papers/why-bother-me-again-benchmarking-personal-agent-memory-for-interaction-preferenc.md) | agent, benchmark, context |
| 2026-10-21 | arXiv | [Uni-Mem: Learning a Long-Horizon Agentic Memory Manager with Unified Online Policy Optimization](content/papers/uni-mem-learning-a-long-horizon-agentic-memory-manager-with-unified-online-polic.md) | agent, long-term, retrieval |
| 2026-10-21 | arXiv | [Remembering Through Change: Provenance-Preserving Hypergraph Memory for Multimodal Agents](content/papers/remembering-through-change-provenance-preserving-hypergraph-memory-for-multimoda.md) | agent, benchmark, long-term |
| 2026-10-21 | arXiv | [MemoryTax: The Bitter Lesson of Agent Memory](content/papers/memorytax-the-bitter-lesson-of-agent-memory.md) | agent, context, conversation |
| 2026-10-21 | arXiv | [Memory-Centric Continual Learning for AI Agents](content/papers/memory-centric-continual-learning-for-ai-agents.md) | agent, context, long-term |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
