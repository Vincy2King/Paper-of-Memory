# LongMemEval-V2: Benchmarking Agent Memory for Experienced Colleagues

- Source: OpenReview
- Venue: SCALE@ICML2026 Oral
- Paper ID: openreview:WUU5KTwCq5
- Published: 2026-05-15
- Updated: 2026-07-05
- Authors: Di Wu, Zixiang Ji, Asmi Kawatkar, Bryan Kwan, Jia-Chen Gu, Nanyun Peng, Kai-Wei Chang
- Tags: agent, benchmark, context, long-term
- Categories: ICML.cc/2026/Workshop/SCALE/-/Submission
- URL: https://openreview.net/forum?id=WUU5KTwCq5

## One-Sentence Summary
Long-term memory is crucial for agents in specialized web environments, where success depends on recalling interface affordances, workflows, state dynamics, and recurring...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `SCALE@ICML2026 Oral` 这个 venue 相关。

从摘要来看，作者主要关注的是：Long-term memory is crucial for agents in specialized web environments, where success depends on recalling interface affordances, workflows, state dynamics, and recurring failure modes.

进一步看，论文的核心做法或实验重点可以概括为：We introduce LongMemEval-V2 (LME-V2), a benchmark for evaluating whether memory systems can accumulate environment-specific experience from multimodal web agent trajectories.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：SCALE@ICML2026 Oral
- 高亮主题命中：agent, benchmark, context, long-term
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：ICML.cc/2026/Workshop/SCALE/-/Submission

## Abstract Snapshot
Long-term memory is crucial for agents in specialized web environments, where success depends on recalling interface affordances, workflows, state dynamics, and recurring failure modes. We introduce LongMemEval-V2 (LME-V2), a benchmark for evaluating whether memory systems can accumulate environment-specific experience from multimodal web agent trajectories. LME-V2 contains 451 manually curated questions from customized shopping, forum, admin, and ServiceNow-style environments, with histories ranging from 25M to 115M tokens. Frontier LLMs reach at most 14.1% without trajectory evidence, confirming that LME-V2 requires learned experience beyond parametric knowledge. We evaluate memory under a context-gathering formulation and propose AgentRunbook: AgentRunbook-R is an efficient RAG pipeline over raw states, transitions, and notes, while AgentRunbook-C uses a scaffolded coding agent to gather evidence from trajectory files. AgentRunbook-C achieves the best overall accuracy, reaching 74.9% on LME-V2-Small and 70.1% on LME-V2-Medium, while improving the accuracy and latency trade-off over an off-the-shelf coding agent. We will release the benchmark and memory implementations.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
