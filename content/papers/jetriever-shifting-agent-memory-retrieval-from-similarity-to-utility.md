# Jetriever: Shifting Agent Memory Retrieval from Similarity to Utility

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.21478v1
- Published: 2026-11-16
- Updated: 2026-11-16
- Authors: Ruizhe Li, Licheng Zhang, Mingxuan Du, Zhendong Mao
- Tags: agent, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2611.21478v1

## One-Sentence Summary
A useful memory need not resemble the question it helps answer.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：A useful memory need not resemble the question it helps answer.

进一步看，论文的核心做法或实验重点可以概括为：Jetriever ranks each stored memory by Jev's decision score for its usefulness to the current question, replacing similarity search with full-pool utility scoring.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory, memory retrieval
- 来源分类信息：cs.CL

## Abstract Snapshot
A useful memory need not resemble the question it helps answer. Jetriever ranks each stored memory by Jev's decision score for its usefulness to the current question, replacing similarity search with full-pool utility scoring. On InMind's 125 indirect-query tasks, it places the gold exchange first in 84.8% of cases; matched BM25 and MiniLM controls reach 1.6% and 0.0% when indexing user turns. A 20-question comparison separates finding evidence from ranking it: Jev and Qwen3.5 9B each find 90% of gold exchanges by rank 50, while Laya finds 30%; at rank one, Jev reaches 85% and Qwen3.5 9B 40%. On a dimension-proportional random sample of 60 MemoryAgentBench questions, Jetriever's four-dimension score is 55.4%, against 44.3% for ReFind on the same questions. Jev retrieval costs USD 0.00834 per InMind question and USD 0.03103 per MAB question on average. These results show the value of world knowledge, scores that rank decisive memories first, and affordable full-pool scoring.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
