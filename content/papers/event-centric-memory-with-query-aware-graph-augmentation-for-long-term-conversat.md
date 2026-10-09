# Event-Centric Memory with Query-Aware Graph Augmentation for Long-Term Conversational Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.11920v1
- Published: 2026-10-08
- Updated: 2026-10-08
- Authors: Yichen Liu, Chunfeng Yuan, Haowei Liu, Wenjuan Li, Zefeng Lin, Bing Li, Xu Chen, Weiming Hu
- Tags: agent, benchmark, context, conversation, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.11920v1

## One-Sentence Summary
For persistent and personalized conversational agents, memory systems can enable them to remember, update, and reason over long histories by storing past interactions and...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：For persistent and personalized conversational agents, memory systems can enable them to remember, update, and reason over long histories by storing past interactions and retrieving relevant information.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory systems typically follow two paradigms: flat-structured memory and graph-based memory.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：agent memory, memory retrieval, working memory
- 来源分类信息：cs.CL

## Abstract Snapshot
For persistent and personalized conversational agents, memory systems can enable them to remember, update, and reason over long histories by storing past interactions and retrieving relevant information. Existing memory systems typically follow two paradigms: flat-structured memory and graph-based memory. The former is lightweight but leaves event relations and state updates implicit, while the latter explicitly models memory structure but incurs additional construction cost and introduces irrelevant relations over long histories. To address these limitations, we propose QGMem, a novel memory construction and activation framework motivated by human memory, in which experience is organized into events and query-relevant events are modeled by graph as working memory. QGMem converts long dialogue histories into event-indexed atomic memory units that preserve individual experiences and consolidates related units into dynamic memory traces that retain state trajectories and current states. When a query arrives, hybrid memory retrieval gathers complementary candidate memories, and query-aware reranking activates the most relevant units as a compact working memory. To expose relational dependencies in the working memory and support conflict-aware reasoning, QGMem organizes the working memory as a local graph, which is then encoded as a graph token and provided to the LLM together with the textual working memory to improve evidence utilization during answer generation. Experiments across six benchmarks validate the framework and show consistent gains in retrieval, multi-hop evidence composition, conflict resolution, and ultra-long dialogue reasoning with compact contexts and moderate inference cost.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
