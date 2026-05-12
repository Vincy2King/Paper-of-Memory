# GRC: Unifying Reasoning-Driven Generation, Retrieval and Compression

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.09100v1
- Published: 2026-05-09
- Updated: 2026-05-09
- Authors: Zhongtao Miao, Qiyu Wu, Yoshimasa Tsuruoka
- Tags: agent, benchmark, compression, context, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2605.09100v1

## One-Sentence Summary
Text embedding and generative tasks are usually trained separately based on large language models (LLMs) nowadays.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Text embedding and generative tasks are usually trained separately based on large language models (LLMs) nowadays.

进一步看，论文的核心做法或实验重点可以概括为：This causes a large amount of training cost and deployment effort.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, context, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CL

## Abstract Snapshot
Text embedding and generative tasks are usually trained separately based on large language models (LLMs) nowadays. This causes a large amount of training cost and deployment effort. Context compression is also a challenging and pressing task, which is vital to reasoning-driven generation, and agentic tasks requiring long context and continual learning. In this paper, we explore how to unify reasoning-driven generation, reasoning-enhanced text representation and context compression tasks in one forward pass for LLMs. Through meta latent tokens and a unified generative, representative and compressive tuning approach, we propose a training framework named GRC that bridges the three tasks. The trained models can accomplish three objectives in a single forward pass while maintaining modular, LEGO-style flexibility during inference. This design greatly reduces the deployment effort for retrieval-augmented generation (RAG) and achieves efficient inference and three times data utilization during training. Furthermore, this framework design enables a new paradigm for text embedding: self-reason-latent embeds, and a new generation paradigm, latent memory-augmented generation, where compressed and internalized KV cache with O(1) length is used as the updatable memory. We also propose hybrid paged attention to speed up the inference of our models. Extensive experiments on reasoning-intensive retrieval benchmarks, generative tasks, document compression, latency evaluation, and RAG settings demonstrate the effectiveness of our method and may shed light on the truly unified model that can handle reasoning-driven generation, embedding and compression tasks seamlessly.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
