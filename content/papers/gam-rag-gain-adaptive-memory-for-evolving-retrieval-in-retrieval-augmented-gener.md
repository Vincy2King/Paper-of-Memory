# GAM-RAG: Gain-Adaptive Memory for Evolving Retrieval in Retrieval-Augmented Generation

- Source: OpenReview
- Venue: ICML 2026 regular
- Paper ID: openreview:9YC7mbloXl
- Published: 2026-04-30
- Updated: 2026-06-24
- Authors: Yifan Wang, Mingxuan Jiang, Zhihao Sun, Yixin Cao, Yicun Liu, Keyang Chen, Guangnan Ye, Hongfeng Chai
- Tags: retrieval
- Categories: ICML.cc/2026/Conference/-/Submission
- URL: https://openreview.net/forum?id=9YC7mbloXl

## One-Sentence Summary
Retrieval-Augmented Generation (RAG) grounds large language models with external evidence, but many implementations rely on pre-built indices that remain static after construction.

## Introduction
这篇论文被纳入仓库，是因为它和 `retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ICML 2026 regular` 这个 venue 相关。

从摘要来看，作者主要关注的是：Retrieval-Augmented Generation (RAG) grounds large language models with external evidence, but many implementations rely on pre-built indices that remain static after construction.

进一步看，论文的核心做法或实验重点可以概括为：Related queries therefore repeat similar multi-hop traversal, increasing latency and compute.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ICML 2026 regular
- 高亮主题命中：retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：ICML.cc/2026/Conference/-/Submission

## Abstract Snapshot
Retrieval-Augmented Generation (RAG) grounds large language models with external evidence, but many implementations rely on pre-built indices that remain static after construction. Related queries therefore repeat similar multi-hop traversal, increasing latency and compute. Motivated by schema-based learning in cognitive neuroscience, we propose GAM-RAG, a training-free framework that accumulates retrieval experience from recurring or related queries and updates retrieval memory over time. GAM-RAG builds a lightweight, relation-free hierarchical index whose links capture potential co-occurrence rather than fixed semantic relations. During inference, successful retrieval episodes provide sentence-level feedback, updating sentence memories so evidence useful for similar reasoning types becomes easier to activate later. To balance stability and adaptability under noisy feedback, we introduce an uncertainty-aware, Kalman-inspired gain rule that jointly updates memory states and uncertainty estimates. It applies fast updates for reliable novel signals and conservative refinement for stable or noisy memories. We provide a theoretical analysis of the update dynamics, and empirically show that GAM-RAG improves average performance by 3.95\% over the strongest baseline and by 8.19\% with 5-turn memory, while reducing inference cost by 61\%.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
