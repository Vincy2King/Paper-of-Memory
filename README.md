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

- Total tracked papers: **591**
- Last generated: **2026-06-26**

## Papers by Source

- ACL Anthology: **4**
- arXiv: **496**
- OpenReview: **91**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-06-26 | OpenReview | [TAME: A Trustworthy Test-Time Evolution of Agent Memory with Systematic Benchmarking](content/papers/tame-a-trustworthy-test-time-evolution-of-agent-memory-with-systematic-benchmark.md) | agent, benchmark |
| 2026-06-25 | arXiv | [The Riddle Riddle: Testing Flexible Reasoning in Large Language Models and Humans](content/papers/the-riddle-riddle-testing-flexible-reasoning-in-large-language-models-and-humans.md) | retrieval |
| 2026-06-25 | arXiv | [Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge](content/papers/temporal-validity-in-retrieval-memory-eliminating-stale-fact-errors-for-ai-agent.md) | agent, benchmark, retrieval |
| 2026-06-25 | arXiv | [EvoEmbedding: Evolvable Representations for Long-Context Retrieval and Agentic Memory](content/papers/evoembedding-evolvable-representations-for-long-context-retrieval-and-agentic-me.md) | agent, benchmark, context |
| 2026-06-25 | OpenReview | [EngramaBench: Evaluating Long-Term Conversational Memory with Structured Graph Retrieval](content/papers/engramabench-evaluating-long-term-conversational-memory-with-structured-graph-re.md) | benchmark, context, conversation |
| 2026-06-25 | arXiv | [ConvMemory v3: A Validity Context Layer for Conversational Memory via Target-Conditioned Relation Verification](content/papers/convmemory-v3-a-validity-context-layer-for-conversational-memory-via-target-cond.md) | benchmark, context, conversation |
| 2026-06-25 | arXiv | [Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents](content/papers/agents-that-know-too-much-a-data-centric-survey-of-privacy-in-llm-agents.md) | agent, benchmark, context |
| 2026-06-24 | OpenReview | [The Override Cliff: How Agent Memory Hijacks LLM Reasoning](content/papers/the-override-cliff-how-agent-memory-hijacks-llm-reasoning.md) | agent, benchmark, retrieval |
| 2026-06-24 | OpenReview | [Temporal Context Reinstatement Drives Episodic-Like Order Memory in Long-Context Language Models](content/papers/temporal-context-reinstatement-drives-episodic-like-order-memory-in-long-context.md) | context, episodic, long-term |
| 2026-06-24 | OpenReview | [PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?](content/papers/persistbench-when-should-long-term-memories-be-forgotten-by-llms.md) | benchmark, context, conversation |
| 2026-06-24 | arXiv | [Memory Makes the Difference: Evaluating How Different Memory Roles Shape Conversational Agents](content/papers/memory-makes-the-difference-evaluating-how-different-memory-roles-shape-conversa.md) | agent, context, conversation |
| 2026-06-24 | arXiv | [Memory Contagion: Cross-Temporal Propagation of Evaluator Bias via Agent Memory](content/papers/memory-contagion-cross-temporal-propagation-of-evaluator-bias-via-agent-memory.md) | agent, long-term |
| 2026-06-24 | OpenReview | [MemRefine: LLM-Guided Compression for Long-Term Agent Memory](content/papers/memrefine-llm-guided-compression-for-long-term-agent-memory.md) | agent, benchmark, compression |
| 2026-06-24 | OpenReview | [MemEvolve: Meta-Evolution of Agent Memory Systems](content/papers/memevolve-meta-evolution-of-agent-memory-systems.md) | agent, benchmark, context |
| 2026-06-24 | arXiv | [Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions with Context Optimization](content/papers/is-graphrag-needed-from-basic-rag-to-graph-agentic-solutions-with-context-optimi.md) | agent, context, retrieval |
| 2026-06-24 | OpenReview | [GAM-RAG: Gain-Adaptive Memory for Evolving Retrieval in Retrieval-Augmented Generation](content/papers/gam-rag-gain-adaptive-memory-for-evolving-retrieval-in-retrieval-augmented-gener.md) | retrieval |
| 2026-06-24 | OpenReview | [Episodic Memory-Guided Controllable Experience Synthesis for Reinforcement Learning](content/papers/episodic-memory-guided-controllable-experience-synthesis-for-reinforcement-learn.md) | episodic |
| 2026-06-24 | OpenReview | [Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks](content/papers/benchmarking-agent-memory-in-interdependent-multi-session-agentic-tasks.md) | agent, benchmark, context |
| 2026-06-24 | arXiv | [Active Adversarial Perturbation-driven Associative Memory Retrieval for RGB-Event Visual Object Tracking](content/papers/active-adversarial-perturbation-driven-associative-memory-retrieval-for-rgb-even.md) | retrieval |
| 2026-06-24 | OpenReview | [AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications](content/papers/ama-bench-evaluating-long-horizon-memory-for-agentic-applications.md) | agent, benchmark, retrieval |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
