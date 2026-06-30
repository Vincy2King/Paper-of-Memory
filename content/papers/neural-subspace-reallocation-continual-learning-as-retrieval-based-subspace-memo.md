# Neural Subspace Reallocation: Continual Learning as Retrieval-Based Subspace Memory Management

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.30067v1
- Published: 2026-06-29
- Updated: 2026-06-29
- Authors: Byeong Hoon Yoon
- Tags: benchmark, compression, retrieval
- Categories: cs.LG, cs.AI, cs.CV
- URL: http://arxiv.org/abs/2606.30067v1

## One-Sentence Summary
We introduce Neural Subspace Reallocation (NSR), which reframes continual learning as memory management over parameter subspaces.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, compression, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We introduce Neural Subspace Reallocation (NSR), which reframes continual learning as memory management over parameter subspaces.

进一步看，论文的核心做法或实验重点可以概括为：Instead of treating Low-Rank Adaptation (LoRA) modules as disposable per-task adapters, NSR manages them as compressible, retrievable memory units on a frozen backbone through a recurring cycle: (1) compress learned...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, compression, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.LG, cs.AI, cs.CV

## Abstract Snapshot
We introduce Neural Subspace Reallocation (NSR), which reframes continual learning as memory management over parameter subspaces. Instead of treating Low-Rank Adaptation (LoRA) modules as disposable per-task adapters, NSR manages them as compressible, retrievable memory units on a frozen backbone through a recurring cycle: (1) compress learned LoRAs via SVD, (2) reserve them in a TaskKnowledgeBank, (3) recall related past LoRAs by embedding similarity to warm-start new or returning tasks, and (4) reallocate the active subspace accordingly, with distillation protecting prior tasks. We prove that in cyclic environments any memoryless allocation policy incurs cumulative regret Omega(T(M-1)Delta_switch) relative to a history-aware policy backed by the Bank (Theorem 1). Empirically, on Split-CIFAR-100 the Bank reduces cyclic recovery time by 10x, exactly as predicted, and on the heterogeneous 5-Datasets benchmark NSR achieves the highest accuracy and the least forgetting, about 9x closer to zero backward transfer than the memoryless heuristics. Crucially, we run a controlled study that isolates which component matters: holding the Bank fixed and varying only the allocation rule, we find that a simple similarity-based retrieval rule matches or beats a learned reinforcement-learning controller (recovering recurring tasks in 0 vs 1.8 steps and reaching equal accuracy). Our central, honest finding is therefore that the memory mechanism -- compression and similarity retrieval -- rather than a learned allocation policy, drives continual-learning performance under fixed capacity. A memory-budget analysis confirms the compressed Bank stays small -- 0.29 MB of parameter memory per task -- so a top-K retention cap bounds the total footprint while preserving fast recovery for retained tasks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
