# EquiMem: Calibrating Shared Memory in Multi-Agent Debate via Game-Theoretic Equilibrium

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.09278v1
- Published: 2026-05-10
- Updated: 2026-05-10
- Authors: Yuqiao Meng, Sakshi Sunil Narvekar, Luoxi Tang, Rupali Rajendra Vaje, Yingxue Zhang, Muchao Ye, Zhaohan Xi
- Tags: agent, benchmark, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.09278v1

## One-Sentence Summary
Multi-agent debate (MAD) systems increasingly rely on shared memory to support long-horizon reasoning, but this convenience opens a critical vulnerability: a single corrupted...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multi-agent debate (MAD) systems increasingly rely on shared memory to support long-horizon reasoning, but this convenience opens a critical vulnerability: a single corrupted entry can contaminate the downstream...

进一步看，论文的核心做法或实验重点可以概括为：Existing safeguards filter entries via heuristics or LLM-based validation, yet they rely on AI judgments that share the same failure modes and overlook the cross-agent dynamics of MAD.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Multi-agent debate (MAD) systems increasingly rely on shared memory to support long-horizon reasoning, but this convenience opens a critical vulnerability: a single corrupted entry can contaminate the downstream memory-augmented reasoning, and debate alone fails to filter such errors. Existing safeguards filter entries via heuristics or LLM-based validation, yet they rely on AI judgments that share the same failure modes and overlook the cross-agent dynamics of MAD. We address this gap by formulating memory updating in MAD as a zero-trust memory game, in which no agent is assumed honest and the game's equilibrium serves as an indicator of optimal memory trust. Guided by this equilibrium, we propose EquiMem, an inference-time calibration mechanism that quantifies each update algorithmically against the shared memory state, using agents' existing retrieval queries and traversal paths as evidence rather than soliciting any LLM judgment. EquiMem instantiates calibration for both embedding- and graph-based memory, and across diverse benchmarks, MAD frameworks, and memory architectures, it consistently outperforms existing safeguards, remains robust under adversarial agents, and incurs negligible inference overhead.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
