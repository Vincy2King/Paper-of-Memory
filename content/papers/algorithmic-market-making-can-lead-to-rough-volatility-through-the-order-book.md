# Algorithmic Market Making Can Lead to Rough Volatility Through the Order Book

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.24028v1
- Published: 2026-11-18
- Updated: 2026-11-18
- Authors: Sai Niranjan Ramachandran
- Tags: agent
- Categories: cs.LG, q-fin.MF, q-fin.TR
- URL: http://arxiv.org/abs/2611.24028v1

## One-Sentence Summary
Existing work suggests that markets can show volatility with paths rougher than those of Brownian motion.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Existing work suggests that markets can show volatility with paths rougher than those of Brownian motion.

进一步看，论文的核心做法或实验重点可以概括为：In theory this can happen when the order flow is close to instability with memory that decays as a power law.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.LG, q-fin.MF, q-fin.TR

## Abstract Snapshot
Existing work suggests that markets can show volatility with paths rougher than those of Brownian motion. In theory this can happen when the order flow is close to instability with memory that decays as a power law. However, it is not fully clear how such order flow could arise from the predominantly algorithmic market making that characterizes order book dynamics. We show one such consistent mechanism. We treat each market maker as a desk that uses a first-order gradient rule to move the distances of its orders from the mid price toward target distances provided by an unknown oracle. We assume that distinct desks do not act synchronously in time but act whenever new information relevant to their respective oracles arrives, which each desk samples over its own characteristic lookback horizon. Across all desks the rule therefore takes the form of stochastic gradient descent (SGD) with information-driven (mini-batch) noise. In the continuum limit this update rule makes the volume of the order book follow a conservative stochastic partial differential equation (the Dean--Kawasaki equation) whose fluctuations drive the order flow. The distinct horizons of the desks further induce a persistent memory in the order flow that decays as a power law. Standard scaling arguments then lead to rough volatility. We confirm the key predictions of the model on simulated agents and on six months of Binance data with about 790 million orders. In liquid markets governed mainly by market makers, such as the perpetual futures of Binance, the order books are consistent with how our desks change the book.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
