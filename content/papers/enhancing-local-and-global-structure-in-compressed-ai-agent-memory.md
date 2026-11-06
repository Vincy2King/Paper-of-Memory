# Enhancing Local and Global Structure in Compressed AI Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.08341v1
- Published: 2026-11-05
- Updated: 2026-11-05
- Authors: Henry Han
- Tags: agent, compression
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.08341v1

## One-Sentence Summary
AI agents store text as embedding vectors and compress them at scale.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：AI agents store text as embedding vectors and compress them at scale.

进一步看，论文的核心做法或实验重点可以概括为：A compression is accepted when each item's nearest neighbors survive, but agents also consolidate, delete, and compare memories, tasks that depend on which items lie far apart.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
AI agents store text as embedding vectors and compress them at scale. A compression is accepted when each item's nearest neighbors survive, but agents also consolidate, delete, and compare memories, tasks that depend on which items lie far apart. We evaluate both ends with two label-free fidelities from our prior work: the local fidelity $L$ at 10 neighbors and the global fidelity $G$ at 30 to 50 percent of the memory. At 96 bytes per passage, rescored binary codes reach an $L$ of 0.97 yet move 10.1 percent of passages to another theme; PCA with 8-bit codes, at an $L$ of 0.77, moves 1.7 percent. Rescoring leaves the stored codes, and thus $G$, unchanged. We prove that across the $G$ band, $1-ν_k$ is at most 2 to 2.18 times the square root of the near-far rank-violation rate, and that this rate follows the distance noise of the compression (correlation 0.979). Our locality-aware quantization (LAQ) turns the bound into a hinge objective on the codebooks of an OPQ index, keeping its bytes, rotation, and search. To our knowledge, LAQ is the first quantizer whose objective comes from a proven bound on the far end. Reconstruction alone raises $G$ in 0 of 52 held-out runs; the far hinge raises it in all 52. LAQ raises $G$ in all 52 ($p=8.5\times 10^{-4}$ over 13 memory-encoder groups), including the external FinDER memory, has the highest $G$ of seven equal-size quantizers in all 12 Multi-Doc-2025 runs, scales to a million passages, and keeps evidence recall.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
