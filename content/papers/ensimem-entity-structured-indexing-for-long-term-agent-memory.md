# EnSIMem: Entity-Structured Indexing for Long-Term Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.27279v1
- Published: 2026-09-23
- Updated: 2026-09-23
- Authors: Xuanyu Meng, Xing Fan, Xinyi Fan, Chenlei Guo, Yixuan Xie, Jiawei Han
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2609.27279v1

## One-Sentence Summary
An agent that interacts with users over long periods must recall facts, preferences, events, and changes from a continuously growing interaction history.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：An agent that interacts with users over long periods must recall facts, preferences, events, and changes from a continuously growing interaction history.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory systems often compress interactions into generic summaries or retrieve anonymous text chunks, making it difficult for an agent to identify the correct entity, property, and supporting evidence.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
An agent that interacts with users over long periods must recall facts, preferences, events, and changes from a continuously growing interaction history. Existing memory systems often compress interactions into generic summaries or retrieve anonymous text chunks, making it difficult for an agent to identify the correct entity, property, and supporting evidence. We present EnSIMem, an entity-structured long-term memory architecture for an agent. During offline construction, the system organizes interactions into theme-coherent episodes and builds dialogue-grounded index entries of the form [entity][entity type][property:value]. Each entry preserves its source turns, temporal information, and available multimodal fields. During online interaction, the agent's request is decomposed into evidence requirements whose properties are aligned with the memory index. Entity-property lookup and adaptive retrieval then collect the evidence needed for point, temporal, compositional, and aggregation reasoning. The agent generates its response from the preserved source evidence rather than from lossy memory summaries. On long-term agent-memory benchmarks, EnSIMem achieves high answer accuracy while maintaining compact contexts and favorable online efficiency. These results show that entity-structured indexing and episode-level provenance provide a reliable foundation for long-term memory in agents. The code of our model is available at https://github.com/RamonMeng/EnSIMem.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
