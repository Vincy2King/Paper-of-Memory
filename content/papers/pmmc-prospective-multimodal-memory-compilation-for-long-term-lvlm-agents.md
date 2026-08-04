# PMMC: Prospective Multimodal Memory Compilation for Long-Term LVLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.00962v1
- Published: 2026-08-02
- Updated: 2026-08-02
- Authors: Jingyu Sun, Yan Lin, Yuyang Xue, Yifan Wang, Zhengtao Yao, Rui Qian, Zefeng Xu, Jiachen Li, Xianyang Liu, Jiancheng Pan, Jingyuan Sun, Syed Murtuza Baker, Hongpeng Zhou
- Tags: agent, benchmark, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.00962v1

## One-Sentence Summary
Long-term memory is essential for LVLM agents to maintain consistency and integrate information across extended multimodal interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory is essential for LVLM agents to maintain consistency and integrate information across extended multimodal interactions.

进一步看，论文的核心做法或实验重点可以概括为：Existing agent memory systems, however, often reduce visual experiences into textual summaries or rely on static retrieve-then-reason pipelines, which are inefficient at query time and brittle when questions require...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory, memory benchmark, memory benchmarks, memory reasoning
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term memory is essential for LVLM agents to maintain consistency and integrate information across extended multimodal interactions. Existing agent memory systems, however, often reduce visual experiences into textual summaries or rely on static retrieve-then-reason pipelines, which are inefficient at query time and brittle when questions require image-text binding, temporal updates, or visual details. We propose Prospective Multimodal Memory Compilation, a framework that shifts part of the memory reasoning process from query time to memory consolidation time. Given accumulated multimodal interactions, a Questioner predicts future question candidates, a Planner compiles question-conditioned multimodal memory programs, and a Doubter verifies whether the planned evidence path can support the predicted answer. The verified question-program pairs form a structured question bank for efficient query-time routing and evidence retrieval. Experiments on multimodal long-term memory benchmarks show that our method improves answer quality and visual evidence recall while reducing query-time token and latency costs. Extensive ablations analyze the effects of self-feedback, dynamic planning, raw-image access, and question bank coverage.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
