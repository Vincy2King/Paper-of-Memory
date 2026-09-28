# Compressing Long Context into Answer-Aligned Memory Embeddings for LLM Inference

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.25537v1
- Published: 2026-09-22
- Updated: 2026-09-22
- Authors: Md Mostafizer Rahman, Md Faizul Ibne Amin, Md Shahajada Mia, Yutaka Watanobe, Fang Liu
- Tags: benchmark, compression, context
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2609.25537v1

## One-Sentence Summary
Large language model (LLM) inference is constrained by the quadratic scaling of self-attention and the linear scaling of the KV cache, increasing latency, energy consumption,...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) inference is constrained by the quadratic scaling of self-attention and the linear scaling of the KV cache, increasing latency, energy consumption, and GPU memory demand as context length...

进一步看，论文的核心做法或实验重点可以概括为：Existing soft-compression methods either lack query-guided memory selection at inference time, train without answer-targeted supervision, or couple compression tightly to a specific decoder architecture.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, compression, context
- 检索关键词命中：context memory, memory compression
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Large language model (LLM) inference is constrained by the quadratic scaling of self-attention and the linear scaling of the KV cache, increasing latency, energy consumption, and GPU memory demand as context length scales. Existing soft-compression methods either lack query-guided memory selection at inference time, train without answer-targeted supervision, or couple compression tightly to a specific decoder architecture. We propose a Context-to-Answer-Aligned Memory Compression (CMC) framework, which compresses long input contexts into compact Context Memory Embeddings (CMEs) aligned to any frozen decoder's embedding space, reducing inference costs without modifying decoder weights. CMC introduces a two-tier KV cache that combines question-guided CME selection with a local context window, and trains the compressor with answer-targeted distillation from a frozen LLM. Experiments across nine encoder-decoder combinations and four QA benchmarks show that CMC consistently outperforms the baseline, achieving up to 7.3 EM and 4.0 F1 point gains on SQuAD, while reducing inference time and energy consumption by up to 20% and peak reserved GPU memory by up to 50% at 3,000 generation tokens. Ablation studies confirm that each architectural component and training objective contributes to the performance.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
