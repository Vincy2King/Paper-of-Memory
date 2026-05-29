# Unlocking the Working Memory of Large Language Models for Latent Reasoning

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.30343v1
- Published: 2026-05-28
- Updated: 2026-05-28
- Authors: Lukas Aichberger, Sepp Hochreiter
- Tags: benchmark
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2605.30343v1

## One-Sentence Summary
To improve the reasoning capabilities of large language models, test-time compute is typically scaled by generating intermediate tokens before the final answer.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：To improve the reasoning capabilities of large language models, test-time compute is typically scaled by generating intermediate tokens before the final answer.

进一步看，论文的核心做法或实验重点可以概括为：However, this couples reasoning to autoregressive generation and thereby conflates internal computation with external communication.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：working memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
To improve the reasoning capabilities of large language models, test-time compute is typically scaled by generating intermediate tokens before the final answer. However, this couples reasoning to autoregressive generation and thereby conflates internal computation with external communication. In contrast, human cognition can use working memory to hold and manipulate information internally without the need to externalize intermediate thoughts. Drawing on this principle, we introduce Reasoning in Memory (RiM), a latent reasoning method that replaces the autoregressive generation of reasoning steps with memory blocks. These memory blocks are fixed sequences of special tokens that unlock the working-memory capacity of large language models. Since they are fixed rather than generated, they can be processed in a single forward pass, enabling compute-efficient latent reasoning. To operationalize these memory blocks, we employ a two-stage curriculum. First, we ground them by predicting explicit reasoning steps after each memory block. Second, we discard this step-level supervision and iteratively refine the final answer after each memory block. Our experiments on reasoning benchmarks show that, across language models of different families and sizes, RiM matches or exceeds existing latent reasoning methods while avoiding the autoregressive generation of thoughts. These results demonstrate that large language models can be trained to use working memory as an effective mechanism for latent reasoning.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
