# When Errors Become Memories: Causal Pathway Tracing in Multi-Turn Memory-Augmented LLMs

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.30198v1
- Published: 2026-08-31
- Updated: 2026-08-31
- Authors: Shuyao Xiao, Shengling Wang, Xuan Chen, Ke Chao, Ming Cui, Feifei Qian, Fanlin Meng, Chaoyang Mei, Chaoyong Jiang, Qi Ouyang, Junxi Yi
- Tags: long-term
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.30198v1

## One-Sentence Summary
Long-term memory enables large language models (LLMs) to preserve and reuse information across interactions, but it can also turn localized errors into persistent risks.

## Introduction
这篇论文被纳入仓库，是因为它和 `long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory enables large language models (LLMs) to preserve and reuse information across interactions, but it can also turn localized errors into persistent risks.

进一步看，论文的核心做法或实验重点可以概括为：Existing work mainly evaluates whether memory systems store and retrieve information correctly, leaving limited understanding of how errors propagate across responses, memory states, and future interactions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：long-term
- 检索关键词命中：long-term memory, memory augmented, memory-augmented
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-term memory enables large language models (LLMs) to preserve and reuse information across interactions, but it can also turn localized errors into persistent risks. Existing work mainly evaluates whether memory systems store and retrieve information correctly, leaving limited understanding of how errors propagate across responses, memory states, and future interactions. We propose a structural causal model (SCM)-based framework for cross-turn error propagation in memory-augmented LLMs. We model user questions, model responses, and memory states as a dynamic causal process, and identify two entry pathways: internal memory updating and external question feedback. By intervening on these pathways, we construct four counterfactual trajectories and quantify their downstream effects and interaction. Error influence is evaluated at four levels: memory retention, natural responses, targeted diagnostic probing, and probability-level error preference. Experiments show that error influence generally decays with interaction distance, while the memory-update pathway contributes more persistent effects than question feedback; latent errors may remain even after disappearing from natural responses. Propagation patterns also vary across memory categories and memory mechanisms. Pathway-guided restoration further validates this decomposition: Question Repair reduces residual error by 27.5%, Memory Repair by 70.2%, and Joint Repair by 98.3%, nearly eliminating residual propagation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
