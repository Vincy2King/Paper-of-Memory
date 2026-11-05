# RECAP: Context-Aware Prediction Recycling with Request-Local and Persistent Memories for Multimodal Speculative Decoding

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.05894v1
- Published: 2026-11-04
- Updated: 2026-11-04
- Authors: Hengjie Zhu, Dayan Wu, Xinze Liu, Peng Fu, Zheng Lin, Weiping Wang
- Tags: benchmark, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.05894v1

## One-Sentence Summary
Recycling a target model's own predictions offers a training-free source of proposals for speculative decoding.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recycling a target model's own predictions offers a training-free source of proposals for speculative decoding.

进一步看，论文的核心做法或实验重点可以概括为：In vision-language models, however, existing recycling indexes predictions by the last token alone, conflating predictions computed under different images and prefixes; we find that such reuse fails most often at...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Recycling a target model's own predictions offers a training-free source of proposals for speculative decoding. In vision-language models, however, existing recycling indexes predictions by the last token alone, conflating predictions computed under different images and prefixes; we find that such reuse fails most often at image-sensitive decoding states. Longer keys reduce this aliasing but match fewer states. We introduce \method, which stores target predictions under one-, two-, and three-token keys: contextual memories live only for the current request and are thus implicitly conditioned on its image, while token-level memory persists across requests to retain coverage. At each lookup, entropy-confidence weighting fuses the retrieved predictions according to their key specificity and concentration. Best-first search composes the fused transitions into a candidate tree, supplemented by suffix-matched continuations, and one target pass verifies the tree under greedy decoding. Without training or an auxiliary draft model, \method\ achieves mean speedups over autoregressive decoding of $1.66\speed$ and $1.56\speed$ across seven single-turn benchmarks on Qwen2.5-VL-7B and LLaVA-1.6-7B, exceeding the strongest training-free baseline, Token Recycling ($1.51\speed$ and $1.37\speed$). Our implementation is available in https://github.com/Senmo996/RECAP-official-code.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
