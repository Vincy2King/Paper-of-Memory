# What Eviction Destroys: A Restore-Counterfactual Audit of Forgetting in Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.08279v1
- Published: 2026-09-08
- Updated: 2026-09-08
- Authors: Chen Shen
- Tags: agent, benchmark, context, conversation, retrieval
- Categories: cs.CL, cs.AI, cs.DB
- URL: http://arxiv.org/abs/2609.08279v1

## One-Sentence Summary
Agent memory systems must discard stored information when their history exceeds a fixed token budget.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agent memory systems must discard stored information when their history exceeds a fixed token budget.

进一步看，论文的核心做法或实验重点可以概括为：Existing budget-accuracy frontiers quantify the resulting loss in accuracy, but do not distinguish irreversible losses caused by eviction from recoverable retrieval failures.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL, cs.AI, cs.DB

## Abstract Snapshot
Agent memory systems must discard stored information when their history exceeds a fixed token budget. Existing budget-accuracy frontiers quantify the resulting loss in accuracy, but do not distinguish irreversible losses caused by eviction from recoverable retrieval failures. We introduce the restore counterfactual, a per-question paired intervention that reinstates the question's gold evidence in the read-time context and reruns the same reader. Combining the change in correctness with whether the evidence was retained after eviction classifies each oracle-answerable error as recoverable, irreversible, or residual; in the residual case, the answer remains incorrect after restoration. We evaluate FIFO, random, redundancy-aware, and LLM-importance eviction on LongMemEval-S at three budgets and under two retrieval regimes, using GPT-4o-mini as the primary reader and judge and GPT-5.4-mini as a robustness reader. Under top-k retrieval at an 80k-token budget, the irreversible share among errors corrected by restoration is 0.67-0.73 for FIFO, random, and redundancy-aware eviction, compared with 0.60 for LLM-importance. At 8k tokens, it reaches 1.00 for all four policies. Recoverable errors occur under top-k retrieval at 80k tokens but are absent under forced-gold injection by construction, so budget-accuracy results are not directly comparable unless the retrieval regime is reported. An exploratory matched-accuracy analysis detects no difference in irreversible rate among accuracy-matched policy pairs at a resolution of 1.2-6 percentage points. The same analysis detects the deliberately destructive control. To our knowledge, this is the first per-item, per-question restore-counterfactual audit of eviction for external agent-memory stores on a standard conversational benchmark.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
