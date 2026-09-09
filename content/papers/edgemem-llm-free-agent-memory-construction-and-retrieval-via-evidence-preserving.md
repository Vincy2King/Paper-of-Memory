# EdgeMem: LLM-Free Agent Memory Construction and Retrieval via Evidence-Preserving Multi-Anchor Hypergraph

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.05553v1
- Published: 2026-09-03
- Updated: 2026-09-03
- Authors: Zeyang Cui, Jiannong Cao, Zhiyuan Wen, Bo Yuan, Junlan Feng, Shengyuan Chen
- Tags: agent, conversation, episodic, retrieval
- Categories: cs.AI, cs.MA
- URL: http://arxiv.org/abs/2609.05553v1

## One-Sentence Summary
Agent memory allows LLM agents to use earlier interactions when answering new queries.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agent memory allows LLM agents to use earlier interactions when answering new queries.

进一步看，论文的核心做法或实验重点可以概括为：Existing methods often compress interaction histories into summaries or other LLM-generated representations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, episodic, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI, cs.MA

## Abstract Snapshot
Agent memory allows LLM agents to use earlier interactions when answering new queries. Existing methods often compress interaction histories into summaries or other LLM-generated representations. Repeated generation adds cost and can discard answer-bearing details before the system knows what a future query will require. We propose EdgeMem, an agent-memory method built around a simple principle: preserve original interaction turns and organize them through complementary content, temporal, and episodic cues. EdgeMem realizes this principle with a multi-anchor hypergraph constructed by lightweight local processing. Retrieval directly returns source evidence and reserves LLM use for final answer generation, combining structured access to multi-session histories with faithful retention of the original conversation. Experiments on LoCoMo and LongMemEval-S show strong retrieval and memory-grounded question answering; on LoCoMo, EdgeMem achieves the highest strict-judge score among seven reproduced systems under a shared prompt (61.01 versus 58.70), while construction and retrieval require no generative-LLM calls. Overall, EdgeMem shows that preserving and organizing source evidence provides an effective and efficient foundation for agent memory without generative memory management.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
