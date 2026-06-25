# Forget to Improve: On-Device LLM-Agent Continual Learning via Budget-Curated Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.25115v1
- Published: 2026-06-23
- Updated: 2026-06-23
- Authors: Beining Wu, Zihao Ding, Jun Huang, Yanxiao Zhao
- Tags: agent, benchmark
- Categories: cs.LG, cs.NI
- URL: http://arxiv.org/abs/2606.25115v1

## One-Sentence Summary
On-device language-model agents improve by accumulating experience in retrieved memory rather than by updating weights.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：On-device language-model agents improve by accumulating experience in retrieved memory rather than by updating weights.

进一步看，论文的核心做法或实验重点可以概括为：This memory is hard-bounded and exposed: it consumes RAM and energy, reaches peers through a thin uplink, and becomes an attack surface because it is writable by what the agent reads.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：agent memory, retrieval memory
- 来源分类信息：cs.LG, cs.NI

## Abstract Snapshot
On-device language-model agents improve by accumulating experience in retrieved memory rather than by updating weights. This memory is hard-bounded and exposed: it consumes RAM and energy, reaches peers through a thin uplink, and becomes an attack surface because it is writable by what the agent reads. Existing systems each cover one part of this problem: agentic memories grow without a budget, on-device methods keep entries by success alone, and poisoning is studied mainly as an attack rather than as a memory-governance problem. We propose \sys{}, a single net-value-per-byte score that governs an agent's experience-memory lifecycle. The main idea is to let the budget act as the curator: each entry is scored as value minus harm, per byte, so one ruler decides what to keep, share, and trust. \sys{} makes three decisions: (1) \textbf{KEEP} evicts low-value bytes under the RAM and energy budget; (2) \textbf{SHARE} sends an insight only when its value exceeds its uplink cost; and (3) \textbf{TRUST} gates a peer entry by provenance. On language-model-agent task-drift benchmarks and a real heterogeneous Jetson testbed with two robot-arm nodes and a hub, \sys{} reduces memory by $2.7\times$ and uplink by $2.4\times$, drives injection success from 0.75 to zero, and raises accuracy on cases corrupted by poison or stale memory. Curating by net value reduces footprint, energy, uplink, and injection success together without reducing accuracy. In this setting, forgetting by net value improves the agent rather than weakening it.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
