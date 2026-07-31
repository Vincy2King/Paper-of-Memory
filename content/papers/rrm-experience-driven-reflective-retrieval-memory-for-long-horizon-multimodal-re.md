# RRM: Experience-Driven Reflective Retrieval Memory for Long-Horizon Multimodal Reasoning

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.28156v1
- Published: 2026-07-30
- Updated: 2026-07-30
- Authors: Jingxiang Fan, Junbao Zhuo, Bochao Zou
- Tags: agent, context, episodic, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2607.28156v1

## One-Sentence Summary
Existing multimodal long-term memory agents use external memory to overcome the limited context available for long videos.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, episodic, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Existing multimodal long-term memory agents use external memory to overcome the limited context available for long videos.

进一步看，论文的核心做法或实验重点可以概括为：However, most methods emphasize what to store rather than how stored memory should be retrieved.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, episodic, long-term, retrieval
- 检索关键词命中：long-term memory, retrieval memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Existing multimodal long-term memory agents use external memory to overcome the limited context available for long videos. However, most methods emphasize what to store rather than how stored memory should be retrieved. When retrieval becomes inaccurate or repeatedly fails to obtain useful evidence, existing agents lack mechanisms to diagnose failures from previous task trajectories and adapt future search strategies.We introduce Reflective Retrieval Memory (RRM), a reflective memory framework for long-horizon multimodal reasoning. RRM augments an entity-centric multimodal memory graph with reflective experience memory, which distills transferable procedural retrieval knowledge from historical task trajectories. Unlike episodic and semantic memories that preserve factual evidence from the current video, reflective experience memory captures reusable search strategies across tasks. RRM converts retrieved experiences into query-level guidance, while answer generation remains conditioned only on factual evidence newly retrieved from the current video. A lifecycle management mechanism further regulates experience memory through usage frequency, reuse feedback, and temporal decay, thereby reducing redundancy and noise. RRM consistently outperforms previous state-of-the-art approaches on M3-Bench-Robot, M3-Bench-Web, and Video-MME-Long, demonstrating the effectiveness of reflective retrieval memory for long-horizon multimodal reasoning.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
