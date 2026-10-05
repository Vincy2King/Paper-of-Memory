# The Surprising Effectiveness of Shared Memory in Looped Transformers

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.02383v1
- Published: 2026-10-01
- Updated: 2026-10-01
- Authors: Giovanni Monea, Keshav Ramji, Yousef El-Kurdi, Luis A. Lastras, Yoav Artzi, Nathan Godey, Ramón Fernandez Astudillo
- Tags: context
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2610.02383v1

## One-Sentence Summary
Looped Transformers apply the same layers several times per token, adding compute to improve quality without more parameters.

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Looped Transformers apply the same layers several times per token, adding compute to improve quality without more parameters.

进一步看，论文的核心做法或实验重点可以概括为：Each recursion, however, writes its own key-value cache, so memory still grows with compute.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：context memory
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Looped Transformers apply the same layers several times per token, adding compute to improve quality without more parameters. Each recursion, however, writes its own key-value cache, so memory still grows with compute. Inference-time techniques can shrink this cache at a cost in quality. We pretrain looped language models to share memory: only the first recursion writes a cache, and later recursions read it while keeping a short window of their own. Surprisingly, we find that sharing memory does not cost quality and instead improves it. At 150M-1B parameters, our Looped Prediction Transformer (LPT) and its hybrid variant set a new quality-memory frontier for looped models: with five recursions, the hybrid lowers validation perplexity on FineWeb-Edu by 1.12-1.82 relative to a same-size standard Transformer while using 76-79% less context memory. Through an extensive analysis, we investigate why memory sharing helps. Shared and local memory develop different representations, and later recursions attend mostly to the shared memory, which also acts as a gradient highway to the first recursion.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
