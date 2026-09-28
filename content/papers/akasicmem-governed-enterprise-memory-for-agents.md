# AkasicMEM: Governed Enterprise Memory for Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.25563v1
- Published: 2026-09-22
- Updated: 2026-09-22
- Authors: Jeongmin Bae, Yongjae Kim, Kyoung Hur, Donghyoung Han, Min-Soo Kim
- Tags: agent, retrieval
- Categories: cs.DB, cs.AI
- URL: http://arxiv.org/abs/2609.25563v1

## One-Sentence Summary
Agent memory enables enterprise agents to retain knowledge acquired during work and reuse it across tasks and agents, turning execution experience into persistent organizational...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agent memory enables enterprise agents to retain knowledge acquired during work and reuse it across tasks and agents, turning execution experience into persistent organizational knowledge.

进一步看，论文的核心做法或实验重点可以概括为：Realizing this potential requires both source--memory integration, through which enterprise sources and accumulated memory can be utilized together, and memory governance, through which shared memory remains subject...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.DB, cs.AI

## Abstract Snapshot
Agent memory enables enterprise agents to retain knowledge acquired during work and reuse it across tasks and agents, turning execution experience into persistent organizational knowledge. Realizing this potential requires both source--memory integration, through which enterprise sources and accumulated memory can be utilized together, and memory governance, through which shared memory remains subject to organizational policies throughout its lifecycle. These requirements interact when information from enterprise sources persists in memory. As this information is repeatedly derived and reused under changing principals and policies, source restrictions may be bypassed, resulting in information leakage. Preventing such leakage requires authorization continuity, under which source restrictions remain effective throughout source-to-memory and memory-to-memory derivation and reuse. Existing approaches address these concerns individually, but do not treat source--memory integration, memory governance, and authorization continuity as combined core design targets across the memory lifecycle. We define Governed Enterprise Memory as agent memory designed around this combined scope and present AkasicMEM as its realization. AkasicMEM realizes authorization continuity through transitive lineage, policy composition during memory formation, and policy re-evaluation during retrieval. It is built on GraphAI's AkasicDB, a unified vector--graph--relational database whose storage and execution substrate enables the underlying operations of these mechanisms to be jointly optimized and executed.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
