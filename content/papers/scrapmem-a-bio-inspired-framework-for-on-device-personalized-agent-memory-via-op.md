# ScrapMem: A Bio-inspired Framework for On-device Personalized Agent Memory via Optical Forgetting

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.03804v1
- Published: 2026-05-05
- Updated: 2026-05-05
- Authors: Jiale Chang, Yuxiang Ren
- Tags: agent, compression, episodic, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.03804v1

## One-Sentence Summary
Long-term personalized memory for LLM agents is challenging on resource-limited edge devices due to high storage costs and multimodal complexity.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression, episodic, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term personalized memory for LLM agents is challenging on resource-limited edge devices due to high storage costs and multimodal complexity.

进一步看，论文的核心做法或实验重点可以概括为：To address this, we propose ScrapMem, a framework that integrates multimodal data into "Scrapbook Page." ScrapMem introduces Optical Forgetting, an optical compression mechanism that progressively reduces the...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression, episodic, long-term
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term personalized memory for LLM agents is challenging on resource-limited edge devices due to high storage costs and multimodal complexity. To address this, we propose ScrapMem, a framework that integrates multimodal data into "Scrapbook Page." ScrapMem introduces Optical Forgetting, an optical compression mechanism that progressively reduces the resolution of older memories, lowering storage cost while suppressing low-value details. To maintain semantic consistency, we construct an Episodic Memory Graph (EM-Graph) that organizes key events into a causal-temporal structure. Extensive experiments on the multimodal ATM-Bench showcase that ScrapMem provides three main benefits: (1) strong performance, achieving a new state-of-the-art with a 51.0% Joint@10 score; (2) high storage efficiency, reducing memory usage by up to 93% via optical forgetting; and (3) improved recall, increasing Recall@10 to 70.3% through structured aggregation. ScrapMem offers an effective and storage-efficient solution for on-device long-term memory in multimodal LLM agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
