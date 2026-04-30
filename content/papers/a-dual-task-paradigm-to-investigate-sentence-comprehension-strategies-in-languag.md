# A Dual-Task Paradigm to Investigate Sentence Comprehension Strategies in Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.26351v1
- Published: 2026-04-29
- Updated: 2026-04-29
- Authors: Rei Emura, Saku Sugawara
- Tags: working memory
- Categories: cs.CL
- URL: http://arxiv.org/abs/2604.26351v1

## One-Sentence Summary
Language models (LMs) behave more like humans when their cognitive resources are restricted, particularly in predicting sentence processing costs such as reading times.

## Introduction
这篇论文被纳入仓库，是因为它和 `working memory` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Language models (LMs) behave more like humans when their cognitive resources are restricted, particularly in predicting sentence processing costs such as reading times.

进一步看，论文的核心做法或实验重点可以概括为：However, it remains unclear whether such constraints similarly affect sentence comprehension strategies.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：working memory
- 检索关键词命中：working memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Language models (LMs) behave more like humans when their cognitive resources are restricted, particularly in predicting sentence processing costs such as reading times. However, it remains unclear whether such constraints similarly affect sentence comprehension strategies. Besides, existing methods do not directly target the balance between memory storage and sentence processing, which is central to human working memory. To address this issue, we propose a dual-task paradigm that combines an arithmetic computation task with a sentence comprehension task, such as "The 2 cocktail + blended 3 =..." Our experiments show that under dual-task conditions, GPT-4o, o3-mini, and o4-mini shift toward plausibility-based comprehension, mirroring humans' rational inference. Specifically, these models show a greater accuracy gap between plausible sentences (e.g., "The cocktail was blended by the bartender") and implausible sentences (e.g., "The bartender was blended by the cocktail") in the dual-task condition compared to the single-task conditions. These findings suggest that constraints on the balance between memory and processing resources promote rational inference in LMs. More broadly, they support the view that human-like sentence comprehension fundamentally arises from the allocation of limited cognitive resources.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
