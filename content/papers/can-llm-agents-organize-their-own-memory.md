# Can LLM Agents Organize Their Own Memory?

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.11929v1
- Published: 2026-11-09
- Updated: 2026-11-09
- Authors: Zichuan Fu, Junjia Qi, Wenlin Zhang, Yimin Deng, Shirong Wang, Jinyang Li, Xian Wu, Xiangyu Zhao
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.11929v1

## One-Sentence Summary
In most LLM agents, weights are fixed after deployment, so new information must be retained in external memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：In most LLM agents, weights are fixed after deployment, so new information must be retained in external memory.

进一步看，论文的核心做法或实验重点可以概括为：Existing approaches often rely on predefined records and fixed organizational rules, which cannot readily accommodate evolving tasks and interactions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
In most LLM agents, weights are fixed after deployment, so new information must be retained in external memory. Existing approaches often rely on predefined records and fixed organizational rules, which cannot readily accommodate evolving tasks and interactions. This raises the question: can LLM agents organize their own memory using ordinary documents? We introduce self-organized memory (SoMem), a framework that stores memory in linked documents. The agent decides what to summarize, how to group related information, and when to revise existing topics, and every summary it produces stays linked to the original interactions as evidence. The runtime validates updates and automatically derives temporal, relational, and recent-memory views from the organized content. At query time, the agent chooses what to search and read, following document links and inspecting original evidence as needed. On LoCoMo, BEAM-100K, and LongMemEval-S, SoMem outperforms the strongest baseline by 2.66, 3.10, and 2.00 percentage points, respectively. The constructed memory can be reused across models, and additional reasoning effort can further improve answer quality. These findings demonstrate the feasibility of agents organizing and using their own persistent memory through ordinary documents. Code is available at: https://github.com/Qi202/SoMem.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
