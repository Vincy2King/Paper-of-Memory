# Memory Augmentation Unlocks Efficient Chain-of-Thought Reasoning

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.21265v1
- Published: 2026-08-21
- Updated: 2026-08-21
- Authors: Simeng Zhang, Yilong Chen, Wenyuan Zhang, Zhenyu Zhang, Yao Chen, Junyuan Shang, Tingwen Liu
- Tags: compression, context
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.21265v1

## One-Sentence Summary
Large language models often rely on Chain-of-Thought (CoT) reasoning to solve complex tasks, but verbose reasoning traces introduce substantial inference overhead.

## Introduction
这篇论文被纳入仓库，是因为它和 `compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models often rely on Chain-of-Thought (CoT) reasoning to solve complex tasks, but verbose reasoning traces introduce substantial inference overhead.

进一步看，论文的核心做法或实验重点可以概括为：CoT compression shortens generation, yet aggressive compression may disrupt logical coherence and degrade performance.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression, context
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CL

## Abstract Snapshot
Large language models often rely on Chain-of-Thought (CoT) reasoning to solve complex tasks, but verbose reasoning traces introduce substantial inference overhead. CoT compression shortens generation, yet aggressive compression may disrupt logical coherence and degrade performance. We formalize this trade-off as the \textit{Context-Generation Substitution Law}, where explicit reasoning context substitutes for part of decode-time generation. Based on this principle, we propose \textit{Memory-Augmented Compression}, a training-free framework that constructs reusable reasoning memories from historical traces and retrieves them as prefill-side scaffolds. Rather than using raw demonstrations, these memories summarize reusable reasoning patterns, key constraints, and critical operations to compensate for information lost during compression. Experiments show that Memory consistently improves prompt-based Chain-of-Draft (CoD) compression across mathematical reasoning, complex reasoning, and science question answering tasks, yielding accuracy gains of 21.4, 28.0, 29.5, and 6.61 points over CoD on GSM8K, MATH, BBH, and MMLU-Sci, while achieving a 1.14--1.49$\times$ latency speedup over standard CoT. Memory is also compatible with token-level, reasoning-trace-level, and inference-state compression mechanisms. Further analyzes show that the gains come from relevant reasoning memories rather than simply increasing context length.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
