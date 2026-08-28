# When Memory Takes Gradients: Collaborative Vector Memory for Agentic Recommender Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.26895v1
- Published: 2026-08-27
- Updated: 2026-08-27
- Authors: Hanchong Chen, Xing Tang, Lingjie Li, Xiongfeng Shan, Xiuqiang He
- Tags: agent, benchmark, context
- Categories: cs.IR, cs.AI
- URL: http://arxiv.org/abs/2608.26895v1

## One-Sentence Summary
Agentic recommender systems ground each decision of a large language model (LLM) in a persistent memory of the user, and in existing agents that memory is text: a narrative...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agentic recommender systems ground each decision of a large language model (LLM) in a persistent memory of the user, and in existing agents that memory is text: a narrative written and maintained by further LLM calls.

进一步看，论文的核心做法或实验重点可以概括为：Text limits this memory in two ways.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：agent memory, persistent memory
- 来源分类信息：cs.IR, cs.AI

## Abstract Snapshot
Agentic recommender systems ground each decision of a large language model (LLM) in a persistent memory of the user, and in existing agents that memory is text: a narrative written and maintained by further LLM calls. Text limits this memory in two ways. It is updated one rewrite at a time, so exploiting the full interaction history is prohibitively expensive; and collaborative evidence, graded similarity over an entire catalog, does not survive translation into sentences. We propose CoVeMem (Collaborative Vector Memory), which vectorizes the collaborative core of the agent's memory. Frozen LightGCN user and item states form the memory bank; at each decision, the candidate set itself retrieves the most relevant historical states, which enter the LLM's context as soft tokens alongside a light textual profile. Contrastive alignment to item-semantic anchors, followed by listwise co-training with masked candidates, teaches the model to read these states and to rank through them; a pointwise yes/no readout scores each candidate. Across four instruction-grounded recommendation benchmarks, CoVeMem matches or exceeds the strongest collaborative text-memory agent on 19 of 20 metric cells while requiring zero additional LLM calls for memory maintenance beyond the shared static profile, against per-interaction calls for text memory. The memory now takes gradients: the full interaction history, out of reach for text, becomes available as training data for what the agent remembers and for how it reads what it remembers.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
