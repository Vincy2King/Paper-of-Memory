# DRAM: Delta-rule Recurrent Associative Memory for Robot Manipulation Policies

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.32453v1
- Published: 2026-09-26
- Updated: 2026-09-26
- Authors: Xinyu Zhao, Yixiang Shan, Tao Yang, Runyu Lei, Yiming Zhao, Jiaxin Fan, Zongbao Feng, Peng Jia
- Tags: context, long-term
- Categories: cs.RO, cs.AI
- URL: http://arxiv.org/abs/2609.32453v1

## One-Sentence Summary
Robotic manipulation is inherently history-dependent, yet most pretrained robotic policies condition on only the current observation or a short temporal window.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Robotic manipulation is inherently history-dependent, yet most pretrained robotic policies condition on only the current observation or a short temporal window.

进一步看，论文的核心做法或实验重点可以概括为：Equipping such policies with long-term memory remains challenging: existing approaches either feed the backbone multi-frame observation windows, which substantially increase inference cost, or rely on pre-defined...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.RO, cs.AI

## Abstract Snapshot
Robotic manipulation is inherently history-dependent, yet most pretrained robotic policies condition on only the current observation or a short temporal window. Equipping such policies with long-term memory remains challenging: existing approaches either feed the backbone multi-frame observation windows, which substantially increase inference cost, or rely on pre-defined semantic features, which limit task generality and may also require the retraining of the backbone to adapt to the memory. We introduce DRAM (Delta-rule Recurrent Associative Memory), a plug-and-play memory module that can be attached to a wide range of pretrained robotic policies, endowing them with long-horizon memory without architectural modification or backbone retraining, requiring only task-specific post-training of the memory module and action expert. DRAM maintains a fixed-size associative memory using gated delta-rule linear attention, with a modified update that incorporates all tokens within each frame in parallel. An architecture-agnostic readout integrates historical context into action prediction across different policy architectures. Experiments show that DRAM consistently improves frozen pretrained policies over short-context baselines and alternative compact memory designs, validating its effectiveness as a fixed-size, post-hoc memory module trained with the backbone frozen.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
