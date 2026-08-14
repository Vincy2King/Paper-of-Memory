# RippleMem: From Isolated Retrieval to Associative Recollection for Long-Term Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.13334v1
- Published: 2026-08-13
- Updated: 2026-08-13
- Authors: Jingbo Ji, Lingyi Li, Xilong Cheng, Yuhao Zhou, Wenji Zhang, Yuting Tan, Yunxiao Qin
- Tags: agent, context, episodic, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.13334v1

## One-Sentence Summary
LLM-based agents increasingly rely on external memory to support long-horizon reasoning and interaction.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, episodic, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM-based agents increasingly rely on external memory to support long-horizon reasoning and interaction.

进一步看，论文的核心做法或实验重点可以概括为：However, the main bottleneck is not simply storing past experience, but recovering the right set of evidence when relevant information is distributed across many interactions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, episodic, long-term, retrieval
- 检索关键词命中：agent memory, episodic memory, long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
LLM-based agents increasingly rely on external memory to support long-horizon reasoning and interaction. However, the main bottleneck is not simply storing past experience, but recovering the right set of evidence when relevant information is distributed across many interactions. Existing approaches struggle with this access problem. Full-context methods require noisy long-context search, flat retrieval often returns isolated and incomplete records, and graph-based memory systems can be expensive to construct while compressing rich event context. We introduce RippleMem, a long-term memory system that replaces one-shot retrieval with adaptive associative recollection. Inspired by cue-dependent episodic retrieval and associative completion, RippleMem stores interaction history as cue-rich episodic memory units and organizes them in an event-centric memory graph. Given a query, it first recalls relevant memory anchors through hybrid cues, then expands from these anchors along semantic and structural associations to recover missing supporting evidence. In this way, initially recalled memories serve not only as answer context, but also as cues for completing the evidence needed to answer. Experiments on LoCoMo and LongMemEval-S show that RippleMem achieves the best overall performance across evaluated settings, improving LLM-as-a-Judge accuracy by 3.95% on LoCoMo and up to 11.87% on LongMemEval-S, while reducing graph construction cost by about 30x.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
