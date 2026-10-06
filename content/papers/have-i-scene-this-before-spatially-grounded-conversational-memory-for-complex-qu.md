# Have I Scene This Before? Spatially Grounded Conversational Memory for Complex Queries in Egocentric Assistants

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.05526v1
- Published: 2026-10-04
- Updated: 2026-10-04
- Authors: Jiazhou Liang, Liam Gallagher, Kiko Chen, David Guo, Armin Toroghi, Yifan Simon Liu, Scott Sanner
- Tags: benchmark, context, conversation, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.05526v1

## One-Sentence Summary
Egocentric assistants must connect what users say with what they see across long interaction histories.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Egocentric assistants must connect what users say with what they see across long interaction histories.

进一步看，论文的核心做法或实验重点可以概括为：We formalize this challenge as Spatially grounded Conversational Reasoning (SpaCR): cross-scene, recall-oriented, and counterfactual spatial queries that combine user-stated facts with geometric evidence.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, conversation, retrieval
- 检索关键词命中：conversational memory, working memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Egocentric assistants must connect what users say with what they see across long interaction histories. We formalize this challenge as Spatially grounded Conversational Reasoning (SpaCR): cross-scene, recall-oriented, and counterfactual spatial queries that combine user-stated facts with geometric evidence. Direct vision-language models incur high inference costs and context limits as histories grow, while keyframe selection and retrieval can omit objects or evidence needed for complete recall. We propose Spatially grounded Conversational Memory (SpaC-MEM), an object-centric working memory that uses 3D reconstruction and segmentation to ground conversational information in persistent physical objects. It compresses multimodal histories while preserving spatial evidence and allowing object-specific facts to be updated through dialogue. We also introduce Ego-SpaCR, a benchmark comprising 620 ScanNet video sessions augmented with 95 task-oriented conversations and 3,100 evaluation queries. SpaC-MEM achieves the highest overall answer accuracy among the evaluated methods and improves object recall while requiring substantially fewer reference input tokens than native-video baselines. Removing 3D spatial information substantially degrades performance, highlighting the importance of preserving spatial and conversational evidence together.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
