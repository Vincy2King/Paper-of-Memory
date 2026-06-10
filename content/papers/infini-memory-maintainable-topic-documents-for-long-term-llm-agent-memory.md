# Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.10677v1
- Published: 2026-06-09
- Updated: 2026-06-09
- Authors: Suozhao Ji, Baodong Wu, Zehao Wang, Lei Xia, Qingping Li, Ruisong Wang, Wenbo Ding, Zhenhua Zhu, Boxun Li, Guohao Dai, Yu Wang
- Tags: agent, context, long-term, retrieval
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2606.10677v1

## One-Sentence Summary
Long-term LLM agents need persistent memory that can track changing facts and provide relevant evidence across sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term LLM agents need persistent memory that can track changing facts and provide relevant evidence across sessions.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory systems often store observations as isolated records, summaries, or indexed fragments, which makes evidence aggregation, fact revision, and memory maintenance difficult.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory, persistent memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Long-term LLM agents need persistent memory that can track changing facts and provide relevant evidence across sessions. Existing memory systems often store observations as isolated records, summaries, or indexed fragments, which makes evidence aggregation, fact revision, and memory maintenance difficult. We propose Infini Memory, a maintainable text-based persistent memory architecture that treats agent memory as topic-structured documents. Each topic document serves as a semantic unit for collecting related evidence, preserving metadata, and revising facts over time. New observations are first staged in a buffer and periodically consolidated into coherent textual contexts. At inference time, an agentic retrieval procedure lets the LLM read memory through iterative tool calls rather than a single retrieval step. On MemoryAgentBench, Infini Memory achieves 64.7% overall score. Ablations show that topic-structured maintenance and iterative evidence inspection improve complementary aspects of long-term memory use.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
