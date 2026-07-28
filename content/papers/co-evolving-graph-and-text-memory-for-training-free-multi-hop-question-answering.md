# Co-Evolving Graph and Text Memory for Training-Free Multi-Hop Question Answering

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.23278v1
- Published: 2026-07-25
- Updated: 2026-07-25
- Authors: Hieu Man, Thien Huu Nguyen
- Tags: agent, benchmark, context, retrieval
- Categories: cs.CL, cs.MA
- URL: http://arxiv.org/abs/2607.23278v1

## One-Sentence Summary
Multi-hop question answering requires coordinating relational and textual evidence across reasoning steps, a combination neither a text corpus nor a knowledge graph can supply...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multi-hop question answering requires coordinating relational and textual evidence across reasoning steps, a combination neither a text corpus nor a knowledge graph can supply alone.

进一步看，论文的核心做法或实验重点可以概括为：Prior work often emphasizes only part of this loop: graph-augmented RAG retrieves from a pre-built or query-updated graph, KGQA systems search within topic-centered subgraphs, and memory-augmented agents maintain...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：memory augmented, memory-augmented, working memory
- 来源分类信息：cs.CL, cs.MA

## Abstract Snapshot
Multi-hop question answering requires coordinating relational and textual evidence across reasoning steps, a combination neither a text corpus nor a knowledge graph can supply alone. Prior work often emphasizes only part of this loop: graph-augmented RAG retrieves from a pre-built or query-updated graph, KGQA systems search within topic-centered subgraphs, and memory-augmented agents maintain evolving memories without continuously reconciling graph memory with textual context. We propose Co-E, a training-free system built around synchronized bidirectional graph-text working memory. A synchronization cycle consolidates textual memory, extracts relational triples into graph memory, and injects graph facts back into the generation context. Because both memories are maintained, they shape subsequent retrieval and generation. Evaluated on six multi-hop QA benchmarks, Co-E improves over comparable training-free open-backbone baselines and is competitive with larger or trained systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
