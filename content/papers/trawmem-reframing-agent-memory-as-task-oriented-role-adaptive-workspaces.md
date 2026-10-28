# TrawMem: Reframing Agent Memory as Task-Oriented Role-Adaptive Workspaces

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.36918v1
- Published: 2026-10-27
- Updated: 2026-10-27
- Authors: Mingyu Zhang, Zixu Li, Zhiheng Fu, Zhiwei Chen, Jinhe Bi, Yupeng Hu
- Tags: agent, context, long-term
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.36918v1

## One-Sentence Summary
Large language model (LLM) agents rely on memory systems to leverage long-term interactions, yet existing systems typically retrieve memories based on their relevance to the...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents rely on memory systems to leverage long-term interactions, yet existing systems typically retrieve memories based on their relevance to the current query and use them as contextual...

进一步看，论文的核心做法或实验重点可以概括为：However, relevance alone does not characterize how a memory contributes to task solving: the same memory may serve different roles across tasks, such as directly supporting the answer or linking to complementary...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term
- 检索关键词命中：agent memory, retrieval memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Large language model (LLM) agents rely on memory systems to leverage long-term interactions, yet existing systems typically retrieve memories based on their relevance to the current query and use them as contextual evidence. However, relevance alone does not characterize how a memory contributes to task solving: the same memory may serve different roles across tasks, such as directly supporting the answer or linking to complementary memories with weaker semantic relevance but necessary information. We therefore reframe agent memory systems as Task-Oriented Role-Adaptive Workspaces, where memories are selected and organized by their task-oriented roles and relations. Based on this view, we propose TrawMem, which organizes interaction histories into local threads and constructs task-oriented workspaces by assigning roles and jointly selecting complementary memories. Experiments on LoCoMo and MemGallery with four open- and closed-source backbones show consistent improvements over representative memory systems, with macro-F1 gains of 2.23-3.14 points. On LoCoMo, TrawMem improves the LLM-Judge score over SimpleMem by 4.07 and 4.31 percentage points on Qwen3.5-9B and DeepSeek-V4-Flash, respectively, while requiring approximately 12.8% and 5.1% fewer context tokens, respectively.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
