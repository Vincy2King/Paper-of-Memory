# $μ$VLA: On Recurrent Memory for Partially Observable Manipulation in VLA Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.12497v1
- Published: 2026-06-10
- Updated: 2026-06-10
- Authors: Egor Cherepanov, Nikita Kachaev, Daniil Zelezetsky, Aydar Bulatov, Artem Pshenitsyn, Yuri Kuratov, Alexey Skrynnik, Aleksandr I. Panov, Alexey K. Kovalev
- Tags: compression, retrieval
- Categories: cs.LG, cs.RO
- URL: http://arxiv.org/abs/2606.12497v1

## One-Sentence Summary
Vision-language-action (VLA) models predict chunks of future actions from the current observation, an assumption that fails under partial observability, where decisions depend...

## Introduction
这篇论文被纳入仓库，是因为它和 `compression, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Vision-language-action (VLA) models predict chunks of future actions from the current observation, an assumption that fails under partial observability, where decisions depend on information no longer visible.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory-augmented VLAs simultaneously introduce recurrence, retrieval, compression modules, auxiliary objectives, hierarchical memory, or task-specific architectural changes, so the contribution of recurrence...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.LG, cs.RO

## Abstract Snapshot
Vision-language-action (VLA) models predict chunks of future actions from the current observation, an assumption that fails under partial observability, where decisions depend on information no longer visible. Existing memory-augmented VLAs simultaneously introduce recurrence, retrieval, compression modules, auxiliary objectives, hierarchical memory, or task-specific architectural changes, so the contribution of recurrence itself remains entangled with surrounding machinery. We present a controlled isolation study of recurrence in a strong pretrained VLA backbone. Our formulation augments the transformer with a small set of learnable memory tokens carried across timesteps and updated through self-attention, trained end to end with truncated backpropagation through time, with no auxiliary losses and no architectural changes. We instantiate this as $μ$VLA, a family of OpenVLA-OFT variants parameterized by memory width m, TBPTT length K, and the memory update rule (cross-step gradients or a detached EMA), so that recurrence is the only varying factor. On MIKASA-Robo, $μ$VLA improves average success rate on five training tasks from 0.42 to 0.84 at the strongest setting and reaches 0.23 on held-out tasks with the same memory structure versus 0.07 for the memoryless baseline. On tasks requiring different memory structure, performance remains near baseline. On LIBERO, the strongest recurrent variant achieves 96.2% average success, indicating no regression under full observability. We interpret these results as a calibration of the capability envelope of minimal in-backbone recurrence, identifying the regime in which it is sufficient and the regime where additional memory structure is required. Demos and videos can be found in https://avanturist322.github.io/mu-vla/.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
