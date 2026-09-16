# LifeFuse-Mem: Lifecycle-Aware State Fusion Against Temporary Overwriting for Long-Term Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.12436v1
- Published: 2026-09-11
- Updated: 2026-09-11
- Authors: Hanyu Zhao, Yuqian Feng, Zhenyu Song, Yuanchao Cheng, Yance Jiao, Tengfei Pan, Li Du
- Tags: agent, benchmark, context, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.12436v1

## One-Sentence Summary
Long-running LLM agents require memory mechanisms that maintain coherent internal states across interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-running LLM agents require memory mechanisms that maintain coherent internal states across interactions.

进一步看，论文的核心做法或实验重点可以概括为：We study a lifecycle-labeled memory setting in which write episodes provide lifecycle metadata during training, and phase-aware readout is used during evaluation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term
- 检索关键词命中：long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-running LLM agents require memory mechanisms that maintain coherent internal states across interactions. We study a lifecycle-labeled memory setting in which write episodes provide lifecycle metadata during training, and phase-aware readout is used during evaluation. This setting reflects the need to distinguish information that should remain influential across future interactions from information that should affect only the current context. A mismatch between these lifecycles can cause temporary information to overwrite durable knowledge, leading to behavioral drift in persistent agents. Within this setting, we introduce \textbf{LifeFuse-Mem}, a lifecycle-aware neural memory framework that separates information according to its temporal commitment. LifeFuse-Mem uses dedicated memory components and lifecycle-aware updates to allow stable and transient knowledge to evolve locally without converting temporary context into durable state. On the controlled anti-overwrite benchmark, LifeFuse-Mem improves acquisition-controlled retention and reduces temporary overwrite; on two public long-memory benchmarks, it remains broadly competitive. These results suggest that explicit lifecycle signals can help diagnose and mitigate overwrite in compact online memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
