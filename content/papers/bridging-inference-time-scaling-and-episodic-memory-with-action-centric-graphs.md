# Bridging Inference-Time Scaling and Episodic Memory with Action-Centric Graphs

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.27415v1
- Published: 2026-07-29
- Updated: 2026-07-29
- Authors: Xu Zheng, Chaohao Lin, Zhuomin Chen, Weijieying Ren, Haifeng Chen, Wei Cheng, Dongsheng Luo
- Tags: agent, benchmark, context, episodic
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.27415v1

## One-Sentence Summary
Recent advancements in inference-time scaling have significantly unlocked the complex reasoning capabilities of Large Language Models~(LLMs).

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recent advancements in inference-time scaling have significantly unlocked the complex reasoning capabilities of Large Language Models~(LLMs).

进一步看，论文的核心做法或实验重点可以概括为：However, for agents, these approaches suffer from a critical inefficiency, operating in a stateless manner and engaging in redundant search processes.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Recent advancements in inference-time scaling have significantly unlocked the complex reasoning capabilities of Large Language Models~(LLMs). However, for agents, these approaches suffer from a critical inefficiency, operating in a stateless manner and engaging in redundant search processes. Existing memory mechanisms largely rely on the reasoning capabilities of LLMs, leading to prohibitive computational costs. In this paper, we propose a novel framework, \textit{GAMER}~(Graph-based Action-centric Memory with Episodic Reasoning), that bridges the gap between inference scaling and episodic memory. Our approach models historical reasoning as a dynamic \textit{Action-Centric Graph}. By decoupling the memory mechanism from LLMs, our method can save token/money usage by providing less memory context than memory mechanism baselines. To extract knowledge from the graph effectively, we use a dual-stream Temporal Difference learning mechanism to estimate the positive~(suggestion) and negative~(avoidance) value of action nodes based on past successes and failures. During the inference phase, this learned value function optimizes decision-making bi-directionally, so that positive values provide action suggestions, while negative values indicate high-risk actions. By performing efficient searches on the graph, our method significantly improves the efficiency of inference scaling. Experiments on multiple benchmarks demonstrate that \textit{GAMER} achieves superior performance by \textbf{20.81\%/6.17\%} for success/progress rate compared to vanilla baselines.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
