# AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.19847v1
- Published: 2026-06-18
- Updated: 2026-06-18
- Authors: Yanyu Yao, Shangze Li, Zhi Zheng, Hui Zheng, Qi Liu, Tong Xu, Enhong Chen
- Tags: agent, benchmark, context, episodic, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2606.19847v1

## One-Sentence Summary
Large language models (LLMs) demonstrate strong reasoning and generation abilities, but their fixed context windows limit long-term information accumulation and reuse across...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models (LLMs) demonstrate strong reasoning and generation abilities, but their fixed context windows limit long-term information accumulation and reuse across multi-session interactions.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory-augmented systems often construct memory in a coarse and unstable manner, relying on inefficient memory representations or unstable unconstrained updates.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, episodic, long-term, retrieval
- 检索关键词命中：long-term memory, memory augmented, memory-augmented
- 来源分类信息：cs.CL

## Abstract Snapshot
Large language models (LLMs) demonstrate strong reasoning and generation abilities, but their fixed context windows limit long-term information accumulation and reuse across multi-session interactions. Existing memory-augmented systems often construct memory in a coarse and unstable manner, relying on inefficient memory representations or unstable unconstrained updates. To address these challenges, we propose AtomMem, a long-term memory system designed for value-dense storage and stable memory evolution. AtomMem introduces a Fact Executor, which selectively extracts high value atomic facts from long form interactions to serve as highly efficient memory representations. Subsequently, AtomMem organizes these facts into hierarchical event structures and temporal profiles, capturing coherent episodic contexts and tracking dynamically evolving user attributes over time. During retrieval, the system activates an associative memory graph to connect fragmented memories. Experiments on the LoCoMo benchmark confirm that AtomMem achieves state-of-the-art performance across various reasoning tasks, offering a scalable and economically viable solution for deploying intelligent personalized agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
