# MemPose: Category-level Object Pose Estimation with Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.04930v1
- Published: 2026-07-06
- Updated: 2026-07-06
- Authors: Xiao Lin, Minghao Zhu, Yun Peng, Liuyi Wang, Qiyi Wang, Chengju Liu, Qijun Chen
- Tags: benchmark
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2607.04930v1

## One-Sentence Summary
In the pursuit of robust and generalizable category-level object pose estimation, most existing methods adopt parametric formulations that learn effective representations from...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：In the pursuit of robust and generalizable category-level object pose estimation, most existing methods adopt parametric formulations that learn effective representations from data, yet they primarily encode category-...

进一步看，论文的核心做法或实验重点可以概括为：In this paper, we rethink category-level pose estimation from a memory-centric perspective and present MemPose, a memory-augmented framework that explicitly incorporates category-level geometric memory into the pose...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
In the pursuit of robust and generalizable category-level object pose estimation, most existing methods adopt parametric formulations that learn effective representations from data, yet they primarily encode category-level patterns into fixed shape priors or static parameter weights, which limits their scalability to highly diverse instances. In this paper, we rethink category-level pose estimation from a memory-centric perspective and present MemPose, a memory-augmented framework that explicitly incorporates category-level geometric memory into the pose estimation pipeline. We introduce an external memory buffer that stores and dynamically updates structural representations from previously observed instances, enabling the model to leverage accumulated experience to support current perception. Extensive experiments on four challenging benchmarks (REAL275, CAMERA25, Housecat6D and Wild6D) demonstrate the superiority of our proposed method over previous state-of-the-art approaches.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
