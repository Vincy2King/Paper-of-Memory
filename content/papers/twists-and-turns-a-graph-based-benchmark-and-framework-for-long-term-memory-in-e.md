# Twists and Turns: A Graph-Based Benchmark and Framework for Long-Term Memory in Exploration Tasks

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.06414v1
- Published: 2026-11-04
- Updated: 2026-11-04
- Authors: Chongyuan Dai, Yaling Shen, Zirui Song, Junfeng Liao, Jinpeng Hu, Xiuying Chen
- Tags: benchmark, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2611.06414v1

## One-Sentence Summary
Long-term problem-solving processes, such as scientific research and software development, proceed along an evolving trial-and-error trajectory toward a central goal.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term problem-solving processes, such as scientific research and software development, proceed along an evolving trial-and-error trajectory toward a central goal.

进一步看，论文的核心做法或实验重点可以概括为：We term these \textit{exploration tasks}, which require models to remember not only facts but also how solutions are tested against intermediate outcomes and early attempts are continually revised or revived.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-term problem-solving processes, such as scientific research and software development, proceed along an evolving trial-and-error trajectory toward a central goal. We term these \textit{exploration tasks}, which require models to remember not only facts but also how solutions are tested against intermediate outcomes and early attempts are continually revised or revived. However, existing long-term memory research focuses on factual recall and updates, overlooking the interconnected nature of exploration. We observe that exploration processes naturally form graphs, with branching approaches linked by revisions and reconsiderations. Motivated by this, we propose \textsc{LExMem}, a graph-guided benchmark designed to evaluate \underline{\textsc{Mem}}ory in \underline{\textsc{L}}ong-term \underline{\textsc{Ex}}ploration tasks. We model exploration processes as graphs and introduce an evolutionary mechanism to increase their structural complexity, yielding 224 dialogues and 2,018 question-answer instances derived from graph structures. Building on the same insight, we propose \textsc{LExGraph}, a graph-based memory framework that incrementally organizes dialogues into interconnected memory nodes and retrieves evidence through hybrid retrieval and neighbor expansion. Extensive experiments demonstrate that \textsc{LExMem} poses a significant challenge to existing retrieval- and memory-based systems, whereas \textsc{LExGraph} achieves superior performance and generalizes effectively to external benchmarks. Codes and datasets are available at https://github.com/mbzuai-nlp/LExMem.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
