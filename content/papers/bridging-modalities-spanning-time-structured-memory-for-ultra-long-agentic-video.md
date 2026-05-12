# Bridging Modalities, Spanning Time: Structured Memory for Ultra-Long Agentic Video Reasoning

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.08271v1
- Published: 2026-05-08
- Updated: 2026-05-08
- Authors: Jiazheng Li, Chi-Hao Wu, Yunze Liu, Kaize Ding, Jundong Li, Chuxu Zhang
- Tags: agent, benchmark, context, episodic, retrieval
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2605.08271v1

## One-Sentence Summary
Understanding ultra-long videos such as egocentric recordings, live streams, or surveillance footage spanning days to weeks, remains a challenge.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Understanding ultra-long videos such as egocentric recordings, live streams, or surveillance footage spanning days to weeks, remains a challenge.

进一步看，论文的核心做法或实验重点可以概括为：For current multimodal LLMs: even with million-token context windows, frame budgets cover only tens of minutes of densely sampled video, and most evidence is discarded before inference begins.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, episodic, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Understanding ultra-long videos such as egocentric recordings, live streams, or surveillance footage spanning days to weeks, remains a challenge. For current multimodal LLMs: even with million-token context windows, frame budgets cover only tens of minutes of densely sampled video, and most evidence is discarded before inference begins. Memory-augmented and agentic approaches help with scale, but their retrieval remains fragmented across modalities and lacks long-range narrative summaries that span days or weeks. We propose \textbf{MAGIC-Video}, a training-free framework built around a multimodal memory graph with interleaved narrative chain: the graph unifies episodic, semantic, and visual content through six typed edges and supports cross-modal retrieval, while the chain distils long-horizon entity biographies and recurring activity events. At inference time, an agentic loop interleaves graph retrieval with narrative fact injection, covering both the modality and time dimensions of ultra-long video in a single retrieval pipeline. On EgoLifeQA, Ego-R1 and MM-Lifelong, MAGIC-Video consistently outperforms strong general-purpose, long-video, and agentic baselines, with gains of 10.1, 7.4, and 5.9 points over the prior best agentic system on each benchmark. Code is available at https://github.com/lijiazheng0917/MAGIC-video.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
