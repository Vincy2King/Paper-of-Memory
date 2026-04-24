# REMem: Reasoning with Episodic Memory in Language Agent

- Source: OpenReview
- Venue: ICLR 2026 Poster
- Paper ID: openreview:fugnQxbvMm
- Published: 2026-01-26
- Updated: 2026-04-11
- Authors: Yiheng Shu, Saisri Padmaja Jonnalagedda, Xiang Gao, Bernal Jiménez Gutiérrez, Weijian Qi, Kamalika Das, Huan Sun, Yu Su
- Tags: agent, benchmark, context, episodic, retrieval
- Categories: ICLR.cc/2026/Conference/-/Submission
- URL: https://openreview.net/forum?id=fugnQxbvMm

## One-Sentence Summary
Humans excel at remembering concrete experiences along spatiotemporal contexts and performing reasoning across those events, i.e., the capacity for episodic memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ICLR 2026 Poster` 这个 venue 相关。

从摘要来看，作者主要关注的是：Humans excel at remembering concrete experiences along spatiotemporal contexts and performing reasoning across those events, i.e., the capacity for episodic memory.

进一步看，论文的核心做法或实验重点可以概括为：In contrast, memory in language agents remains mainly semantic, and current agents are not yet capable of effectively recollecting and reasoning over interaction histories.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ICLR 2026 Poster
- 高亮主题命中：agent, benchmark, context, episodic, retrieval
- 检索关键词命中：episodic memory, memory benchmark, memory benchmarks
- 来源分类信息：ICLR.cc/2026/Conference/-/Submission

## Abstract Snapshot
Humans excel at remembering concrete experiences along spatiotemporal contexts and performing reasoning across those events, i.e., the capacity for episodic memory. In contrast, memory in language agents remains mainly semantic, and current agents are not yet capable of effectively recollecting and reasoning over interaction histories. We identify and formalize the core challenges of episodic recollection and reasoning from this gap, and observe that existing work often overlooks episodicity, lacks explicit event modeling, or overemphasizes simple retrieval rather than complex reasoning. We present REMem, a two-phase framework for constructing and reasoning with episodic memory: 1) Offline indexing, where REMem converts experiences into a hybrid memory graph that flexibly links time-aware gists and facts. 2) Online inference, where REMem employs an agentic retriever with carefully curated tools for iterative retrieval over the memory graph. Comprehensive evaluation across four episodic memory benchmarks shows that REMem substantially outperforms state-of-the-art memory systems such as Mem0 and HippoRAG 2, showing 3.4% and 13.4% absolute improvements on episodic recollection and reasoning tasks, respectively. Moreover, REMem also demonstrates more robust refusal behavior for unanswerable questions.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
