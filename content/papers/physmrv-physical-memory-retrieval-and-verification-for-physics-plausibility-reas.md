# PhysMRV: Physical Memory Retrieval and Verification for Physics Plausibility Reasoning

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.10190v1
- Published: 2026-07-11
- Updated: 2026-07-11
- Authors: Wenyuan Wang, Lianyu Hu, Hao Wang, Yang Liu
- Tags: benchmark, context, retrieval
- Categories: cs.LG, cs.AI, cs.CV
- URL: http://arxiv.org/abs/2607.10190v1

## One-Sentence Summary
Video-language models (VLMs) have achieved remarkable performance on video understanding and visual question answering, yet they remain unreliable in reasoning about physical...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Video-language models (VLMs) have achieved remarkable performance on video understanding and visual question answering, yet they remain unreliable in reasoning about physical plausibility, where understanding object...

进一步看，论文的核心做法或实验重点可以概括为：This limitation is particularly evident on challenging physical reasoning benchmarks, revealing a persistent gap in physical commonsense reasoning.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.LG, cs.AI, cs.CV

## Abstract Snapshot
Video-language models (VLMs) have achieved remarkable performance on video understanding and visual question answering, yet they remain unreliable in reasoning about physical plausibility, where understanding object interactions, causal dynamics, and fundamental physical principles is essential. This limitation is particularly evident on challenging physical reasoning benchmarks, revealing a persistent gap in physical commonsense reasoning. To address this challenge, we propose PhysMRV, a training-free physical memory and verification framework for physical plausibility reasoning. Unlike retrieval-augmented VLMs that retrieve semantically similar videos as additional context, PhysMRV transforms training videos into a Hierarchical Memory Bank of structured physical knowledge comprising three complementary levels: scene descriptions capturing visual context, physical-event graphs modeling object interactions and causal structure, and physics-rule summaries distilling reusable physical principles and cues. During inference, PhysMRV retrieves physically relevant memories and leverages their structured physical evidence to guide a frozen VLM in verifying physical plausibility, requiring neither fine-tuning nor parameter updates. We evaluate PhysMRV on three challenging physical reasoning benchmarks, ImplausiBench, IntPhys2, and GRASP Level 2, across multiple state-of-the-art VLMs. Experimental results demonstrate consistent improvements over direct prompting across diverse VLMs and evaluation benchmarks, showing that structured physical memories provide an effective and scalable means of enhancing physical plausibility reasoning without additional training.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
