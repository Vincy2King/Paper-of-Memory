# Controlled Memory Interference in Continual LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.07622v1
- Published: 2026-08-07
- Updated: 2026-08-07
- Authors: Ao Ding, Hongzong LI, Shiqin Tang, Li Zhang, Liang Chen, Xuyang Chen, Zi Liang
- Tags: agent, long-term, retrieval
- Categories: cs.AI, cs.IR, cs.LG
- URL: http://arxiv.org/abs/2608.07622v1

## One-Sentence Summary
Long-term memory enables AI agents to maintain continuity across sessions, personalize behavior, and evolve through accumulated experience.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory enables AI agents to maintain continuity across sessions, personalize behavior, and evolve through accumulated experience.

进一步看，论文的核心做法或实验重点可以概括为：Yet memory evolution is not simply a process of storing more information: new experiences may reinforce, revise, or interfere with existing memory states.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.AI, cs.IR, cs.LG

## Abstract Snapshot
Long-term memory enables AI agents to maintain continuity across sessions, personalize behavior, and evolve through accumulated experience. Yet memory evolution is not simply a process of storing more information: new experiences may reinforce, revise, or interfere with existing memory states. Existing systems mainly emphasize memory construction and relevance-based retrieval, but several memories may remain simultaneously relevant while differing in state, temporal validity, or authority. We introduce Controlled Memory Interference (CMI), a controlled diagnostic and data-generation framework for studying how agent memory evolves under different memory relationships. Across controlled memory evolution, benign accumulation has limited effects, whereas relationship-specific interference sharply suppresses update plasticity with little stability gain, either by blocking target-memory exposure or by disrupting its downstream use. Lexical and Dense retrieval exhibit distinct interference pathways, while poisoning is more sensitive to update-authority cues than to recency alone. Beyond diagnosis, CMI provides targeted examples for interference-aware memory learning, improving the distinction between valid updates and interference-inducing memories while preserving performance on original memory tasks. These findings show that memory evolution is shaped not only by memory scale, but also by interactions among accumulated experiences. More broadly, memory interference emerges as an important factor for reliable continual agent memory systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
