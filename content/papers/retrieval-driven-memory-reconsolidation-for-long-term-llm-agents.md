# Retrieval-Driven Memory Reconsolidation for Long-Term LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.16053v1
- Published: 2026-09-13
- Updated: 2026-09-13
- Authors: Yuanyi Song, Yukai Wang, Xinbei Ma, Zhihui Fu, Jianghao Lin, Weiwen Liu, Jun Wang, Huarong Deng, Yong Yu, Weinan Zhang
- Tags: agent, long-term, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2609.16053v1

## One-Sentence Summary
Long-term memory is essential for LLM-based agents operating over extended interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory is essential for LLM-based agents operating over extended interactions.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory systems primarily update memory when new information arrives, treating retrieval as the endpoint of memory access rather than a driver of memory evolution.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Long-term memory is essential for LLM-based agents operating over extended interactions. Existing memory systems primarily update memory when new information arrives, treating retrieval as the endpoint of memory access rather than a driver of memory evolution. Consequently, retrieval feedback is rarely exploited to reorganize memory for future access continuously. Moreover, most existing approaches rely on predefined memory structures together with fixed retrieval pipelines, limiting the agent's ability to organize and evolve its own memory autonomously. Inspired by memory reconsolidation in cognitive neuroscience, we propose \textbf{REALM}, a \textbf{r}econsolidation-\textbf{e}volution \textbf{a}gentic \textbf{l}ong-term \textbf{m}emory framework. It models long-term memory as a continual lifecycle by autonomously organizing memories into a heterogeneous cognitive graph, retrieving evidence via adaptively composed graph-search atoms, and continually reconsolidating memories based on retrieval feedback. REALM achieves an average accuracy of 75.97\% on LoCoMo and 65.11\% on LongMemEval, outperforming the strongest baselines by 7.17 and 1.31 points respectively. Ablation studies confirm that memory reconsolidation consistently boosts performance, with further analyses revealing that it progressively reorganizes related memory units into more coherent local structures for collective evidence recall and utilization during reasoning. These results suggest that retrieval-driven memory reconsolidation provides an effective mechanism for continually evolving long-term memory in LLM agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
