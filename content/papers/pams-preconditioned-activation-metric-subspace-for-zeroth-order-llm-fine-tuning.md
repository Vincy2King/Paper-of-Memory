# PAMS: Preconditioned Activation-Metric Subspace for Zeroth-Order LLM Fine-tuning

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.28476v1
- Published: 2026-11-21
- Updated: 2026-11-21
- Authors: Pradeep Kumar Ragu Chanthar, Saksham Sahai Srivastava, Jaewoo Lee
- Tags: persistent memory
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2611.28476v1

## One-Sentence Summary
Zeroth-order (ZO) optimization provides a computationally efficient approach to fine-tuning large language models (LLMs), but conventional methods typically rely on isotropic...

## Introduction
这篇论文被纳入仓库，是因为它和 `persistent memory` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Zeroth-order (ZO) optimization provides a computationally efficient approach to fine-tuning large language models (LLMs), but conventional methods typically rely on isotropic perturbations that ignore the anisotropic...

进一步看，论文的核心做法或实验重点可以概括为：We introduce Preconditioned Activation-Metric Subspace (PAMS), a ZO optimization framework that uses forward-pass activation statistics to construct structured, layer-wise perturbation geometries without computing...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：persistent memory
- 检索关键词命中：persistent memory
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Zeroth-order (ZO) optimization provides a computationally efficient approach to fine-tuning large language models (LLMs), but conventional methods typically rely on isotropic perturbations that ignore the anisotropic structure of neural-network parameter spaces. We introduce Preconditioned Activation-Metric Subspace (PAMS), a ZO optimization framework that uses forward-pass activation statistics to construct structured, layer-wise perturbation geometries without computing gradients or forming dense curvature matrices. PAMS tracks a low-rank approximation of the dominant activation subspace and its associated spectrum online, and uses the spectrum to softly reweight perturbation variance while preserving exploration in directions outside the retained subspace. A trace normalization separates the perturbation geometry from its overall scale, enabling consistent perturbation magnitudes across layers. We show theoretically that the resulting perturbation covariance induces right-side preconditioning of the gradient of the corresponding Gaussian-smoothed objective. We further characterize the estimator's smoothing bias and second moment and derive a nonconvex convergence guarantee that captures the effects of the perturbation geometry and smoothing radius. The proposed low-rank tracking procedure requires $\mathcal{O}(n_l r)$ persistent memory for a layer with input dimension nl and retained rank r, avoiding the $\mathcal{O}(n_l^2)$ memory required by a dense activation covariance. Experiments on transformer-based language-model fine-tuning tasks across GLUE and SuperGLUE demonstrate that PAMS improves the effectiveness and stability of zeroth-order optimization while retaining its gradient-free and objective-evaluation-based advantages.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
