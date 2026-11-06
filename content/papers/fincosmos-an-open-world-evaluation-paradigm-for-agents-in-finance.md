# FINCOSMOS: An Open-World Evaluation Paradigm for Agents in Finance

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.07464v1
- Published: 2026-11-05
- Updated: 2026-11-05
- Authors: Yupeng Cao, Xueqing Peng, Lingfei Qian, Haohang Li, Yangyang Yu, Anke Xu, Wenbo Cao, Yan Wang, Yuechen Jiang, Yuyan Wang, Zhuohan Xie, Yankai Chen, Zehan Li, Jimin Huang, Xue Liu, Jian-Yun Nie, Sophia Ananiadou
- Tags: agent, benchmark
- Categories: cs.AI, cs.CL, q-fin.CP
- URL: http://arxiv.org/abs/2611.07464v1

## One-Sentence Summary
Language agents increasingly work for users on the open Web, and finance is where trusting them is hardest.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Language agents increasingly work for users on the open Web, and finance is where trusting them is hardest.

进一步看，论文的核心做法或实验重点可以概括为：The data must come from the Web, the strategy lives in the user's head, and correctness depends on time, so an agent can fail silently: a strategy the user never asked for, unverified data, or a backtest that uses the...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI, cs.CL, q-fin.CP

## Abstract Snapshot
Language agents increasingly work for users on the open Web, and finance is where trusting them is hardest. The data must come from the Web, the strategy lives in the user's head, and correctness depends on time, so an agent can fail silently: a strategy the user never asked for, unverified data, or a backtest that uses the future yields a report as convincing as a correct one. Existing benchmarks close the world somewhere, fixing the task, the data, or the timeline, and thereby remove these failures instead of measuring them. We introduce FINCOSMOS, an open-world evaluation paradigm for agents doing financial work. A simulated user holds a hidden strategy sampled from a compositional grammar and reveals it only when asked. The agent receives no data, so it must acquire data from the Web, build its own backtest under a data cutoff, and deliver verifiable results. Grading needs no reference answer. Programs verify point-in-time correctness and recompute every reported metric, the delivered strategy is checked against the hidden specification, and a run is accepted only when the user is satisfied and none of 15 veto checks fails. Across four coding agents and a model without tools in 150 sessions, no session is accepted: every session that the simulated user signed off fails a program check, and agents raise only 54--64\% of the details they were not told. Human experts attribute 88.33\% of failures to the agents. With FINCOSMOS feedback, an agent with persistent memory learned all ten tasks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
