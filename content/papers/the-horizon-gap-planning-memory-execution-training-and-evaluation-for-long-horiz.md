# The Horizon Gap: Planning, Memory, Execution, Training, and Evaluation for Long-Horizon LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.06663v1
- Published: 2026-08-07
- Updated: 2026-08-07
- Authors: Mingguang Chen, Licheng Wang, Bo Qu
- Tags: agent, context, long-term
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.06663v1

## One-Sentence Summary
Frontier language models solve reasoning problems in a single forward pass that would have been research contributions years ago, yet fail at multi-hour tasks: losing track of...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Frontier language models solve reasoning problems in a single forward pass that would have been research contributions years ago, yet fail at multi-hour tasks: losing track of earlier decisions, declaring half-...

进一步看，论文的核心做法或实验重点可以概括为：We call this the horizon gap and survey 1,547 arXiv papers (2024-2026) collected via systematic seed harvest with a disclosed 26.8% bleed filter, extended by targeted supplementation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Frontier language models solve reasoning problems in a single forward pass that would have been research contributions years ago, yet fail at multi-hour tasks: losing track of earlier decisions, declaring half-finished work done, or drifting from goals. We call this the horizon gap and survey 1,547 arXiv papers (2024-2026) collected via systematic seed harvest with a disclosed 26.8% bleed filter, extended by targeted supplementation. We disambiguate three routinely conflated properties: long-horizon (task property: required steps), long-context (model property: token capacity), and long-term memory (system property: persistence across steps/sessions). We organize the corpus into six categories tracking a long-horizon task's lifecycle -- planning, memory, execution, training, evaluation, and foundations/safety -- crossed with an axis capturing where horizons are carried (within-context, within-task-beyond-context, or cross-task-persistent). Across all categories, we find the same pattern: outcome-only signals grow uninformative as horizons lengthen, and the field's response -- whether process reward models, credit assignment, or trajectory-level diagnostics -- manufactures denser step-level signals. We treat critical and diagnostic literature as first-class threads throughout, arguing that segregating critique from method would routinely split single papers across chapters. We close by naming open measurement problems: decomposing model versus harness capability, managing correlated bias in process-level signals used for both training and evaluation, and whether long-horizon reliability admits general predictive theory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
