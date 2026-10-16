# LTM: Latent Transition Based In-Context Memory for Vision-Language-Action Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.21362v1
- Published: 2026-10-15
- Updated: 2026-10-15
- Authors: Qixin Sun, WenLong Gao, Xiansheng Chen, Zhongyuan Wang, Si Liu, Pengwei Wang
- Tags: compression, context
- Categories: cs.RO, cs.AI
- URL: http://arxiv.org/abs/2610.21362v1

## One-Sentence Summary
Robotic manipulation often requires remembering interactions that are no longer visible.

## Introduction
这篇论文被纳入仓库，是因为它和 `compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Robotic manipulation often requires remembering interactions that are no longer visible.

进一步看，论文的核心做法或实验重点可以概括为：We introduce Latent Transition Memory (LTM), which stores history as compact latent transitions between consecutive observations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression, context
- 检索关键词命中：context memory
- 来源分类信息：cs.RO, cs.AI

## Abstract Snapshot
Robotic manipulation often requires remembering interactions that are no longer visible. We introduce Latent Transition Memory (LTM), which stores history as compact latent transitions between consecutive observations. Instantiated on $π_{0.5}$ as LTM-$π$, our method uses a frozen latent action encoder, a lightweight adapter, and causal KV caching for incremental inference without memory-specific semantic annotations or external reasoning-model calls. With DreamDojo transitions, LTM-$π$ achieves 58.54% success on RoboMME and 80.5% on LIBERO-Mem, performing best among baselines without external reasoning models or memory-specific annotations. Ablations support the contribution of transition content beyond temporal cues and the efficiency of delayed memory admission. Scaling RoboMME demonstrations tenfold improves success from 57.67% to 87.50%, while a Cup Swap diagnostic highlights the role of process supervision in temporal composition. Under a 200-token memory budget, success remains 84.00%, versus 87.50% without compression. Finally, real-robot counting success improves from 11.25% to 82.50%. Together, these results demonstrate the effectiveness, scalability, and efficiency of latent transition memory, highlighting its capacity for complex temporal information, bounded-context operation, and real-world robotic control.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
