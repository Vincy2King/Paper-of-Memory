# OilSAM2: Memory-Augmented SAM2 for Scalable SAR Oil Spill Detection

- Source: OpenReview
- Venue: CoRR 2026
- Paper ID: openreview:3R3GPwjuDQ
- Published: 2026-12-31
- Updated: 2026-07-14
- Authors: {'fullname': 'Shuaiyu Chen', 'username': ''}, {'fullname': 'Ming Yin', 'username': ''}, {'fullname': 'Peng Ren', 'username': ''}, {'fullname': 'Chunbo Luo', 'username': '~Chunbo_Luo2'}, {'fullname': 'Zeyu Fu', 'username': ''}
- Tags: memory augmented, memory-augmented
- Categories: OpenReview.net/Public_Article/DBLP.org/-/Record
- URL: https://openreview.net/forum?id=3R3GPwjuDQ

## One-Sentence Summary
Segmenting oil spills from Synthetic Aperture Radar (SAR) imagery remains challenging due to severe appearance variability, scale heterogeneity, and the absence of temporal...

## Introduction
这篇论文被纳入仓库，是因为它和 `memory augmented, memory-augmented` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `CoRR 2026` 这个 venue 相关。

从摘要来看，作者主要关注的是：Segmenting oil spills from Synthetic Aperture Radar (SAR) imagery remains challenging due to severe appearance variability, scale heterogeneity, and the absence of temporal continuity in real world monitoring scenarios.

进一步看，论文的核心做法或实验重点可以概括为：While foundation models such as Segment Anything (SAM) enable prompt driven segmentation, existing SAM based approaches operate on single images and cannot effectively reuse information across scenes.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：CoRR 2026
- 高亮主题命中：memory augmented, memory-augmented
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：OpenReview.net/Public_Article/DBLP.org/-/Record

## Abstract Snapshot
Segmenting oil spills from Synthetic Aperture Radar (SAR) imagery remains challenging due to severe appearance variability, scale heterogeneity, and the absence of temporal continuity in real world monitoring scenarios. While foundation models such as Segment Anything (SAM) enable prompt driven segmentation, existing SAM based approaches operate on single images and cannot effectively reuse information across scenes. Memory augmented variants (e.g., SAM2) further assume temporal coherence, making them prone to semantic drift when applied to unordered SAR image collections. We propose OilSAM2, a memory augmented segmentation framework tailored for unordered SAR oil spill monitoring. OilSAM2 introduces a hierarchical feature aware multi scale memory bank that explicitly models texture, structure, and semantic level representations, enabling robust cross image information reuse. To mitigate memory drift, we further propose a structure semantic consistent memory update strategy that selectively refreshes memory based on semantic discrepancy and structural variation.Experiments on two public SAR oil spill datasets demonstrate that OilSAM2 achieves state of the art segmentation performance, delivering stable and accurate results under noisy SAR monitoring scenarios. The source code is available at https://github.com/Chenshuaiyu1120/OILSAM2.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
