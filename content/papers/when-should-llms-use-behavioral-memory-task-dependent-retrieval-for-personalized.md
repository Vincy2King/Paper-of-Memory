# When Should LLMs Use Behavioral Memory? Task-Dependent Retrieval for Personalized Long-Term Memory

- Source: OpenReview
- Venue: IEEE IROS 2026 Workshop BEMHAT
- Paper ID: openreview:hC72QPtiz3
- Published: 2026-08-08
- Updated: 2026-08-28
- Authors: Keonvin Park, John J. Sohn
- Tags: long-term, retrieval
- Categories: OpenReview.net/Archive/-/Direct_Upload
- URL: https://openreview.net/forum?id=hC72QPtiz3

## One-Sentence Summary
Long-term memory enables large language models (LLMs) to personalize responses using prior user interactions, yet different queries may require different forms of memory evidence.

## Introduction
这篇论文被纳入仓库，是因为它和 `long-term, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `IEEE IROS 2026 Workshop BEMHAT` 这个 venue 相关。

从摘要来看，作者主要关注的是：Long-term memory enables large language models (LLMs) to personalize responses using prior user interactions, yet different queries may require different forms of memory evidence.

进一步看，论文的核心做法或实验重点可以概括为：This study investigates whether behavioral signals, including recency, preference, and user updates, improve personalized memory retrieval and whether these signals can be selected adaptively according to the query.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：IEEE IROS 2026 Workshop BEMHAT
- 高亮主题命中：long-term, retrieval
- 检索关键词命中：long-term memory, memory retrieval
- 来源分类信息：OpenReview.net/Archive/-/Direct_Upload

## Abstract Snapshot
Long-term memory enables large language models (LLMs) to personalize responses using prior user interactions, yet different queries may require different forms of memory evidence. This study investigates whether behavioral signals, including recency, preference, and user updates, improve personalized memory retrieval and whether these signals can be selected adaptively according to the query. We evaluate six retrieval strategies on 589 PersonaMem queries using a common LLM backbone. Preference-Aware retrieval achieves the highest overall accuracy of 47.88%, followed by Query-Adaptive retrieval at 47.54% and Static Semantic retrieval at 47.20%. Task-level results show that the effectiveness of behavioral signals varies substantially across query types. Query-adaptive routing does not significantly outperform the strongest fixed strategies, while oracle selection reaches 50.42%, leaving only 2.55 percentage points of headroom. These results show that behavioral memory is task-dependent and highlight the need to determine when specific behavioral evidence should be used rather than uniformly combining multiple memory signals.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
