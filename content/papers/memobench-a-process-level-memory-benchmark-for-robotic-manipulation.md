# MEMOBench: A Process Level Memory Benchmark for Robotic Manipulation

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.07047v1
- Published: 2026-09-07
- Updated: 2026-09-07
- Authors: Haiyang Sun, Haoxiao Wang, Junming Chen, Weicheng Fang, Zihao Su, Jingkun Yi, Wenyou Yi, Hao Chen, Zhou Zhao
- Tags: benchmark, compression
- Categories: cs.RO, cs.AI
- URL: http://arxiv.org/abs/2609.07047v1

## One-Sentence Summary
Robotic manipulation often requires acting on information that is no longer visible, yet Vision-Language-Action policies are usually evaluated when the current observation...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, compression` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Robotic manipulation often requires acting on information that is no longer visible, yet Vision-Language-Action policies are usually evaluated when the current observation largely determines the next action.

进一步看，论文的核心做法或实验重点可以概括为：Existing robotic memory benchmarks expose this gap, but they still rely mainly on final task success and therefore conflate forgetting with manipulation failure.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, compression
- 检索关键词命中：memory augmented, memory benchmark, memory benchmarks, memory compression, memory-augmented
- 来源分类信息：cs.RO, cs.AI

## Abstract Snapshot
Robotic manipulation often requires acting on information that is no longer visible, yet Vision-Language-Action policies are usually evaluated when the current observation largely determines the next action. Existing robotic memory benchmarks expose this gap, but they still rely mainly on final task success and therefore conflate forgetting with manipulation failure. We present \textbf{MEMOBench}, a benchmark for process level memory evaluation in robotic manipulation. MEMOBench includes 30 history dependent tasks, 1{,}500 expert demonstrations, and 4{,}200 executable checkpoint instances from 84 templates. Each checkpoint pairs coarse to fine language with a simulator predicate and labels one memory operation: Storage, Update, or Compression. These annotations define Memory Storage Rate, Memory Update Rate, and Memory Compression Rate, which measure memory fidelity alongside task success. Across standard and memory augmented VLA policies, the strongest memory module baseline reaches only 31.9\% average success rate, and high storage often coexists with weak update and compression. Checkpoint language also supervises semantic, contrastive, and framewise memory alignment objectives, yielding modest gains across different memory operations. MEMOBench provides a diagnostic evaluation suite and training supervision for memory grounded robotic policies. The project page is available at https://github.com/Collab-Gen/MEMOBench.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
