# GenMem: Generative Symbolic Memory for Self-Evolving Harness

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.34633v1
- Published: 2026-09-28
- Updated: 2026-09-28
- Authors: Xinke Jiang, Tao Feng, Weixuan Xu, Zhixin Zhang, Zhibang Yang, Wentao Zhang, Runchuan Zhu, Xu Chu, Junfeng Zhao, Yasha Wang
- Tags: agent, long-term, retrieval
- Categories: cs.LG
- URL: http://arxiv.org/abs/2609.34633v1

## One-Sentence Summary
Long-term memory supports the self-evolution of LLM agents by retaining experience and skills across tasks and enabling their retrieval, reuse, and revision in subsequent long-...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory supports the self-evolution of LLM agents by retaining experience and skills across tasks and enabling their retrieval, reuse, and revision in subsequent long-horizon decision-making.

进一步看，论文的核心做法或实验重点可以概括为：Yet existing memory management approaches remain limited to discriminative retrieval and to address the sparse, hierarchical, and highly redundant structure of reusable experience: only a small, task-dependent subset...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：long-term memory, memory augmented, memory-augmented
- 来源分类信息：cs.LG

## Abstract Snapshot
Long-term memory supports the self-evolution of LLM agents by retaining experience and skills across tasks and enabling their retrieval, reuse, and revision in subsequent long-horizon decision-making. Yet existing memory management approaches remain limited to discriminative retrieval and to address the sparse, hierarchical, and highly redundant structure of reusable experience: only a small, task-dependent subset of trajectories and memories warrants retention, retrieval, or revision. Learning these operations is further complicated by sparse, delayed, and indirect task-level feedback, with weak supervision across the memory lifecycle. Moreover, continual memory evolution introduces an architectural tension as addressing invariance: stored experience is perpetually revised, yet the addressing interface consumed by learned retrieval policies must remain stable. To address, we present GenMem, which reformulates memory management as generative symbolic addressing. Its core mechanism is the Symbolic Identifier (SID), a multi-level discrete token tuple drawn from a Cartesian-product address space that factorizes a million-scale sparse memory space using fewer than one hundred discrete symbols. Instead of generating ever-changing raw content, the memory agent learns to generate SIDs, while memory evolution rewrites the payload at a fixed address without shifting the address itself. Architecturally, GenMem couples a MemRetriever and a MemEvolver within a multi-agent harness, trained via GRPO with dense process and outcome rewards with two-channels optimization. Under offline memory evolution, experiments spanning ALFWorld, WebShop, multi-hop QA, medical reasoning, and deep research evaluate GenMem against strong memory-augmented baselines...

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
