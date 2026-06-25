# Memory Makes the Difference: Evaluating How Different Memory Roles Shape Conversational Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.25361v1
- Published: 2026-06-24
- Updated: 2026-06-24
- Authors: Yuxin Wang, Paul Thomas, Zhiwei Yu, Yuan Gao, Saeed Hassanpour, Soroush Vosoughi, Robert Sim, Nick Craswell
- Tags: agent, context, conversation, long-term
- Categories: cs.CL, cs.AI, cs.IR
- URL: http://arxiv.org/abs/2606.25361v1

## One-Sentence Summary
Prior research on memory mechanism in RAG-based conversational system has emphasized how memory is stored and retrieved.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Prior research on memory mechanism in RAG-based conversational system has emphasized how memory is stored and retrieved.

进一步看，论文的核心做法或实验重点可以概括为：However, far less is known about how memories with different functional roles influence response quality.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, long-term
- 检索关键词命中：conversational memory, retrieval memory
- 来源分类信息：cs.CL, cs.AI, cs.IR

## Abstract Snapshot
Prior research on memory mechanism in RAG-based conversational system has emphasized how memory is stored and retrieved. However, far less is known about how memories with different functional roles influence response quality. Specifically, how they shape an agent's responses under varying conversational contexts and whether they lead to substantively different response behaviors. Existing evaluations in conversational system are also largely reference-based, insufficiently capturing the nuances in responses that may address users' preferences differently. In this work, we probe the impact of different memory types in shaping agents' responses. We present a fine-grained taxonomy of conversational memory, classify retrieved memories into different role types, and design a user-centric evaluation framework that simulates user perspectives. Through comparative experiments on long-term datasets and frontier LLMs, our analysis reveal many differentiated effects of memories: e.g., clarifying memory improves responses' factual accuracy and constraint awareness, making them more correct and personalized; irrelevant memory reduces topic relevance and degrades constraint awareness. Despite the power of frontier LLMs, these findings shed light on how different memory types can be leveraged to produce more personalized responses and inspire further research in this direction.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
