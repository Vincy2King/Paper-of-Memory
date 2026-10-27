# ConMem: Counterfactual Multi-Scenario Probing for Resolving LLM Memory Misalignment

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.33432v1
- Published: 2026-10-24
- Updated: 2026-10-24
- Authors: Shuning Zhang, Tenghao Ji, Jingruo Chen, Eryue Xu, Bohao Chu, Xin Yi
- Tags: agent, benchmark, context, conversation, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.33432v1

## One-Sentence Summary
Long-term memory is critical for autonomous Large Language Model (LLM) agents executing multi-session, long-horizon tasks.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory is critical for autonomous Large Language Model (LLM) agents executing multi-session, long-horizon tasks.

进一步看，论文的核心做法或实验重点可以概括为：However, existing memories often inappropriately store, retain, or retrieve over-generalized, misattributed, or privacy-sensitive information, a problem we term memory misalignment.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term memory is critical for autonomous Large Language Model (LLM) agents executing multi-session, long-horizon tasks. However, existing memories often inappropriately store, retain, or retrieve over-generalized, misattributed, or privacy-sensitive information, a problem we term memory misalignment. To study this problem, we construct \textbf{MemAlign}, a benchmark comprising 1,079 curated memory cases grounded in synthetic, validated multi-session conversational contexts covering diverse misalignment taxonomies. We then propose ConMem, an algorithm that reframes retention decisions as prospective counterfactual causal inference. \textbf{ConMem} synthesizes counterfactual interaction scenarios to prospectively audit downstream intervention effects across three aspects: relevant task execution, irrelevant invariance checks, and risk-sensitive boundary shifts. Experiments show that ConMem outperforms other methods, achieving 75.16\% accuracy, 64.15\% balanced accuracy, and a Macro-F1 of 65.31\%, effectively mitigating over-retention biases without sacrificing personalization utility.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
