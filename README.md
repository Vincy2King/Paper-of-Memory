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

- Total tracked papers: **565**
- Last generated: **2026-06-23**

## Papers by Source

- ACL Anthology: **4**
- arXiv: **477**
- OpenReview: **84**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-06-23 | OpenReview | [MemoryVLN: Memory-Augmented Vision-Language Navigation](content/papers/memoryvln-memory-augmented-vision-language-navigation.md) | agent, benchmark, context |
| 2026-06-23 | OpenReview | [AgenticLOCI: A Multi-Agent Memory Framework for Conversational AI with Longitudinal Personalization](content/papers/agenticloci-a-multi-agent-memory-framework-for-conversational-ai-with-longitudin.md) | agent, benchmark, context |
| 2026-06-22 | arXiv | [Unlimited OCR Works](content/papers/unlimited-ocr-works.md) | compression |
| 2026-06-22 | arXiv | [Towards Root Memories: Benchmarking and Enhancing Implicit Logical Memory Retrieval for Personalized LLMs](content/papers/towards-root-memories-benchmarking-and-enhancing-implicit-logical-memory-retriev.md) | agent, benchmark, long-term |
| 2026-06-22 | arXiv | [RaMem: Contextual Reinstatement for Long-term Agentic Memory](content/papers/ramem-contextual-reinstatement-for-long-term-agentic-memory.md) | agent, benchmark, context |
| 2026-06-22 | arXiv | [Memory Contagion: Cross-Temporal Propagation of Evaluator Bias via Agent Memory](content/papers/memory-contagion-cross-temporal-propagation-of-evaluator-bias-via-agent-memory.md) | agent, long-term |
| 2026-06-22 | arXiv | [GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge](content/papers/gitofthoughts-version-controlled-reasoning-and-agent-memory-you-can-replay-diff-.md) | agent, benchmark, context |
| 2026-06-22 | OpenReview | [GATEMEM: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents](content/papers/gatemem-benchmarking-memory-governance-in-multi-principal-shared-memory-agents.md) | agent, benchmark, context |
| 2026-06-22 | arXiv | [FinAcumen: Financial Multimodal Reasoning via Self-Evolving Experience Memory Harness](content/papers/finacumen-financial-multimodal-reasoning-via-self-evolving-experience-memory-har.md) | agent, benchmark, retrieval |
| 2026-06-22 | arXiv | [DynamicMem: A Long-Horizon Memory Benchmark in Real-World Settings](content/papers/dynamicmem-a-long-horizon-memory-benchmark-in-real-world-settings.md) | agent, benchmark, context |
| 2026-06-22 | ACL Anthology | [CloneMem: Benchmarking Long-Term Memory for AI Clones](content/papers/clonemem-benchmarking-long-term-memory-for-ai-clones.md) | benchmark, long-term |
| 2026-06-22 | ACL Anthology | [Beyond Markovian Forgetfulness: Episodic Memory for Reasoning-Intensive Retrieval](content/papers/beyond-markovian-forgetfulness-episodic-memory-for-reasoning-intensive-retrieval.md) | episodic, retrieval |
| 2026-06-22 | ACL Anthology | [BMAM: Brain-inspired Multi-Agent Memory Framework](content/papers/bmam-brain-inspired-multi-agent-memory-framework.md) | agent |
| 2026-06-22 | OpenReview | [AtomMem: Learnable Dynamic Agentic Memory with Atomic Memory Operation](content/papers/atommem-learnable-dynamic-agentic-memory-with-atomic-memory-operation.md) | agent, benchmark, context |
| 2026-06-21 | arXiv | [PairAlign: A Framework for Sequence Tokenization via Self-Alignment with Applications to Audio Tokenization](content/papers/pairalign-a-framework-for-sequence-tokenization-via-self-alignment-with-applicat.md) | retrieval |
| 2026-06-21 | OpenReview | [EngramaBench: Evaluating Long-Term Conversational Memory with Structured Graph Retrieval](content/papers/engramabench-evaluating-long-term-conversational-memory-with-structured-graph-re.md) | benchmark, context, conversation |
| 2026-06-21 | OpenReview | [Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems](content/papers/caching-for-the-future-scrub-jay-episodic-memory-principles-for-agent-memory-sys.md) | agent, benchmark, context |
| 2026-06-21 | arXiv | [Benchmarking Robot Memory Under Interference](content/papers/benchmarking-robot-memory-under-interference.md) | benchmark, context |
| 2026-06-20 | OpenReview | [TAME: A Trustworthy Test-Time Evolution of Agent Memory with Systematic Benchmarking](content/papers/tame-a-trustworthy-test-time-evolution-of-agent-memory-with-systematic-benchmark.md) | agent, benchmark |
| 2026-06-20 | OpenReview | [Same Ranking, Different Winner: How Scoring Targets Shape LLM Memory Benchmarks](content/papers/same-ranking-different-winner-how-scoring-targets-shape-llm-memory-benchmarks.md) | benchmark, conversation, retrieval |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
