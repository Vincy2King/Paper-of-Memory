# Workspace Models: Lightweight Robotic Memory via Saliency-Driven Supervision

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.20820v3
- Published: 2026-09-17
- Updated: 2026-09-30
- Authors: Nitish Dashora, Douglas Chen, Idan Shenfeld, John Marangola, Pulkit Agrawal, Max Simchowitz
- Tags: long-term
- Categories: cs.RO, cs.AI
- URL: http://arxiv.org/abs/2609.20820v3

## One-Sentence Summary
Complex robotic manipulation tasks frequently require a long-term memory of past events and actions.

## Introduction
这篇论文被纳入仓库，是因为它和 `long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Complex robotic manipulation tasks frequently require a long-term memory of past events and actions.

进一步看，论文的核心做法或实验重点可以概括为：As conditioning on full histories renders policies prone to spurious correlations and degrades performance, many approaches to policy memory involve compressing historical information through expensive VLM queries in-...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.RO, cs.AI

## Abstract Snapshot
Complex robotic manipulation tasks frequently require a long-term memory of past events and actions. As conditioning on full histories renders policies prone to spurious correlations and degrades performance, many approaches to policy memory involve compressing historical information through expensive VLM queries in-the-loop to process only task-salient information. In this paper, we propose an alternative approach in which computationally intensive VLM queries are made during train-time to learn a lightweight latent memory that can be efficiently queried at deployment time. Our representation, which we call the workspace token, is trained by (1) using a VLM to identify current and historical information necessary for completing a task, then (2) distilling these into the workspace token using a set-reconstruction decoder loss. In both simulation and hardware, we show that the workspace token can be used as a drop-in replacement for observations during deployment, enabling policies to solve memory-intensive tasks without the need for VLM reasoning in-the-loop, in effect serving as a latent harness for distilling a stronger reasoning models ability to solve long-horizon tasks to a reactive robotic policy. We further demonstrate that the workspace tokens are not only more lightweight, but also lead to better policy performance compared to conditioning policies on explicit modalities like curated past image frames, motivating a latent approach to history curation and reasoning model harnesses more broadly.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
