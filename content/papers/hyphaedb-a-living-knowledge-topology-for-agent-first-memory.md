# HyphaeDB: A Living Knowledge Topology for Agent-First Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.28781v1
- Published: 2026-06-27
- Updated: 2026-06-27
- Authors: Krishna Halaharvi
- Tags: agent
- Categories: cs.AI, cs.MA
- URL: http://arxiv.org/abs/2606.28781v1

## One-Sentence Summary
Every existing vector database and agent memory framework treats memory as passive storage that agents query explicitly.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Every existing vector database and agent memory framework treats memory as passive storage that agents query explicitly.

进一步看，论文的核心做法或实验重点可以概括为：No system propagates knowledge between agents through the memory layer itself.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI, cs.MA

## Abstract Snapshot
Every existing vector database and agent memory framework treats memory as passive storage that agents query explicitly. No system propagates knowledge between agents through the memory layer itself. We introduce HyphaeDB, an agent-native memory infrastructure that reinterprets the Hierarchical Navigable Small World (HNSW) graph topology the data structure at the core of every modern vector database not as a search optimization, but as a communication fabric for multi-agent AI systems. In HyphaeDB, agents are nodes in the vector space with persistent positions, knowledge propagates via a gossip protocol through the graph's neighbor structure with energy-based attenuation, and emergent behaviors contradiction detection, pattern crystallization, and consensus formation arise from the combination of topology, propagation dynamics, and local interaction rules. We present the architecture built on three primitives (knowledge nodes, topology edges, and memory diffs), a multi-layer abstraction hierarchy with promotion via emergent consensus, and theoretical analysis grounding the system in small-world network theory, epidemic broadcast protocols, and swarm intelligence. We provide a reference implementation on PostgreSQL with pgvector and describe a concrete deployment in Swarm-Driven Development, a multi-agent software engineering methodology. HyphaeDB represents, to our knowledge, the first system to combine navigable small world topology with gossip-based knowledge propagation for multi-agent coordination.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
