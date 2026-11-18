# Déjà View: A Shared Working-Memory Model for Visual Tasks

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.23177v1
- Published: 2026-11-17
- Updated: 2026-11-17
- Authors: Mranmay Shetty, Gabriel Kreiman
- Tags: working memory
- Categories: cs.CV, cs.LG, q-bio.NC
- URL: http://arxiv.org/abs/2611.23177v1

## One-Sentence Summary
A working-memory model must remember stimuli and use its memory flexibly to perform different tasks.

## Introduction
这篇论文被纳入仓库，是因为它和 `working memory` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：A working-memory model must remember stimuli and use its memory flexibly to perform different tasks.

进一步看，论文的核心做法或实验重点可以概括为：Here we introduce a model of working memory for images that combines dynamic activity with temporary associations between image features.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：working memory
- 检索关键词命中：working memory
- 来源分类信息：cs.CV, cs.LG, q-bio.NC

## Abstract Snapshot
A working-memory model must remember stimuli and use its memory flexibly to perform different tasks. Here we introduce a model of working memory for images that combines dynamic activity with temporary associations between image features. We train the model on five tasks, including remembering a sample while other images are presented, categorizing distractor images while remembering the sample, and determining whether an image is new or has been presented before. The same trained model performs all tasks, guided by explicit cues about which response is required. We use this flexible memory model to ask how delay, distraction, and image history affect performance. Delays have little effect on sample-memory performance for the delays we tested, while seeing more images leads to more false alarms even when the target image appeared equally recently in all cases. On the sample-memory-plus-categorization task, the probability of correct responses on all questions decreases as more questions are asked, despite robust sample-memory performance. Finally, the model maintains stable performance across 40 brief trials of each task under the tested conditions. Together, these results demonstrate how a single working-memory system can be flexibly used to perform different tasks, and how its errors depend on both previous images and task demands.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
