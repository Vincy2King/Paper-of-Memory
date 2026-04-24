# Working Memory Constraints Scaffold Learning in Transformers under Data Scarcity

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.20789v2
- Published: 2026-04-22
- Updated: 2026-04-23
- Authors: Pranava Madhyastha, Dagmar Adamcova
- Tags: working memory
- Categories: cs.CL, cs.AI, cs.LG
- URL: http://arxiv.org/abs/2604.20789v2

## One-Sentence Summary
We investigate the integration of human-like working memory constraints into the Transformer architecture and implement several cognitively inspired attention variants,...

## Introduction
这篇论文被纳入仓库，是因为它和 `working memory` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We investigate the integration of human-like working memory constraints into the Transformer architecture and implement several cognitively inspired attention variants, including fixed-width windows based and temporal...

进一步看，论文的核心做法或实验重点可以概括为：Our modified GPT-2 models are trained from scratch on developmentally plausible datasets (10M and 100M words).

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：working memory
- 检索关键词命中：working memory
- 来源分类信息：cs.CL, cs.AI, cs.LG

## Abstract Snapshot
We investigate the integration of human-like working memory constraints into the Transformer architecture and implement several cognitively inspired attention variants, including fixed-width windows based and temporal decay based attention mechanisms. Our modified GPT-2 models are trained from scratch on developmentally plausible datasets (10M and 100M words). Performance is evaluated on grammatical judgment tasks (BLiMP) and alignment with human reading time data. Our results indicate that these cognitively-inspired constraints, particularly fixed-width attention, can significantly improve grammatical accuracy especially when training data is scarce. These constrained models also tend to show a stronger alignment with human processing metrics. The findings suggest that such constraints may serve as a beneficial inductive bias, guiding models towards more robust linguistic representations, especially in data-limited settings.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
