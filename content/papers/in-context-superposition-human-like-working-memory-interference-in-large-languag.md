# In-context superposition: human-like working memory interference in large language models

- Source: OpenReview
- Venue: COLM 2026
- Paper ID: openreview:g1hMOOAX2n
- Published: 2026-07-08
- Updated: 2026-08-24
- Authors: Hua-Dong Xiong, Li Ji-An, Jiaqi Huang, Robert Wilson, Kwonjoon Lee, Xue-Xin Wei
- Tags: compression, context, retrieval
- Categories: colmweb.org/COLM/2026/Conference/-/Submission
- URL: https://openreview.net/forum?id=g1hMOOAX2n

## One-Sentence Summary
Intelligent systems must maintain and manipulate task-relevant information online to adapt to dynamic environments.

## Introduction
这篇论文被纳入仓库，是因为它和 `compression, context, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `COLM 2026` 这个 venue 相关。

从摘要来看，作者主要关注的是：Intelligent systems must maintain and manipulate task-relevant information online to adapt to dynamic environments.

进一步看，论文的核心做法或实验重点可以概括为：This capacity, known as working memory, is fundamental to human reasoning.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：COLM 2026
- 高亮主题命中：compression, context, retrieval
- 检索关键词命中：working memory
- 来源分类信息：colmweb.org/COLM/2026/Conference/-/Submission

## Abstract Snapshot
Intelligent systems must maintain and manipulate task-relevant information online to adapt to dynamic environments. This capacity, known as working memory, is fundamental to human reasoning. Yet, human working memory is strikingly limited, maintaining only three to four items in a brain with billions of neurons. Surprisingly, large language models (LLMs), despite different substrates and direct access to prior context through attention, exhibit similar working memory limitations. Why should such different systems face analogous constraints? We propose that working memory limitations reflect a general trade-off of shared representations: representational compression and reuse support efficient learning and generalization, but also cause simultaneously active representations to interfere. We show a two-layer transformer trained on a working memory task can solve it perfectly, but diverse trained LLMs exhibit human-like limitations: performance declines with memory load, while retrieval is biased by recency and stimulus statistics. Mirroring humans, working memory performance in LLMs is also associated with broader model capability. Mechanistically, we show that LLMs encode multiple memories in entangled representations --- a condition we call \emph{in-context superposition} --- and progressively suppress competing content while aligning the target with the readout. Moreover, a causal intervention that suppresses interfering information improves performance. Together, these findings suggest that working memory capacity reflects the ability to select task-relevant information under interference, a computational challenge shared by biological and artificial systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
