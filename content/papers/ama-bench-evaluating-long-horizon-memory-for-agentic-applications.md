# AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications

- Source: OpenReview
- Venue: ICLR 2026 Workshop MemAgents Oral
- Paper ID: openreview:GoSVL7mLcM
- Published: 2026-03-03
- Updated: 2026-04-25
- Authors: Yujie Zhao, Boqin Yuan, Junbo Huang, Haocheng Yuan, Zhongming Yu, Lanxiang Hu, Haozhou Xu, Abhilash Shankarampeta, Zimeng Huang, Wentao Ni, Yuandong Tian, Jishen Zhao
- Tags: agent, benchmark, retrieval
- Categories: ICLR.cc/2026/Workshop/MemAgent/-/Submission
- URL: https://openreview.net/forum?id=GoSVL7mLcM

## One-Sentence Summary
Large Language Models (LLMs) are deployed as autonomous agents in increasingly complex applications, where enabling long horizon memory is critical for achieving strong...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ICLR 2026 Workshop MemAgents Oral` 这个 venue 相关。

从摘要来看，作者主要关注的是：Large Language Models (LLMs) are deployed as autonomous agents in increasingly complex applications, where enabling long horizon memory is critical for achieving strong performance.

进一步看，论文的核心做法或实验重点可以概括为：However, a significant gap exists between practical applications and current evaluation standards for agent memory: existing benchmarks primarily focus on dialogue centric, human agent interactions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ICLR 2026 Workshop MemAgents Oral
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：ICLR.cc/2026/Workshop/MemAgent/-/Submission

## Abstract Snapshot
Large Language Models (LLMs) are deployed as autonomous agents in increasingly complex applications, where enabling long horizon memory is critical for achieving strong performance. However, a significant gap exists between practical applications and current evaluation standards for agent memory: existing benchmarks primarily focus on dialogue centric, human agent interactions. In reality, agent memory consists of a continuous stream of agent environment interactions that are primarily composed of machine generated representations. To bridge this gap, we introduce AMA Bench (Agent Memory with Any Length) to evaluate long horizon memory for LLMs in real agentic applications. It features two key components: (1) a set of real world agentic trajectories across representative agentic applications paired with expert curated QA, and (2) a set of synthetic agentic trajectories that scale to arbitrary horizons paired with rule based QA. Our comprehensive study shows that existing memory systems underperform on AMA Bench primarily because they suffer from a loss of causality and objective information, and are constrained by the lossy nature of similarity based retrieval employed by many memory systems. To address these limitations, we propose AMA Agent, an effective memory system featuring a causality graph and tool augmented retrieval. Our results demonstrate that AMA Agent achieves 57.22% average accuracy on AMA Bench, surpassing the strongest memory system baselines by 11.16%.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
