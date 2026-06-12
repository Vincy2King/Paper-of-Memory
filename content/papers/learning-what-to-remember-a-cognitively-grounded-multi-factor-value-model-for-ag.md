# Learning What to Remember: A Cognitively Grounded Multi-Factor Value Model for Agentic Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.12945v1
- Published: 2026-06-11
- Updated: 2026-06-11
- Authors: Zhibao Chen, Qian Cheng
- Tags: agent, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.12945v1

## One-Sentence Summary
Long-running LLM agents accumulate interaction histories far larger than any context window, forcing a standing decision: what to encode deeply, what to forget, and what to...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-running LLM agents accumulate interaction histories far larger than any context window, forcing a standing decision: what to encode deeply, what to forget, and what to retrieve under a fixed memory budget.

进一步看，论文的核心做法或实验重点可以概括为：Production systems answer with semantic similarity or recency -- both mis-specified for the forgetting decision, which is made at consolidation time before the future query is known.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-running LLM agents accumulate interaction histories far larger than any context window, forcing a standing decision: what to encode deeply, what to forget, and what to retrieve under a fixed memory budget. Production systems answer with semantic similarity or recency -- both mis-specified for the forgetting decision, which is made at consolidation time before the future query is known. We propose a multi-factor memory value function V(m)=\sum_i w_i f_i(m) over seven interpretable factors (emotional intensity, goal relevance, value alignment, self/user relevance, task utility, reliability, and usage history) drawn from cognitive psychology, whose weights are learned from a downstream objective by a gradient-free optimiser, and whose single scalar uniformly controls encoding depth, forget risk, and retrieval rank. We make a methodological point: on LongMemEval, scoring goal relevance against the held-out evaluation question saturates gold-evidence retention at \approx 0.98 -- this measures retrieval, not forgetting. In the realistic blind regime, a learned multi-factor value retains 0.770 \pm 0.011 of gold evidence across 479 usable cases, versus 0.657 for uniform weights, 0.518 for the best single factor, and 0.368 for recency; every paired gap's 95% bootstrap CI is above zero, and a neural network over the same factors ties the linear model. The learned weights are interpretable -- reliability, emotional intensity, and self/user relevance dominate, while query-time goal similarity is correctly down-weighted for the forgetting decision. A controlled synthetic task with planted confounds confirms the learner recovers a separating weighting (1.00 retention) where uniform weighting fails (0.62). The substrate is open-source; all experiments run on a single CPU with no API calls.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
