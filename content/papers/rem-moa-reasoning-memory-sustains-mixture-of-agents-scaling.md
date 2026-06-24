# ReM-MoA: Reasoning Memory Sustains Mixture-of-Agents Scaling

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.24437v1
- Published: 2026-06-23
- Updated: 2026-06-23
- Authors: Heng Ping, Arijit Bhattacharjee, Peiyu Zhang, Shixuan Li, Wei Yang, Ali Jannesari, Nesreen Ahmed, Paul Bogdan
- Tags: agent, benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.24437v1

## One-Sentence Summary
Mixture-of-Agents (MoA) architectures improve inference-time scaling by organizing multiple LLM agents into layered reasoning pipelines.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Mixture-of-Agents (MoA) architectures improve inference-time scaling by organizing multiple LLM agents into layered reasoning pipelines.

进一步看，论文的核心做法或实验重点可以概括为：However, existing MoA variants fail to sustain gains as depth increases, exhibiting degradation, early plateauing, or saturation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Mixture-of-Agents (MoA) architectures improve inference-time scaling by organizing multiple LLM agents into layered reasoning pipelines. However, existing MoA variants fail to sustain gains as depth increases, exhibiting degradation, early plateauing, or saturation. We propose ReM-MoA, a memory-augmented MoA framework that sustains scaling through two mechanisms: (1) a Ranked Reasoning Memory that persistently stores and ranks reasoning traces from all layers using a comparative Reviewer Agent, and (2) a Curated Diversified Memory Routing scheme that exposes different agents to distinct combinations of successful and failed traces, preserving exploration diversity while propagating high-quality reasoning. We further introduce an optional multi-domain Reviewer distillation pipeline that improves ranking quality through frontier-model supervision. Across five reasoning benchmarks spanning math, formal logic, code, knowledge, and commonsense, ReM-MoA consistently outperforms prior MoA variants across both depth and width scaling, and its advantage widens with depth, establishing structured cross-layer reasoning memory as a key missing mechanism for scalable multi-agent inference.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
