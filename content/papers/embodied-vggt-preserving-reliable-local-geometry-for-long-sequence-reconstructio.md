# Embodied-VGGT: Preserving Reliable Local Geometry for Long-Sequence Reconstruction

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.33964v1
- Published: 2026-11-25
- Updated: 2026-11-25
- Authors: Yiheng Han, Ziang Chen, Zhuyong Fu, Yiqing Yin, Nan Ma
- Tags: benchmark, context
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2611.33964v1

## One-Sentence Summary
Long sequence reconstruction must correct accumulated drift while preserving locally consistent geometry.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long sequence reconstruction must correct accumulated drift while preserving locally consistent geometry.

进一步看，论文的核心做法或实验重点可以概括为：In robotics and autonomous driving, embodied acquisition provides recurring platform- environment geometry and repeated observations of scene structure and platform motion.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context
- 检索关键词命中：context memory, memory augmented, memory-augmented
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Long sequence reconstruction must correct accumulated drift while preserving locally consistent geometry. In robotics and autonomous driving, embodied acquisition provides recurring platform- environment geometry and repeated observations of scene structure and platform motion. We present Embodied-VGGT, which exploits these cues to establish reliable local relationships and selectively preserve them during global refinement. Memory-Augmented Grounded Chunks (MAGC) builds on Scal3R's global context memory and uses relative scale references derived from predicted ground geometry to regularize test-time memory updates, encouraging cross-chunk consistency while limiting changes to reliable local geometry. Superpoint Alignment (SA) and Cross-Loop Optimization (CL) jointly address the robust establishment and preservation of geometric relationships. SA balances ground and non-ground evidence across spatial regions to estimate inter-chunk translation. CL uses geometric and motion consistency across interleaved windows to select coherent chunk groups, each receiving a shared Sim(3) correction that preserves its internal relative transformations during global optimization. Experiments on five public driving benchmarks demonstrate consistent and substantial improvements in long sequence reconstruction. On KITTI Odometry, Embodied-VGGT achieves a mean absolute trajectory error of 7.30 m and a Chamfer distance of 2.67 m, reducing these errors by 46.8% and 23.3% compared with the state-of-the-art baseline under same evaluation protocol. To facilitate reproducibility, we released our code: https://github.com/Ang-Sheep/Embodied-VGGT.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
