# SafeHarbor: Hierarchical Memory-Augmented Guardrail for LLM Agent Safety

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.05704v1
- Published: 2026-05-07
- Updated: 2026-05-07
- Authors: Zhe Liu, Zonghao Ying, Wenxin Zhang, Quanchen Zou, Deyue Zhang, Dongdong Yang, Xiangzheng Zhang, Hao Peng
- Tags: agent, context
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2605.05704v1

## One-Sentence Summary
With the rapid evolution of foundation models, Large Language Model (LLM) agents have demonstrated increasingly powerful tool-use capabilities.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：With the rapid evolution of foundation models, Large Language Model (LLM) agents have demonstrated increasingly powerful tool-use capabilities.

进一步看，论文的核心做法或实验重点可以概括为：However, this proficiency introduces significant security risks, as malicious actors can manipulate agents into executing tools to generate harmful content.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
With the rapid evolution of foundation models, Large Language Model (LLM) agents have demonstrated increasingly powerful tool-use capabilities. However, this proficiency introduces significant security risks, as malicious actors can manipulate agents into executing tools to generate harmful content. While existing defensive mechanisms are effective, they frequently suffer from the over-refusal problem, where increased safety strictness compromises the agent's utility on benign tasks. To mitigate this trade-off, we propose \textsc{SafeHarbor}, a novel framework designed to establish precise decision boundaries for LLM agents. Unlike static guidelines, \textsc{SafeHarbor} extracts context-aware defense rules through enhanced adversarial generation. We design a local hierarchical memory system for dynamic rule injection, offering a training-free, efficient, and plug-and-play solution. Furthermore, we introduce an information entropy-based self-evolution mechanism that continuously optimizes the memory structure through dynamic node splitting and merging. Extensive experiments demonstrate that \textsc{SafeHarbor} achieves state-of-the-art performance on both ambiguous benign tasks and explicit malicious attacks, notably attaining a peak benign utility of 63.6\% on GPT-4o while maintaining a robust refusal rate exceeding 93\% against harmful requests. The source code is publicly available at https://github.com/ljj-cyber/SafeHarbor.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
