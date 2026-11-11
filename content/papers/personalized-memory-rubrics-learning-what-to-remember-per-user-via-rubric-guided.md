# Personalized Memory Rubrics: Learning What to Remember per User via Rubric-Guided Credit Assignment

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.14017v1
- Published: 2026-11-10
- Updated: 2026-11-10
- Authors: Yupeng Han, Kai Zhang, Shuochen Liu, Ze Liu, Xianquan Wang, Zhihong Pan, Xiangyu Zhao, Qi Liu, Enhong Chen
- Tags: agent, benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.14017v1

## One-Sentence Summary
Long-horizon personalized agents maintain an evolving memory by continuously deciding what to add, modify, or discard.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon personalized agents maintain an evolving memory by continuously deciding what to add, modify, or discard.

进一步看，论文的核心做法或实验重点可以概括为：However, learning an optimal update policy remains challenging.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-horizon personalized agents maintain an evolving memory by continuously deciding what to add, modify, or discard. However, learning an optimal update policy remains challenging. Conventional training relies solely on terminal question-answering accuracy, yielding a coarse feedback signal that treats all intermediate updates identically. Furthermore, update utility is inherently user-specific, as identical memory actions may yield opposite effects across different user personas. Existing methods fail to address this heterogeneity, relying on globally shared evaluation standards with at most a single scalar intermediate reward. To address these challenges, we propose \textbf{Personalized Memory Rubrics} (\textbf{PMR}), a framework that translates terminal feedback into fine-grained, per-step, and per-user credit assignment. PMR decomposes evaluation into a universal layer capturing cross-persona failure patterns and a per-user adaptive layer modeling individual traits as a specialized delta over the universal baseline. Through \textbf{Rubric-Guided Credit Assignment}, PMR redistributes credit at the token level, selectively amplifying validated decisions on successful trajectories while falling back to standard policy optimization on failed ones to avoid unreliable attribution. The rubric and memory policy \textbf{co-evolve} in a closed loop with anti-circularity guarantees. Crucially, PMR incurs zero inference overhead, operating without any rubric or external judge during deployment. Extensive experiments across four benchmarks demonstrate consistent gains over strong memory-augmented baselines.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
