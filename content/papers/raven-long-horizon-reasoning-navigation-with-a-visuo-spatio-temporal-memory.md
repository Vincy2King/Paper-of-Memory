# RAVEN: Long-Horizon Reasoning & Navigation with a Visuo-Spatio-Temporal Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.25206v1
- Published: 2026-06-23
- Updated: 2026-06-23
- Authors: Yixun Hu, Zhicheng Zheng, Lihan Zha, Chunwei Xing, Rajdeep Singh, Omar Hossain, Antonio Loquercio, Dhruv Shah
- Tags: agent, benchmark, long-term, retrieval
- Categories: cs.RO, cs.AI, cs.CL
- URL: http://arxiv.org/abs/2606.25206v1

## One-Sentence Summary
Long-term robot deployment requires a compact and scalable memory that preserves fine-grained visual semantics, grounds observations in space and time, and enables efficient...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term robot deployment requires a compact and scalable memory that preserves fine-grained visual semantics, grounds observations in space and time, and enables efficient storage and retrieval.

进一步看，论文的核心做法或实验重点可以概括为：In this paper, we propose RAVEN, an agentic memory system for long-horizon robotic question answering and navigation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.RO, cs.AI, cs.CL

## Abstract Snapshot
Long-term robot deployment requires a compact and scalable memory that preserves fine-grained visual semantics, grounds observations in space and time, and enables efficient storage and retrieval. In this paper, we propose RAVEN, an agentic memory system for long-horizon robotic question answering and navigation. RAVEN stores visual embeddings with pose and time in a vector database, and grounds retrieval in a spatial map to answer queries and navigate to goals. By operating directly on visual embeddings, RAVEN avoids lossy image-to-text captioning and enables accurate semantic, spatial, and temporal retrieval at scale. Across several simulated and real-world video question-answering benchmarks, RAVEN consistently surpasses caption-based memory systems and matches frontier VLMs on long-horizon tasks at 10$\times$ lower retrieval cost. Finally, we instantiate RAVEN on a Unitree Go1 robot for the task of long-horizon navigation for natural language goal-reaching, and show successful deployment over several large indoor environments.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
