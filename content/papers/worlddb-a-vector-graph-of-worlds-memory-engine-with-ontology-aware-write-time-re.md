# WorldDB: A Vector Graph-of-Worlds Memory Engine with Ontology-Aware Write-Time Reconciliation

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.18478v1
- Published: 2026-04-20
- Updated: 2026-04-20
- Authors: Harish Santhanalakshmi Ganesan
- Tags: agent, conversation, retrieval
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2604.18478v1

## One-Sentence Summary
Persistent memory is the bottleneck separating stateless chatbots from long-running agentic systems.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent memory is the bottleneck separating stateless chatbots from long-running agentic systems.

进一步看，论文的核心做法或实验重点可以概括为：Retrieval-augmented generation (RAG) over flat vector stores fragments facts into chunks, loses cross-session identity, and has no first-class notion of supersession or contradiction.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Persistent memory is the bottleneck separating stateless chatbots from long-running agentic systems. Retrieval-augmented generation (RAG) over flat vector stores fragments facts into chunks, loses cross-session identity, and has no first-class notion of supersession or contradiction. Recent bitemporal knowledge-graph systems (Graphiti, Memento, Hydra DB) add typed edges and valid-time metadata, but the graph itself remains flat: no recursive composition, no content-addressed invariants on nodes, and edge types carry no behavior beyond a label. We present WorldDB, a memory engine built on three commitments: (i) every node is a world -- a container with its own interior subgraph, ontology scope, and composed embedding, recursive to arbitrary depth; (ii) nodes are content-addressed and immutable, so any edit produces a new hash at the node and every ancestor, giving a Merkle-style audit trail for free; (iii) edges are write-time programs -- each edge type ships on_insert/on_delete/on_query_rewrite handlers (supersession closes validity, contradicts preserves both sides, same_as stages a merge proposal), so no raw append path exists. On LongMemEval-s (500 questions, ~115k-token conversational stacks), WorldDB with Claude Opus 4.7 as answerer achieves 96.40% overall / 97.11% task-averaged accuracy, a +5.61pp improvement over the previously reported Hydra DB state-of-the-art (90.79%) and +11.20pp over Supermemory (85.20%), with perfect single-session-assistant recall and robust performance on temporal reasoning (96.24%), knowledge update (98.72%), and preference synthesis (96.67%). Ablations show that the engine's graph layer -- resolver-unified entities and typed refers_to edges -- contributes +7.0pp task-averaged independently of the underlying answerer.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
