# Unlimited OCR Works 2

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.39308v1
- Published: 2026-10-29
- Updated: 2026-10-29
- Authors: Shu Wei, Jingjing Wu, Qunyi Xie, Lingshu Zhang, Xiangcheng Du, Yannian Fu, Mengjie Wang, Zuyi Wang, Zhichao Liu, Yangliu Xu, YY, Yi Yang
- Tags: benchmark, context
- Categories: cs.CL, cs.CV
- URL: http://arxiv.org/abs/2610.39308v1

## One-Sentence Summary
Unlimited OCR ushers the era of long-horizon parsing, substantially mitigating the growth of working memory as document lengthens.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Unlimited OCR ushers the era of long-horizon parsing, substantially mitigating the growth of working memory as document lengthens.

进一步看，论文的核心做法或实验重点可以概括为：However, as document length scales to hundreds of pages, the visual context grows substantially, sharply increasing the computational cost of each decoding step and limiting the scalability of ultra-long document...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context
- 检索关键词命中：working memory
- 来源分类信息：cs.CL, cs.CV

## Abstract Snapshot
Unlimited OCR ushers the era of long-horizon parsing, substantially mitigating the growth of working memory as document lengthens. However, as document length scales to hundreds of pages, the visual context grows substantially, sharply increasing the computational cost of each decoding step and limiting the scalability of ultra-long document parsing. Inspired by human book transcription via localized focus without re-scanning preceding pages, we introduce Unlimited OCR 2, a document parsing model that looks only at what it transcribes. Building on Unlimited OCR, we upgrade all the decoder attention modules to Sparse Reference Sliding Window Attention (SR-SWA), bounding active reference tokens to a fixed capacity and thus sustaining constant computational costs across arbitrarily long documents. By combining SR-SWA with Unlimited-Horizon Decoding Paradigm, Unlimited OCR 2 enables document parsing over virtually unlimited lengths without prohibitive memory overhead. At the hundred-page scale, Unlimited OCR 2 achieves 7.0$\times$ and 5.6$\times$ per-step speedups over Full Attention and R-SWA, respectively. Furthermore, it delivers state-of-the-art end-to-end performance on both MPDocBench and MarathonDocBench, our newly proposed benchmark targeting hundred-page document parsing. Ultimately, the capacity for uninterrupted, one-shot document parsing signifies a fundamental paradigm shift into the OCR 3.0 era.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
