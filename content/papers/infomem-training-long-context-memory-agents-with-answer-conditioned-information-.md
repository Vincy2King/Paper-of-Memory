# InfoMem: Training Long-Context Memory Agents with Answer-Conditioned Information Gain

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.03329v1
- Published: 2026-06-02
- Updated: 2026-06-02
- Authors: Tiancheng Han, Yong Li, Wuzhou Yu, Qiaosheng Zhang, Wenqi Shao
- Tags: agent, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.03329v1

## One-Sentence Summary
Long-context tasks require LLMs to identify and preserve answer-relevant information from large contexts.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-context tasks require LLMs to identify and preserve answer-relevant information from large contexts.

进一步看，论文的核心做法或实验重点可以概括为：Chunk-wise memory agents address this issue by sequentially reading document chunks, updating a compact memory, and generating the final answer from the accumulated memory.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：context memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-context tasks require LLMs to identify and preserve answer-relevant information from large contexts. Chunk-wise memory agents address this issue by sequentially reading document chunks, updating a compact memory, and generating the final answer from the accumulated memory. However, existing RL-based chunk-wise agents either rely on sparse final-answer rewards or use lexical intermediate rewards for memory and retrieval actions. These signals supervise task success or local overlap, but do not directly evaluate whether the final memory supports the ground-truth answer. We propose InfoMem, a reward mechanism for training chunk-wise memory agents that evaluates final-memory utility using answer-conditioned information. InfoMem measures how much the final memory increases the model's per-token log-likelihood of the ground-truth answer. To stabilize RL optimization, InfoMem applies this signal only to successful trajectories and normalizes it before reward composition. Under the same GRPO framework and training budget, InfoMem improves long-context memory-agent performance over comparable memory-agent RL baselines. Analyses show that effective final-memory rewards should operate on successful trajectories, be normalized before reward composition, and be conditioned on the answer rather than the query. Our code is available at https://github.com/GenSouKa1/InfoMem.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
