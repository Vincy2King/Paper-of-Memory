# MATE: Adaptive Long- and Short-Term User Memory for LLM-Based Recommendation

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.06050v1
- Published: 2026-10-05
- Updated: 2026-10-05
- Authors: Yu Hou
- Tags: context, long-term
- Categories: cs.IR
- URL: http://arxiv.org/abs/2610.06050v1

## One-Sentence Summary
Large language model (LLM)-enhanced recommender systems leverage rich item semantics to support personalized recommendation.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM)-enhanced recommender systems leverage rich item semantics to support personalized recommendation.

进一步看，论文的核心做法或实验重点可以概括为：However, semantic representations alone do not determine which historical behaviors reflect persistent preferences and which mainly indicate recent interests, leaving an important aspect of user understanding unresolved.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.IR

## Abstract Snapshot
Large language model (LLM)-enhanced recommender systems leverage rich item semantics to support personalized recommendation. However, semantic representations alone do not determine which historical behaviors reflect persistent preferences and which mainly indicate recent interests, leaving an important aspect of user understanding unresolved. Recent advances in LLM inference show that newly available information can be used to refine the internal state during inference, thereby improving subsequent predictions. Inspired by this principle, we propose MATE (Memory Adaptation with Temporal Evidence), an adaptive user modeling framework for LLM-enhanced sequential recommendation. MATE first evaluates each newly observed interaction from two temporal perspectives: whether it is repeatedly supported by historical behaviors and whether it is consistent with recent interactions. The resulting temporal evidence controls the updates of two user-specific memories, where the long-term memory conservatively preserves persistent preferences while the short-term memory rapidly adapts to recent interests. For each recommendation, a recent-context representation dynamically determines how strongly the two memories contribute to the current user representation. During offline training, next-item prediction is jointly optimized with temporal supervision, while during online adaptation, the shared model remains fixed and only the two user memories are updated from newly observed interactions. Experiments on MovieLens-10M, Amazon Luxury Beauty, and KuaiRec show that MATE improves mean NDCG@10 over the strongest external baseline by 7.0--13.2%. Further analyses support its ability to adapt to recent interests while retaining useful information about recurring earlier preferences.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
