# GASim: A Graph-Accelerated Hybrid Framework for Social Simulation

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.07692v1
- Published: 2026-05-08
- Updated: 2026-05-08
- Authors: Xuan Zhou, Yanhui Sun, Hantao Yao, Allen He, Yongdong Zhang, Wu Liu
- Tags: agent, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.07692v1

## One-Sentence Summary
Large-scale social simulators are essential for studying complex social patterns.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large-scale social simulators are essential for studying complex social patterns.

进一步看，论文的核心做法或实验重点可以概括为：Prior work explores hybrid methods to scale up simulations, combining large language models (LLM)-based agents with numerical agent-based models (ABM).

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.AI

## Abstract Snapshot
Large-scale social simulators are essential for studying complex social patterns. Prior work explores hybrid methods to scale up simulations, combining large language models (LLM)-based agents with numerical agent-based models (ABM). However, this incurs high latency due to expensive memory retrieval and sequential ABM execution. To address this challenge, we propose GASim, a graph-accelerated hybrid multi-agent framework for large-scale social simulations. For core agents driven by LLM, GASim introduces Graph-Optimized Memory (GOM) to replace intensive LLM-based retrieval pipelines with lightweight propagation over a sparse memory graph. For the majority of ordinary agents, GASim employs Graph Message Passing (GMP), substituting sequential ABM execution with parallel updates by fine-grained feature aggregation and Graph Attention Network. We further introduce Entropy-Driven Grouping (EDG) that coordinates this hybrid partitioning, leveraging information entropy to dynamically identify emergent core agents situated in information-diverse neighborhoods. Extensive experiments show that GASim not only delivers a substantial 9.94-fold end-to-end speedup over the traditional hybrid framework but also consumes less than 20% of baseline tokens, significantly reducing costs while preserving strong alignment with real-world public opinion trends. Our code is available at https://github.com/Jasmine0201/GASim.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
