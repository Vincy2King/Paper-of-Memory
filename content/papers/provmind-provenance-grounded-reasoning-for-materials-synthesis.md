# ProvMind: Provenance-grounded reasoning for materials synthesis

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.28487v1
- Published: 2026-05-27
- Updated: 2026-05-27
- Authors: Yiming Zhang, Ryo Tamura, Koji Tsuda
- Tags: benchmark, retrieval
- Categories: cs.AI, cs.LG
- URL: http://arxiv.org/abs/2605.28487v1

## One-Sentence Summary
Materials process optimization requires reasoning over routes, conditions, tools and causal dependencies, yet most computational formulations flatten synthesis procedures into...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Materials process optimization requires reasoning over routes, conditions, tools and causal dependencies, yet most computational formulations flatten synthesis procedures into text or ordered steps.

进一步看，论文的核心做法或实验重点可以概括为：We introduce MatProcBench, a provenance-grounded benchmark constructed from literature-mined MatPROV graphs, to evaluate seven process-reasoning tasks spanning route continuity, step-level variable inference and...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, retrieval
- 检索关键词命中：memory reasoning
- 来源分类信息：cs.AI, cs.LG

## Abstract Snapshot
Materials process optimization requires reasoning over routes, conditions, tools and causal dependencies, yet most computational formulations flatten synthesis procedures into text or ordered steps. We introduce MatProcBench, a provenance-grounded benchmark constructed from literature-mined MatPROV graphs, to evaluate seven process-reasoning tasks spanning route continuity, step-level variable inference and global causal consistency under both same-split and shift-aware evaluation, including a strict dual-OOD split that combines temporal and material-class shift. We further introduce ProvMind, a process-memory reasoning framework that retrieves analogous training processes, converts them into provenance-aware option-level compatibility scores, and uses a language model for constrained final decision making. ProvMind achieves 52.84\% accuracy on the dual-OOD split, outperforming prompting, retrieval-augmented and supervised fine-tuning baselines.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
