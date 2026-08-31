# ContextPilot: Teaching Agents for Proactive Context Management via Fine-grained RL

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.28476v1
- Published: 2026-08-28
- Updated: 2026-08-28
- Authors: Zhuoshi Pan, Qizhi Pei, Junru Lu, Honglin Lin, H. Vicky Zhao, Di Yin, Xing Sun
- Tags: agent, benchmark, compression, context, long-term
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.28476v1

## One-Sentence Summary
Long-horizon agentic tasks require large language models (LLMs) to iteratively retrieve, integrate, and maintain dispersed information across multi-turn interactions, but...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon agentic tasks require large language models (LLMs) to iteratively retrieve, integrate, and maintain dispersed information across multi-turn interactions, but preserving all interaction histories leads to...

进一步看，论文的核心做法或实验重点可以概括为：Recent proactive context management methods allow models to edit their own working context with specialized tools, yet they still face three key limitations: (1) a limited toolset restricted to search, deletion, and...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, context, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-horizon agentic tasks require large language models (LLMs) to iteratively retrieve, integrate, and maintain dispersed information across multi-turn interactions, but preserving all interaction histories leads to a continuously growing working context. Recent proactive context management methods allow models to edit their own working context with specialized tools, yet they still face three key limitations: (1) a limited toolset restricted to search, deletion, and summarization, with no support for global planning, long-term memory, and adaptive compression; (2) inefficient exploration that treats context management actions uniformly despite their heterogeneous impacts on final outcomes; and (3) coarse-grained credit assignment that assigns the final trajectory-level reward to all intermediate context editing actions during RL. To bridge these gaps, we introduce ContextPilot, a proactive context management framework for long-horizon agentic reasoning. Our approach systematically augments the toolset with planning, long-term memory, and soft context offloading tools. We further propose an RL method tailored for context management, which uses context and entropy variation to identify critical editing decisions for branch sampling and estimates action-level advantages from all branched trajectories that pass through the corresponding context editing action. Experiments on long-context QA and deep search tasks show that ContextPilot achieves stronger performance with a more compact working context, consistently outperforming existing baselines across various base models and benchmarks. Code is available at https://github.com/Tencent/ContextPilot.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
