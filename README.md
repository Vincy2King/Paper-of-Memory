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

- Total tracked papers: **411**
- Last generated: **2026-06-03**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **343**
- OpenReview: **67**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-06-02 | OpenReview | [When Users Don’t Ask: Benchmarking Context-Driven Memory Retrieval in Conversational Agents](content/papers/when-users-dont-ask-benchmarking-context-driven-memory-retrieval-in-conversation.md) | agent, benchmark, context |
| 2026-06-02 | OpenReview | [The Override Cliff: How Agent Memory Hijacks LLM Reasoning](content/papers/the-override-cliff-how-agent-memory-hijacks-llm-reasoning.md) | agent, benchmark, retrieval |
| 2026-06-02 | OpenReview | [TAME: A Trustworthy Test-Time Evolution of Agent Memory with Systematic Benchmarking](content/papers/tame-a-trustworthy-test-time-evolution-of-agent-memory-with-systematic-benchmark.md) | agent, benchmark |
| 2026-06-02 | OpenReview | [Schema-Mem: Structured and Evolving Memory for Long-term Conversational Knowledge](content/papers/schema-mem-structured-and-evolving-memory-for-long-term-conversational-knowledge.md) | agent, context, conversation |
| 2026-06-02 | OpenReview | [Same Ranking, Different Winner: How Scoring Targets Shape LLM Memory Benchmarks](content/papers/same-ranking-different-winner-how-scoring-targets-shape-llm-memory-benchmarks.md) | benchmark, conversation, retrieval |
| 2026-06-02 | OpenReview | [SHM-GATE: Structured Hierarchical Memory with Gated Admission for Multi-Agent LLM Hallucination Containment](content/papers/shm-gate-structured-hierarchical-memory-with-gated-admission-for-multi-agent-llm.md) | agent, benchmark, conversation |
| 2026-06-02 | OpenReview | [Remembering by Asking: Retrieval-Induced Memory Evolution for LLM Agents](content/papers/remembering-by-asking-retrieval-induced-memory-evolution-for-llm-agents.md) | agent, long-term, retrieval |
| 2026-06-02 | OpenReview | [Reconstructing the Right Episode: Evaluating Interleaved Conversational Memory Beyond Long Context](content/papers/reconstructing-the-right-episode-evaluating-interleaved-conversational-memory-be.md) | benchmark, context, conversation |
| 2026-06-02 | arXiv | [RGMem: Renormalization Group-inspired Memory Evolution for Language Agents](content/papers/rgmem-renormalization-group-inspired-memory-evolution-for-language-agents.md) | agent, benchmark, context |
| 2026-06-02 | arXiv | [PhotoCraft: Agentic Reasoning with Hierarchical Self-Evolving Memory for Deep Image Search](content/papers/photocraft-agentic-reasoning-with-hierarchical-self-evolving-memory-for-deep-ima.md) | agent, context, episodic |
| 2026-06-02 | OpenReview | [PersonaTree: Structured Lifecycle Memory for Person Understanding in LLM Agents](content/papers/personatree-structured-lifecycle-memory-for-person-understanding-in-llm-agents.md) | agent, benchmark, context |
| 2026-06-02 | arXiv | [Memory Retrieval for Changing Preferences](content/papers/memory-retrieval-for-changing-preferences.md) | benchmark, context, retrieval |
| 2026-06-02 | OpenReview | [Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving Agent Memory](content/papers/memory-beyond-recall-a-dual-process-cognitive-memory-system-for-self-evolving-ag.md) | agent, benchmark, long-term |
| 2026-06-02 | arXiv | [MemTrain: Self-Supervised Context Memory Training](content/papers/memtrain-self-supervised-context-memory-training.md) | agent, benchmark, compression |
| 2026-06-02 | OpenReview | [MemRefine: LLM-Guided Compression for Long-Term Agent Memory](content/papers/memrefine-llm-guided-compression-for-long-term-agent-memory.md) | agent, benchmark, compression |
| 2026-06-02 | arXiv | [MemORAI: Memory Organization and Retrieval via Adaptive Graph Intelligence for LLM Conversational Agents](content/papers/memorai-memory-organization-and-retrieval-via-adaptive-graph-intelligence-for-ll.md) | agent, benchmark, compression |
| 2026-06-02 | OpenReview | [MEMPLANNER: Governing Long-Horizon Agency via Dynamic Memory Management and Planning](content/papers/memplanner-governing-long-horizon-agency-via-dynamic-memory-management-and-plann.md) | agent, context |
| 2026-06-02 | OpenReview | [LightGMEM: Lightweight Agent Graph Memory Generation](content/papers/lightgmem-lightweight-agent-graph-memory-generation.md) | agent, context, conversation |
| 2026-06-02 | arXiv | [InfoMem: Training Long-Context Memory Agents with Answer-Conditioned Information Gain](content/papers/infomem-training-long-context-memory-agents-with-answer-conditioned-information-.md) | agent, context, retrieval |
| 2026-06-02 | OpenReview | [HMARS: A Hierarchical Multi-Agent Memory System for Long-Context Reasoning](content/papers/hmars-a-hierarchical-multi-agent-memory-system-for-long-context-reasoning.md) | agent, benchmark, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
