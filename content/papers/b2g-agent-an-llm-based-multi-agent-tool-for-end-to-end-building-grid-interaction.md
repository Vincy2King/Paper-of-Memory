# B2G-Agent: An LLM-Based Multi-Agent Tool for End-to-End Building-Grid Interactions

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.19036v1
- Published: 2026-11-14
- Updated: 2026-11-14
- Authors: Xueyuan Cui, Qian Zhang, Xiaochen Liu, Yi Wang
- Tags: agent, retrieval
- Categories: cs.HC
- URL: http://arxiv.org/abs/2611.19036v1

## One-Sentence Summary
Buildings are major electricity consumers and can interact with distribution network dispatch through flexible power scheduling.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Buildings are major electricity consumers and can interact with distribution network dispatch through flexible power scheduling.

进一步看，论文的核心做法或实验重点可以概括为：These interactions require distribution network operators (DNOs) and building energy managers (BEMs) to reconcile their operational constraints and perform complex cross-field computations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.HC

## Abstract Snapshot
Buildings are major electricity consumers and can interact with distribution network dispatch through flexible power scheduling. These interactions require distribution network operators (DNOs) and building energy managers (BEMs) to reconcile their operational constraints and perform complex cross-field computations. The lack of cross-domain expertise and unified computational workflows could lead to inefficient or physically infeasible interactions. To address this bottleneck, we develop an end-to-end large language model (LLM)-based multi-agent tool, B2G-Agent, that bridges DNOs and BEMs. The tool deploys three collaborative agents: a Translator for bidirectional cross-domain semantic mapping via hybrid retrieval-augmented generation (RAG); an Actor for automated configuration and execution of joint simulation and optimization through directed acyclic graphs; and a Reviewer for memory-augmented reflective failure diagnosis. This workflow abstracts away cross-field modeling complexities and enables both sides to focus on high-level operational decisions. Comprehensive evaluations across 200 synthesized tasks show that B2G-Agent improves the interaction quality score from 66.71 to 85.57 and increases the task success rate from 38.0% to 69.0% over the baseline while satisfying operational constraints. The open-source tool and interface are available at https://github.com/hkuedl/B2G-Agent.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
