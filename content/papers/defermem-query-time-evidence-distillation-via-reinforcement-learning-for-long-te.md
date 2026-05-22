# DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Memory QA

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.22411v1
- Published: 2026-05-21
- Updated: 2026-05-21
- Authors: Jianing Yin, Tan Tang
- Tags: agent, conversation, long-term, retrieval
- Categories: cs.CL, cs.AI, cs.LG
- URL: http://arxiv.org/abs/2605.22411v1

## One-Sentence Summary
Large language model (LLM) agents still struggle with long-term memory question answering, where answer-supporting evidence is often scattered across long conversational...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents still struggle with long-term memory question answering, where answer-supporting evidence is often scattered across long conversational histories and buried in substantial irrelevant...

进一步看，论文的核心做法或实验重点可以概括为：Existing memory systems typically process memory before future queries are known, then retrieve the resulting units based on similarity rather than their utility for answering the query.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL, cs.AI, cs.LG

## Abstract Snapshot
Large language model (LLM) agents still struggle with long-term memory question answering, where answer-supporting evidence is often scattered across long conversational histories and buried in substantial irrelevant content. Existing memory systems typically process memory before future queries are known, then retrieve the resulting units based on similarity rather than their utility for answering the query. This workflow leaves downstream answerers to denoise retrieved candidates and reconstruct query-specific evidence. We present DeferMem, a long-term memory framework that decouples this problem into high-recall candidate retrieval and query-conditioned evidence distillation. DeferMem uses a lightweight segment-link structure to organize raw history and retrieve broad candidates at query time. It then applies a memory distiller trained with DistillPO, our reinforcement learning algorithm for distilling the high-recall but highly noisy candidates into a set of faithful, self-contained, and query-conditioned evidence. DistillPO formulates post-retrieval evidence distillation as a structured action comprising message selection and evidence rewriting. It optimizes this action with a decomposed-and-gated reward pipeline and structure-aligned advantage assignment, gating reward components from validity to quality checks while exposing task-level correctness feedback early and assigning each reward to its responsible output span. On LoCoMo and LongMemEval-S, DeferMem surpasses strong baselines in QA accuracy and memory-system efficiency, achieving the highest QA accuracy with the fastest runtime and zero commercial-API token cost for memory operations.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
