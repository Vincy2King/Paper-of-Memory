# Contextual Agentic Memory is a Memo, Not True Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.27707v1
- Published: 2026-04-30
- Updated: 2026-04-30
- Authors: Binyan Xu, Xilin Dai, Kehuan Zhang
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2604.27707v1

## One-Sentence Summary
Current agentic memory systems (vector stores, retrieval-augmented generation, scratchpads, and context-window management) do not implement memory: they implement lookup.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Current agentic memory systems (vector stores, retrieval-augmented generation, scratchpads, and context-window management) do not implement memory: they implement lookup.

进一步看，论文的核心做法或实验重点可以概括为：We argue that treating lookup as memory is a category error with provable consequences for agent capability, long-term learning, and security.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：agent memory, persistent memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Current agentic memory systems (vector stores, retrieval-augmented generation, scratchpads, and context-window management) do not implement memory: they implement lookup. We argue that treating lookup as memory is a category error with provable consequences for agent capability, long-term learning, and security. Retrieval generalizes by similarity to stored cases; weight-based memory generalizes by applying abstract rules to inputs never seen before. Conflating the two produces agents that accumulate notes indefinitely without developing expertise, face a provable generalization ceiling on compositionally novel tasks that no increase in context size or retrieval quality can overcome, and are structurally vulnerable to persistent memory poisoning as injected content propagates across all future sessions. Drawing on Complementary Learning Systems theory from neuroscience, we show that biological intelligence solved this problem by pairing fast hippocampal exemplar storage with slow neocortical weight consolidation, and that current AI agents implement only the first half. We formalize these limitations, address four alternative views, and close with a co-existence proposal and a call to action for system builders, benchmark designers, and the memory community.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
