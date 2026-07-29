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

- Total tracked papers: **778**
- Last generated: **2026-07-29**

## Papers by Source

- ACL Anthology: **5**
- arXiv: **655**
- OpenReview: **118**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-07-27 | arXiv | [Reality Monitoring in Large Language Models: Self-Knowledge That Transforms with Conversation Memory](content/papers/reality-monitoring-in-large-language-models-self-knowledge-that-transforms-with-.md) | benchmark, conversation, episodic |
| 2026-07-27 | arXiv | [Not Forgotten: Implementation and Evaluation of a Personalized Episodic Memory for the Humanoid Robot Head Kim](content/papers/not-forgotten-implementation-and-evaluation-of-a-personalized-episodic-memory-fo.md) | context, conversation, episodic |
| 2026-07-27 | arXiv | [MemTX: Transactional Belief Commit for Stateful Agent Memory](content/papers/memtx-transactional-belief-commit-for-stateful-agent-memory.md) | agent |
| 2026-07-27 | arXiv | [MemChain: Learning Interpretable Memory Traces for Memory-Augmented LLM Agents](content/papers/memchain-learning-interpretable-memory-traces-for-memory-augmented-llm-agents.md) | agent, context, long-term |
| 2026-07-27 | arXiv | [Leveling the Playing Field: Temporal Video Segmentation for Individuals with ADHD in Computing Education](content/papers/leveling-the-playing-field-temporal-video-segmentation-for-individuals-with-adhd.md) | working memory |
| 2026-07-27 | arXiv | [Keep It InMind: Benchmarking the Implicit-Association Blind Spot in Agent Memory](content/papers/keep-it-inmind-benchmarking-the-implicit-association-blind-spot-in-agent-memory.md) | agent, benchmark, context |
| 2026-07-27 | OpenReview | [IFCMemoryBench: Evaluating Long-Term Memory of LLM-Based Agents in BIM Information Retrieval](content/papers/ifcmemorybench-evaluating-long-term-memory-of-llm-based-agents-in-bim-informatio.md) | agent, benchmark, context |
| 2026-07-27 | arXiv | [Eviction as Estimation: A Fixed-Lag Smoothing View of Test-Time Memory, and When Measuring Beats Accumulating](content/papers/eviction-as-estimation-a-fixed-lag-smoothing-view-of-test-time-memory-and-when-m.md) | benchmark |
| 2026-07-27 | arXiv | [Dementia classification from spontaneous speech using wrapper-based feature selection](content/papers/dementia-classification-from-spontaneous-speech-using-wrapper-based-feature-sele.md) | memory |
| 2026-07-27 | arXiv | [Agents Don't Just Agree, They Remember: Benchmarking Persistent Sycophancy in Stateful Personal Agents](content/papers/agents-don-t-just-agree-they-remember-benchmarking-persistent-sycophancy-in-stat.md) | agent, benchmark, conversation |
| 2026-07-26 | arXiv | [Compute Globally, Materialize Locally: The Memory Contract of Sparse Event-KV](content/papers/compute-globally-materialize-locally-the-memory-contract-of-sparse-event-kv.md) | agent, episodic, long-term |
| 2026-07-26 | arXiv | [A Frozen 12B Beats Frontier Models on Verified Work: 100% Accuracy, 0 Tokens, Bit-Exact, Forever](content/papers/a-frozen-12b-beats-frontier-models-on-verified-work-100-accuracy-0-tokens-bit-ex.md) | benchmark, context, retrieval |
| 2026-07-25 | OpenReview | [LMEB: Long-horizon Memory Embedding Benchmark](content/papers/lmeb-long-horizon-memory-embedding-benchmark.md) | benchmark, context, episodic |
| 2026-07-25 | arXiv | [Interpreting Quantum Learning Models via Stochastic Processes](content/papers/interpreting-quantum-learning-models-via-stochastic-processes.md) | episodic |
| 2026-07-25 | arXiv | [Co-Evolving Graph and Text Memory for Training-Free Multi-Hop Question Answering](content/papers/co-evolving-graph-and-text-memory-for-training-free-multi-hop-question-answering.md) | agent, benchmark, context |
| 2026-07-25 | OpenReview | [CAST: Character-and-Scene Episodic Memory for Agents](content/papers/cast-character-and-scene-episodic-memory-for-agents.md) | agent, conversation, episodic |
| 2026-07-24 | arXiv | [Neuro-Symbolic Meta-Policies for Temporal Knowledge-Graph Memory under Partial Observability](content/papers/neuro-symbolic-meta-policies-for-temporal-knowledge-graph-memory-under-partial-o.md) | long-term |
| 2026-07-24 | arXiv | [MemNMF: Memory-Augmented NMF on LPC Spectra for Anomalous Sound Detection](content/papers/memnmf-memory-augmented-nmf-on-lpc-spectra-for-anomalous-sound-detection.md) | memory-augmented |
| 2026-07-24 | arXiv | [Key-Value Means: Transformers with Expandable Block-Recurrent Compressed Memory](content/papers/key-value-means-transformers-with-expandable-block-recurrent-compressed-memory.md) | context |
| 2026-07-24 | arXiv | [Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings](content/papers/ground-truth-first-a-longitudinal-evaluation-instrument-for-agent-memory-and-the.md) | agent, benchmark, conversation |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
