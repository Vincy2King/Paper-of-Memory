# SkillMemo: Expert-guided Skill Memory Framework for Compositional Embodied Manipulation

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.05970v1
- Published: 2026-08-06
- Updated: 2026-08-06
- Authors: Changyuan Wang, Chubin Zhang, Zhenyu Wu, Runhao Li, Angyuan Ma, Ke Chao, Yinan Liang, Xiuwei Xu, Ziwei Wang, Yansong Tang, Jiwen Lu
- Tags: benchmark, context, episodic
- Categories: cs.RO, cs.AI
- URL: http://arxiv.org/abs/2608.05970v1

## One-Sentence Summary
Embodied visuomotor models, including Diffusion Policy (DP) and Vision-Language-Action (VLA) models, have demonstrated promising performance on robotic manipulation benchmarks.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Embodied visuomotor models, including Diffusion Policy (DP) and Vision-Language-Action (VLA) models, have demonstrated promising performance on robotic manipulation benchmarks.

进一步看，论文的核心做法或实验重点可以概括为：However, their potential remains fundamentally constrained by the scarcity of large-scale embodied trajectory datasets, leading to insufficient compositional generalization in out-of-distribution (OOD) scenarios with...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.RO, cs.AI

## Abstract Snapshot
Embodied visuomotor models, including Diffusion Policy (DP) and Vision-Language-Action (VLA) models, have demonstrated promising performance on robotic manipulation benchmarks. However, their potential remains fundamentally constrained by the scarcity of large-scale embodied trajectory datasets, leading to insufficient compositional generalization in out-of-distribution (OOD) scenarios with limited capability to capture reusable skill structures. To address this limitation, we propose Skill-Based Memory (SkillMemo) framework that implicitly decomposes long-horizon demonstrations into latent atomic skills and integrates skill-level features into a dynamic episodic memory bank for solving compositional tasks. Specifically, we first introduce an expert-guided trajectory segmentation module built upon a Mixture-of-Experts (MoE) architecture, which implicitly partitions trajectories into distinct skill primitives represented by learned gating coefficients. We further design a skill-level episodic memory architecture that stores compact skill representations as retrievable key-value pairs. During inference, the memory bank retrieves the most relevant skill primitives which are subsequently fused with the model's current gating distribution, providing a robust contextual prior to refine action predictions. Extensive experiments on the simulation benchmark and real-world manipulation tasks demonstrate that SkillMemo consistently enhances both DP and VLA backbones, achieving state-of-the-art performance and outperforming $π_{0.5}$, while exhibiting strong compositional generalization to unseen task configurations.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
