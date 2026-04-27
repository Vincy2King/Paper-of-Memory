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

- Total tracked papers: **77**
- Last generated: **2026-04-27**

## Papers by Source

- arXiv: **47**
- OpenReview: **30**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-04-25 | OpenReview | [WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance](content/papers/webcoach-self-evolving-web-agents-with-cross-session-memory-guidance.md) | agent, benchmark, context |
| 2026-04-25 | OpenReview | [PROCED-MEM: BENCHMARKING PROCEDURAL MEMORY RETRIEVAL IN LANGUAGE AGENTS ACROSS DOMAINS](content/papers/proced-mem-benchmarking-procedural-memory-retrieval-in-language-agents-across-do.md) | agent, benchmark, context |
| 2026-04-25 | OpenReview | [MemoGraph: Augmenting LLMs with Explicit Episodic Memory for Multi-step Mathematical Reasoning](content/papers/memograph-augmenting-llms-with-explicit-episodic-memory-for-multi-step-mathemati.md) | agent, benchmark, context |
| 2026-04-25 | OpenReview | [MEMORY IS RECONSTRUCTED, NOT RETRIEVED: GRAPH MEMORY FOR LLM AGENTS](content/papers/memory-is-reconstructed-not-retrieved-graph-memory-for-llm-agents.md) | agent, benchmark, context |
| 2026-04-25 | OpenReview | [Learning Safe Robot Planning from Unsafe Experiences: An Episodic Memory Approach for LLM-based Agents](content/papers/learning-safe-robot-planning-from-unsafe-experiences-an-episodic-memory-approach.md) | agent, episodic, retrieval |
| 2026-04-25 | OpenReview | [Episodic Memory from Compression Boundaries in Latent Representation Space](content/papers/episodic-memory-from-compression-boundaries-in-latent-representation-space.md) | agent, compression, context |
| 2026-04-25 | OpenReview | [ENGRAM: Effective, Lightweight Memory Orchestration for Conversational Agents](content/papers/engram-effective-lightweight-memory-orchestration-for-conversational-agents.md) | agent, benchmark, context |
| 2026-04-25 | OpenReview | [Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory](content/papers/diagnosing-retrieval-vs-utilization-bottlenecks-in-llm-agent-memory.md) | agent, context, retrieval |
| 2026-04-25 | OpenReview | [CloneMem: Benchmarking Long-Term Memory for AI Clones](content/papers/clonemem-benchmarking-long-term-memory-for-ai-clones.md) | agent, benchmark, conversation |
| 2026-04-25 | OpenReview | [AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications](content/papers/ama-bench-evaluating-long-horizon-memory-for-agentic-applications.md) | agent, benchmark, retrieval |
| 2026-04-24 | arXiv | [Beyond N-gram: Data-Aware X-GRAM Extraction for Efficient Embedding Parameter Scaling](content/papers/beyond-n-gram-data-aware-x-gram-extraction-for-efficient-embedding-parameter-sca.md) | context, retrieval |
| 2026-04-23 | arXiv | [Working Memory Constraints Scaffold Learning in Transformers under Data Scarcity](content/papers/working-memory-constraints-scaffold-learning-in-transformers-under-data-scarcity.md) | working memory |
| 2026-04-23 | arXiv | [Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture](content/papers/spatial-metaphors-for-llm-memory-a-critical-analysis-of-the-mempalace-architectu.md) | benchmark, long-term, retrieval |
| 2026-04-23 | arXiv | [Seeing Further and Wider: Joint Spatio-Temporal Enlargement for Micro-Video Popularity Prediction](content/papers/seeing-further-and-wider-joint-spatio-temporal-enlargement-for-micro-video-popul.md) | benchmark, retrieval |
| 2026-04-23 | arXiv | [Memanto: Typed Semantic Memory with Information-Theoretic Retrieval for Long-Horizon Agents](content/papers/memanto-typed-semantic-memory-with-information-theoretic-retrieval-for-long-hori.md) | agent, benchmark, retrieval |
| 2026-04-23 | arXiv | [FSFM: A Biologically-Inspired Framework for Selective Forgetting of Agent Memory](content/papers/fsfm-a-biologically-inspired-framework-for-selective-forgetting-of-agent-memory.md) | agent, context |
| 2026-04-23 | arXiv | [EngramaBench: Evaluating Long-Term Conversational Memory with Structured Graph Retrieval](content/papers/engramabench-evaluating-long-term-conversational-memory-with-structured-graph-re.md) | benchmark, context, conversation |
| 2026-04-23 | arXiv | [Dementia classification from spontaneous speech using wrapper-based feature selection](content/papers/dementia-classification-from-spontaneous-speech-using-wrapper-based-feature-sele.md) | memory |
| 2026-04-23 | arXiv | [ColorBrowserAgent: Complex Long-Horizon Browser Agent with Adaptive Knowledge Evolution](content/papers/colorbrowseragent-complex-long-horizon-browser-agent-with-adaptive-knowledge-evo.md) | agent, compression |
| 2026-04-23 | arXiv | [Beyond N-gram: Data-Aware X-GRAM Extraction for Efficient Embedding Parameter Scaling](content/papers/beyond-n-gram-data-aware-x-gram-extraction-for-efficient-embedding-parameter-sca.md) | context, retrieval |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
