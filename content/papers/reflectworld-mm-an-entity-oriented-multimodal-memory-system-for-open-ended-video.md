# ReflectWorld-MM: An Entity-Oriented Multimodal Memory System for Open-Ended Video Streams

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.09759v2
- Published: 2026-07-06
- Updated: 2026-07-14
- Authors: Xiaokang Ma, Yifan Sun, Zhihong Jin, Jie Gu, Yudong Luo, Shenyi Shao, Chu Tang, Jingmin Chen, Li Pu
- Tags: agent, benchmark, context, episodic, long-term
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2607.09759v2

## One-Sentence Summary
Building assistants that can continually watch the world, remember what they see, and reason over their accumulated experience is a long-standing goal, and recently multimodal...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Building assistants that can continually watch the world, remember what they see, and reason over their accumulated experience is a long-standing goal, and recently multimodal agents equipped with long-term memory...

进一步看，论文的核心做法或实验重点可以概括为：Unfortunately, existing systems either keep their memory inside the model context or in a flat feature store, and organize it around frames rather than around the persistent entities a stream is really about, which...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, episodic, long-term
- 检索关键词命中：episodic memory, long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Building assistants that can continually watch the world, remember what they see, and reason over their accumulated experience is a long-standing goal, and recently multimodal agents equipped with long-term memory over video streams have attracted increasing interest. Unfortunately, existing systems either keep their memory inside the model context or in a flat feature store, and organize it around frames rather than around the persistent entities a stream is really about, which confines them to bounded videos and weakens their ability to track who and what reappears over time. In this paper, we propose ReflectWorld-MM, an entity-oriented multimodal memory system for open-ended video streams. It consists of three parts. The first is a perception front-end that turns an audiovisual stream into entity-resolved observations under a bounded short-term memory. The second is a hierarchical long-term memory, grounded in human memory theory, that couples a multi-scale episodic memory, an evolving entity-centric semantic memory, and a procedural memory. The third is a complete realization, built for real-world operation, that ingests arbitrary streams and plugs into off-the-shelf assistants. Across six long-video and lifelong-memory benchmarks, ReflectWorld-MM achieves the best accuracy on all six, outperforming strong memory agents and a frontier model.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
