# Keep It Simple: Multi-Key Episodic Memory Retrieval for Ultra-Long Video Understanding

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.07663v1
- Published: 2026-08-07
- Updated: 2026-08-07
- Authors: Yeeun Choi, Youngbeom Yoo, Joon-Young Lee, Hyolim Kang, Seon Joo Kim
- Tags: agent, benchmark, context, episodic, retrieval
- Categories: cs.CV, cs.AI, cs.CL
- URL: http://arxiv.org/abs/2608.07663v1

## One-Sentence Summary
When videos extend from hours to days, directly processing them end-to-end becomes impractical for current Multi-modal Large Language Models (MLLMs).

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：When videos extend from hours to days, directly processing them end-to-end becomes impractical for current Multi-modal Large Language Models (MLLMs).

进一步看，论文的核心做法或实验重点可以概括为：This ultra-long setting necessitates a two-stage paradigm: query-agnostic memory construction followed by retrieval-based inference.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, episodic, retrieval
- 检索关键词命中：episodic memory, memory retrieval
- 来源分类信息：cs.CV, cs.AI, cs.CL

## Abstract Snapshot
When videos extend from hours to days, directly processing them end-to-end becomes impractical for current Multi-modal Large Language Models (MLLMs). This ultra-long setting necessitates a two-stage paradigm: query-agnostic memory construction followed by retrieval-based inference. Prior work invests in complex memory construction to pre-model high-level relations in videos, despite not knowing the downstream query at build time. We instead prioritize high-recall retrievability during memory building, and defer query-specific, high-level relation composition to inference time. To this end, we propose MERIT(Multi-key Episodic Retrieval with Inference-time Temporal expansion), a simple yet effective agentic framework for ultra-long video understanding. First, we formulate an episodic multi-key representation that enables precise retrieval of fine-grained memories through a simple key-matching mechanism. Second, we introduce a neighbor filtering mechanism to capture broader semantic context without the massive computational overhead of global memory construction. This is achieved by expanding the temporal scope exclusively around the retrieved segments at inference time. By leveraging simple key-matching with this on-demand temporal expansion, MERIT achieves state-of-the-art performance across three long-video benchmarks: EgoLifeQA, LVBench, and Video-MME (Long).

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
