# Persistent Memory in Multi-Agent LLM Inference: What It Costs, What It Buys, and When You Can Tell

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.07782v1
- Published: 2026-10-06
- Updated: 2026-10-06
- Authors: Hochan Son, Kyungdoe Han, Jaehan Koh, Xiaowu Dai, Wenlu Xu, Guang Cheng
- Tags: agent, benchmark, context, retrieval
- Categories: cs.AI, cs.CL, cs.DC, cs.LG
- URL: http://arxiv.org/abs/2610.07782v1

## One-Sentence Summary
Decomposing long-context inference across cooperating agents bounds the active KV cache per call rather than total evidence, which matters when KV-cache memory binds.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Decomposing long-context inference across cooperating agents bounds the active KV cache per call rather than total evidence, which matters when KV-cache memory binds.

进一步看，论文的核心做法或实验重点可以概括为：Many such systems add a persistent tier storing and recalling reasoning traces, usually validated by an ablation reporting an accuracy gain.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：agent memory, persistent memory
- 来源分类信息：cs.AI, cs.CL, cs.DC, cs.LG

## Abstract Snapshot
Decomposing long-context inference across cooperating agents bounds the active KV cache per call rather than total evidence, which matters when KV-cache memory binds. Many such systems add a persistent tier storing and recalling reasoning traces, usually validated by an ablation reporting an accuracy gain. We measure both on one three-tier agent architecture. Decomposition delivers: peak KV working set of 14.3 MiB per query against 35.5 and 35.3 MiB for single-pass and retrieval-augmented baselines. The persistent tier does not: across eight controlled dataset pairs at n=100 per arm it costs +0.368 MiB [+0.167, +0.590] of peak cache and produces no detectable accuracy change (+0.015, 95% CI [-0.011, +0.046]). We argue the null is structural: single-question benchmarks supply each item with its own evidence and score it independently, and correctness requires resetting stored traces between conditions, so recall has nothing informative to retrieve. Reaching it took four measurement corrections -- three inflating the apparent benefit, the fourth making an effect that size look resolvable -- none visible in the results table. We give the conditions an agent-memory ablation must satisfy and detection procedures that need no knowledge of the specific defect.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
