# Broad-Persistent Advising in Interactive Reinforcement Learning via Latent State Encoding

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.13712v1
- Published: 2026-11-10
- Updated: 2026-11-10
- Authors: Zhuoran Liang, Francisco Cruz
- Tags: persistent memory
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.13712v1

## One-Sentence Summary
Deep Interactive Reinforcement Learning (Deep IntRL) accelerates reinforcement learning training by incorporating external advice.

## Introduction
这篇论文被纳入仓库，是因为它和 `persistent memory` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Deep Interactive Reinforcement Learning (Deep IntRL) accelerates reinforcement learning training by incorporating external advice.

进一步看，论文的核心做法或实验重点可以概括为：However, conventional Deep IntRL uses each piece of advice only in the current step and discards it after a single interaction.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：persistent memory
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Deep Interactive Reinforcement Learning (Deep IntRL) accelerates reinforcement learning training by incorporating external advice. However, conventional Deep IntRL uses each piece of advice only in the current step and discards it after a single interaction. Persistent Advising and Broad-Persistent Advising (BPA) extend this process by storing advice in persistent memory and reusing it in similar states through state generalisation based on K-means clustering. This research proposes Encoder BPA, which employs a latent encoder to retrieve and reuse advice. In this framework, a trained encoder is used to map a state sequence into a latent representation at every time step. Advice can be retrieved through latent comparison, together with a top-(k) aggregation and a consistency condition to improve reuse stability. Experimental results show that Encoder BPA improves learning efficiency and advice utilisation at an early stage of training compared with different Deep IntRL approaches, especially in complex and partially observable environments.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
