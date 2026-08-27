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

- Total tracked papers: **1034**
- Last generated: **2026-08-27**

## Papers by Source

- ACL Anthology: **5**
- arXiv: **889**
- OpenReview: **140**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-08-26 | arXiv | [When Stale Constraints Go Unchecked: Budgeted Verification Failures in Inherited Agent Memory](content/papers/when-stale-constraints-go-unchecked-budgeted-verification-failures-in-inherited-.md) | agent |
| 2026-08-26 | arXiv | [VISA: Agentic Self-Evolving Data Synthesis for Multimodal Instruction Following](content/papers/visa-agentic-self-evolving-data-synthesis-for-multimodal-instruction-following.md) | agent, benchmark |
| 2026-08-26 | arXiv | [S-EMBER: A Large-Scale Benchmark for Streaming Egocentric Memory Retrieval](content/papers/s-ember-a-large-scale-benchmark-for-streaming-egocentric-memory-retrieval.md) | agent, benchmark, episodic |
| 2026-08-26 | arXiv | [RoboMME-Interference: Benchmarking Robot Memory Under Interference](content/papers/robomme-interference-benchmarking-robot-memory-under-interference.md) | benchmark, context, retrieval |
| 2026-08-26 | arXiv | [Reconstructing the Right Episode: Evaluating Interleaved Conversational Memory Beyond Long Context](content/papers/reconstructing-the-right-episode-evaluating-interleaved-conversational-memory-be.md) | benchmark, context, conversation |
| 2026-08-26 | arXiv | [PolyMemDB: A Polyglot Database System for AI Memory Management](content/papers/polymemdb-a-polyglot-database-system-for-ai-memory-management.md) | agent, long-term |
| 2026-08-26 | arXiv | [Memory Augmentation Unlocks Efficient Chain-of-Thought Reasoning](content/papers/memory-augmentation-unlocks-efficient-chain-of-thought-reasoning.md) | compression, context |
| 2026-08-26 | arXiv | [Learning What to Share and What to Personalize: Hierarchical Strategy Co-Evolution for Agent Memory](content/papers/learning-what-to-share-and-what-to-personalize-hierarchical-strategy-co-evolutio.md) | agent, conversation |
| 2026-08-26 | arXiv | [Governed Persistent Memory: Source-Bound State Semantics and Fail-Closed Release for Long-Horizon Agents](content/papers/governed-persistent-memory-source-bound-state-semantics-and-fail-closed-release-.md) | agent, long-term, retrieval |
| 2026-08-26 | arXiv | [AWM: Answerable Working Memory for Long-Document VQA Agents](content/papers/awm-answerable-working-memory-for-long-document-vqa-agents.md) | agent, context |
| 2026-08-25 | arXiv | [VideoHarness-RSI: Recursive Harness Self-Improvement for Long-Video Understanding with Frozen Vision-Language Models](content/papers/videoharness-rsi-recursive-harness-self-improvement-for-long-video-understanding.md) | agent, benchmark, compression |
| 2026-08-25 | arXiv | [The Von-Neumann State-Space Transformer for neural decoding](content/papers/the-von-neumann-state-space-transformer-for-neural-decoding.md) | benchmark, context |
| 2026-08-25 | arXiv | [Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses](content/papers/recursive-experiential-working-memory-evolution-for-long-horizon-agent-harnesses.md) | agent, benchmark |
| 2026-08-25 | arXiv | [PonderPounce: A Pretrained MLLM as an Episode Context Engine for Robot Control](content/papers/ponderpounce-a-pretrained-mllm-as-an-episode-context-engine-for-robot-control.md) | context |
| 2026-08-25 | OpenReview | [Memory-Bench at Short Context: Only Persistent Memory Beats Softmax Attention at 2048 Tokens](content/papers/memory-bench-at-short-context-only-persistent-memory-beats-softmax-attention-at-.md) | context |
| 2026-08-25 | arXiv | [EviGraph: Towards Verifiable Evidence Construction for Information-Seeking Agents](content/papers/evigraph-towards-verifiable-evidence-construction-for-information-seeking-agents.md) | agent |
| 2026-08-25 | arXiv | [Don't Just Listen, Try Planning: Graph-based Retrieval-Generation Agent for Long-form Audio Meeting Understanding](content/papers/don-t-just-listen-try-planning-graph-based-retrieval-generation-agent-for-long-f.md) | agent, context, long-term |
| 2026-08-25 | arXiv | [Counter with Evidence! A Multi-Agent Memory Efficient Reasoning Framework for Hate Category Informed Counterspeech Generation](content/papers/counter-with-evidence-a-multi-agent-memory-efficient-reasoning-framework-for-hat.md) | agent, context |
| 2026-08-24 | arXiv | [Wontopos Tablet 2: Measuring Multilingual and Multimodal Memory Retrieval Without Lexical Matching](content/papers/wontopos-tablet-2-measuring-multilingual-and-multimodal-memory-retrieval-without.md) | benchmark, long-term, retrieval |
| 2026-08-24 | OpenReview | [Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length](content/papers/unable-to-forget-proactive-interference-reveals-working-memory-limits-in-llms-be.md) | context, retrieval |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
