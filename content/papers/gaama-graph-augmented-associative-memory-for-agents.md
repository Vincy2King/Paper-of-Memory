# GAAMA: Graph Augmented Associative Memory for Agents

- Source: OpenReview
- Venue: CoRR 2026
- Paper ID: openreview:EQtyfL5f2j
- Published: 2026-12-31
- Updated: 2026-05-07
- Authors: {'fullname': 'Swarna Kamal Paul', 'username': '~Swarna_Kamal_Paul2'}, {'fullname': 'Shubhendu Sharma', 'username': ''}, {'fullname': 'Nitin Sareen', 'username': ''}
- Tags: agent, benchmark, compression, conversation, long-term, retrieval
- Categories: OpenReview.net/Public_Article/DBLP.org/-/Record
- URL: https://openreview.net/forum?id=EQtyfL5f2j

## One-Sentence Summary
AI agents that interact with users across multiple sessions require persistent long-term memory to maintain coherent, personalized behavior.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, conversation` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `CoRR 2026` 这个 venue 相关。

从摘要来看，作者主要关注的是：AI agents that interact with users across multiple sessions require persistent long-term memory to maintain coherent, personalized behavior.

进一步看，论文的核心做法或实验重点可以概括为：Current approaches either rely on flat retrieval-augmented generation (RAG), which loses structural relationships between memories, or use memory compression and vector retrieval that cannot capture the associative...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：CoRR 2026
- 高亮主题命中：agent, benchmark, compression, conversation, long-term, retrieval
- 检索关键词命中：long-term memory, memory compression
- 来源分类信息：OpenReview.net/Public_Article/DBLP.org/-/Record

## Abstract Snapshot
AI agents that interact with users across multiple sessions require persistent long-term memory to maintain coherent, personalized behavior. Current approaches either rely on flat retrieval-augmented generation (RAG), which loses structural relationships between memories, or use memory compression and vector retrieval that cannot capture the associative structure of multi-session conversations. There are few graph based techniques proposed in the literature, however they still suffer from hub dominated retrieval and poor hierarchical reasoning over evolving memory. We propose GAAMA, a graph-augmented associative memory system that constructs a concept-mediated hierarchical knowledge graph through a three-step pipeline: (1)~verbatim episode preservation from raw conversations, (2)~LLM-based extraction of atomic facts and topic-level concept nodes, and (3)~synthesis of higher-order reflections. The resulting graph uses four node types (episode, fact, reflection, concept) connected by five structural edge types, with concept nodes providing cross-cutting traversal paths that complement semantic similarity. Retrieval combines cosine-similarity-based $k$-nearest neighbor search with edge-type-aware Personalized PageRank (PPR) through an additive scoring function. On the LoCoMo-10 benchmark (1,540 questions across 10 multi-session conversations), GAAMA achieves 78.9\% mean reward, outperforming a tuned RAG baseline (75.0\%), HippoRAG (69.9\%), A-Mem (47.2\%), and Nemori (52.1\%). Ablation analysis shows that augmenting graph-traversal-based ranking (Personalized PageRank) with semantic search consistently improves over pure semantic search on graph nodes (+1.0 percentage point overall).

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
