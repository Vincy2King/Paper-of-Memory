# Query Obfuscation with Embedding-Optimized Noise (EON): A Representational Blindspot in Agentic Retrieval

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.31344v1
- Published: 2026-11-23
- Updated: 2026-11-23
- Authors: Ankit Gupta, Christoph Adami, Emily Dolson
- Tags: agent, benchmark, episodic, retrieval
- Categories: cs.IR
- URL: http://arxiv.org/abs/2611.31344v1

## One-Sentence Summary
In modern agentic and semantic retrieval systems, dense embedding models increasingly determine which intent, tool, document, memory, or image to retrieve for a query.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：In modern agentic and semantic retrieval systems, dense embedding models increasingly determine which intent, tool, document, memory, or image to retrieve for a query.

进一步看，论文的核心做法或实验重点可以概括为：We identify a representational failure mode in this pipeline: a meaningful query can be replaced by visibly nonsemantic content while preserving much of its retrieval outcome, even when the candidate bank is hidden...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, episodic, retrieval
- 检索关键词命中：agent memory, memory retrieval
- 来源分类信息：cs.IR

## Abstract Snapshot
In modern agentic and semantic retrieval systems, dense embedding models increasingly determine which intent, tool, document, memory, or image to retrieve for a query. We identify a representational failure mode in this pipeline: a meaningful query can be replaced by visibly nonsemantic content while preserving much of its retrieval outcome, even when the candidate bank is hidden from the optimizer. We introduce Embedding-Optimized Noise (EON), constructed using only the natural query representation, without access to candidate embeddings, relevance labels, rankings, retrieval feedback, or guardrail decisions. Despite this corpus-blind objective, EONs frequently preserve intent and tool routing, benchmark document search, episodic agent-memory retrieval, and cross-modal search across multiple dense embedding families. Crucially, this disconnect carries serious security implications: for malicious queries, an EON can reliably evade input guardrails that block the natural query, executing the intended safety-sensitive retrieval undetected. Through the geometry of the embedding space, we then characterize how query-level representation matching can reliably maintain subsequent retrieval outcomes over candidates unseen during optimization. Together, these findings expose a fundamental phenomenon across dual encoders that we call BLINDSPOT, where systems remain operationally blind to nonsemantic artifacts while reliably retrieving real, consequential content.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
