# CMT-RAG: Complementary Memory Traces for Multi-turn Multi-hop RAG

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.26470v1
- Published: 2026-07-29
- Updated: 2026-07-29
- Authors: Lang Zhou, Yingjian Chen, Shuxuan Li, Kun-Yu Lin, Zhilin Zhao
- Tags: benchmark, context, conversation, retrieval
- Categories: cs.CL, cs.IR
- URL: http://arxiv.org/abs/2607.26470v1

## One-Sentence Summary
Multi-turn information-seeking conversations require both multi-hop reasoning and long-range dependency tracking across turns.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multi-turn information-seeking conversations require both multi-hop reasoning and long-range dependency tracking across turns.

进一步看，论文的核心做法或实验重点可以概括为：However, existing RAG systems typically represent conversational memory as raw dialogue history, rewritten queries, or unstructured summaries, making it difficult to recover the specific prior reasoning steps and...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, conversation, retrieval
- 检索关键词命中：conversational memory, persistent memory
- 来源分类信息：cs.CL, cs.IR

## Abstract Snapshot
Multi-turn information-seeking conversations require both multi-hop reasoning and long-range dependency tracking across turns. However, existing RAG systems typically represent conversational memory as raw dialogue history, rewritten queries, or unstructured summaries, making it difficult to recover the specific prior reasoning steps and evidence required for follow-up queries. Our key insight is to align conversational memory with retrieval by representing dialogue context as sub-question-level reasoning traces. Building on this insight, we introduce MuMu-QA, a benchmark for multi-turn multi-hop RAG with explicit cross-turn sub-question dependency annotations, and CMT-RAG, a complementary memory framework for this setting. At each turn, CMT-RAG employs a state-space trace generator, whose recurrent state serves as runtime memory, to incorporate recent conversational context and decompose the current query into structured trace drafts containing retrieval-oriented sub-questions and dependencies on earlier traces. It then grounds these drafts with retrieved evidence and stores them as persistent memory traces in a session-level DAG, enabling future turns to efficiently recover relevant prior reasoning and evidence. Experiments on MuMu-QA and corpus-level RAG benchmarks show that CMT-RAG consistently outperforms five categories of RAG baselines in answer accuracy.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
