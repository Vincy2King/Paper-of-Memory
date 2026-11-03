# Delivered, Not Used: Evaluating Agent Memory at Its Point of Use

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.01718v1
- Published: 2026-11-01
- Updated: 2026-11-01
- Authors: Changran Xu, Zeju Li, Qiang Xu
- Tags: agent, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.01718v1

## One-Sentence Summary
Task success, retrieval quality, and cost do not show whether an LLM agent used a delivered memory or what followed from that use.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Task success, retrieval quality, and cost do not show whether an LLM agent used a delivered memory or what followed from that use.

进一步看，论文的核心做法或实验重点可以概括为：We introduce MemUse, which evaluates memory at its point of use in recorded trajectories: each memory delivery is compared with what the agent could already see and followed through the agent's later actions and their...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Task success, retrieval quality, and cost do not show whether an LLM agent used a delivered memory or what followed from that use. We introduce MemUse, which evaluates memory at its point of use in recorded trajectories: each memory delivery is compared with what the agent could already see and followed through the agent's later actions and their consequences. An agentic judge rates each delivered entry's relevance, accuracy, novelty, influence, and observed effect; programmatic checks enforce complete reading of cited evidence, and fixed rules aggregate the ratings into verdicts linked to memory histories and delivery cost. On 8,000 SWE-bench Verified episodes from three memory systems, resolve rates stay within 0.4 percentage points of a no-memory baseline, yet MemUse shows that most delivered entries were irrelevant, most relevant entries went unused, and in two systems most deliveries restated content the agent could still see. It also surfaces effects that outcomes hide: 23.2\% of episodes with beneficial memory use still failed, and 5 of 16 with harmful use still succeeded.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
