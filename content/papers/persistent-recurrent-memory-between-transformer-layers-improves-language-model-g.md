# Persistent Recurrent Memory Between Transformer Layers - Improves Language Model Generalization

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.17251v1
- Published: 2026-09-15
- Updated: 2026-09-15
- Authors: Eduardo Novaes Hering
- Tags: persistent memory
- Categories: cs.CL
- URL: http://arxiv.org/abs/2609.17251v1

## One-Sentence Summary
We introduce a simple architectural modification to decoder-only transformers: a persistent recurrent state that observes hidden representations via cross-attention, updates...

## Introduction
这篇论文被纳入仓库，是因为它和 `persistent memory` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We introduce a simple architectural modification to decoder-only transformers: a persistent recurrent state that observes hidden representations via cross-attention, updates itself through a GRU, and modulates...

进一步看，论文的核心做法或实验重点可以概括为：Inserted between the lower and upper halves of a 6-layer transformer, this module adds only 3.7\% additional parameters while reducing evaluation loss from $2.438 \pm 0.004$ to $1.743 \pm 0.018$, corresponding to a...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：persistent memory
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
We introduce a simple architectural modification to decoder-only transformers: a persistent recurrent state that observes hidden representations via cross-attention, updates itself through a GRU, and modulates subsequent processing via gated addition. Inserted between the lower and upper halves of a 6-layer transformer, this module adds only 3.7\% additional parameters while reducing evaluation loss from $2.438 \pm 0.004$ to $1.743 \pm 0.018$, corresponding to a 28.5\% reduction on held-out language modeling data. The improvement is statistically significant across 5 random seeds ($p < 0.01$) and corresponds to reduced overfitting (generalization gap 0.12 vs 0.26). Through controlled ablations, we demonstrate that the improvement stems entirely from the persistent memory topology, not from auxiliary self-prediction objectives. A model with identical topology but no auxiliary loss performs equivalently, while a random auxiliary loss provides no benefit. Representation probing reveals that the persistent state encodes narrative position (52\% vs 33\% chance level)---information that standard attention maintains less efficiently. Our results suggest that bridging transformer layers with a lightweight recurrent memory is a simple, effective approach to improving generalization in small-scale language models.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
