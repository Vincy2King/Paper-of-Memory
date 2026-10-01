# Learning to Retrieve Missing Evidence for Long-Term Memory QA

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.37443v1
- Published: 2026-09-29
- Updated: 2026-09-29
- Authors: Yi-Xuan Deng, Yi Zhang, Wei Liu, Chao Xue, Shuojin Yang
- Tags: conversation, long-term, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2609.37443v1

## One-Sentence Summary
Long-term memory enables language models to use past interactions in future conversations.

## Introduction
这篇论文被纳入仓库，是因为它和 `conversation, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory enables language models to use past interactions in future conversations.

进一步看，论文的核心做法或实验重点可以概括为：However, evidence needed to answer a question may be scattered across distant turns, while the question itself omits clues needed to locate it.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：conversation, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Long-term memory enables language models to use past interactions in future conversations. However, evidence needed to answer a question may be scattered across distant turns, while the question itself omits clues needed to locate it. Retrieved facts can reveal these clues, motivating retrieval decisions conditioned on evidence already found. We introduce MERA (Missing-Evidence Retrieval Augmentation), which separates globally searchable memory from a question-specific evidence state. Verified evidence guides subsequent retrieval without restricting access to the global memory. We train a lightweight planner through reinforcement learning, rewarding queries that recover previously missing evidence. MERA achieves strong answer accuracy across Qwen3-30B and GPT-4o-mini backbones. With Qwen3-30B for evidence processing and answer generation, the trained 0.6B planner achieves 77.40% accuracy on LoCoMo and 71.29% on LongMemEval-S, exceeding a 30B planner without retrieval-grounded training by 4.10% and 3.96%, respectively. On LoCoMo, later retrieval rounds increase cumulative evidence recall from 55.5% to 80.5%.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
