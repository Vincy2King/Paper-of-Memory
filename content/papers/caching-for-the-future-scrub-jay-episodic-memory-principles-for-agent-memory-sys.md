# Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems

- Source: OpenReview
- Venue: ACL ARR 2026 May Submission
- Paper ID: openreview:HXNJkclmb9
- Published: 2026-06-02
- Updated: 2026-06-21
- Authors: Unknown
- Tags: agent, benchmark, context, episodic, retrieval
- Categories: aclweb.org/ACL/ARR/2026/May/-/Submission
- URL: https://openreview.net/forum?id=HXNJkclmb9

## One-Sentence Summary
LLM agents that persist across sessions accumulate stored memories whose validity varies enormously by content type, yet existing memory architectures treat all memories as...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 May Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：LLM agents that persist across sessions accumulate stored memories whose validity varies enormously by content type, yet existing memory architectures treat all memories as equally persistent and systematically...

进一步看，论文的核心做法或实验重点可以概括为：We show that per-memory, type-conditioned temporal decay, a property of western scrub jay episodic memory, can be operationalized as an auto-classified coefficient $\pi_i$ in an external LLM-agent memory store,...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 May Submission
- 高亮主题命中：agent, benchmark, context, episodic, retrieval
- 检索关键词命中：agent memory, episodic memory
- 来源分类信息：aclweb.org/ACL/ARR/2026/May/-/Submission

## Abstract Snapshot
LLM agents that persist across sessions accumulate stored memories whose validity varies enormously by content type, yet existing memory architectures treat all memories as equally persistent and systematically contaminate retrieved context with outdated facts. We show that per-memory, type-conditioned temporal decay, a property of western scrub jay episodic memory, can be operationalized as an auto-classified coefficient $\pi_i$ in an external LLM-agent memory store, yielding ScrubJay-MEM: each memory is encoded as a jointly-bound What--Where--When tuple with an estimated perishability $\pi_i$ and utility horizon $\tau_i$, retrieved by query-adaptive scoring, and revised retroactively at $O(1)$ LLM calls per update. We introduce the Temporal Generalization Test (TGT), a benchmark with held-out retention intervals and a Generalization Gap (GenGap) metric. On TGT, ScrubJay-MEM is the only retrieval-based system with substantially positive GenGap ($+0.108$); on MemoryAgentBench EventQA-64k it improves F1 by $+2.66$ over Mem0 and $+3.09$ over Qwen3-Embedding-4B under a llm backbone. A decay ablation collapses GenGap by $5.7\times$, establishing type-conditioned decay as necessary for the result. Gains narrow under stronger backbones and reverse on fact-consolidation tasks, scoping the contribution to temporal reasoning over perishable facts.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
