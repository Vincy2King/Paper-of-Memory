# Finding Is Not Returning, Returning Is Not Reconstructing: A Multi-Dimensional Evaluation of Agent Social Re-entry

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.39781v1
- Published: 2026-10-29
- Updated: 2026-10-29
- Authors: Sheng Wan, Cong Ma, Sichen Dong, Qian'Ang Mao, Chenhan Zhang, Daning Hu, Qiang Yang
- Tags: agent, context, conversation, long-term, retrieval
- Categories: cs.AI, cs.SI
- URL: http://arxiv.org/abs/2610.39781v1

## One-Sentence Summary
As Large Language Model (LLM) agents increasingly participate in persistent social environments, understanding their long-term social interaction capabilities becomes...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：As Large Language Model (LLM) agents increasingly participate in persistent social environments, understanding their long-term social interaction capabilities becomes increasingly important.

进一步看，论文的核心做法或实验重点可以概括为：While existing research has advanced long-term memory and conversational context retrieval, less attention has been paid to whether agents can autonomously re-engage with previously inactive conversations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, long-term, retrieval
- 检索关键词命中：long-term memory, memory retrieval, persistent memory
- 来源分类信息：cs.AI, cs.SI

## Abstract Snapshot
As Large Language Model (LLM) agents increasingly participate in persistent social environments, understanding their long-term social interaction capabilities becomes increasingly important. While existing research has advanced long-term memory and conversational context retrieval, less attention has been paid to whether agents can autonomously re-engage with previously inactive conversations. In particular, remembering a past interaction does not necessarily mean that an agent can identify when to revisit it, decide to return, or reconstruct the context needed for a coherent continuation. To investigate this gap, we introduce agent social re-entry as a multi- dimensional evaluation problem, distinguishing three complementary capabilities: Finding, Returning, and Reconstructing. We develop a shared-snapshot evaluation framework that measures these dimensions independently, allowing us to examine how conversational resurfacing and persistent memory relate to different aspects of social re-entry. Evaluations across six LLM configurations show that resurfacing substantially improves target conversation identification, while persistent memory is associated with higher rates of autonomous target-directed replying. However, neither improvement is accompanied by consistent gains in contextual reconstruction. These results highlight the distinction between accessing previous conversations, choosing to re-engage, and maintaining conversational continuity. Our framework provides a way to evaluate these capabilities separately rather than relying on memory retrieval or conversational response quality alone.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
