# KITE: Retrieval as a Decision Procedure for Long-Term Conversational Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.41521v1
- Published: 2026-10-30
- Updated: 2026-10-30
- Authors: Feng Li, Kailun Tan, Zhibo Zhou, Youxiang Wang, Lejun Liu, Huaigu Li, Fei Du, Huilong An
- Tags: agent, context, conversation, long-term, retrieval
- Categories: cs.IR
- URL: http://arxiv.org/abs/2610.41521v1

## One-Sentence Summary
Many long-term memory systems for LLM agents are built around embedding-based retrieval.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Many long-term memory systems for LLM agents are built around embedding-based retrieval.

进一步看，论文的核心做法或实验重点可以概括为：Al- though effective for semantic matching, similarity ranking alone does not establish whether re- trieved memories satisfy the conditions implied by a question.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, long-term, retrieval
- 检索关键词命中：conversational memory, long-term memory
- 来源分类信息：cs.IR

## Abstract Snapshot
Many long-term memory systems for LLM agents are built around embedding-based retrieval. Al- though effective for semantic matching, similarity ranking alone does not establish whether re- trieved memories satisfy the conditions implied by a question. In this paper, we introduce KITE (Knowledge-Indexed Temporal Evidence), a vector-free framework that formulates memory re- trieval as an explicit decision procedure. KITE organizes multi-session conversations as structured knowledge indexed by a governed topic vocabulary, which evolves through controlled expansion and consolidation. At query time, questions are compiled into inspectable retrieval plans over the same knowledge index that guides memory construction. The plans are then executed through fixed lookup and ranking operations, while sparse lexical retrieval recovers surface details omitted from the structured representation. Experiments on LoCoMo and LongMemEval-S show that KITE achieves 93.5% and 86.0% accuracy while using only about 1.6k reader-context tokens per ques- tion. These results demonstrate that conversational memory can move beyond similarity ranking by unifying memory construction and query compilation around a governed index, turning retrieval into an inspectable decision procedure for determining which evidence satisfies the question.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
