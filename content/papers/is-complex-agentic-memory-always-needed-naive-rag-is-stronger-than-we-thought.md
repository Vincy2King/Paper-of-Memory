# Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.30755v1
- Published: 2026-10-22
- Updated: 2026-10-22
- Authors: Zhengye Bao, Shengtao Zhang, Haokai Zhang, Shiqi Lou, Muning Wen, Minnan Luo
- Tags: agent, benchmark, conversation, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.30755v1

## One-Sentence Summary
LLM memory is widely used in long-term conversation understanding.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM memory is widely used in long-term conversation understanding.

进一步看，论文的核心做法或实验重点可以概括为：Agentic memory systems often use mutation, structural organization, learned retrieval strategies, or other complex operations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, long-term, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
LLM memory is widely used in long-term conversation understanding. Agentic memory systems often use mutation, structural organization, learned retrieval strategies, or other complex operations. Is this complexity always necessary? We study Raw-RAG, a naive RAG baseline using dense retrieval and reranking over raw history to supply evidence to a reader LLM. Across LoCoMo, LongMemEval, MEME, and MemoryAgentBench, Raw-RAG ranks first among the compared memory systems in six of seven benchmark-model settings, outperforming the strongest compared agentic memory system by 0.13-5.53 points. We investigate why raw-history retrieval remains competitive. Evidence analysis shows that its higher coverage of necessary evidence can offset lower utilization. Useful evidence includes both answer values and the relations and dependency paths needed to derive them. Even complete access to transformed memory stores leaves an accuracy gap relative to raw evidence, highlighting the importance of preserving raw information. These findings challenge the necessity of complex agentic memory for the evaluated conversation tasks and establish naive RAG as an essential baseline.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
