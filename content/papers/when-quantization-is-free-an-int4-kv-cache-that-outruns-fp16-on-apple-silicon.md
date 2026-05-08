# When Quantization Is Free: An int4 KV Cache That Outruns fp16 on Apple Silicon

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.05699v1
- Published: 2026-05-07
- Updated: 2026-05-07
- Authors: Mohamed Amine Bergach
- Tags: compression, context
- Categories: cs.PF, cs.AI
- URL: http://arxiv.org/abs/2605.05699v1

## One-Sentence Summary
KV-cache quantization is framed as a quality--latency trade-off.

## Introduction
这篇论文被纳入仓库，是因为它和 `compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：KV-cache quantization is framed as a quality--latency trade-off.

进一步看，论文的核心做法或实验重点可以概括为：We show it is \emph{inverted} on Apple Silicon's unified memory: a single fused Metal kernel (sign-randomized FFT $+$ per-channel $λ$ $+$ per-group abs-max $+$ int4 nibble pack), exposed as a HuggingFace...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression, context
- 检索关键词命中：memory compression, persistent memory
- 来源分类信息：cs.PF, cs.AI

## Abstract Snapshot
KV-cache quantization is framed as a quality--latency trade-off. We show it is \emph{inverted} on Apple Silicon's unified memory: a single fused Metal kernel (sign-randomized FFT $+$ per-channel $λ$ $+$ per-group abs-max $+$ int4 nibble pack), exposed as a HuggingFace \texttt{Cache} subclass, runs \emph{faster than fp16} across $256$--$4096$-token prefixes on Gemma-3 1B ($-3$ to $-8\%$ ms/tok) and at short context on Qwen2.5-1.5B ($-0.7$ to $-2.6\%$ through $1$K), with $3\times$ persistent memory compression and quality preserved ($\dPPL = 0.000$ Qwen short-prompt; $+3.6$ hook $\dPPL$ Gemma). The kernel's $\sim\!25$\,ns/vec overhead is below the bandwidth savings from $3\times$ compression. The fused kernel also closes Qwen's 4-bit per-token catastrophe ($\dPPL = +7975 \to +638.6$, $12.5\times$ reduction) at $182$\,GFLOPS / $D{=}128$. Supporting findings: $\SRFT$ and $\SRHT$ are statistically indistinguishable for KV quality (we pick $\SRFT$ for mixed-radix and matrix-multiply alignment); a learned-rotation ablation surfaces a regularization role for the fixed random SRFT base (learning $R+λ$ without SRFT lowers calibration MSE $84.9\%$ vs $50.3\%$ but yields worse PPL); Householder rotations at $k{=}d/2$ reflectors are effectively lossless at $d{=}256$.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
