# Trace Only What You Need: Structure-Aware On-Demand Hypergraph Memory for Long-Document Question Answering

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.10921v1
- Published: 2026-06-09
- Updated: 2026-06-09
- Authors: Xiangjun Zai, Xingyu Tan, Chen Chen, Xiaoyang Wang, Wenjie Zhang
- Tags: agent, context, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2606.10921v1

## One-Sentence Summary
Long-document question answering (QA) requires large language models (LLMs) to reason over evidence scattered across lengthy documents, where answers often depend on event...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-document question answering (QA) requires large language models (LLMs) to reason over evidence scattered across lengthy documents, where answers often depend on event order, section-level context, and cross-part...

进一步看，论文的核心做法或实验重点可以概括为：Although retrieval-augmented generation (RAG) reduces the input context by retrieving relevant evidence, existing structured RAG methods still face three limitations: costly query-agnostic knowledge organization,...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：working memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-document question answering (QA) requires large language models (LLMs) to reason over evidence scattered across lengthy documents, where answers often depend on event order, section-level context, and cross-part evidence connections. Although retrieval-augmented generation (RAG) reduces the input context by retrieving relevant evidence, existing structured RAG methods still face three limitations: costly query-agnostic knowledge organization, insufficient use of original document structure, and no reuse of historical reasoning experience. To address these limitations, we propose DocTrace, a multi-agent RAG framework for long-document QA that supports query-triggered knowledge organization, document-structure-aware and experience-guided reasoning. DocTrace preserves document hierarchy with a lightweight document structural tree index, constructs agent-shared hypergraph-structured working memory on demand during reasoning, and stores successful reasoning plans in graph-structured experience memory for future reuse, enabling adaptive exploration across related long-document questions. Experiments on four long-document QA datasets show that DocTrace achieves the best performance on three datasets, surpassing the strongest baseline, ComoRAG, by up to 8.85% in F1 and 4.40% in EM, while reducing the overall computational cost by 53.32%

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
