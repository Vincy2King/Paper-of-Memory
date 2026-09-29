# PairPref: When Should Memory Guide the Answer? A Benchmark for Contextual Preference Use

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.34526v1
- Published: 2026-09-28
- Updated: 2026-09-28
- Authors: Mingfei Lu, Mengjia Wu, Yi Zhang
- Tags: benchmark, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.34526v1

## One-Sentence Summary
Memory-augmented assistants use retrieved preferences to guide their responses.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-augmented assistants use retrieved preferences to guide their responses.

进一步看，论文的核心做法或实验重点可以概括为：A small change in the situation can change whether a preference is appropriate while barely affecting its retrieval similarity.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, retrieval
- 检索关键词命中：memory augmented, memory benchmark, memory benchmarks, memory-augmented, retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Memory-augmented assistants use retrieved preferences to guide their responses. A small change in the situation can change whether a preference is appropriate while barely affecting its retrieval similarity. Memory benchmarks typically test whether systems store and retrieve preferences, with less attention to when those preferences should apply. We introduce PairPref, a benchmark of contextual preference use. Each pair changes only the situation, keeping the preference, request, and four candidate replies fixed. The preference remains valid in both situations. In the selection track, models must choose the reply that applies the preference only where appropriate. In the free-generation track, they must decide when to apply it without seeing candidate replies. Both tracks use the same 1,227 pairs across 45 preferences and eight situation categories. We evaluate eight models, most of which achieve selection scores ($Δ$) of 51 to 65 points. In free generation, however, both responses are appropriate for their respective situations in only 3.6\% to 18.3\% of pairs. Models continue to apply the preference in both situations even with fewer retrieved memories, alternative presentation formats, and a stricter prompt. These results show that models still struggle to judge when user preferences apply and respond accordingly.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
