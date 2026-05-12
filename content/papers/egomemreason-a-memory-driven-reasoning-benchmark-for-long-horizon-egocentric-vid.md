# EgoMemReason: A Memory-Driven Reasoning Benchmark for Long-Horizon Egocentric Video Understanding

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.09874v1
- Published: 2026-05-11
- Updated: 2026-05-11
- Authors: Ziyang Wang, Yue Zhang, Shoubin Yu, Ce Zhang, Zengqi Zhao, Jaehong Yoon, Hyunji Lee, Gedas Bertasius, Mohit Bansal
- Tags: agent, benchmark, context
- Categories: cs.CV, cs.AI, cs.CL
- URL: http://arxiv.org/abs/2605.09874v1

## One-Sentence Summary
Next-generation visual assistants, such as smart glasses, embodied agents, and always-on life-logging systems, must reason over an entire day or more of continuous visual...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Next-generation visual assistants, such as smart glasses, embodied agents, and always-on life-logging systems, must reason over an entire day or more of continuous visual experience.

进一步看，论文的核心做法或实验重点可以概括为：In ultra-long video settings, relevant information is sparsely distributed across hours or days, making memory a fundamental challenge: models must accumulate information over time, recall prior states, track temporal...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：context memory
- 来源分类信息：cs.CV, cs.AI, cs.CL

## Abstract Snapshot
Next-generation visual assistants, such as smart glasses, embodied agents, and always-on life-logging systems, must reason over an entire day or more of continuous visual experience. In ultra-long video settings, relevant information is sparsely distributed across hours or days, making memory a fundamental challenge: models must accumulate information over time, recall prior states, track temporal order, and abstract recurring patterns. However, existing week-long video benchmarks are primarily designed for perception and recognition, such as moment localization or global summarization, rather than reasoning that requires integrating evidence across multiple days. To address this gap, we introduce EgoMemReason, a comprehensive benchmark that systematically evaluates week-long egocentric video understanding through memory-driven reasoning. EgoMemReason evaluates three complementary memory types: entity memory, tracking how object states evolve and change across days; event memory, recalling and ordering activities separated by hours or days; and behavior memory, abstracting recurring patterns from sparse, repeated observations over the whole week period. EgoMemReason comprises 500 questions across three memory types and six core challenges, with an average of 5.1 video segments of evidence per question and 25.9 hours of memory backtracking. We evaluate EgoMemReason on 17 methods across MLLMs and agentic frameworks, revealing that even the best model achieves only 39.6% overall accuracy. Further analysis shows that the three memory types fail for distinct reasons and that performance degrades as evidence spans longer temporal horizons, revealing that long-horizon memory remains far from solved. We believe EgoMemReason establishes a strong foundation for evaluating and advancing long-context, memory-aware multimodal systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
