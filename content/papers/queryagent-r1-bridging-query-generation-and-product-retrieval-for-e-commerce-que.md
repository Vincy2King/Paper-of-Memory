# QueryAgent-R1: Bridging Query Generation and Product Retrieval for E-Commerce Query Recommendation

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.05671v1
- Published: 2026-06-04
- Updated: 2026-06-04
- Authors: Dike Sun, Zheng Zou, Jingtong Zang, Qi Sun, Huaipeng Zhaoand Tao Luo, Xiaoyi Zeng
- Tags: agent, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2606.05671v1

## One-Sentence Summary
Query recommendation in e-commerce search aims to proactively suggest queries that match users' potential interests.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Query recommendation in e-commerce search aims to proactively suggest queries that match users' potential interests.

进一步看，论文的核心做法或实验重点可以概括为：However, existing methods mainly optimize query-level relevance, while neglecting whether the retrieved products align with users' downstream preferences.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CL

## Abstract Snapshot
Query recommendation in e-commerce search aims to proactively suggest queries that match users' potential interests. However, existing methods mainly optimize query-level relevance, while neglecting whether the retrieved products align with users' downstream preferences. This mismatch often leads to high query click through rates (CTR) but low product conversion rates (CVR). To bridge this gap, we propose QueryAgent-R1, a memory-augmented agentic framework that improves end-to-end alignment via chain-of-retrieval optimization. Our QueryAgent-R1 grounds query generation in real inventory retrieval, allowing the agent to validate and refine queries based on retrieved products. We also design a consistency reward in the agentic reinforcement learning (RL) process to jointly optimize query relevance and downstream engagement. In addition, we construct a memory abstraction module for efficient user profiling. To support offline evaluation, we construct two datasets based on both proprietary industrial data and public datasets, on which QueryAgent-R1 consistently outperforms strong baselines. Moreover, on a large scale production platform, QueryAgent-R1 improves Query CTR by 2.9% and guided CVR by 3.1% in online A/B tests.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
