# Collaborative Memory Augmentation for Generative Recommendation

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.01315v1
- Published: 2026-08-02
- Updated: 2026-08-02
- Authors: Enze Liu, Zhen Tian, Wayne Xin Zhao
- Tags: compression, context, retrieval
- Categories: cs.IR
- URL: http://arxiv.org/abs/2608.01315v1

## One-Sentence Summary
Generative Recommendation (GR) has exhibited great potential by modeling item transitions as a sequence-to-sequence task.

## Introduction
这篇论文被纳入仓库，是因为它和 `compression, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Generative Recommendation (GR) has exhibited great potential by modeling item transitions as a sequence-to-sequence task.

进一步看，论文的核心做法或实验重点可以概括为：Despite the success of GR, existing frameworks primarily focus on modeling individual user sequences within a constrained internal parametric space, failing to explicitly leverage cross-user collaborative signals.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression, context, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.IR

## Abstract Snapshot
Generative Recommendation (GR) has exhibited great potential by modeling item transitions as a sequence-to-sequence task. Despite the success of GR, existing frameworks primarily focus on modeling individual user sequences within a constrained internal parametric space, failing to explicitly leverage cross-user collaborative signals. To address this issue, we propose \textbf{OMEGA}, a cOllaborative MEmory augmentation framework for Generative recommendAtion. OMEGA bridges the gap between implicit parametric knowledge and explicit collaborative signals. We first introduce a latent context compression method that utilizes learnable query tokens to distill sequential user behavior into compact representations, significantly reducing storage overhead. These compressed representations are aggregated into a collaborative memory bank, serving as an explicit repository of global behavioral patterns. To ensure precise knowledge acquisition, we design a lightweight and target-aware retrieval mechanism that identifies pertinent memories by considering both sequence-level and target-level similarities. Furthermore, a context-aware integration module, equipped with a gated cross-attention mechanism, is employed to adaptively fuse the retrieved collaborative memories with the local user context while mitigating the interference of noisy patterns. Empirical evaluations on multiple real-world datasets demonstrate that OMEGA significantly outperforms existing advanced GR models, validating the potential of external memory as a complement to the generative paradigm.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
