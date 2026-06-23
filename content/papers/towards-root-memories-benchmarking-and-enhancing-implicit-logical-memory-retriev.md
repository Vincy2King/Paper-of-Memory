# Towards Root Memories: Benchmarking and Enhancing Implicit Logical Memory Retrieval for Personalized LLMs

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.23283v1
- Published: 2026-06-22
- Updated: 2026-06-22
- Authors: Hongxun Ding, Xiang Yu, Chengbing Wang, Jianfei Xiao, Keqin Bao, Wenjie Wang, Xiangnan He
- Tags: agent, benchmark, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2606.23283v1

## One-Sentence Summary
Memory systems are essential for personalized Large Language Models (LLMs).

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory systems are essential for personalized Large Language Models (LLMs).

进一步看，论文的核心做法或实验重点可以概括为：However, existing retrieval methods in these systems primarily rely on semantic similarity, potentially missing logically critical memories with limited semantic overlap.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term, retrieval
- 检索关键词命中：memory benchmark, memory benchmarks, memory retrieval
- 来源分类信息：cs.CL

## Abstract Snapshot
Memory systems are essential for personalized Large Language Models (LLMs). However, existing retrieval methods in these systems primarily rely on semantic similarity, potentially missing logically critical memories with limited semantic overlap. Current benchmarks remain inadequate for evaluating this problem. To address this gap, we construct IMLogic, the first high-quality benchmark targeting implicit logical memory retrieval in long-dialogue scenarios. Motivated by this challenge, we introduce root memory, a structured, decision-preserving representation that distills reusable personalized logic from long-term user histories. We then propose RootMem, a plug-and-play framework that first distills raw histories into structured root memories and then uses an LLM-based router to activate logically relevant ones, complementing semantic retrieval with personalized decision logic. Extensive experiments demonstrate that RootMem significantly outperforms the strongest retrieval baselines and consistently boosts the accuracy of existing memory agents. Our benchmark and codes will be available at https://anonymous.4open.science/r/IMLogic-DBB3.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
