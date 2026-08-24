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

- Total tracked papers: **996**
- Last generated: **2026-08-24**

## Papers by Source

- ACL Anthology: **5**
- arXiv: **852**
- OpenReview: **139**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-08-24 | OpenReview | [Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length](content/papers/unable-to-forget-proactive-interference-reveals-working-memory-limits-in-llms-be.md) | context, retrieval |
| 2026-08-24 | OpenReview | [TierMem: Balancing Compressed Memory and Raw Evidence for Long-Horizon Agent Memory](content/papers/tiermem-balancing-compressed-memory-and-raw-evidence-for-long-horizon-agent-memo.md) | agent, benchmark |
| 2026-08-24 | OpenReview | [In-context superposition: human-like working memory interference in large language models](content/papers/in-context-superposition-human-like-working-memory-interference-in-large-languag.md) | compression, context, retrieval |
| 2026-08-24 | OpenReview | [Back to Basics: Let Conversational Agents Remember with Just Retrieval and Generation](content/papers/back-to-basics-let-conversational-agents-remember-with-just-retrieval-and-genera.md) | agent, benchmark, context |
| 2026-08-23 | OpenReview | [Human-inspired Perspectives: A Survey on AI Long-term Memory](content/papers/human-inspired-perspectives-a-survey-on-ai-long-term-memory.md) | long-term |
| 2026-08-22 | OpenReview | [Knowledge Graph Enhanced Memory-Augmented Retrieval for Long Context Modeling](content/papers/knowledge-graph-enhanced-memory-augmented-retrieval-for-long-context-modeling.md) | context, retrieval |
| 2026-08-21 | arXiv | [Weighted Memory Tree: Remembering What Matters for Long-Horizon LLM Agents](content/papers/weighted-memory-tree-remembering-what-matters-for-long-horizon-llm-agents.md) | agent, context |
| 2026-08-21 | arXiv | [Utility Under Attack: Agent Memory Poisoning and the Limits of Content Screening and Provenance Ranking](content/papers/utility-under-attack-agent-memory-poisoning-and-the-limits-of-content-screening-.md) | agent, retrieval |
| 2026-08-21 | arXiv | [Towards Faithful Simulation of Human Shopping Behavior](content/papers/towards-faithful-simulation-of-human-shopping-behavior.md) | agent, benchmark, context |
| 2026-08-21 | OpenReview | [Reason Before Remembering: An Entity-Centric Framework for Trustworthy Conversational Memory](content/papers/reason-before-remembering-an-entity-centric-framework-for-trustworthy-conversati.md) | context, conversation, retrieval |
| 2026-08-21 | arXiv | [Memory Augmentation Unlocks Efficient Chain-of-Thought Reasoning](content/papers/memory-augmentation-unlocks-efficient-chain-of-thought-reasoning.md) | compression, context |
| 2026-08-21 | arXiv | [MemWM: Memory-Augmented Text-Based World Model](content/papers/memwm-memory-augmented-text-based-world-model.md) | agent, benchmark |
| 2026-08-21 | arXiv | [ForeDreamer: A Self-Evolving Dual-Agent Memory Architecture for Future Event Prediction](content/papers/foredreamer-a-self-evolving-dual-agent-memory-architecture-for-future-event-pred.md) | agent, retrieval |
| 2026-08-21 | arXiv | [DreamBench-SWE: A Multi-Session Memory-Hygiene Benchmark for Software Agents](content/papers/dreambench-swe-a-multi-session-memory-hygiene-benchmark-for-software-agents.md) | agent, benchmark |
| 2026-08-21 | OpenReview | [D-ACR: Dialogue-Aware Context Retrieval for Long-Term Conversational Memory](content/papers/d-acr-dialogue-aware-context-retrieval-for-long-term-conversational-memory.md) | benchmark, context, conversation |
| 2026-08-20 | arXiv | [SABET-QA: Temporal Knowledge Graph Question Answering](content/papers/sabet-qa-temporal-knowledge-graph-question-answering.md) | context |
| 2026-08-20 | arXiv | [Remember, Verify, or Ask? Cross-Family Evaluation of Memory Commitment in LLM Agents](content/papers/remember-verify-or-ask-cross-family-evaluation-of-memory-commitment-in-llm-agent.md) | agent, context |
| 2026-08-20 | arXiv | [MemTrapBench: Benchmarking Cognitive Traps in LLM Memory Use](content/papers/memtrapbench-benchmarking-cognitive-traps-in-llm-memory-use.md) | benchmark, long-term |
| 2026-08-20 | arXiv | [Compress and Forget: bitsandbytes Quantization Amplifies Proactive Interference in LLMs](content/papers/compress-and-forget-bitsandbytes-quantization-amplifies-proactive-interference-i.md) | benchmark, context, retrieval |
| 2026-08-20 | arXiv | [Can Agent Memory Systems Track Evolving State?](content/papers/can-agent-memory-systems-track-evolving-state.md) | agent, benchmark, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
