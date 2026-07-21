# Beyond Memory Leaderboards: Evaluating Scientific Memory as Budgeted Context Restoration

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.16848v1
- Published: 2026-07-18
- Updated: 2026-07-18
- Authors: Maksim Sheverev, David Finkelstein, Sergey Nikolenko
- Tags: agent, benchmark, context, conversation, long-term, retrieval
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2607.16848v1

## One-Sentence Summary
Long-term memory is becoming a core component of LLM agents, but most memory benchmarks evaluate conversations or compact summaries, while research agents need to restore...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory is becoming a core component of LLM agents, but most memory benchmarks evaluate conversations or compact summaries, while research agents need to restore evidence from full scientific papers.

进一步看，论文的核心做法或实验重点可以概括为：We introduce two full-text scientific-memory benchmarks, Public AI Memory (PAIM; 81 papers, 66 questions) and Public Transformers (PTr; 252 papers, 98 questions).

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：long-term memory, memory benchmark, memory benchmarks, memory retrieval
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Long-term memory is becoming a core component of LLM agents, but most memory benchmarks evaluate conversations or compact summaries, while research agents need to restore evidence from full scientific papers. We introduce two full-text scientific-memory benchmarks, Public AI Memory (PAIM; 81 papers, 66 questions) and Public Transformers (PTr; 252 papers, 98 questions). We evaluate eight memory/retrieval systems, including our own proposed Theoria, plus a no-retrieval baseline. Our results show that memory leaderboards are not interpretable without the full protocol: ingestion granularity, raw-text preservation, retrieval budget, retrieval modality, rubric audit, and judge choice all affect the outcome. For example, on PAIM Graphiti wins convincingly but uses 2.6M characters of retrieved context per query, and after controlling for retrieval budget the lead disappears. On PTr, for the systems where BM25 retrieval can be added cleanly, the sparse-dense hybrid is the single most significant intervention: hybrid variants of Simple RAG, Mem0, and Theoria tie for the lead within 0.03 points. Multi-judge and human side-by-side calibration show that LLM-as-a-judge rankings are consistent across frontier judges and agree with human evaluation, with an effective resolution of roughly one point on a ten-point scale. We argue that scientific memory should be evaluated as budgeted, modality-aware context restoration rather than as an unconstrained architecture leaderboard, and we release the datasets, harness, raw outputs, judgments, and scripts to reproduce our results and serve as tools for such evaluation. Our code is available at http://gitlab.com/quantellence/research/scientific-recall-bench , and the datasets are available at http://huggingface.co/datasets/quantellence/srb-data .

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
