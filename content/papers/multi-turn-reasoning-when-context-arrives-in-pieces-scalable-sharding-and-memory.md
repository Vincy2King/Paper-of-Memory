# Multi-Turn Reasoning When Context Arrives in Pieces: Scalable Sharding and Memory-Augmented RL

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.12941v1
- Published: 2026-06-11
- Updated: 2026-06-11
- Authors: Shu Tong Luo, Wenqin Liu, Rui Liu, Mingming Gong, Jiaxian Guo
- Tags: context, conversation
- Categories: cs.CL
- URL: http://arxiv.org/abs/2606.12941v1

## One-Sentence Summary
When a user reveals task-critical information across several conversation turns, LLM accuracy drops by up to 65% despite full context availability.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：When a user reveals task-critical information across several conversation turns, LLM accuracy drops by up to 65% despite full context availability.

进一步看，论文的核心做法或实验重点可以概括为：We show that this Lost in Conversation degradation can be substantially mitigated by training models to maintain a compact rolling memory instead of attending to a growing history.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, conversation
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CL

## Abstract Snapshot
When a user reveals task-critical information across several conversation turns, LLM accuracy drops by up to 65% despite full context availability. We show that this Lost in Conversation degradation can be substantially mitigated by training models to maintain a compact rolling memory instead of attending to a growing history. To make such training scalable, we introduce a low-cost sharding pipeline that converts single-turn QA datasets into multi-turn fragmented-information episodes, eliminating the need for hours of manual annotation. Training only on sharded GSM8K, our memory-augmented policy significantly improves multi-turn accuracy and generalises zero-shot to harder math and out-of-domain long-context QA. Moreover, memory-trained models outperform full-history baselines even when given the full history at test time, suggesting that learning to compress induces more robust incremental reasoning than full-context exposure alone.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
