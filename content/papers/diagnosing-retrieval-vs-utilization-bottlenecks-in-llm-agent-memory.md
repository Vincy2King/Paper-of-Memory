# Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory

- Source: OpenReview
- Venue: ICLR 2026 Workshop MemAgents Poster
- Paper ID: openreview:cxYbqAtBIz
- Published: 2026-03-03
- Updated: 2026-04-25
- Authors: Boqin Yuan, Yue Su, Kun Yao
- Tags: agent, context, retrieval
- Categories: ICLR.cc/2026/Workshop/MemAgent/-/Submission
- URL: https://openreview.net/forum?id=cxYbqAtBIz

## One-Sentence Summary
Memory-augmented LLM agents store and retrieve information from prior interactions, yet the relative importance of how memories are written versus how they are retrieved remains...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ICLR 2026 Workshop MemAgents Poster` 这个 venue 相关。

从摘要来看，作者主要关注的是：Memory-augmented LLM agents store and retrieve information from prior interactions, yet the relative importance of how memories are written versus how they are retrieved remains unclear.

进一步看，论文的核心做法或实验重点可以概括为：We introduce a diagnostic framework that analyzes how performance differences manifest across write strategies, retrieval methods, and memory utilization behavior, and apply it to a $3 \times 3$ study crossing three...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ICLR 2026 Workshop MemAgents Poster
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：agent memory, memory-augmented
- 来源分类信息：ICLR.cc/2026/Workshop/MemAgent/-/Submission

## Abstract Snapshot
Memory-augmented LLM agents store and retrieve information from prior interactions, yet the relative importance of how memories are written versus how they are retrieved remains unclear. We introduce a diagnostic framework that analyzes how performance differences manifest across write strategies, retrieval methods, and memory utilization behavior, and apply it to a $3 \times 3$ study crossing three write strategies (raw chunks, Mem0-style fact extraction, MemGPT-style summarization) with three retrieval methods (cosine, BM25, hybrid reranking). On LoCoMo, retrieval method is the dominant factor: average accuracy spans $20$ points across retrieval methods ($57.1\%$ to $77.2\%$) but only $3$-$8$ points across write strategies. Raw chunked storage, which requires zero LLM calls, matches or outperforms expensive lossy alternatives, suggesting that current memory pipelines may discard useful context that downstream retrieval mechanisms fail to compensate for. Failure analysis shows that performance breakdowns most often manifest at the retrieval stage rather than at utilization. We argue that, under current retrieval practices, improving retrieval quality yields larger gains than increasing write-time sophistication.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
