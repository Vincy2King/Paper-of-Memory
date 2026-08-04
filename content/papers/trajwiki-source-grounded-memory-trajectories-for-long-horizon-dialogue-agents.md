# TrajWiki: Source-Grounded Memory Trajectories for Long-Horizon Dialogue Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.00967v1
- Published: 2026-08-02
- Updated: 2026-08-02
- Authors: Jingyu Sun, Yuyang Xue, Mingyang Li, Zhengtao Yao, Jiachen Li, Yang Cui, Wenhao Cai, Haozhe Liu, Fangying Wang, Magdalene Katharina Montgomery, Syed Murtuza Baker, Hongpeng Zhou
- Tags: agent, context, conversation, episodic, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.00967v1

## One-Sentence Summary
Large language model agents have shown strong capabilities in generating coherent and contextually appropriate responses, yet robust long-horizon dialogue remains limited by the...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model agents have shown strong capabilities in generating coherent and contextually appropriate responses, yet robust long-horizon dialogue remains limited by the lack of external memory that is...

进一步看，论文的核心做法或实验重点可以概括为：Existing memory-augmented agents often store memories as isolated records or overwritable states, making it difficult to preserve how information originates, evolves, conflicts, or becomes obsolete over time.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, episodic, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language model agents have shown strong capabilities in generating coherent and contextually appropriate responses, yet robust long-horizon dialogue remains limited by the lack of external memory that is traceable, updatable, and diagnostically transparent. Existing memory-augmented agents often store memories as isolated records or overwritable states, making it difficult to preserve how information originates, evolves, conflicts, or becomes obsolete over time. We propose TrajWiki, a trajectory-based memory framework for long-horizon conversational agents. Instead of treating memory as static entries, TrajWiki represents each memory as a source-grounded evolution trajectory, maintained through immutable episodic snapshots and claim-level operations such as ADD, REVISE, and DEPRECATE. To reduce fragmentation and retrieval cost, TrajWiki further introduces Memory Wiki, a persistent intermediate layer that incrementally compiles dialogue history into structured and interlinked wiki pages capturing salient entities, events, quantities, topics, and conflicts. At inference time, queries are routed hierarchically from relevant wiki pages to linked memory trajectories, then to corresponding snapshots and source messages for evidence-grounded answer synthesis. Experiments on LoCoMo and MedMT show that TrajWiki improves long-horizon dialogue performance across both open-source and closed-source LLM backbones, while providing greater interpretability and diagnostic visibility into memory evolution, retrieval failures, and answer generation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
