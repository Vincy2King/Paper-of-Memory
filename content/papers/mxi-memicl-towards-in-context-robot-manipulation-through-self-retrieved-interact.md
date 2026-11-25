# MXI-MemICL: Towards In-Context Robot Manipulation through Self-Retrieved Interaction Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.32564v1
- Published: 2026-11-24
- Updated: 2026-11-24
- Authors: Jialong Peng, Shihao Zhou, Feng Yan, Wen Xiao, Haozheng Wang, Wenqi Ren, Wenyuan Sheng, Jian Qiao, Jiaxu Miao, Lin Ma, Chao Yang
- Tags: context
- Categories: cs.RO, cs.AI
- URL: http://arxiv.org/abs/2611.32564v1

## One-Sentence Summary
In-context learning (ICL) offers robots a way to acquire new skills from a single demonstration without parameter updates.

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：In-context learning (ICL) offers robots a way to acquire new skills from a single demonstration without parameter updates.

进一步看，论文的核心做法或实验重点可以概括为：However, existing robotic ICL methods either rely on large-scale pretraining constrained by scarce, costly robot interaction data or require additional annotations yet struggle to generalize across tasks.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.RO, cs.AI

## Abstract Snapshot
In-context learning (ICL) offers robots a way to acquire new skills from a single demonstration without parameter updates. However, existing robotic ICL methods either rely on large-scale pretraining constrained by scarce, costly robot interaction data or require additional annotations yet struggle to generalize across tasks. To bridge this gap, we propose MXI-MemICL, a framework for memory-guided ICL in vision-language-action (VLA) models. By treating demonstrations as retrievable memory, MXI-MemICL enables in-context manipulation without additional large-scale pretraining or specialized annotations. Specifically, a visual-action causal encoder turns actions and their observed effects in demonstrations and completed interactions into reusable memory to guide execution. To retrieve experience suited to upcoming execution, an intention predictor forecasts the next stage's intent and uses it to query memory. The retrieved experience conditions the language backbone through experience-token prefixes and gated cross-attention, guiding action generation with a learned gate that regulates its influence. MXI-MemICL improves success over the baseline by +8.2% and +14.4% on RoboCasa365 and RoboTwin 2.0. Real-robot experiments show a +9.0% gain, with demonstrations adding +5.0% on seen and +16.7% on unseen tasks. The code will be made publicly available.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
