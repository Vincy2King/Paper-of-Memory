# MemoNav: Working Memory Model for Visual Navigation

- Source: OpenReview
- Venue: CVPR 2024
- Paper ID: openreview:SSYG5cri9Y
- Published: 2024-01-01
- Updated: 2026-06-19
- Authors: Hongxin Li, Zeyu Wang, Xu Yang, Yuran Yang, Shuqi Mei, Zhaoxiang Zhang
- Tags: agent, long-term
- Categories: DBLP.org/-/Record
- URL: https://openreview.net/forum?id=SSYG5cri9Y

## One-Sentence Summary
Image-goal navigation is a challenging task that requires an agent to navigate to a goal indicated by an image in unfamiliar environments.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `CVPR 2024` 这个 venue 相关。

从摘要来看，作者主要关注的是：Image-goal navigation is a challenging task that requires an agent to navigate to a goal indicated by an image in unfamiliar environments.

进一步看，论文的核心做法或实验重点可以概括为：Existing methods utilizing diverse scene memories suffer from inefficient exploration since they use all historical observations for decision-making without considering the goal-relevant fraction.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：CVPR 2024
- 高亮主题命中：agent, long-term
- 检索关键词命中：long-term memory, working memory
- 来源分类信息：DBLP.org/-/Record

## Abstract Snapshot
Image-goal navigation is a challenging task that requires an agent to navigate to a goal indicated by an image in unfamiliar environments. Existing methods utilizing diverse scene memories suffer from inefficient exploration since they use all historical observations for decision-making without considering the goal-relevant fraction. To address this limitation, we present MemoNav, a novel memory model for image-goal navigation, which utilizes a working memory-inspired pipeline to improve navigation performance. Specifically, we employ three types of navigation memory. The node features on a map are stored in the short-term memory (STM), as these features are dynamically updated. A forgetting module then retains the informative STM fraction to increase efficiency. We also introduce long-term memory (LTM) to learn global scene representations by progressively aggregating STM features. Subsequently, a graph attention module encodes the retained STM and the LTM to generate working memory (WM) which contains the scene features essential for efficient navigation. The synergy among these three memory types boosts navigation performance by enabling the agent to learn and leverage goal-relevant scene features within a topological map. Our evaluation on multi-goal tasks demonstrates that MemoNav significantly outperforms previous methods across all difficulty levels in both Gibson and Matterport3D scenes. Qualitative results further illustrate that MemoNav plans more efficient routes.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
