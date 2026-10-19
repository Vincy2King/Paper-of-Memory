# Learning Personalized Memory Gating from Delayed One-Sided Feedback

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.23812v1
- Published: 2026-10-16
- Updated: 2026-10-16
- Authors: Kaixuan Ji, Zixiang Chen, Wenting Zhao, Cheng Qian, Heng Wang, Weizhi Zhang, Jielin Qiu, Liangwei Yang, Quanquan Gu, Silvio Savarese, Shelby Heinecke, Huan Wang
- Tags: agent, context, long-term, retrieval
- Categories: cs.LG
- URL: http://arxiv.org/abs/2610.23812v1

## One-Sentence Summary
Long-term memory enables language-model agents to personalize future interactions, but a finite memory bank cannot preserve every extracted fact.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory enables language-model agents to personalize future interactions, but a finite memory bank cannot preserve every extracted fact.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory gating policies are typically shared across users and therefore fail to account for user-specific patterns of future reuse.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Long-term memory enables language-model agents to personalize future interactions, but a finite memory bank cannot preserve every extracted fact. Existing memory gating policies are typically shared across users and therefore fail to account for user-specific patterns of future reuse. In this paper, we study memory gating at the fact level. We first propose a retrieval-based labeling strategy that labels each fact by whether it is later retrieved and incorporated into responses. We then formulate online memory gating as contextual apple tasting with delayed one-sided feedback, and propose Warm-Start UCB, which combines offline learning from existing data with online adaptation to the current user. Our theoretical analysis establishes a high-probability regret upper bound of $\tilde{O}(Tε\wedge d\sqrt{T})$ when the delay window is at most $O(\sqrt{T})$, where $T$ is the total number of rounds, $ε$ is the initialization error, $d$ is the dimension of the feature map, and $\tilde{O}(\cdot)$ hides constant and poly-logarithmic factors. The results of our experiment demonstrate that our method outperforms all baselines under different memory budgets and history lengths, establishing it as a promising personalized memory gating policy.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
