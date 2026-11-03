# Pulse: Long-Horizon Tasks Need Streaming Personalization

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.00988v1
- Published: 2026-10-31
- Updated: 2026-10-31
- Authors: Qijia Zhuang, Jialiang Liang, Yuxiang Ren
- Tags: agent, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.00988v1

## One-Sentence Summary
Large language model agents increasingly undertake complex, long-horizon tasks that benefit from sustained personalized support through long-term memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model agents increasingly undertake complex, long-horizon tasks that benefit from sustained personalized support through long-term memory.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory-augmented methods retrieve and use memory primarily from the initial request, with limited awareness of ongoing execution and emerging personalization needs.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term
- 检索关键词命中：long-term memory, memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language model agents increasingly undertake complex, long-horizon tasks that benefit from sustained personalized support through long-term memory. Existing memory-augmented methods retrieve and use memory primarily from the initial request, with limited awareness of ongoing execution and emerging personalization needs. Agents may therefore overlook user preferences and project constraints during multistep tasks. We propose Pulse, a streaming personalization method for long-horizon tasks. An independent, lightweight memory agent continuously monitors execution, identifies emerging personalization needs and potential preference conflicts, and uses user and project memories to provide targeted interventions at appropriate stages. Reinforcement learning optimizes when and how the memory agent intervenes, improving the timeliness and accuracy of personalized support. Pulse scores 71.9% on $π$-Bench and 46.4% on MCP-Persona, achieving the highest overall scores among the compared methods on both datasets while improving task execution efficiency.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
