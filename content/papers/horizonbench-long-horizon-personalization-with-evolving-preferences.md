# HorizonBench: Long-Horizon Personalization with Evolving Preferences

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.17283v1
- Published: 2026-04-19
- Updated: 2026-04-19
- Authors: Shuyue Stella Li, Bhargavi Paranjape, Kerem Oktar, Zhongyao Ma, Gelin Zhou, Lin Guan, Na Zhang, Sem Park, Lin Chen, Diyi Yang, Yulia Tsvetkov, Asli Celikyilmaz
- Tags: benchmark, context, conversation
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2604.17283v1

## One-Sentence Summary
User preferences evolve across months of interaction, and tracking them requires inferring when a stated preference has been changed by a subsequent life event.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：User preferences evolve across months of interaction, and tracking them requires inferring when a stated preference has been changed by a subsequent life event.

进一步看，论文的核心做法或实验重点可以概括为：We define this problem as long-horizon personalization and observe that progress on it is limited by data availability and measurement, with no existing resource providing both naturalistic long-horizon interactions...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, conversation
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
User preferences evolve across months of interaction, and tracking them requires inferring when a stated preference has been changed by a subsequent life event. We define this problem as long-horizon personalization and observe that progress on it is limited by data availability and measurement, with no existing resource providing both naturalistic long-horizon interactions and the ground-truth provenance needed to diagnose why models fail. We introduce a data generator that produces conversations from a structured mental state graph, yielding ground-truth provenance for every preference change across 6-month timelines, and from it construct HorizonBench, a benchmark of 4,245 items from 360 simulated users with 6-month conversation histories averaging ~4,300 turns and ~163K tokens. HorizonBench provides a testbed for long-context modeling, memory-augmented architectures, theory-of-mind reasoning, and user modeling. Across 25 frontier models, the best model reaches 52.8% and most score at or below the 20% chance baseline. When these models err on evolved preferences, over a third of the time they select the user's originally stated value without tracking the updated user state. This belief-update failure persists across context lengths and expression explicitness levels, identifying state-tracking capability as the primary bottleneck for long-horizon personalization.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
