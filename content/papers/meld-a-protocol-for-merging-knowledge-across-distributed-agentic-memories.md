# MELD: A Protocol for Merging Knowledge Across Distributed Agentic Memories

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.16357v1
- Published: 2026-08-17
- Updated: 2026-08-17
- Authors: Lauri Lovén, Jaakko Sauvola, Jukka Riekki, Sasu Tarkoma
- Tags: agent, context
- Categories: cs.DC, cs.AI, cs.MA
- URL: http://arxiv.org/abs/2608.16357v1

## One-Sentence Summary
Autonomous agents share a transport and can call each other's tools, but they cannot share what they know: no protocol lets two agents' memories reconcile a fact phrased two...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Autonomous agents share a transport and can call each other's tools, but they cannot share what they know: no protocol lets two agents' memories reconcile a fact phrased two ways, link related facts held apart, or...

进一步看，论文的核心做法或实验重点可以概括为：We present MELD, a self-managing coherence mechanism for a federation of agent memories whose run-time model is the knowledge graph itself.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：agent memory
- 来源分类信息：cs.DC, cs.AI, cs.MA

## Abstract Snapshot
Autonomous agents share a transport and can call each other's tools, but they cannot share what they know: no protocol lets two agents' memories reconcile a fact phrased two ways, link related facts held apart, or reconcile contradictory knowledge without silently discarding either claim. We present MELD, a self-managing coherence mechanism for a federation of agent memories whose run-time model is the knowledge graph itself. Each brain admits every incoming claim through a five-outcome procedure (insert, merge, relate, conflict, or reject), decided from three signals (scoped claim-key identity, embedding similarity, and a natural-language-inference verdict) under context and freshness gates, and acting through exactly one auditable, authenticated Patch, the only object that mutates state. A binding onto standard publish/subscribe transport with a per-claim status CRDT keeps sovereign brains coherent in claim status without a coordinator: self-healing after partitions and under lossy routing, and self-protecting against silent rewrite by a peer, under a benign-fault model. MELD does not adjudicate truth; a detected contradiction is preserved for later adjudication, never silently resolved. On HotpotQA distractor, distributed merge is recall-non-inferior to a centralized store under a pre-specified equivalence test and recall-superior to naive union at about 11% less live storage; the merge classifier separates at AUC 0.968 with a 0.013 false-merge rate on adjudicated candidate pairs; the status CRDT reconverges in 30/30 real partition-heal trials where last-writer-wins manages 11/30; and semantic routing delivers about 3x fewer messages at matched recall. We evaluate on a real computing continuum spanning an operator-grade 5G edge, national HPC, and a local tier, with empirically calibrated thresholds.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
