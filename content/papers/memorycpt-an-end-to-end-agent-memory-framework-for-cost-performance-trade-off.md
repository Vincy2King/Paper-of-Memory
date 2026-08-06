# MemoryCPT: An End-to-End Agent Memory Framework for Cost-Performance Trade-off

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.04843v1
- Published: 2026-08-05
- Updated: 2026-08-05
- Authors: Songxin Lei, Kun Ouyang, Weilin Ruan, Yuqian Wu, Zhijiang Guo, Yushi Sun, Fugee Tsung
- Tags: agent, context, retrieval
- Categories: cs.IR
- URL: http://arxiv.org/abs/2608.04843v1

## One-Sentence Summary
Long-horizon LLM agents require memory systems that recover useful evidence from large interaction histories without passing excessive context to downstream models.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon LLM agents require memory systems that recover useful evidence from large interaction histories without passing excessive context to downstream models.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory pipelines often rely on hand-crafted heuristics and repeated LLM calls, which can introduce redundant context and high inference cost.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.IR

## Abstract Snapshot
Long-horizon LLM agents require memory systems that recover useful evidence from large interaction histories without passing excessive context to downstream models. Existing memory pipelines often rely on hand-crafted heuristics and repeated LLM calls, which can introduce redundant context and high inference cost. We propose MemoryCPT, an end-to-end trainable agent memory pipeline that spans offline memory construction and online query-conditioned context generation. MemoryCPT consists of two stages: Query-agnostic Distillation (QAD), which distills a modular memory-construction pipeline into a compact model using explicit reasoning traces; and Query-aware Retrieval and Summarization (QAR), which combines reciprocal rank fusion (RRF) with a LoRA-based summarizer trained via Group Relative Policy Optimization (GRPO) under a cost-aware reward. We further introduce Quality per Cost (QPC) to quantify answer quality per unit inference cost. Experiments on LoCoMo and LongMemEval show that MemoryCPT improves the cost-performance trade-off over the evaluated baselines, while ablation and sensitivity analyses characterize the contributions of its components and the effects of key design choices.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
