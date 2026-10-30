# The Price of Scale in Proactive Memory Recall

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.34507v2
- Published: 2026-10-25
- Updated: 2026-10-29
- Authors: Yichuan Chen, Xin Wang
- Tags: benchmark
- Categories: cs.CL, cs.AI, cs.IR, stat.ML
- URL: http://arxiv.org/abs/2610.34507v2

## One-Sentence Summary
A long-lived assistant that brings up memories without being asked must decide at every turn whether anything in its store is worth an interruption.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：A long-lived assistant that brings up memories without being asked must decide at every turn whether anything in its store is worth an interruption.

进一步看，论文的核心做法或实验重点可以概括为：We show that this decision is a multiple-testing problem whose difficulty grows with the store size N.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：cs.CL, cs.AI, cs.IR, stat.ML

## Abstract Snapshot
A long-lived assistant that brings up memories without being asked must decide at every turn whether anything in its store is worth an interruption. We show that this decision is a multiple-testing problem whose difficulty grows with the store size N. On streaming replays of LongMemEval, a similarity threshold tuned to 5% false alarms at N=8 reaches 84-100% at N=2048 across embedding models and cue types, and LoCoMo and LLM judges show it too. We prove that a gate which thresholds the best of N independent irrelevant scores at false-alarm rate alpha operates at a per-item false-positive rate of about -ln(1-alpha)/N, which pins its hit rate to the far left of the single-comparison ROC curve and, under regular variation, makes it regularly varying in N. A finite-pool form of this bound predicts the hit rate of a label-tuned threshold on held-out questions to within 6.1 points. At matched false alarms the deployed score recalls 14-26 points more than raw cosine. A cue-swap conformal gate, which ranks the current cue among other cues on the same store, has a finite-sample false-alarm guarantee under exchangeability. With a background drawn from the user's unfiltered history it keeps false alarms at 3-6% on LongMemEval at the hit rate of a label-tuned threshold; on LoCoMo it overshoots or turns conservative depending on where its reference cues come from. In a chronological replay with the user's own earlier messages as references, it speaks on 6-8% of session-opening turns, against 57% for the deployed gate at N=2048, at about 50 ms per decision on one CPU thread. A cross-encoder reranker pays the same price of scale, and on a prospective-memory benchmark, similarity gates recall at most 9% of constraints at controlled false alarms. One human and two LLM annotators judge most false alarms unhelpful for a response. Code and data: https://github.com/RiverChenStillCompiling/price-of-scale

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
