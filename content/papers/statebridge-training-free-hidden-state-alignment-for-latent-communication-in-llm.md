# StateBridge: Training-free Hidden-state Alignment for Latent Communication in LLM Multi-Agent Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.13317v1
- Published: 2026-08-13
- Updated: 2026-08-13
- Authors: Yanwen Peng, Delvin Ce Zhang, Xi Wang, Nikolaos Aletras
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.13317v1

## One-Sentence Summary
Large language model based multi-agent systems usually communicate in text, i.e., using discrete tokens.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model based multi-agent systems usually communicate in text, i.e., using discrete tokens.

进一步看，论文的核心做法或实验重点可以概括为：However, text introduces a discrete bottleneck.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：working memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language model based multi-agent systems usually communicate in text, i.e., using discrete tokens. However, text introduces a discrete bottleneck. Converting the sender's continuous hidden states into discrete tokens discards information that token identities alone cannot capture. Recent work proposes latent communication as an alternative, where agents transmit hidden representations directly without converting them to text. However, existing latent methods either inject working memory layer by layer across the transformers, or require trained projectors that limit portability. We propose StateBridge, a training-free latent communication approach that aligns the sender's final-layer hidden states to the receiver's input space via a closed-form orthogonal transformation. Lightweight norm calibration and vocabulary anchoring ensure compatibility with the pretrained input distribution. The aligned states are prepended to the input of the receiver agent as a continuous prefix. We evaluate StateBridge on math reasoning, code generation, and question answering with four models from two families. StateBridge achieves the best or tied-best score on 22 out of 26 model-task pairs, consistently outperforming the strongest baseline.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
