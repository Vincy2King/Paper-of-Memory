# Beyond the Final Embedding: Retrieving Memories from Token-Level Evidence

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.13277v1
- Published: 2026-10-09
- Updated: 2026-10-09
- Authors: Han Luo, Zhan Zhuang, Xu He, Jujia Zhao, Yu Li, Suqin Yuan, Dong Li, Lei Feng
- Tags: benchmark, context, conversation, long-term, retrieval
- Categories: cs.IR, cs.CL
- URL: http://arxiv.org/abs/2610.13277v1

## One-Sentence Summary
Memory-augmented assistants retrieve evidence from stored conversations and documents to answer queries.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-augmented assistants retrieve evidence from stored conversations and documents to answer queries.

进一步看，论文的核心做法或实验重点可以概括为：Most embedding-based retrievers compare single-vector representations of queries and memories, even when relevance depends on a small part of the content.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：long-term memory, memory augmented, memory benchmark, memory benchmarks, memory-augmented, retrieval memory
- 来源分类信息：cs.IR, cs.CL

## Abstract Snapshot
Memory-augmented assistants retrieve evidence from stored conversations and documents to answer queries. Most embedding-based retrievers compare single-vector representations of queries and memories, even when relevance depends on a small part of the content. Such local evidence can be matched to queries using the contextual token representations already computed by the same embedding models. Our method uses sparse token matching to improve retrieval without additional training. Each query token retrieves a small set of matching tokens across candidate memories. The matching scores are aggregated for each memory and combined with whole-memory similarity to rank memories. An optional low-rank query adapter can be trained with supervision while keeping the encoder and stored memory representations fixed. Our method improves retrieval across eight benchmarks and multiple model families without additional training. Query adaptation further increases the gains to 13.3 and 14.3 percentage points in average Recall@10 and NDCG@10 on Qwen3-Embedding-4B. These retrieval gains translate into higher question-answering accuracy on long-term memory benchmarks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
