# MEMOREPAIR: Barrier-First Cascade Repair in Agentic Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.07242v1
- Published: 2026-05-08
- Updated: 2026-05-08
- Authors: Yang Zhao, Chengxiao Dai, Mengying Kou, Yue Xiu
- Tags: agent
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2605.07242v1

## One-Sentence Summary
Agentic memory evolves across tasks into durable derived artifacts: summaries, cached outputs, embeddings, learned skills, and executable tool procedures.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agentic memory evolves across tasks into durable derived artifacts: summaries, cached outputs, embeddings, learned skills, and executable tool procedures.

进一步看，论文的核心做法或实验重点可以概括为：When a source artifact is deleted, corrected, or invalidated by tool or API migration, descendants derived from that source can remain visible and steer future actions with stale support.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Agentic memory evolves across tasks into durable derived artifacts: summaries, cached outputs, embeddings, learned skills, and executable tool procedures. When a source artifact is deleted, corrected, or invalidated by tool or API migration, descendants derived from that source can remain visible and steer future actions with stale support. We formalize this failure mode as the cascade update problem, where repair targets the visible derived state of the memory store. We present MemoRepair, a barrier-first cascade-repair contract for agentic memory. A repair event induces a controlled transition from invalidated descendant state to validated successor state: affected descendants are withdrawn before repair, successors are constructed from retained support and staged repaired predecessors under the current interface, and republication is restricted to validated predecessor-closed successors. This contract induces a scalarized repair-selection problem for a fixed repair-cost tradeoff. We show that the induced publication problem reduces to maximum-weight predecessor closure and can be solved exactly by a single s-t min-cut. Experiments on ToolBench and MemoryArena show that, with complete influence provenance, MemoRepair reduces invalidated-memory exposure from 69.8-94.3% under systems without cascade repair to 0%. Compared with exhaustive Repair all, it recovers 91.1-94.3% of validated successors while reducing normalized repair-operator cost from 1.00 to 0.57-0.76.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
