# TAGGRAPH: Tag-Augmented Graphs for Graph Retrieval of Agent Persistent Histories

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.38353v1
- Published: 2026-09-29
- Updated: 2026-09-29
- Authors: Yu-Su Chen, Yu-Jung Liang, Pengtao Xie
- Tags: agent, conversation, long-term, retrieval
- Categories: cs.IR, cs.AI
- URL: http://arxiv.org/abs/2609.38353v1

## One-Sentence Summary
Long-term memory lets LLM agents recall past interactions and remain consistent across sessions, but memory systems are hard to compare because they often vary in...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory lets LLM agents recall past interactions and remain consistent across sessions, but memory systems are hard to compare because they often vary in representation, indexing, retrieval, and evaluation.

进一步看，论文的核心做法或实验重点可以概括为：We present a controlled evaluation framework based on shared 5W-style conversational memories.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, long-term, retrieval
- 检索关键词命中：conversational memory
- 来源分类信息：cs.IR, cs.AI

## Abstract Snapshot
Long-term memory lets LLM agents recall past interactions and remain consistent across sessions, but memory systems are hard to compare because they often vary in representation, indexing, retrieval, and evaluation. We present a controlled evaluation framework based on shared 5W-style conversational memories. Localized graph configurations traverse a common base graph; AdaptiveGraph adds chronological edges and Personalized PageRank diffusion. We also evaluate BM25 over the same extracted notes and OpenClaw as a raw-input external reference. Retrieval rankings vary across memory settings. On LongMemEval-S, AdaptiveGraph is the strongest graph configuration at 0.844 MRR, but BM25 reaches 0.867 and OpenClaw 0.880. On ATANT Core, localized graph traversal outperforms diffusion and BM25, whereas BM25 leads the stress rounds. Reducing LongMemEval-S within the tested range does not reproduce the ATANT diffusion penalty, but the smallest tested store remains larger than ATANT Core, so store size cannot be ruled out. The penalty also persists under a permissive content-match criterion. Vocabulary normalization and extraction quality substantially affect graph retrieval, and missing extraction tags are common among top-five misses. Retrieval strategies should therefore be evaluated jointly with the memory setting and against strong lexical baselines.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
