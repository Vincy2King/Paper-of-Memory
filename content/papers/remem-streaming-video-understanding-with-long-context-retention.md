# ReMem: Streaming Video Understanding With Long Context Retention

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.05940v1
- Published: 2026-10-05
- Updated: 2026-10-05
- Authors: Li Yiheng, He Xu, Wang Shaobo, Shao Ling, Lu Shijian
- Tags: benchmark, compression, context
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2610.05940v1

## One-Sentence Summary
Despite their impressive performance on a wide range of video understanding tasks, current Vision Language Models (VLMs) are predominantly designed for offline scenarios and...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Despite their impressive performance on a wide range of video understanding tasks, current Vision Language Models (VLMs) are predominantly designed for offline scenarios and struggle to handle online streaming videos...

进一步看，论文的核心做法或实验重点可以概括为：Several studies have explored memory and token compression strategies in an attempt to adapt offline VLMs for streaming video understanding tasks.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, compression, context
- 检索关键词命中：context memory
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Despite their impressive performance on a wide range of video understanding tasks, current Vision Language Models (VLMs) are predominantly designed for offline scenarios and struggle to handle online streaming videos that demand low latency response. Several studies have explored memory and token compression strategies in an attempt to adapt offline VLMs for streaming video understanding tasks. However, through our probing experiment, we identify that most existing works tend to progressively lose long context information as length of input stream increases. To address this, we propose ReMem, a novel training-free adaptation technique that enables VLMs to process streaming videos of arbitrary lengths while improving their long context information retention capability. ReMem exploits memory from two perspectives, implemented as two core components. The Streaming Context Memory (SCM) continuously compresses historical context with query-independent attention. The Retrieved Vision Memory (RVM) then retrieves the most salient, query-relevant context from memory to augment the VLM's input. Comprehensive experiments demonstrate that the proposed ReMem achieves state-of-the-art (SOTA) performance across a variety of widely used benchmarks, spanning both streaming video and general long video understanding tasks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
