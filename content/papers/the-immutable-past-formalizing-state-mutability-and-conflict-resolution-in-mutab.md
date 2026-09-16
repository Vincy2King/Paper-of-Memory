# The Immutable Past: Formalizing State Mutability and Conflict Resolution in Mutable RAG

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.16073v1
- Published: 2026-09-13
- Updated: 2026-09-13
- Authors: Hamed HaddadPajouh, Amir AmiriTabat
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2609.16073v1

## One-Sentence Summary
Retrieval-Augmented Generation (RAG) serves as the primary memory architecture for long-horizon autonomous agents.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Retrieval-Augmented Generation (RAG) serves as the primary memory architecture for long-horizon autonomous agents.

进一步看，论文的核心做法或实验重点可以概括为：However, treating shared memory as an append-only stream introduces \textit{Semantic Shadowing}, a critical failure mode where conflicting historical observations accumulate and statistically dominate valid recent...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Retrieval-Augmented Generation (RAG) serves as the primary memory architecture for long-horizon autonomous agents. However, treating shared memory as an append-only stream introduces \textit{Semantic Shadowing}, a critical failure mode where conflicting historical observations accumulate and statistically dominate valid recent updates. In dynamic environments, this results in severe state divergence as agents retrieve and act upon obsolete facts. This paper formalizes the mechanics of State Mutability to prove that standard dense retrieval suffers from Asymptotic Recall Decay. Furthermore, we formally demonstrate a Majority Vote Trap, revealing that increasing the retrieval context window paradoxically degrades generation accuracy by diluting the attention mechanism under conditions of semantic equivalence. To resolve this, we introduce GC-Mem (Garbage Collection for Memory), a strict inference-time consistency protocol. Unlike heuristic time-decay mechanisms---which indiscriminately destroy valid long-term memory---GC-Mem relies purely on a temporal dominance operator ($Φ_{\mathcal{T}}$) paired with contradiction detection to surgically excise shadowed context. Evaluated across a rigorous, behaviorally inferred benchmark of 137,760 memory chunks and continuous accumulation sweeps, standard RAG and timestamp re-ranking baselines experience severe degradation. In contrast, GC-Mem empirically recovers $>90\%$ conflict resolution accuracy. We establish strict precision and recall deployment thresholds, ensuring state convergence where standard mutable RAG fundamentally fails.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
