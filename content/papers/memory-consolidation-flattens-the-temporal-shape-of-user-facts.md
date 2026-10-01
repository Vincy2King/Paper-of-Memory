# Memory Consolidation Flattens the Temporal Shape of User Facts

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.36457v1
- Published: 2026-09-29
- Updated: 2026-09-29
- Authors: Sugam Panthi, Muhaiminul Yeamin, Siyan Luo, Rabab Abdelfattah
- Tags: benchmark, conversation, long-term
- Categories: cs.CL
- URL: http://arxiv.org/abs/2609.36457v1

## One-Sentence Summary
Long-term memory systems turn conversations into short stored notes.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory systems turn conversations into short stored notes.

进一步看，论文的核心做法或实验重点可以概括为：A note can keep a user fact while losing evidence about whether the fact still holds.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, conversation, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-term memory systems turn conversations into short stored notes. A note can keep a user fact while losing evidence about whether the fact still holds. For example, "I am driving a Peugeot" can become "The user drives a Peugeot," which drops the cue that the activity is ongoing. We call this aspectual flattening and measure it with LAPSE, a benchmark of matched user statements that differ only in temporal form. We find that memory writers flatten aspect selectively. Three writer models flattened the progressive statement but kept its simple-present match in 244 of 381 pairs, never the reverse. The asymmetry holds in all 11 model configurations tested and in the installed pipelines mem0, Graphiti, and Letta. The lost cue matters to later readers. In exploratory tests, changing only the stored verb shifted all three readers' estimates that a fact still holds. When readers could ask the user before acting, two of three acted without asking more often on flattened notes. Our planned memory-use task could not detect this, because readers there acted on almost every stored fact, even expired ones. Memory writing can thus remove evidence that later models use to decide whether to act.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
