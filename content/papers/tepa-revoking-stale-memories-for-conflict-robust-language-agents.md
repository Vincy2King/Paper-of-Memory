# TEPA: Revoking Stale Memories for Conflict-Robust Language Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.07429v1
- Published: 2026-08-07
- Updated: 2026-08-07
- Authors: Yan Zhou, Yue Ouyang, Kaiyang Zheng, Suncheng Xiang
- Tags: agent, context, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.07429v1

## One-Sentence Summary
Long-term memory enables language agents to reuse past facts, preferences, and task experience.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory enables language agents to reuse past facts, preferences, and task experience.

进一步看，论文的核心做法或实验重点可以概括为：Persistence also creates a central falsifiability problem: when the world changes, stale memories can remain retrievable and pollute the prompt.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term memory enables language agents to reuse past facts, preferences, and task experience. Persistence also creates a central falsifiability problem: when the world changes, stale memories can remain retrievable and pollute the prompt. We characterize this failure mode as memory pollution: degradation caused by active memories that newer conflicting evidence has superseded. We introduce TEPA, a revocable evidence-memory mechanism that makes validity an explicit state of memory. TEPA represents observations as keyed precedents and revokes active precedents when fresh evidence contradicts them under the same key, allowing retrieval to draw from current evidence while preserving revoked history for audit. Across controlled hidden-regime drift, real file-backed executable drift, and preference-update streams, revocation prevents stale active memory from remaining in the retrieval set after reversal. In controlled drift over 50 seeds, append-only and last-write-wins memory fell below no memory during full reversal (append-only and last-write-wins both 0.210, no memory 0.309, TEPA 0.950), and the same pattern reproduced under real file execution (append-only 0.203, no memory 0.298, TEPA 0.950). On clean MemoryAgentBench SH-6k, TEPA matches a strong last-write-wins cache, confirming that current-key replacement is the decisive operation for single-hop fact consolidation. Boundary tests on multi-hop and very long-context MemoryAgentBench settings expose retrieval-chain and context-selection bottlenecks beyond fact-level validity tracking. Together, these results establish lifecycle revocation as a core memory operation for agents that must falsify, audit, and later re-promote evolving knowledge.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
