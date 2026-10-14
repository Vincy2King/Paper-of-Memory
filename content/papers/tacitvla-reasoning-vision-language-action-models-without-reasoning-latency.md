# TacitVLA: Reasoning Vision-Language-Action Models Without Reasoning Latency

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.17540v1
- Published: 2026-10-13
- Updated: 2026-10-13
- Authors: Jack Lu, Yurong You, Boyi Li, Yulong Cao, Thomas Tian, Chaowei Xiao, Xiangyu Chen, Wenjie Luo, Boris Ivanovic, Marco Pavone, Yan Wang
- Tags: benchmark, episodic
- Categories: cs.AI, cs.RO
- URL: http://arxiv.org/abs/2610.17540v1

## One-Sentence Summary
Textual reasoning before acting has improved vision-language-action (VLA) models, but at the cost of latency: every action conditioned on the reasoning text must wait for...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Textual reasoning before acting has improved vision-language-action (VLA) models, but at the cost of latency: every action conditioned on the reasoning text must wait for autoregressive decoding.

进一步看，论文的核心做法或实验重点可以概括为：We show that actions do not need to wait for or condition on the generated reasoning to benefit from it, because the reasoning supervision already improves the backbone representation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI, cs.RO

## Abstract Snapshot
Textual reasoning before acting has improved vision-language-action (VLA) models, but at the cost of latency: every action conditioned on the reasoning text must wait for autoregressive decoding. We show that actions do not need to wait for or condition on the generated reasoning to benefit from it, because the reasoning supervision already improves the backbone representation. We introduce TacitVLA, a reasoning VLA whose action expert never attends to the reasoning it generates for the current call. On long-horizon tasks where the reasoning text also serves as episodic memory, it can generate each entry during action execution rather than before acting. We evaluate it in a controlled study on four benchmarks spanning manipulation and autonomous driving, memory and non-memory tasks: RoboMME, RMBench, LIBERO, and PhysicalAI-AV. On all four, TacitVLA matches the performance of its explicit-reasoning counterpart at up to 3.4x lower latency, and matches the latency of the same architecture trained without reasoning at up to +17.1% success. In absolute terms, it surpasses the best previously published results on the RoboMME Counting suite (82.7% vs. 66.8%) and RMBench (77.5% vs. 56.5%), and reaches 72.9% on LIBERO-Plus and a 52.5% scene score on the public split of the PhysicalAI-AV closed-loop driving challenge. Project page: https://tacitvla.github.io.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
