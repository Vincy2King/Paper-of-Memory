# Temporal Order Matters for Agentic Memory: Segment Trees for Long-Horizon Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.04555v1
- Published: 2026-06-03
- Updated: 2026-06-03
- Authors: Yifan Simon Liu, Liam Gallagher, Faeze Moradi Kalarde, Jiazhou Liang, Armin Toroghi, Scott Sanner
- Tags: agent, benchmark, context, conversation, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2606.04555v1

## One-Sentence Summary
Long-horizon conversational agents need to interact with users through evolving events, tasks, and goals.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon conversational agents need to interact with users through evolving events, tasks, and goals.

进一步看，论文的核心做法或实验重点可以概括为：Such histories are naturally temporal, yet many existing memory systems organize information primarily by topical similarity and may ignore the order in which events occur.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, retrieval
- 检索关键词命中：agent memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Long-horizon conversational agents need to interact with users through evolving events, tasks, and goals. Such histories are naturally temporal, yet many existing memory systems organize information primarily by topical similarity and may ignore the order in which events occur. We introduce Segment Tree Memory, or SegTreeMem, a memory architecture that represents conversation history as a temporally ordered Segment Tree over utterances. SegTreeMem incrementally inserts new utterances through an online rightmost-frontier update rule, preserving chronological order while forming hierarchical memory segments. For retrieval, SegTreeMem propagates relevance scores through the tree to combine local semantic matching with hierarchical temporal context. Across three long-horizon memory benchmarks and two LLM backbones, SegTreeMem improves answer quality over flat retrieval, graph-structured memory, and tree-structured memory baselines. Additional temporal-order permutation analysis shows that the performance gain depends on preserving temporal order during memory construction, supporting the claim that temporal order is a key structure for agentic memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
