# Seeing Further and Wider: Joint Spatio-Temporal Enlargement for Micro-Video Popularity Prediction

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.20311v2
- Published: 2026-04-22
- Updated: 2026-04-23
- Authors: Dali Wang, Yunyao Zhang, Junqing Yu, Yi-Ping Phoebe Chen, Chen Xu, Zikai Song
- Tags: benchmark, retrieval
- Categories: cs.MM, cs.AI
- URL: http://arxiv.org/abs/2604.20311v2

## One-Sentence Summary
Micro-video popularity prediction (MVPP) aims to forecast the future popularity of videos on online media, which is essential for applications such as content recommendation and...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Micro-video popularity prediction (MVPP) aims to forecast the future popularity of videos on online media, which is essential for applications such as content recommendation and traffic allocation.

进一步看，论文的核心做法或实验重点可以概括为：In real-world scenarios, it is critical for MVPP approaches to understand both the temporal dynamics of a given video (temporal) and its historical relevance to other videos (spatial).

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.MM, cs.AI

## Abstract Snapshot
Micro-video popularity prediction (MVPP) aims to forecast the future popularity of videos on online media, which is essential for applications such as content recommendation and traffic allocation. In real-world scenarios, it is critical for MVPP approaches to understand both the temporal dynamics of a given video (temporal) and its historical relevance to other videos (spatial). However, existing approaches sufer from limitations in both dimensions: temporally, they rely on sparse short-range sampling that restricts content perception; spatially, they depend on flat retrieval memory with limited capacity and low efficiency, hindering scalable knowledge utilization. To overcome these limitations, we propose a unified framework that achieves joint spatio-temporal enlargement, enabling precise perception of extremely long video sequences while supporting a scalable memory bank that can infinitely expand to incorporate all relevant historical videos. Technically, we employ a Temporal Enlargement driven by a frame scoring module that extracts highlight cues from video frames through two complementary pathways: sparse sampling and dense perception. Their outputs are adaptively fused to enable robust long-sequence content understanding. For Spatial Enlargement, we construct a Topology-Aware Memory Bank that hierarchically clusters historically relevant content based on topological relationships. Instead of directly expanding memory capacity, we update the encoder features of the corresponding clusters when incorporating new videos, enabling unbounded historical association without unbounded storage growth. Extensive experiments on three widely used MVPP benchmarks demonstrate that our method consistently outperforms 11 strong baselines across mainstream metrics, achieving robust improvements in both prediction accuracy and ranking consistency.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
