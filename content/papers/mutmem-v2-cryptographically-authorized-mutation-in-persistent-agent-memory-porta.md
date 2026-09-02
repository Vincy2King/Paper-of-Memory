# MutMem-V2: Cryptographically Authorized Mutation in Persistent Agent Memory Portable Verification and Reproducible Evidence

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.01235v1
- Published: 2026-09-01
- Updated: 2026-09-01
- Authors: Walid Saidi
- Tags: agent
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2609.01235v1

## One-Sentence Summary
MutMem V1 introduced retention-preserving, cryptographically authorized mutation for persistent agent memory but did not provide a complete portable verification contract or...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：MutMem V1 introduced retention-preserving, cryptographically authorized mutation for persistent agent memory but did not provide a complete portable verification contract or clean-install reproduction path.

进一步看，论文的核心做法或实验重点可以概括为：MutMem V2 closes that publication gap without introducing a second memory engine.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
MutMem V1 introduced retention-preserving, cryptographically authorized mutation for persistent agent memory but did not provide a complete portable verification contract or clean-install reproduction path. MutMem V2 closes that publication gap without introducing a second memory engine. It specifies exact canonical bytes, domain-separated object and bundle commitments, mandatory recall-evidence membership and ordering, external trust anchors, identity epochs, revocation, authorization, request receipts, ordered disclosure, and three mutation terminal types. The released protocol contains 18 versioned object schemas, 39 recall vectors, 15 mutation vectors, and 37 closed recall failure reasons. Independent Node and Python implementations agree on verdict and primary reason for all 72 structural and cryptographic terminals; a production-conformance corpus agrees on 42/42 cases across 28 required classes. A clean Node v26.8.1 installation reaches first-boot, restart, and scheduler readiness with no experimental memories. A separately scoped 120-unit Canary experiment supports only explicit-marker traversal. Every public table regenerates from a self-hashed aggregate, and an independent verifier reconstructs the statistics and claim boundaries. Historical V1 empirical results remain historical. MutMem V2 supports claims about portable integrity, authorization, traceability, conformance, and reproducibility under stated assumptions; it does not establish semantic truth, universal robustness, or independent replication.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
