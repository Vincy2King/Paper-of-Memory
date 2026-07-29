# LazyMem: Retrieve Broadly, Construct Selectively for Efficient Long-Term Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.22690v2
- Published: 2026-07-17
- Updated: 2026-07-28
- Authors: Jing Yu, Yibo Zhao, Jiaming Zhang, Xiang Li
- Tags: agent, compression, context, conversation, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.22690v2

## One-Sentence Summary
Long-term memory enables LLM agents to leverage past interactions, but dialogue histories quickly exceed the context window, forcing agents to retrieve relevant subsets at query...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory enables LLM agents to leverage past interactions, but dialogue histories quickly exceed the context window, forcing agents to retrieve relevant subsets at query time.

进一步看，论文的核心做法或实验重点可以概括为：Because useful evidence is sparse and scattered across verbose conversations, retrieval faces a fundamental tension: broadening recall improves coverage but floods downstream reasoning with noise, while compressing...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression, context, conversation, long-term, retrieval
- 检索关键词命中：agent memory, context memory, long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term memory enables LLM agents to leverage past interactions, but dialogue histories quickly exceed the context window, forcing agents to retrieve relevant subsets at query time. Because useful evidence is sparse and scattered across verbose conversations, retrieval faces a fundamental tension: broadening recall improves coverage but floods downstream reasoning with noise, while compressing memories at write time eases retrieval but irreversibly discards details that future queries may need. We introduce LazyMem, which resolves this tension by deferring all memory construction to query time. Given a retrieved candidate pool, a lightweight model processes it in overlapping parallel windows, selectively retaining and compressing only query-relevant content. The model is trained with supervised fine-tuning followed by reinforcement learning, using a reward that jointly encourages the identification of relevant messages and the generation of compressions that are faithful to the source and useful for answering the query. On LongMemEval, LazyMem-4B achieves an LLM-judge accuracy of 0.85, outperforming the strongest non-oracle baseline while using only 213 answer-context memory tokens, 21.0 times fewer than the baseline. It further generalizes to LoCoMo without target-domain training and reduces mean latency relative to the prior query-time baseline. Code is available at https://github.com/allacnobug/LazyMem.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
