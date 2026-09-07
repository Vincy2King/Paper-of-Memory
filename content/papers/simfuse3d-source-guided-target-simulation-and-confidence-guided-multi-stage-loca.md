# SimFuse3D: Source-Guided Target Simulation and Confidence-Guided Multi-Stage Localization Reweighting for Cross-Platform 3D Object Detection

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.04886v1
- Published: 2026-09-04
- Updated: 2026-09-04
- Authors: Yongchun Lin, Xinliang Zhang, Yun Zou, Zhixuan Xiao, Liang Lei, Jianya Guo, Yuqiang Zhai, Xiaofeng Wang, HaiKuo Xu, Haoang Li
- Tags: memory
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2609.04886v1

## One-Sentence Summary
Changes in sensor height and viewpoint alter object-level point distributions, making cross-platform LiDAR unsupervised domain adaptation (UDA) difficult.

## Introduction
这篇论文被纳入仓库，是因为它和 `memory research` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Changes in sensor height and viewpoint alter object-level point distributions, making cross-platform LiDAR unsupervised domain adaptation (UDA) difficult.

进一步看，论文的核心做法或实验重点可以概括为：Self-training uses labeled source scans and unlabeled target scans, yet a retained prediction may provide a useful target location while enclosing sparse foreground returns, background clutter, or points inconsistent...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Changes in sensor height and viewpoint alter object-level point distributions, making cross-platform LiDAR unsupervised domain adaptation (UDA) difficult. Self-training uses labeled source scans and unlabeled target scans, yet a retained prediction may provide a useful target location while enclosing sparse foreground returns, background clutter, or points inconsistent with the predicted box. We refer to this mismatch as box-point inconsistency. We introduce SimFuse3D, which preserves the target placement and repairs the associated pseudo-object using measured geometry from labeled source scans. Object Memory retrieves a compatible labeled source instance. Target Simulation places its ground-truth box at the target location, aligns its points with the target viewing geometry, and filters the aligned crop to approximate the target observation. Confidence-Guided Multi-Stage Localization Reweighting (CMLR) maps each target pseudo-object confidence score to a bounded weight shared by RPN localization and R-CNN box regression. All components operate only during adaptation, leaving the detector architecture and inference graph unchanged. Across six cross-platform transfers, SimFuse3D exceeds Pi3DET-Net on every reported AP metric and ranks first among the compared adaptation methods on nearly all metrics. On nuScenes-to-KITTI, it ranks first among the compared adaptation methods with both evaluated detectors.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
