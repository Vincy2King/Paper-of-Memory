# Decoupled Knowledge Retrieval and Compact Memory Enable Reliable Lifelong Model Editing

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.25861v1
- Published: 2026-11-19
- Updated: 2026-11-19
- Authors: Yue Che, Jingze Wang, Chen Guoyi, Yujie Wu, Xuming Ran, Mingkun Xu
- Tags: benchmark, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.25861v1

## One-Sentence Summary
Lifelong model editing requires continuously incorporating new facts into deployed large language models (LLMs) without expensive retraining or compromising existing capabilities.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Lifelong model editing requires continuously incorporating new facts into deployed large language models (LLMs) without expensive retraining or compromising existing capabilities.

进一步看，论文的核心做法或实验重点可以概括为：Memory-based editors offer an appealing solution by keeping the base parameters untouched, yet their practical use is hindered by linearly growing storage requirements and deteriorating retrieval performance as edits...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, long-term, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.AI

## Abstract Snapshot
Lifelong model editing requires continuously incorporating new facts into deployed large language models (LLMs) without expensive retraining or compromising existing capabilities. Memory-based editors offer an appealing solution by keeping the base parameters untouched, yet their practical use is hindered by linearly growing storage requirements and deteriorating retrieval performance as edits accumulate. To tackle these problems, we introduce BiSpace, a lifelong model editing framework that decouples memory retrieval from knowledge injection across two distinct representation spaces. BiSpace routes queries and identifies relevant edits in an external semantic space, while injecting the corresponding knowledge into the internal representation space of the LLM through sparse and storage-efficient updates. Extensive experiments show that BiSpace shrinks each entry's storage to only about 10.2% of the original and shows strong resilience to long edit sequences of up to 16K edits. On a more challenging benchmark, BiSpace further improves Overall Performance by more than 23% over existing methods. These results advance memory-based editing toward reliable long-term model maintenance at scale.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
