# Memory Retrieval for Changing Preferences

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.02976v1
- Published: 2026-06-02
- Updated: 2026-06-02
- Authors: Yuehan Qin, Li Li, Linxin Song, Wei Yang, Jiate Li, Yuqing Yang, Yue Zhao
- Tags: benchmark, context, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2606.02976v1

## One-Sentence Summary
Long-context dialogue systems must decide both when to access memory and which parts of the interaction history are relevant.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-context dialogue systems must decide both when to access memory and which parts of the interaction history are relevant.

进一步看，论文的核心做法或实验重点可以概括为：Existing approaches typically rely on heuristic retrieval signals or always-on memory usage, failing to account for the changing and potentially inconsistent nature of user preferences.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, retrieval
- 检索关键词命中：memory benchmarks, memory retrieval
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-context dialogue systems must decide both when to access memory and which parts of the interaction history are relevant. Existing approaches typically rely on heuristic retrieval signals or always-on memory usage, failing to account for the changing and potentially inconsistent nature of user preferences. In this work, we propose a unified framework for memory access and selection based on changing preferences. We formulate personalized memory retrieval as identifying which historical turns provide evidence about a user's latent preference state, rather than relying on surface-level semantic similarity. To this end, we quantify the utility of each memory turn using a Bayes factor, defined as the improvement in the model's likelihood of the reference response when the turn is included in context. This provides a principled measure of evidence strength and a unified signal for both memory access and selection. By framing memory retrieval as utility estimation, the model learns to identify salient turns and regulate memory usage based on expected utility. Experiments on four heterogeneous memory benchmarks show that our approach outperforms existing embedding-based retrieval on long-context, preference-intensive tasks where modeling changing preferences is essential, while remaining competitive in low-density regimes where semantic similarity suffices.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
