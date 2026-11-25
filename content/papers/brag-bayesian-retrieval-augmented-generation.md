# BRAG: Bayesian Retrieval Augmented Generation

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.31656v1
- Published: 2026-11-23
- Updated: 2026-11-23
- Authors: Javier Movellan, Manjot Bilkhu, Young-mok Jung, Sirajul Salekin, Henry Tran, Zhao Huang
- Tags: agent, benchmark, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.31656v1

## One-Sentence Summary
Retrieval-augmented generation (RAG) ranks memory chunks by semantic similarity to the query.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Retrieval-augmented generation (RAG) ranks memory chunks by semantic similarity to the query.

进一步看，论文的核心做法或实验重点可以概括为：Many methods improve on this by learning from feedback on what was retrieved, but each is a separate heuristic, with no account of when it is the right choice.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term, retrieval
- 检索关键词命中：memory benchmarks
- 来源分类信息：cs.AI

## Abstract Snapshot
Retrieval-augmented generation (RAG) ranks memory chunks by semantic similarity to the query. Many methods improve on this by learning from feedback on what was retrieved, but each is a separate heuristic, with no account of when it is the right choice. We introduce BRAG, a generative model of retrieval with use. Each chunk generates the queries it answers from a mixture of von Mises-Fisher components anchored at its original embedding, and each chunk has a latent utility that drifts over time. The model gives the optimal inference, a closed-form filter that stores a few keys and two scalars per chunk and updates them online from the labels of a curator, and it frames retrieval as a control problem. It also shows when existing methods are optimal. Query averaging, Rocchio-style feedback and frequency reranking are special cases with fixed parameters, NUDGE is the case of one key per chunk with no dynamics, and LADER the limit of one key per past query. On two public long-term memory benchmarks, BRAG matches these methods on queries asked before, as expected, because when nothing changes over time the assumptions behind these special cases hold. On harder problems, where a new chunk makes an old one obsolete, BRAG outscores them. They all stay at plain-search level (Recall@5 0.67-0.71), while BRAG retrieves the new chunk 0.80-0.86 of the time. We also ran BRAG on three of NUDGE's seven text benchmarks, and it matches or beats NUDGE on all three. On nine months of a personal agent's memory (20,640 chunks), BRAG raises Recall@5 on held-out queries from 0.75 to 0.98 and Recall@1 from 0.44 to 0.97, with little change on chunks never queried.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
