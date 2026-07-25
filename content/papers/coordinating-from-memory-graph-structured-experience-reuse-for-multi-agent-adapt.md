# Coordinating from Memory: Graph-Structured Experience Reuse for Multi-Agent Adaptation in Dynamic Manufacturing

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.19985v1
- Published: 2026-07-22
- Updated: 2026-07-22
- Authors: Chengxiao Dai, Zhanhui Lin, Zhaokun Yan, Youyang Ni, Chenjun Lei, Luyan Zhang
- Tags: agent, benchmark, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.19985v1

## One-Sentence Summary
Dynamic manufacturing environments require multi-agent systems to coordinate effectively under frequent operational disturbances such as machine failures, urgent job arrivals,...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Dynamic manufacturing environments require multi-agent systems to coordinate effectively under frequent operational disturbances such as machine failures, urgent job arrivals, and processing time variations.

进一步看，论文的核心做法或实验重点可以概括为：Existing multi-agent reinforcement learning approaches treat each disturbance episode independently, discarding valuable coordination experience that could accelerate future adaptation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Dynamic manufacturing environments require multi-agent systems to coordinate effectively under frequent operational disturbances such as machine failures, urgent job arrivals, and processing time variations. Existing multi-agent reinforcement learning approaches treat each disturbance episode independently, discarding valuable coordination experience that could accelerate future adaptation. In this paper, we propose a Graph-Structured Experiential Memory (GSEM) framework for multi-agent coordination in dynamic manufacturing. The framework encodes historical coordination episodes as heterogeneous relational graphs that capture task dependencies, machine states, and inter-agent collaboration patterns. When a new disturbance occurs, a graph neural network-based retrieval mechanism identifies structurally similar past episodes, enabling experience-guided policy adaptation rather than learning from scratch. Experiments on dynamic flexible job-shop scheduling benchmarks with three disturbance types show that GSEM reduces makespan by 4.1%-10.0% and adaptation time by 33%-38% compared to the strongest memory-augmented baseline, with the advantage increasing under higher disturbance frequency. Ablation studies and cross-disturbance transfer experiments further validate the necessity of graph-structured encoding and similarity-based retrieval and demonstrate the cross-disturbance generalizability of learned coordination patterns.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
