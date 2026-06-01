# Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.31158v1
- Published: 2026-05-29
- Updated: 2026-05-29
- Authors: Jiacheng Lu, Haoyi Zhu, Sipei Yi, Enze Xie, Yu Li, Cheng Zhuo
- Tags: context
- Categories: cs.CV, cs.LG
- URL: http://arxiv.org/abs/2605.31158v1

## One-Sentence Summary
Interactive video world models generate video chunk by chunk in response to user-controlled camera movements, enabling applications such as real-time game simulation, virtual...

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Interactive video world models generate video chunk by chunk in response to user-controlled camera movements, enabling applications such as real-time game simulation, virtual scene navigation, and embodied AI training.

进一步看，论文的核心做法或实验重点可以概括为：However, scaling to long interactive trajectories is prohibitively expensive due to growing context memory, quadratic attention complexity, and repeated denoising steps.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：context memory
- 来源分类信息：cs.CV, cs.LG

## Abstract Snapshot
Interactive video world models generate video chunk by chunk in response to user-controlled camera movements, enabling applications such as real-time game simulation, virtual scene navigation, and embodied AI training. However, scaling to long interactive trajectories is prohibitively expensive due to growing context memory, quadratic attention complexity, and repeated denoising steps. We present Light Interaction, a training-free inference acceleration framework for interactive video world models. Our key insight is that interaction naturally enables trajectory-dependent adaptive computation: retrieved spatial memory can be discarded during novel exploration, temporal context can be adjusted according to local latent dynamics, and early-step model outputs can be reused when the camera revisits familiar regions. Based on this insight, Light Interaction combines adaptive context management, denoising cache acceleration, and hardware-software co-designed 3D block sparse attention with fused Triton kernels. Evaluated on HY-WorldPlay and Matrix-Game-3.0, Light Interaction achieves up to 2.59x speedup without model retraining while maintaining competitive visual quality.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
