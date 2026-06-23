# Negative Knowledge as Failure-aware Shared Memory for AutoResearch

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.21024v1
- Published: 2026-06-19
- Updated: 2026-06-19
- Authors: Hanchun Wang
- Tags: agent, compression
- Categories: cs.AI, cs.CY, cs.LG, cs.MA
- URL: http://arxiv.org/abs/2606.21024v1

## One-Sentence Summary
AI-assisted research systems generate many failed attempts, but those failures rarely become a durable, shared knowledge asset.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：AI-assisted research systems generate many failed attempts, but those failures rarely become a durable, shared knowledge asset.

进一步看，论文的核心做法或实验重点可以概括为：We propose a negative knowledge memory layer: a curator agent converts each failed attempt into a bounded, typed record in a shared bank, and a downstream research agent explicitly adopts or rejects those records...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression
- 检索关键词命中：memory compression
- 来源分类信息：cs.AI, cs.CY, cs.LG, cs.MA

## Abstract Snapshot
AI-assisted research systems generate many failed attempts, but those failures rarely become a durable, shared knowledge asset. We propose a negative knowledge memory layer: a curator agent converts each failed attempt into a bounded, typed record in a shared bank, and a downstream research agent explicitly adopts or rejects those records before proposing its next experiment. We evaluate this layer in two settings: same-task retry on ScienceAgentBench and cross-task scientific research on two nonlinear math-physics PDE problems. The negative knowledge layer outperforms vanilla AutoResearch baselines while using fewer tokens; agents with the negative knowledge bank solve new tasks that all baselines fail to solve in PDE systems research. We also show that the previous negative knowledge bank can transfer and enhance AutoResearch on different PDE problems. These results suggest that structured negative knowledge is a knowledge asset that should be explicitly maintained in broader AI-engaged scientific research beyond a memory-compression or debugging aid, alongside positive findings, as a collective infrastructure for scientific memory. Code is available at https://github.com/hch-wang/Negative_Knowledge.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
