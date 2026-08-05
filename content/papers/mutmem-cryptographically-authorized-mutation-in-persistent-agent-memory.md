# MutMem: Cryptographically Authorized Mutation in Persistent Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.02843v1
- Published: 2026-08-03
- Updated: 2026-08-03
- Authors: Walid Saidi
- Tags: agent, retrieval
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2608.02843v1

## One-Sentence Summary
Persistent agent memory must adapt as later outcomes change earlier evidence, yet mutable retrieval weights create an attribution problem: reviewers must distinguish authorized...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent agent memory must adapt as later outcomes change earlier evidence, yet mutable retrieval weights create an attribution problem: reviewers must distinguish authorized adaptation from database tampering.

进一步看，论文的核心做法或实验重点可以概括为：We present MutMem, an authorized-mutation protocol in HOM-AIMOS, a persistent agent-memory engine.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Persistent agent memory must adapt as later outcomes change earlier evidence, yet mutable retrieval weights create an attribution problem: reviewers must distinguish authorized adaptation from database tampering. We present MutMem, an authorized-mutation protocol in HOM-AIMOS, a persistent agent-memory engine. MutMem retains memory content, records signed positive and negative outcome evidence without age-based expiry, and commits each nontrivial weight change as a housekeeper-authorized transition. Each transition binds a terminal provenance node, signer epoch, quantized old and new weights, a no-fork predecessor, and two domain-separated SHA-256 commitments. Ed25519 verification runs in both the database writer and a portable verifier. Content classified as poison-likely is retained with signed, revisable labels used by recall as trust evidence. We evaluate utility, mutation integrity, and poisoning adaptation. HOM-AIMOS answers 459/500 LongMemEval questions correctly under LLM judgment (91.8%). On LoCoMo, it obtains 74.12% judged accuracy and, under a separate upstream-compatible protocol, 58.20 token F1. A native suite passes all declared authorization, topology, tamper, signer-epoch, and post-mutation-recall cases; median signed-transition latency is 4.865 ms. In a declared N=100 PoisonedRAG adaptation, no injected poison appears in attacked top-5 disclosures (0/100; 95% Wilson upper bound 3.70%), while induced target-answer attack success among 98 clean-negative targets is 1/98 (1.02%). A preregistered four-arm ablation attributes the retrieval reduction to signed stored labels: the retriever selects poison for 94/100 targets when epistemic policy is bypassed and 0/100 when labels are restored. MutMem provides evidence of integrity, authorization, traceability, and historical continuity; it does not establish content truth.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
