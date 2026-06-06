# SaliMory: Orchestrating Cognitive Memory for Conversational Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.04120v1
- Published: 2026-06-02
- Updated: 2026-06-02
- Authors: Kai Zhang, Xinyuan Zhang, Hongda Jiang, Shiun-Zu Kuo, Hyokun Yun, Ejaz Ahmed, Shereen Oraby, Ziyun Li, Sanat Sharma, Ann Lee, Ahmed A Aly, Anuj Kumar, Raffay Hamid, Xin Luna Dong
- Tags: agent, context, conversation, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2606.04120v1

## One-Sentence Summary
Conversational agents that serve as lifelong companions must maintain persistent memory across all interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Conversational agents that serve as lifelong companions must maintain persistent memory across all interactions.

进一步看，论文的核心做法或实验重点可以概括为：However, simply expanding context windows with raw retrieval degrades reasoning quality, while training memory agents via standard reinforcement learning creates a severe credit assignment bottleneck in a multi-stage...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, retrieval
- 检索关键词命中：persistent memory, working memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Conversational agents that serve as lifelong companions must maintain persistent memory across all interactions. However, simply expanding context windows with raw retrieval degrades reasoning quality, while training memory agents via standard reinforcement learning creates a severe credit assignment bottleneck in a multi-stage pipeline. To solve this, we introduce SALIMORY, a framework that trains a single language model to manage a cognitively-structured memory-spanning user facts, preferences, and working memory. By introducing a hierarchical stage-wise process reward and reward-decomposed contrastive refinement, SALIMORY provides isolated supervision for distinct memory operations (selective filtering, consolidation, and cue-driven recall) end-to-end. SALIMORY cuts memory-attributed failures by one-third, outperforms the state-of-the-art by over 10% in end-to-end accuracy, and more than doubles the Good Personalization rate.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
