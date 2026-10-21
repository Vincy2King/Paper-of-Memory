# Recast the Past: Stable Long Video Generation with Full Context Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.27986v1
- Published: 2026-10-20
- Updated: 2026-10-20
- Authors: Yukuo Ma, Cong Liu, Junke Wang, Junqi Liu, Haibin Huang, Zuxuan Wu, Xuelong Li
- Tags: context
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2610.27986v1

## One-Sentence Summary
Long-horizon video generation requires retaining an ever-expanding history, but conditioning on its growing token sequence is costly.

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon video generation requires retaining an ever-expanding history, but conditioning on its growing token sequence is costly.

进一步看，论文的核心做法或实验重点可以概括为：Existing methods restrict or compress historical context, potentially losing information needed for future generation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：context memory
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Long-horizon video generation requires retaining an ever-expanding history, but conditioning on its growing token sequence is costly. Existing methods restrict or compress historical context, potentially losing information needed for future generation. This work proposes ReCam, which groups local spatiotemporal blocks of historical latents into vectors and projects them directly into the high-dimensional hidden space of a Diffusion Transformer. The model learns to use the resulting memory tokens through native self-attention, reducing token count while retaining block-level access to the full history. To mitigate temporal drift during autoregressive rollout, we further introduce dual-pointer denoising with separate noise schedules for recent context and target frames. Among the evaluated methods, ReCam achieves the highest VBench-Long overall score of 80.1 and competitive static-scene revisitation performance on R2M-Bench. It also leads on all four consistency metrics for off-screen subject reappearance, including clothing consistency of 4.09 versus 3.03 for the best baseline.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
