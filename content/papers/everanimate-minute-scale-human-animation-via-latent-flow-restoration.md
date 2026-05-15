# EverAnimate: Minute-Scale Human Animation via Latent Flow Restoration

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.15042v1
- Published: 2026-05-14
- Updated: 2026-05-14
- Authors: Wuyang Li, Yang Gao, Mariam Hassan, Lan Feng, Wentao Pan, Po-Chien Luan, Alexandre Alahi
- Tags: context
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2605.15042v1

## One-Sentence Summary
We propose EverAnimate, an efficient post-training method for long-horizon animated video generation that preserves visual quality and character identity.

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We propose EverAnimate, an efficient post-training method for long-horizon animated video generation that preserves visual quality and character identity.

进一步看，论文的核心做法或实验重点可以概括为：Long-form animation remains challenging because highly dynamic human motion must be synthesized against relatively static environments, making chunk-based generation prone to accumulated drift: (i) low-level quality...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：context memory
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
We propose EverAnimate, an efficient post-training method for long-horizon animated video generation that preserves visual quality and character identity. Long-form animation remains challenging because highly dynamic human motion must be synthesized against relatively static environments, making chunk-based generation prone to accumulated drift: (i) low-level quality drift, such as progressive degradation of static backgrounds, and (ii) high-level semantic drift, such as inconsistent character identity and view-dependent attributes. To address this issue, EverAnimate restores drifted flow trajectories by anchoring generation to a persistent latent context memory, consisting of two complementary mechanisms. (i) Persistent Latent Propagation maintains a context memory across chunks to propagate identity and motion in latent space while mitigating temporal forgetting. (ii) Restorative Flow Matching introduces an implicit restoration objective during sampling through velocity adjustment, improving within-chunk fidelity. With only lightweight LoRA tuning, EverAnimate outperforms state-of-the-art long-animation methods in both short- and long-horizon settings: at 10 seconds, it improves PSNR/SSIM by 8%/7% and reduces LPIPS/FID by 22%/11%; at 90 seconds, the gains increase to 15%/15% and 32%/27%, respectively.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
