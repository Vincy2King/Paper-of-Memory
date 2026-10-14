# MemoryVLN: From Ego-Aware Memory Representation to Cross-Context Memory Reuse in Vision-Language Navigation

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.18478v1
- Published: 2026-10-13
- Updated: 2026-10-13
- Authors: Xueyao Wei, Yifei Wang, Delun Li, Shaoan Wang, Junzhi Yu, Wenjie Song, Xingyu Chen
- Tags: agent, compression, context
- Categories: cs.RO, cs.AI
- URL: http://arxiv.org/abs/2610.18478v1

## One-Sentence Summary
Large vision-language models (LVLMs) have shown strong potential for embodied vision-language navigation (VLN), yet their performance degrades on long-horizon trajectories due...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large vision-language models (LVLMs) have shown strong potential for embodied vision-language navigation (VLN), yet their performance degrades on long-horizon trajectories due to context-length limits, redundant...

进一步看，论文的核心做法或实验重点可以概括为：These issues make it difficult to both compress long navigation histories and reliably reuse past spatial experience.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression, context
- 检索关键词命中：context memory
- 来源分类信息：cs.RO, cs.AI

## Abstract Snapshot
Large vision-language models (LVLMs) have shown strong potential for embodied vision-language navigation (VLN), yet their performance degrades on long-horizon trajectories due to context-length limits, redundant historical observations, and unstable spatial alignment across time. These issues make it difficult to both compress long navigation histories and reliably reuse past spatial experience. To address these limitations, we propose \textbf{MemoryVLN}, a unified memory-driven navigation system built around memory construction and management. During memory construction, \emph{Long Sequence Compression} employs forgetting-curve-inspired temporal sampling to preserve dense recent evidence and sparse yet representative distant observations under a limited token budget. \emph{Ego-Aware Memory Representation} further integrates 2D semantic tokens, 3D geometric tokens, and 6D agent poses, allowing each memory to encode both what was observed and where it was observed. During memory management, \emph{Hierarchical Memory Bank} maintains in-episode and context-level memories through cross-context warm-start and confidence-controlled write-back. \emph{Memory Enhancement} then retrieves the Top-$K$ relevant memories according to the current navigation state and fuses them with the current visual tokens. Together, these mechanisms transform raw navigation history into compact, spatially grounded, selectively retrievable, and reusable navigation experience. Extensive experiments on R2R-CE and RxR-CE demonstrate consistent improvements over the state-of-the-art baselines by a substantial margin (i.e., 2\% and 6.5\% in successful rate).

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
