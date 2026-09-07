# Linguistic Trajectory Encoding for Efficient Long-Horizon Spatial Memory in Embodied Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.04802v1
- Published: 2026-09-04
- Updated: 2026-09-04
- Authors: Tianyidan Xie, Shenyi Wang, Qiang Tang, Mingjie Wang, Zhicheng Qiu, Xuanfu Li, Zhan Xu, Jian Yang, Lanjun Wang, Zili Yi
- Tags: agent, benchmark, compression, context, retrieval
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2609.04802v1

## One-Sentence Summary
Embodied agents performing long-horizon tasks require a memory representation in which the state transitions of dynamic objects remain queryable in natural language across...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Embodied agents performing long-horizon tasks require a memory representation in which the state transitions of dynamic objects remain queryable in natural language across hours-to-days observation horizons.

进一步看，论文的核心做法或实验重点可以概括为：Existing systems either drop fine-grained motion (clip-level video-language embeddings), keep it only as raw coordinates (geometric SLAM), or organise it around immediate task context (agent working memories).

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, context, retrieval
- 检索关键词命中：memory benchmark, memory benchmarks, working memory
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Embodied agents performing long-horizon tasks require a memory representation in which the state transitions of dynamic objects remain queryable in natural language across hours-to-days observation horizons. Existing systems either drop fine-grained motion (clip-level video-language embeddings), keep it only as raw coordinates (geometric SLAM), or organise it around immediate task context (agent working memories). None of them gives the agent a per-object timeline whose state transitions are themselves queryable in language. Our key contribution is \textbf{Linguistic Trajectory Encoding} (LTE), which compresses dynamic object motion histories via a hybrid representation combining natural language descriptions, sparse spatial anchors, and visual anchors. LTE adapts compression to motion complexity by anchoring periods without reliable observations to the last seen location, while representing motion with geometric waypoints and linguistic descriptions to preserve accuracy. To evaluate these capabilities across extended time horizons, we construct the \textbf{Spatial Memory Benchmark} (SMB) from EgoLife multi-day recordings, targeting capabilities absent in existing benchmarks: semantic trajectory retrieval and long-horizon object retrieval. On SMB, the LTE-based system achieves $45.3\%$ success in semantic trajectory retrieval and $48.7\%$ in long-horizon object retrieval, outperforming structured-memory and VLM baselines (best prior: $31.9\%$ and $34.4\%$). LTE achieves trajectory compression by factors of $8.7\times$ to $26.1\times$ with sub-second query latency on $24$\,h video. On Ego4D natural-language queries, the system reaches $28.75\%$ / $55.10\%$ R@1/R@5, $+15.80$ / $+31.30$ pts over EgoVLPv2.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
