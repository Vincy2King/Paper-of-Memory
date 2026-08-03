# TransMem: Transforming Hidden States into Memory for Large Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.29032v1
- Published: 2026-07-31
- Updated: 2026-07-31
- Authors: Haodong Lei, Junming Liu, Yirong Chen, Pinlong Cai, Botian Shi, Ding Wang, Hongsong Wang
- Tags: agent, context
- Categories: cs.MA, cs.CL
- URL: http://arxiv.org/abs/2607.29032v1

## One-Sentence Summary
Large language model (LLM) agents increasingly operate over long interaction histories, where effective reasoning requires identifying and exploiting task-relevant evidence...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents increasingly operate over long interaction histories, where effective reasoning requires identifying and exploiting task-relevant evidence distributed across past observations and...

进一步看，论文的核心做法或实验重点可以概括为：However, useful information encoded in previously computed representations is often underutilized during subsequent generation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.MA, cs.CL

## Abstract Snapshot
Large language model (LLM) agents increasingly operate over long interaction histories, where effective reasoning requires identifying and exploiting task-relevant evidence distributed across past observations and actions. However, useful information encoded in previously computed representations is often underutilized during subsequent generation. We propose \textbf{TransMem}, a lightweight inference-time parametric memory module that transforms sparse historical hidden states from a frozen LLM backbone into reusable memory representations. TransMem uses a lightweight gating network to dynamically apply the latent intervention to the current hidden states, without repeatedly encoding the preceding context. To learn transferable memory utilization rather than task-specific knowledge, we introduce evidence-conditioned self-distillation. A memory-augmented student processes the full context and matches the predictive distribution of an evidence-only teacher that shares the same frozen backbone. Experiments on LoCoMo, HotpotQA, and MemoryAgentBench demonstrate consistent improvements across different model architectures and scales. TransMem yields gains of 11.58--29.25 $F_1$ on LoCoMo and 10.20--13.03 $F_1$ on HotpotQA, while improving the average MemoryAgentBench accuracy from 29.54\% to 40.00\%. These results establish sparse historical hidden states as an effective and efficient memory substrate for long-context LLM agents. Our code is available at https://github.com/Haodong-Lei-Ray/TransMem.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
