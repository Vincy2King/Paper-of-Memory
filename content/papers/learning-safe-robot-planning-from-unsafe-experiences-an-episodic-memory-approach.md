# Learning Safe Robot Planning from Unsafe Experiences: An Episodic Memory Approach for LLM-based Agents

- Source: OpenReview
- Venue: ICLR 2026 Workshop MemAgents
- Paper ID: openreview:KrmyJtyE6k
- Published: 2026-03-03
- Updated: 2026-04-25
- Authors: Hang Zhao, Jing Du, Shengwei An
- Tags: agent, episodic, retrieval
- Categories: ICLR.cc/2026/Workshop/MemAgent/-/Submission
- URL: https://openreview.net/forum?id=KrmyJtyE6k

## One-Sentence Summary
LLM-based robotic agents can generate unsafe commands that harm humans, objects, or the environment.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, episodic, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ICLR 2026 Workshop MemAgents` 这个 venue 相关。

从摘要来看，作者主要关注的是：LLM-based robotic agents can generate unsafe commands that harm humans, objects, or the environment.

进一步看，论文的核心做法或实验重点可以概括为：We propose an episodic safety memory system that learns to filter harmful instructions by storing and retrieving past violation experiences.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ICLR 2026 Workshop MemAgents
- 高亮主题命中：agent, episodic, retrieval
- 检索关键词命中：episodic memory, memory retrieval
- 来源分类信息：ICLR.cc/2026/Workshop/MemAgent/-/Submission

## Abstract Snapshot
LLM-based robotic agents can generate unsafe commands that harm humans, objects, or the environment. We propose an episodic safety memory system that learns to filter harmful instructions by storing and retrieving past violation experiences. Our memory architecture maintains episodic stores of unsafe instances and consolidates recurring patterns into semantic constraints. Real-time memory retrieval blocks similar unsafe commands before execution. Preliminary experiments on ConceptGraphs-based planning show 94% safety rate (vs. 52% baseline) while maintaining 97% task success, suggesting that learning from unsafe experiences can enable safer LLM-based robotic agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
