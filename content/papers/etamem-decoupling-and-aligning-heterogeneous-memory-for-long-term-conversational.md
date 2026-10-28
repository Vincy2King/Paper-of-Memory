# ETAMem: Decoupling and Aligning Heterogeneous Memory for Long-Term Conversational Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.37443v1
- Published: 2026-10-27
- Updated: 2026-10-27
- Authors: Xinying Qian, Ying Zhang, Yu Zhao, Xubo Liu, Baohang Zhou, Jeff Z. Pan
- Tags: agent, conversation, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.37443v1

## One-Sentence Summary
Long-term memory enables Large Language Models (LLMs) to maintain coherent and personalized interactions across extended conversations.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory enables Large Language Models (LLMs) to maintain coherent and personalized interactions across extended conversations.

进一步看，论文的核心做法或实验重点可以概括为：However, existing memory systems face two key challenges: (1) Information Entanglement, where heterogeneous information is mixed within coarse-grained memory units; and (2) Organizational Mismatch, where memory...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-term memory enables Large Language Models (LLMs) to maintain coherent and personalized interactions across extended conversations. However, existing memory systems face two key challenges: (1) Information Entanglement, where heterogeneous information is mixed within coarse-grained memory units; and (2) Organizational Mismatch, where memory structures based primarily on semantic similarity may overlook other associations. To address these challenges, we propose ETAMem, a multi-view memory framework that decouples heterogeneous conversational information and aligns memory representations and organization with its distinct characteristics. Specifically, heterogeneous information parsing extracts atomic memory units and identifies affective information. View-specific memory structuring then organizes these units into three complementary hierarchical views: Event, Affect, and Time. ETAMem incrementally maintains memory structures with adaptively calibrated thresholds. For retrieval, entropy-based retrieval allocates query-specific budgets across views and performs hierarchical search within each view. Experiments on LoCoMo and LongMemEval-S demonstrate that ETAMem outperforms state-of-the-art baselines, achieving relative accuracy improvements of 12.46% and 7.96%, respectively, while maintaining competitive token efficiency. Further analyses demonstrate the complementary benefits of different memory views.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
