# Compressing Observation History into Agent Memory: Distilling Transformers into Recurrent Transformers

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.21562v1
- Published: 2026-06-19
- Updated: 2026-06-19
- Authors: Philippe Weinzaepfel, Christian Wolf, Bülent Mert Sariyildiz, Guillaume Bono, Gianluca Monaci
- Tags: agent, compression
- Categories: cs.CV, cs.LG
- URL: http://arxiv.org/abs/2606.21562v1

## One-Sentence Summary
Transformers are AI's workhorse with strong performance in modeling sequential data, but their computational cost becomes prohibitive when processing long sequences.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Transformers are AI's workhorse with strong performance in modeling sequential data, but their computational cost becomes prohibitive when processing long sequences.

进一步看，论文的核心做法或实验重点可以概括为：We target long-horizon streaming vision and robotics applications like map-free pose estimation, where it is particularly impractical to store and maintain a history of observations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression
- 检索关键词命中：agent memory
- 来源分类信息：cs.CV, cs.LG

## Abstract Snapshot
Transformers are AI's workhorse with strong performance in modeling sequential data, but their computational cost becomes prohibitive when processing long sequences. We target long-horizon streaming vision and robotics applications like map-free pose estimation, where it is particularly impractical to store and maintain a history of observations. Recurrent Transformers address this limitation by maintaining fixed-size memory but their performance lags behind that of transformers operating over the full observation history. We argue that this gap does not stem from architectural limitations, but from differences in how these models learn to compress past information. Without access to an observation history, recurrent models must explicitly decide what to retain in memory at each step, a significantly harder learning problem. In this work, we propose a distillation approach that transfers the compression strategy of a classical full-history transformer to a recurrent variant. We enable this by designing a teacher model that explicitly compresses its observation history into a fixed-size bottleneck representation. By directly supervising the student's memory with this bottleneck representation, we align the two compression mechanisms. We show that this approach allows to train a recurrent latent robotic memory with linear-time complexity while substantially narrowing the performance gap to full-history transformers.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
