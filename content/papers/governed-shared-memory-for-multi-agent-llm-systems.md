# Governed Shared Memory for Multi-Agent LLM Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.24535v1
- Published: 2026-06-23
- Updated: 2026-06-23
- Authors: Yanki Margalit, Nurit Cohen-Inger, Erni Avram, Ran Taig, Oded Margalit
- Tags: agent, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.24535v1

## One-Sentence Summary
Multi-agent LLM environments require robust mechanisms for shared knowledge management.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multi-agent LLM environments require robust mechanisms for shared knowledge management.

进一步看，论文的核心做法或实验重点可以概括为：This paper formalizes the fleet-memory problem and identifies four foundational failure modes: unauthorized leakage, stale propagation, contradiction persistence, and provenance collapse.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Multi-agent LLM environments require robust mechanisms for shared knowledge management. This paper formalizes the fleet-memory problem and identifies four foundational failure modes: unauthorized leakage, stale propagation, contradiction persistence, and provenance collapse. To address these, we define explicit systems-level primitives: scoped retrieval, temporal supersession, provenance tracking, and policy-governed memory propagation. These primitives are implemented in MemClaw, a production multi-tenant memory service, and evaluated via ArgusFleet, a reproducible harness testing four governance dimensions. Rather than a baseline comparison, this study measures a live production service, emphasizing real-world architectural insights and negative results. Key Evaluation Results Provenance: Successfully reconstructed 100% of depth-four derivation chains with correct writer identity at sub-second per-hop latency. Propagation: Demonstrated high intra-fleet visibility with zero cross-fleet leakage. Under strong write mode, write-to-visible latency was optimized to a single search round-trip. Production Architectural Issues Discovered Asymmetric Scope Enforcement: Tenant isolation held, but sub-tenant scope was initially bypassed on direct GET-by-id requests for agent-scoped credentials (disclosed and remediated during the study). Pipeline Ordering Conflict: While contradiction supersession works for admitted writes, a synchronous near-duplicate gate can prematurely reject contradictory writes before the asynchronous contradiction detector can evaluate them. Conclusion: Long-context retrieval alone is insufficient for production multi-agent memory. Governed shared memory demands explicit systems-level abstractions, and live evaluation is vital to expose enforcement and pipeline-ordering failures missed by design-only treatments.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
