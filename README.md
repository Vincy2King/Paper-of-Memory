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

- Total tracked papers: **1023**
- Last generated: **2026-08-26**

## Papers by Source

- ACL Anthology: **5**
- arXiv: **878**
- OpenReview: **140**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-08-25 | arXiv | [VideoHarness-RSI: Recursive Harness Self-Improvement for Long-Video Understanding with Frozen Vision-Language Models](content/papers/videoharness-rsi-recursive-harness-self-improvement-for-long-video-understanding.md) | agent, benchmark, compression |
| 2026-08-25 | arXiv | [Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses](content/papers/recursive-experiential-working-memory-evolution-for-long-horizon-agent-harnesses.md) | agent, benchmark |
| 2026-08-25 | arXiv | [PonderPounce: A Pretrained MLLM as an Episode Context Engine for Robot Control](content/papers/ponderpounce-a-pretrained-mllm-as-an-episode-context-engine-for-robot-control.md) | context |
| 2026-08-25 | OpenReview | [Memory-Bench at Short Context: Only Persistent Memory Beats Softmax Attention at 2048 Tokens](content/papers/memory-bench-at-short-context-only-persistent-memory-beats-softmax-attention-at-.md) | context |
| 2026-08-25 | arXiv | [EviGraph: Towards Verifiable Evidence Construction for Information-Seeking Agents](content/papers/evigraph-towards-verifiable-evidence-construction-for-information-seeking-agents.md) | agent |
| 2026-08-25 | arXiv | [Don't Just Listen, Try Planning: Graph-based Retrieval-Generation Agent for Long-form Audio Meeting Understanding](content/papers/don-t-just-listen-try-planning-graph-based-retrieval-generation-agent-for-long-f.md) | agent, context, long-term |
| 2026-08-25 | arXiv | [Counter with Evidence! A Multi-Agent Memory Efficient Reasoning Framework for Hate Category Informed Counterspeech Generation](content/papers/counter-with-evidence-a-multi-agent-memory-efficient-reasoning-framework-for-hat.md) | agent, context |
| 2026-08-24 | arXiv | [Wontopos Tablet 2: Measuring Multilingual and Multimodal Memory Retrieval Without Lexical Matching](content/papers/wontopos-tablet-2-measuring-multilingual-and-multimodal-memory-retrieval-without.md) | benchmark, long-term, retrieval |
| 2026-08-24 | OpenReview | [Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length](content/papers/unable-to-forget-proactive-interference-reveals-working-memory-limits-in-llms-be.md) | context, retrieval |
| 2026-08-24 | OpenReview | [TierMem: Balancing Compressed Memory and Raw Evidence for Long-Horizon Agent Memory](content/papers/tiermem-balancing-compressed-memory-and-raw-evidence-for-long-horizon-agent-memo.md) | agent, benchmark |
| 2026-08-24 | arXiv | [The Retriever Should Remember: Experience-Amortized Reranking for Long-Term Agent Memory](content/papers/the-retriever-should-remember-experience-amortized-reranking-for-long-term-agent.md) | agent, conversation, long-term |
| 2026-08-24 | arXiv | [The Compaction Cliff in Long-Running AI Agent Memory](content/papers/the-compaction-cliff-in-long-running-ai-agent-memory.md) | agent, benchmark, context |
| 2026-08-24 | arXiv | [SEAM: Shot Entity-Attribute Memory for Consistent Short-Drama Generation at Scale](content/papers/seam-shot-entity-attribute-memory-for-consistent-short-drama-generation-at-scale.md) | agent, benchmark, context |
| 2026-08-24 | OpenReview | [On Memory Construction and Retrieval for Personalized Conversational Agents](content/papers/on-memory-construction-and-retrieval-for-personalized-conversational-agents.md) | agent, benchmark, compression |
| 2026-08-24 | arXiv | [InjecMEM: Memory Injection Attack on LLM Agent Memory Systems](content/papers/injecmem-memory-injection-attack-on-llm-agent-memory-systems.md) | agent, context, retrieval |
| 2026-08-24 | OpenReview | [In-context superposition: human-like working memory interference in large language models](content/papers/in-context-superposition-human-like-working-memory-interference-in-large-languag.md) | compression, context, retrieval |
| 2026-08-24 | arXiv | [ForeDreamer: A Self-Evolving Dual-Agent Memory Architecture for Future Event Prediction](content/papers/foredreamer-a-self-evolving-dual-agent-memory-architecture-for-future-event-pred.md) | agent, retrieval |
| 2026-08-24 | arXiv | [EarthVerse: Benchmarking Scientific Agents Across Dynamic Earth Systems and Natural Hazards](content/papers/earthverse-benchmarking-scientific-agents-across-dynamic-earth-systems-and-natur.md) | agent, benchmark |
| 2026-08-24 | arXiv | [Does Episodic Memory Help Close the Lexical Frequency Gap in Sensitivity to Syntactic Contrasts? A Test Using Retrieval-Augmented Language Models](content/papers/does-episodic-memory-help-close-the-lexical-frequency-gap-in-sensitivity-to-synt.md) | episodic, retrieval |
| 2026-08-24 | arXiv | [Counter with Evidence! A Multi-Agent Memory Efficient Reasoning Framework for Hate Category Informed Counterspeech Generation](content/papers/counter-with-evidence-a-multi-agent-memory-efficient-reasoning-framework-for-hat.md) | agent, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
