# Agentic Recommender System with Hierarchical Belief-State Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.14401v1
- Published: 2026-05-14
- Updated: 2026-05-14
- Authors: Xiang Shen, Yuhang Zhou, Yifan Wu, Zhuokai Zhao, Siyu Lin, Lei Huang, Qianqian Zhong, Lizhu Zhang, Benyu Zhang, Xiangjun Fan, Hong Yan
- Tags: agent, benchmark
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2605.14401v1

## One-Sentence Summary
Memory-augmented LLM agents have advanced personalized recommendation, yet existing approaches universally adopt flat memory representations that conflate ephemeral signals with...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-augmented LLM agents have advanced personalized recommendation, yet existing approaches universally adopt flat memory representations that conflate ephemeral signals with stable preferences, and none provides a...

进一步看，论文的核心做法或实验重点可以概括为：We propose MARS (Memory-Augmented Agentic Recommender System), a framework that treats recommendation as a partially observable problem and maintains a structured belief state that progressively abstracts noisy...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Memory-augmented LLM agents have advanced personalized recommendation, yet existing approaches universally adopt flat memory representations that conflate ephemeral signals with stable preferences, and none provides a complete lifecycle governing how memory should evolve. We propose MARS (Memory-Augmented Agentic Recommender System), a framework that treats recommendation as a partially observable problem and maintains a structured belief state that progressively abstracts noisy behavioral observations into a compact estimate of user preferences. MARS organizes this belief state into three tiers: event memory buffers raw signals, preference memory maintains fine-grained mutable chunks with explicit strength and evidence tracking, and profile memory distills all preferences into a coherent natural language narrative. A complete lifecycle of six operations -- extraction, reinforcement, weakening, consolidation, forgetting, and resynthesis -- is adaptively scheduled by an LLM-based planner rather than fixed-interval heuristics. Experiments on four InstructRec benchmark domains show that \ours achieves state-of-the-art performance with average improvements of 26.4% in HR@1 and 10.3% in NDCG@10 over the strongest baselines with further gains from agentic scheduling in evolving settings.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
