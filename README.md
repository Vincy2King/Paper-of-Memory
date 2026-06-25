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

- Total tracked papers: **578**
- Last generated: **2026-06-25**

## Papers by Source

- ACL Anthology: **4**
- arXiv: **483**
- OpenReview: **91**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-06-24 | OpenReview | [The Override Cliff: How Agent Memory Hijacks LLM Reasoning](content/papers/the-override-cliff-how-agent-memory-hijacks-llm-reasoning.md) | agent, benchmark, retrieval |
| 2026-06-24 | OpenReview | [Temporal Context Reinstatement Drives Episodic-Like Order Memory in Long-Context Language Models](content/papers/temporal-context-reinstatement-drives-episodic-like-order-memory-in-long-context.md) | context, episodic, long-term |
| 2026-06-24 | OpenReview | [PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?](content/papers/persistbench-when-should-long-term-memories-be-forgotten-by-llms.md) | benchmark, context, conversation |
| 2026-06-24 | OpenReview | [MemRefine: LLM-Guided Compression for Long-Term Agent Memory](content/papers/memrefine-llm-guided-compression-for-long-term-agent-memory.md) | agent, benchmark, compression |
| 2026-06-24 | OpenReview | [MemEvolve: Meta-Evolution of Agent Memory Systems](content/papers/memevolve-meta-evolution-of-agent-memory-systems.md) | agent, benchmark, context |
| 2026-06-24 | OpenReview | [GAM-RAG: Gain-Adaptive Memory for Evolving Retrieval in Retrieval-Augmented Generation](content/papers/gam-rag-gain-adaptive-memory-for-evolving-retrieval-in-retrieval-augmented-gener.md) | retrieval |
| 2026-06-24 | OpenReview | [Episodic Memory-Guided Controllable Experience Synthesis for Reinforcement Learning](content/papers/episodic-memory-guided-controllable-experience-synthesis-for-reinforcement-learn.md) | episodic |
| 2026-06-24 | OpenReview | [EngramaBench: Evaluating Long-Term Conversational Memory with Structured Graph Retrieval](content/papers/engramabench-evaluating-long-term-conversational-memory-with-structured-graph-re.md) | benchmark, context, conversation |
| 2026-06-24 | OpenReview | [Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks](content/papers/benchmarking-agent-memory-in-interdependent-multi-session-agentic-tasks.md) | agent, benchmark, context |
| 2026-06-24 | OpenReview | [AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications](content/papers/ama-bench-evaluating-long-horizon-memory-for-agentic-applications.md) | agent, benchmark, retrieval |
| 2026-06-23 | arXiv | [Reasoning as Attractor Dynamics: Latent Memory Retrieval via Gibbs-Weighted Energy Minimization](content/papers/reasoning-as-attractor-dynamics-latent-memory-retrieval-via-gibbs-weighted-energ.md) | retrieval |
| 2026-06-23 | arXiv | [ReMMD: Realistic Multilingual Multi-Image Agentic Verification for Multimodal Misinformation Detection](content/papers/remmd-realistic-multilingual-multi-image-agentic-verification-for-multimodal-mis.md) | agent, benchmark |
| 2026-06-23 | arXiv | [ReM-MoA: Reasoning Memory Sustains Mixture-of-Agents Scaling](content/papers/rem-moa-reasoning-memory-sustains-mixture-of-agents-scaling.md) | agent, benchmark |
| 2026-06-23 | OpenReview | [MemoryVLN: Memory-Augmented Vision-Language Navigation](content/papers/memoryvln-memory-augmented-vision-language-navigation.md) | agent, benchmark, context |
| 2026-06-23 | arXiv | [MEMPROBE: Probing Long-Term Agent Memory via Hidden User-State Recovery](content/papers/memprobe-probing-long-term-agent-memory-via-hidden-user-state-recovery.md) | agent, benchmark, long-term |
| 2026-06-23 | arXiv | [Governed Shared Memory for Multi-Agent LLM Systems](content/papers/governed-shared-memory-for-multi-agent-llm-systems.md) | agent, context, retrieval |
| 2026-06-23 | arXiv | [Are We Ready For An Agent-Native Memory System?](content/papers/are-we-ready-for-an-agent-native-memory-system.md) | agent, benchmark, retrieval |
| 2026-06-23 | OpenReview | [AgenticLOCI: A Multi-Agent Memory Framework for Conversational AI with Longitudinal Personalization](content/papers/agenticloci-a-multi-agent-memory-framework-for-conversational-ai-with-longitudin.md) | agent, benchmark, context |
| 2026-06-22 | arXiv | [Unlimited OCR Works](content/papers/unlimited-ocr-works.md) | compression |
| 2026-06-22 | arXiv | [Towards Root Memories: Benchmarking and Enhancing Implicit Logical Memory Retrieval for Personalized LLMs](content/papers/towards-root-memories-benchmarking-and-enhancing-implicit-logical-memory-retriev.md) | agent, benchmark, long-term |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
