# BrowseNet: Graph-Based Associative Memory for Contextual Information Retrieval

- Source: OpenReview
- Venue: ICLR 2026 Poster
- Paper ID: openreview:2q5CugVPoK
- Published: 2026-01-26
- Updated: 2026-04-11
- Authors: PAVAN KUMAR S, Kiran Kumar Nakka, C Vamshi Krishna Reddy, Divyateja Pasupuleti, Prakhar Agarwal, Harpinder Jot Singh, Anshu Avinash, Nirav Pravinbhai Bhatt
- Tags: context, retrieval
- Categories: ICLR.cc/2026/Conference/-/Submission
- URL: https://openreview.net/forum?id=2q5CugVPoK

## One-Sentence Summary
Associative memory systems face significant challenges in efficiently retrieving semantically related information from large document collections, particularly when queries...

## Introduction
这篇论文被纳入仓库，是因为它和 `context, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ICLR 2026 Poster` 这个 venue 相关。

从摘要来看，作者主要关注的是：Associative memory systems face significant challenges in efficiently retrieving semantically related information from large document collections, particularly when queries require traversing complex relationships...

进一步看，论文的核心做法或实验重点可以概括为：Traditional retrieval-augmented generation (RAG) approaches often struggle to capture intricate associative patterns and relationships embedded within textual data.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ICLR 2026 Poster
- 高亮主题命中：context, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：ICLR.cc/2026/Conference/-/Submission

## Abstract Snapshot
Associative memory systems face significant challenges in efficiently retrieving semantically related information from large document collections, particularly when queries require traversing complex relationships between concepts. Traditional retrieval-augmented generation (RAG) approaches often struggle to capture intricate associative patterns and relationships embedded within textual data. To address this limitation, we propose BrowseNet, a novel associative memory framework that leverages query-specific subgraph exploration within a named-entity-based graph for enhanced information retrieval. Our method transforms unstructured text into a graph-of-chunks representation, where nodes encode document chunks with semantic embeddings and edges capture lexical relationships between content segments. By dynamically traversing the graph-of-chunks based on query characteristics, BrowseNet emulates content-addressable memory systems that enable efficient pattern matching and associative recall. The framework incorporates both structural similarity derived from lexical relationships and semantic similarity based on embedding representations to optimize retrieval performance. We evaluate BrowseNet against established RAG baselines and state-of-the-art (SOTA) pipelines using publicly available datasets that require associative reasoning across multiple information sources. Experimental results demonstrate that BrowseNet achieves SOTA performance in exact match score over both the graph-based RAG approaches and the dense retrieval methods. The two-pronged approach combining structural graph traversal with semantic embeddings enables more effective associative memory retrieval, particularly for queries requiring the integration of disparate but related information. The code and datasets are open-sourced at: https://github.com/bisect-group/BrowseNet

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
