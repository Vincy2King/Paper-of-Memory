# MedCache: Efficient and Temporally Valid Memory for Longitudinal Clinical Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.29528v1
- Published: 2026-08-30
- Updated: 2026-08-30
- Authors: Hei Ting, Chan, Chenwei Wu, Xueshen Liu, Boyuan Zheng, Liyue Shen, Jiasi Chen, Z. Morley Mao
- Tags: agent, benchmark, context, retrieval
- Categories: cs.LG, cs.DC, cs.MA
- URL: http://arxiv.org/abs/2608.29528v1

## One-Sentence Summary
Longitudinal clinical agents must maintain an evolving patient state from evidence distributed across visits, time points, and specialties.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Longitudinal clinical agents must maintain an evolving patient state from evidence distributed across visits, time points, and specialties.

进一步看，论文的核心做法或实验重点可以概括为：However, how agent memory should be designed for this setting remains unclear.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：agent memory, memory augmented, memory-augmented
- 来源分类信息：cs.LG, cs.DC, cs.MA

## Abstract Snapshot
Longitudinal clinical agents must maintain an evolving patient state from evidence distributed across visits, time points, and specialties. However, how agent memory should be designed for this setting remains unclear. We introduce a benchmark of multi-visit, multi-specialty patient records that evaluates long-context evidence retrieval, cross-time evidence aggregation, and cross-specialty clinical reasoning. Using this benchmark, we systematically study four memory design choices: curation, organization, retrieval, and memory-augmented reasoning. We find that temporal validity is more important than simply retaining more history; specialty-factorized memory reduces context but can hide shared evidence; and multiple agents help when specialists must reason together, not merely when evidence comes from multiple memories. Guided by these findings, we propose \textit{MedCache}, a hybrid framework that constructs temporally valid patient memory, organizes evidence into overlapping specialty views, routes each query to relevant memories, and adaptively invokes one or multiple specialists. Experiments show that MedCache improves reasoning accuracy and memory efficiency over strong single-agent and multi-agent baselines, while generalizing across model backbones and external datasets.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
