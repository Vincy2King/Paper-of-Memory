# Suggested Is Not Superseded: A Pre-Registered Evaluation of a System-One Model as a Memory-Retirement Gate

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.15710v1
- Published: 2026-10-11
- Updated: 2026-10-11
- Authors: Xupeng Chen, Chenqian Le
- Tags: benchmark, conversation, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.15710v1

## One-Sentence Summary
Long-term memory for assistants needs a gate that decides when a new utterance retires an old stored claim.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory for assistants needs a gate that decides when a new utterance retires an old stored claim.

进一步看，论文的核心做法或实验重点可以概括为：Benchmark labels for this step mark a pair as changed or not, so they cannot tell a gate that acts on established change from one that acts on a hint.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, conversation, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term memory for assistants needs a gate that decides when a new utterance retires an old stored claim. Benchmark labels for this step mark a pair as changed or not, so they cannot tell a gate that acts on established change from one that acts on a hint. We write a task contract that separates the two (SUPERSEDED vs. NEEDS-CONFIRMATION vs. COMPATIBLE), label 500 test pairs built from STALE (change pairs plus same-user controls) with three LLM annotators and two human adjudicators (one author and a second annotator; provenance reported), and evaluate Jev, a typed "System One" decision model, under pre-registered hypotheses. Of the 179 test pairs STALE marks as changed, 72 meet the contract's bar for an established change. Jev never retired a claim on 141 same-conversation non-changes. Its failure is premature retirement: the binary gate retires 39.2% of claims whose change is only suggested. A three-way decision cuts this to 15.5% at a 15.3-point detection cost, which misses our pre-registered 10-point budget, and it lands on the binary gate's own threshold frontier; these verdicts hold under three readings of the gold labels. On a held-out vault scored against a second annotator's labels, a cascade that escalated uncertain cases to a reasoning model and looked best on development data was indistinguishable from simply raising the threshold (premature retirement 26.8% vs. 6.5% on dev). Part of the gap comes from the gold labels: relative to that annotator's reading, LLM-majority gold shares most of its errors with a same-family escalation model, and an identity for binary labels says how much such shared errors hide. The rest is small-sample selection on development data. For builders this means a binary score should not be wired to delete: route suggested changes to pending evidence, and do not trust a cascade selected on development data of this size.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
