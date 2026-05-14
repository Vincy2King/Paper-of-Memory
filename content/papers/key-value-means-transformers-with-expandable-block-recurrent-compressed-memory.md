# Key-Value Means: Transformers with Expandable Block-Recurrent Compressed Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.09877v2
- Published: 2026-05-11
- Updated: 2026-05-13
- Authors: Daniel Goldstein, Eugene Cheah
- Tags: context
- Categories: cs.LG, cs.AI, cs.CL
- URL: http://arxiv.org/abs/2605.09877v2

## One-Sentence Summary
We present Key-Value Means ("KVM"), a novel block-recurrence for attention that can accommodate either fixed-size or growing state.

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We present Key-Value Means ("KVM"), a novel block-recurrence for attention that can accommodate either fixed-size or growing state.

进一步看，论文的核心做法或实验重点可以概括为：Equipping a strong transformer baseline with fixed-size KVM attention layers yields a strong $O(N)$ chunked RNN, while adding only an insignificant number of new parameters.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：context memory
- 来源分类信息：cs.LG, cs.AI, cs.CL

## Abstract Snapshot
We present Key-Value Means ("KVM"), a novel block-recurrence for attention that can accommodate either fixed-size or growing state. Equipping a strong transformer baseline with fixed-size KVM attention layers yields a strong $O(N)$ chunked RNN, while adding only an insignificant number of new parameters. We train a transformer with a growable KVM cache and show it performs competitively on long-context tests with only subquadratic prefill time and sublinear state growth. KVM is implementable with standard operations and without custom kernels, and supports chunk-wise parallelizable training and prefill. It provides many of the benefits of both traditional transformers (expandable context memory, chunk-wise parallelizable training and prefill) and linear RNNs in a single unified package. It can be used on every layer, saving KV-cache memory, and allowing a continuous range of choices of prefill time complexity between $O(N)$ and $O(N^2)$. It can also be implemented in a hybrid solution in tandem with LRNN layers in place of traditional attention, to supplement the LRNN with improved sublinear memory growth context length usage and long context decoding. We release our code at https://github.com/recursal/KVM-paper and trained models at https://huggingface.co/collections/recursal/key-value-means under the Apache 2.0 license.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
