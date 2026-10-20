# When Agent Memory Needs to Compute: Evidence Access and Executable Aggregation

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.19474v2
- Published: 2026-10-14
- Updated: 2026-10-17
- Authors: Zerui Yang, Quan Xue, Chaorui Zhang, Xueyan Niu, Xuanyu Zheng, Xiyuan Wang, Haolin Ruan, Guangcheng Song, Weixi Zhang, Wei Han, Bo Bai
- Tags: agent, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.19474v2

## One-Sentence Summary
Questions about an agent's history often require aggregating events, which retrieval alone does not resolve.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Questions about an agent's history often require aggregating events, which retrieval alone does not resolve.

进一步看，论文的核心做法或实验重点可以概括为：We combine source-preserving evidence access with executable aggregation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Questions about an agent's history often require aggregating events, which retrieval alone does not resolve. We combine source-preserving evidence access with executable aggregation. Trajectory Memory (TM) retains the original trajectory and constructs a source-addressable reading view at question time. TallyMem augments it with a reusable event ledger, model-generated event specifications and deterministic execution. With a commit-specific adaptation on 776 questions from 99 held-out MINTEval repositories, TallyMem raises Qwen3-32B exact match from 35.2% to 49.0%, a 13.8-point gain over TM; gains span 12.8-13.9 points across three readers. A controlled probe with event sets parsed independently from raw logs shows an 11.0-point gain, from 82.8% to 93.8%, without routing. On full AMA-Bench, the routed system yields a smaller 1.3-point gain, from 69.8% to 71.1%. These results support executable aggregation on tasks that require combining events, with benefits dependent on the task and event specification, the largest residual system-error category in our diagnostic analysis.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
