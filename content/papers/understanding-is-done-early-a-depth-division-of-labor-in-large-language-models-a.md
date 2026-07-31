# Understanding Is Done Early: A Depth Division of Labor in Large Language Models and Its Use for Unbounded-Context Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.28263v1
- Published: 2026-07-30
- Updated: 2026-07-30
- Authors: Hanzuo Liu, Xuan Qi, Chunyu Liu, Haotian Zhong, Yulong Wang, Rayying, Key, Alex Lamb, Mingyu Gao
- Tags: compression, context, conversation, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2607.28263v1

## One-Sentence Summary
Transformer depth is not used uniformly: lower and middle layers build semantic representations, while upper layers increasingly specialize them for prediction.

## Introduction
这篇论文被纳入仓库，是因为它和 `compression, context, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Transformer depth is not used uniformly: lower and middle layers build semantic representations, while upper layers increasingly specialize them for prediction.

进一步看，论文的核心做法或实验重点可以概括为：We turn this division of labor into CoMem (Comprehension Memory), which writes each context chunk only through an intermediate layer, retrieves a fixed number of cached residual states, and recomputes the query-...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression, context, conversation, retrieval
- 检索关键词命中：context memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Transformer depth is not used uniformly: lower and middle layers build semantic representations, while upper layers increasingly specialize them for prediction. We turn this division of labor into CoMem (Comprehension Memory), which writes each context chunk only through an intermediate layer, retrieves a fixed number of cached residual states, and recomputes the query-conditioned upper layers over the resulting pack. For a fixed retrieval budget, model-side read compute and memory are independent of stored-context length. We evaluate a continued-trained Qwen3-8B base LM under a unified chat-template-free protocol. The backbone is frozen; the flagship trains only a rank-32 self-distillation LoRA on plain PG19, and we report an adapter-free arm separately. CoMem reaches 97.05 on RULER and 38.27 on LoCoMo versus 34.59 for full-context KV-Direct; the dialogue-memory advantage survives conversation-cluster resampling and an independent judge. Results on additional long-context and long-document tasks expose both the benefits of bounded retrieval and its in-window compression tax. Controlled depth sweeps show that deeper caching lowers per-query recomputation but incurs a fidelity loss that self-distillation substantially repairs. In a separate adapter-free efficiency control on an NVIDIA H20 at 128k, CoMem uses 18.26 GB rather than 89.36 GB and achieves a 7.83x prefill speedup. These results show that long-context memory can be organized along the layer axis, not only the token axis.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
