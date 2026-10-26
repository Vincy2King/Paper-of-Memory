# ActionRAG: Evidence-Refining Graph Diffusion for Long-Term Memory in LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.32752v1
- Published: 2026-10-23
- Updated: 2026-10-23
- Authors: Navyansh Mahla, Sashank Vandrangi
- Tags: agent, long-term, retrieval
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2610.32752v1

## One-Sentence Summary
LLM agents need long-term memory that can recover precise and mutually consistent evidence from growing interaction histories, particularly when answers depend on relations...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM agents need long-term memory that can recover precise and mutually consistent evidence from growing interaction histories, particularly when answers depend on relations among facts rather than isolated semantic...

进一步看，论文的核心做法或实验重点可以概括为：Current memory pipelines remain vulnerable at two stages: indexing errors can fragment repeated entities or merge distinct ones, and online retrieval often treats initial similarity scores as final even when the...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
LLM agents need long-term memory that can recover precise and mutually consistent evidence from growing interaction histories, particularly when answers depend on relations among facts rather than isolated semantic matches. Current memory pipelines remain vulnerable at two stages: indexing errors can fragment repeated entities or merge distinct ones, and online retrieval often treats initial similarity scores as final even when the surrounding graph provides evidence for revising them. We introduce ActionRAG, a graph memory architecture that couples cautious indexing with query-time graph retroevaluation. Its indexing pipeline reconciles type labels and applies tiered entity resolution. Given a query, dual-channel entity and triple retrieval forms an initial evidence set and induces a bounded local graph. Query-conditioned receiver-normalized diffusion refines triple scores using local path structure. Seed protection, hub-penalized flux, and triple materialization preserve direct evidence while recovering missed connections. We evaluate ActionRAG on MemoryAgentBench (MAB), which tests accurate retrieval, conflict resolution, long-range understanding, and test-time learning. Across its eight deterministic-scoring columns, ActionRAG achieves 55.1 average accuracy, improving over the strongest retrieval-based memory baseline by 5.4 points. Under MAB's query-time cost accounting, mean synthesis cost stays below \$0.001 per query on the four reported cost columns, and the sum of separately measured retrieval-side p99 components is 440.7 ms on our consumer Apple Silicon setup.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
