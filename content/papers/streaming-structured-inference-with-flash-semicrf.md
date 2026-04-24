# Streaming Structured Inference with Flash-SemiCRF

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.18780v1
- Published: 2026-04-20
- Updated: 2026-04-20
- Authors: Benjamin K. Johnson, Thomas Goralski, Ayush Semwal, Hui Shen, H. Josh Jang
- Tags: working memory
- Categories: cs.LG
- URL: http://arxiv.org/abs/2604.18780v1

## One-Sentence Summary
Semi-Markov Conditional Random Fields (semi-CRFs) assign labels to segments of a sequence rather than to individual positions, enabling exact inference over segment-level...

## Introduction
这篇论文被纳入仓库，是因为它和 `working memory` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Semi-Markov Conditional Random Fields (semi-CRFs) assign labels to segments of a sequence rather than to individual positions, enabling exact inference over segment-level features and principled uncertainty estimates...

进一步看，论文的核心做法或实验重点可以概括为：However, existing implementations must materialize a large edge potential tensor whose size grows with sequence length, maximum segment length, and label count, becoming prohibitive for speech-scale state spaces and...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：working memory
- 检索关键词命中：working memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Semi-Markov Conditional Random Fields (semi-CRFs) assign labels to segments of a sequence rather than to individual positions, enabling exact inference over segment-level features and principled uncertainty estimates at their boundaries. However, existing implementations must materialize a large edge potential tensor whose size grows with sequence length, maximum segment length, and label count, becoming prohibitive for speech-scale state spaces and intractable at genomic scales where sequences can exceed 100,000 positions. This memory bottleneck has limited the adoption of exact segment-level inference for long sequences and large label sets. We identify that the core inefficiency is materializing edge potentials that can instead be evaluated on-the-fly from a compact prefix-sum array, and make several improvements. First, replacing the stored edge tensor with prefix-sum lookup reduces the memory footprint by a factor proportional to the product of segment length and label count. Second, a streaming forward-backward pass with checkpoint-boundary normalization keeps working memory sublinear in sequence length while preserving exact gradients. Third, zero-centered cumulative scores control numerical drift and induce an adaptive duration prior under label imbalance. We integrate these ideas into Flash-SemiCRF, a fused Triton kernel that enables exact semi-CRF inference on previously intractable problem sizes. Available at https://github.com/biobenkj/flash-semicrf.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
