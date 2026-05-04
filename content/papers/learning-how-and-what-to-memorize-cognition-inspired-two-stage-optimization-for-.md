# Learning How and What to Memorize: Cognition-Inspired Two-Stage Optimization for Evolving Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.00702v1
- Published: 2026-05-01
- Updated: 2026-05-01
- Authors: Derong Xu, Shuochen Liu, Pengfei Luo, Pengyue Jia, Yingyi Zhang, Yi Wen, Yimin Deng, Wenlin Zhang, Enhong Chen, Xiangyu Zhao, Tong Xu
- Tags: agent, benchmark, context, long-term
- Categories: cs.CL
- URL: http://arxiv.org/abs/2605.00702v1

## One-Sentence Summary
Large language model (LLM) agents require long-term user memory for consistent personalization, but limited context windows hinder tracking evolving preferences over long...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents require long-term user memory for consistent personalization, but limited context windows hinder tracking evolving preferences over long interactions.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory systems mainly rely on static, hand-crafted update rules; although reinforcement learning (RL)-based agents learn memory updates, sparse outcome rewards provide weak supervision, resulting in unstable...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：cs.CL

## Abstract Snapshot
Large language model (LLM) agents require long-term user memory for consistent personalization, but limited context windows hinder tracking evolving preferences over long interactions. Existing memory systems mainly rely on static, hand-crafted update rules; although reinforcement learning (RL)-based agents learn memory updates, sparse outcome rewards provide weak supervision, resulting in unstable long-horizon optimization. Drawing on memory schema theory and the functional division between prefrontal regions and hippocampus regions, we introduce MemCoE, a cognition-inspired two-stage optimization framework that learns how memory should be organized and what information to update. In the first stage, we propose Memory Guideline Induction to optimize a global guideline via contrastive feedback interpreted as textual gradients; in the second stage, Guideline-Aligned Memory Policy Optimization uses the induced guideline to define structured process rewards and performs multi-turn RL to learn a guideline-following memory evolution policy. We evaluate on three personalization memory benchmarks, covering explicit/implicit preference and different sizes and noise, and observe consistent improvements over strong baselines with favorable robustness, transferability, and efficiency.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
