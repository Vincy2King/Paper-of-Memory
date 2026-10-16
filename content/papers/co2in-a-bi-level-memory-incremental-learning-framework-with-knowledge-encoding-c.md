# Co2In: a Bi-level Memory Incremental Learning Framework with Knowledge Encoding, Consolidation, and Integration

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.21804v1
- Published: 2026-10-15
- Updated: 2026-10-15
- Authors: Wenju Sun, Qingyong Li, Boyang Li, Wen Wang, Siyu Zhang, Yi Wei, Yangliao Geng
- Tags: long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.21804v1

## One-Sentence Summary
Incremental learning (IL) aims to continually acquire new knowledge (plasticity) while retaining previously learned information (stability).

## Introduction
这篇论文被纳入仓库，是因为它和 `long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Incremental learning (IL) aims to continually acquire new knowledge (plasticity) while retaining previously learned information (stability).

进一步看，论文的核心做法或实验重点可以概括为：However, striking a balance between plasticity and stability remains a significant challenge for intelligent systems.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：long-term
- 检索关键词命中：long-term memory, working memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Incremental learning (IL) aims to continually acquire new knowledge (plasticity) while retaining previously learned information (stability). However, striking a balance between plasticity and stability remains a significant challenge for intelligent systems. The human brain achieves exceptional balance, owing to various memory units that collaboratively encode and store information. Inspired by human memory mechanisms, this paper introduces an IL framework with knowledge enCoding, Consolidation, and Integration (Co2In). Co2In is designed as a bi-level memory architecture: a working memory for adaptive knowledge acquisition and a long-term memory dedicated to the persistent retention of information. The two memory modules work cooperatively during IL. The working memory first learns from new data to encode knowledge into parameters. Subsequently, Co2In performs a consolidation process to identify underlying patterns in the learned parameters and re-express them into a compact knowledge representation. Next, the knowledge representation and the identified patterns are transformed into separate network layers and integrated into the long-term memory. These designs empower Co2In to accumulate knowledge with high plasticity and stability. We evaluate Co2In on CIFAR-10, CIFAR-100, and Tiny-ImageNet under exemplar-free Class-IL and Task-IL settings. Experimental results show that Co2In achieves state-of-the-art performance with efficient memory consumption.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
