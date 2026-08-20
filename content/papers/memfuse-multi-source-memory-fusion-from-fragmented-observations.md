# MemFuse: Multi-Source Memory Fusion from Fragmented Observations

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.18704v1
- Published: 2026-08-19
- Updated: 2026-08-19
- Authors: Chao Li, Yuanfa Li, Wenhao Wu, Xule Liu, Zhi Wang, Kun Shao
- Tags: agent, benchmark, episodic, long-term, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2608.18704v1

## One-Sentence Summary
Long-term memory is essential for agents that operate across extended interactions, yet existing memory systems and benchmarks predominantly focus on single-source textual...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, episodic, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory is essential for agents that operate across extended interactions, yet existing memory systems and benchmarks predominantly focus on single-source textual histories.

进一步看，论文的核心做法或实验重点可以概括为：In realistic settings, however, relevant information is often fragmented across applications and devices, as well as across users and time, requiring agents to integrate dispersed observations into coherent episodic...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, episodic, long-term, retrieval
- 检索关键词命中：episodic memory, long-term memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Long-term memory is essential for agents that operate across extended interactions, yet existing memory systems and benchmarks predominantly focus on single-source textual histories. In realistic settings, however, relevant information is often fragmented across applications and devices, as well as across users and time, requiring agents to integrate dispersed observations into coherent episodic memories while preserving their source provenance. To address these gaps, we introduce **MemFuseBench**, a benchmark for *multi-source memory fusion*. MemFuseBench is built with a Scene-to-Sensor pipeline that synthesizes controllable scenarios into source-tagged observations, evidence-grounded questions, and adversarial distractors. It enables systematic evaluation of temporal reasoning, cross-source evidence fusion, and robustness to noise. We further propose **MemFuse**, a structured memory system that preserves source-level evidence in event-layer atomic memory and organizes related atomic events into cluster-layer fused memory within a causal fusion graph. During retrieval, MemFuse retrieves and organizes related evidence fragments while maintaining traceability to original source events. Experiments on MemFuseBench show that MemFuse achieves the best overall performance among the evaluated memory systems under all three LLM settings and consistently improves performance on questions requiring cross-source evidence fusion.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
