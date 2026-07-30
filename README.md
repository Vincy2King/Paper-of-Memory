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

- Total tracked papers: **787**
- Last generated: **2026-07-30**

## Papers by Source

- ACL Anthology: **5**
- arXiv: **664**
- OpenReview: **118**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-07-28 | arXiv | [RoboMME-Interference: Benchmarking Robot Memory Under Interference](content/papers/robomme-interference-benchmarking-robot-memory-under-interference.md) | benchmark, context, retrieval |
| 2026-07-28 | arXiv | [Neuro-Symbolic Meta-Policies for Temporal Knowledge-Graph Memory under Partial Observability](content/papers/neuro-symbolic-meta-policies-for-temporal-knowledge-graph-memory-under-partial-o.md) | long-term |
| 2026-07-28 | arXiv | [MemTX: Transactional Belief Commit for Stateful Agent Memory](content/papers/memtx-transactional-belief-commit-for-stateful-agent-memory.md) | agent |
| 2026-07-28 | arXiv | [MemLens: A Value-Aware Memory Management System with Interactive Analytics for LLM-based Agents](content/papers/memlens-a-value-aware-memory-management-system-with-interactive-analytics-for-ll.md) | agent, long-term, retrieval |
| 2026-07-28 | arXiv | [LazyMem: Retrieve Broadly, Construct Selectively for Efficient Long-Term Agent Memory](content/papers/lazymem-retrieve-broadly-construct-selectively-for-efficient-long-term-agent-mem.md) | agent, compression, context |
| 2026-07-28 | arXiv | [Improving Human-Robot Teamwork in Urban Search and Rescue Through Episodic Memory of Prior Collaboration](content/papers/improving-human-robot-teamwork-in-urban-search-and-rescue-through-episodic-memor.md) | episodic |
| 2026-07-28 | arXiv | [A Control System, a Dataset, and a Recipe for Making Frozen LLM Agents Learn a Domain](content/papers/a-control-system-a-dataset-and-a-recipe-for-making-frozen-llm-agents-learn-a-dom.md) | agent, context, retrieval |
| 2026-07-27 | arXiv | [Reality Monitoring in Large Language Models: Self-Knowledge That Transforms with Conversation Memory](content/papers/reality-monitoring-in-large-language-models-self-knowledge-that-transforms-with-.md) | benchmark, conversation, episodic |
| 2026-07-27 | arXiv | [Not Forgotten: Implementation and Evaluation of a Personalized Episodic Memory for the Humanoid Robot Head Kim](content/papers/not-forgotten-implementation-and-evaluation-of-a-personalized-episodic-memory-fo.md) | context, conversation, episodic |
| 2026-07-27 | arXiv | [MusiChat: Vibe Composing for Music Creation](content/papers/musichat-vibe-composing-for-music-creation.md) | conversation |
| 2026-07-27 | arXiv | [MemTX: Transactional Belief Commit for Stateful Agent Memory](content/papers/memtx-transactional-belief-commit-for-stateful-agent-memory.md) | agent |
| 2026-07-27 | arXiv | [MemChain: Learning Interpretable Memory Traces for Memory-Augmented LLM Agents](content/papers/memchain-learning-interpretable-memory-traces-for-memory-augmented-llm-agents.md) | agent, context, long-term |
| 2026-07-27 | arXiv | [Leveling the Playing Field: Temporal Video Segmentation for Individuals with ADHD in Computing Education](content/papers/leveling-the-playing-field-temporal-video-segmentation-for-individuals-with-adhd.md) | working memory |
| 2026-07-27 | arXiv | [Keep It InMind: Benchmarking the Implicit-Association Blind Spot in Agent Memory](content/papers/keep-it-inmind-benchmarking-the-implicit-association-blind-spot-in-agent-memory.md) | agent, benchmark, context |
| 2026-07-27 | OpenReview | [IFCMemoryBench: Evaluating Long-Term Memory of LLM-Based Agents in BIM Information Retrieval](content/papers/ifcmemorybench-evaluating-long-term-memory-of-llm-based-agents-in-bim-informatio.md) | agent, benchmark, context |
| 2026-07-27 | arXiv | [Eviction as Estimation: A Fixed-Lag Smoothing View of Test-Time Memory, and When Measuring Beats Accumulating](content/papers/eviction-as-estimation-a-fixed-lag-smoothing-view-of-test-time-memory-and-when-m.md) | benchmark |
| 2026-07-27 | arXiv | [Dementia classification from spontaneous speech using wrapper-based feature selection](content/papers/dementia-classification-from-spontaneous-speech-using-wrapper-based-feature-sele.md) | memory |
| 2026-07-27 | arXiv | [Beyond the Post Hoc User Study: Modeling Visual Decision-Making with Active Inference](content/papers/beyond-the-post-hoc-user-study-modeling-visual-decision-making-with-active-infer.md) | agent |
| 2026-07-27 | arXiv | [Agents Don't Just Agree, They Remember: Benchmarking Persistent Sycophancy in Stateful Personal Agents](content/papers/agents-don-t-just-agree-they-remember-benchmarking-persistent-sycophancy-in-stat.md) | agent, benchmark, conversation |
| 2026-07-26 | arXiv | [Compute Globally, Materialize Locally: The Memory Contract of Sparse Event-KV](content/papers/compute-globally-materialize-locally-the-memory-contract-of-sparse-event-kv.md) | agent, episodic, long-term |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
