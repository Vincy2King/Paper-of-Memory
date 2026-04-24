# AEL: Agent Evolving Learning for Open-Ended Environments

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.21725v1
- Published: 2026-04-23
- Updated: 2026-04-23
- Authors: Wujiang Xu, Jiaojiao Han, Minghao Guo, Kai Mei, Xi Zhu, Han Zhang, Dimitris N. Metaxas
- Tags: agent, benchmark, retrieval
- Categories: cs.CL, cs.AI, cs.CE
- URL: http://arxiv.org/abs/2604.21725v1

## One-Sentence Summary
LLM agents increasingly operate in open-ended environments spanning hundreds of sequential episodes, yet they remain largely stateless: each task is solved from scratch without...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM agents increasingly operate in open-ended environments spanning hundreds of sequential episodes, yet they remain largely stateless: each task is solved from scratch without converting past experience into better...

进一步看，论文的核心做法或实验重点可以概括为：The central obstacle is not \emph{what} to remember but \emph{how to use} what has been remembered, including which retrieval policy to apply, how to interpret prior outcomes, and when the current strategy itself must...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.CL, cs.AI, cs.CE

## Abstract Snapshot
LLM agents increasingly operate in open-ended environments spanning hundreds of sequential episodes, yet they remain largely stateless: each task is solved from scratch without converting past experience into better future behavior. The central obstacle is not \emph{what} to remember but \emph{how to use} what has been remembered, including which retrieval policy to apply, how to interpret prior outcomes, and when the current strategy itself must change. We introduce \emph{Agent Evolving Learning} (\ael{}), a two-timescale framework that addresses this obstacle. At the fast timescale, a Thompson Sampling bandit learns which memory retrieval policy to apply at each episode; at the slow timescale, LLM-driven reflection diagnoses failure patterns and injects causal insights into the agent's decision prompt, giving it an interpretive frame for the evidence it retrieves. On a sequential portfolio benchmark (10 sector-diverse tickers, 208 episodes, 5 random seeds), \ael{} achieves a Sharpe ratio of 2.13$\pm$0.47, outperforming five published self-improving methods and all non-LLM baselines while maintaining the lowest variance among all LLM-based approaches. A nine-variant ablation reveals a ``less is more'' pattern: memory and reflection together produce a 58\% cumulative improvement over the stateless baseline, yet every additional mechanism we test (planner evolution, per-tool selection, cold-start initialization, skill extraction, and three credit assignment methods) \emph{degrades} performance. This demonstrates that the bottleneck in agent self-improvement is \emph{self-diagnosing how to use} experience rather than adding architectural complexity. Code and data: https://github.com/WujiangXu/AEL.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
