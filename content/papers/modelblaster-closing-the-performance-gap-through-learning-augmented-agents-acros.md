# ModelBlaster: Closing the Performance Gap through Learning-Augmented Agents Across Models, Kernels and Hardware Backends

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.04104v1
- Published: 2026-11-03
- Updated: 2026-11-03
- Authors: Shengjun Kris Dong, Dima Nikiforov, Sahil Modi, Sana Damani, Edward C Lin, Siva Kumar Sastry Hari, Christos Kozyrakis
- Tags: agent, context
- Categories: cs.LG
- URL: http://arxiv.org/abs/2611.04104v1

## One-Sentence Summary
Optimizing accelerator code across hardware architectures is difficult.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Optimizing accelerator code across hardware architectures is difficult.

进一步看，论文的核心做法或实验重点可以概括为：ML compilers search predefined spaces of schedules and micro-kernels, while LLM-guided optimization can explore alternative algorithms, operator decompositions, and hardware-specific techniques.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.LG

## Abstract Snapshot
Optimizing accelerator code across hardware architectures is difficult. ML compilers search predefined spaces of schedules and micro-kernels, while LLM-guided optimization can explore alternative algorithms, operator decompositions, and hardware-specific techniques. However, existing LLM agents typically target a single programming interface, toolchain, or accelerator family, focus on kernel-level optimization without model-level transforms, and offer limited reuse of experience across hardware targets. We present ModelBlaster, a Memory-Augmented In-Context Reinforcement Learning (MAIC-RL) framework for optimizing data-parallel kernels and whole models across heterogeneous SIMD and SIMT accelerators. Its mutable policy is a persistent knowledge base updated at inference time by Actor-Critic Textual Gradient Descent (AC-TGD). The knowledge base maps performance states to actions, outcomes, and constraints, enabling experience reuse across kernels, models, and hardware targets. A model-level optimizer uses kernel-level knowledge to inform whole-model decisions. The same optimization loop and knowledge schema support CUDA on NVIDIA GPUs, OpenCL on Qualcomm GPUs, and RVV intrinsics on RISC-V vector cores, with only lowering and measurement layers specific to each target. Compared with PyTorch, ModelBlaster achieves geometric-mean speedups of 1.85x, 5.58x, and 5.18x on KernelBench Levels 1, 2, and 3, and 1.69x on SOL-ExecBench Levels 1 and 2 on a B200 GPU. On Qualcomm Adreno GPUs, it achieves 5.8x over the vendor SDK and 1.7x over Apache TVM; on RISC-V vector cores, it achieves 2.7x over ExecuTorch with XNNPACK across 70 KernelBench problems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
