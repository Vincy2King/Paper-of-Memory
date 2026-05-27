# Mitigating Provenance-Role Collapse in Long-Term Agents via Typed Memory Representation

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.25869v1
- Published: 2026-05-25
- Updated: 2026-05-25
- Authors: Zhengda Jin, Bingbing Wang, Jing Li, Ruifeng Xu, Min Zhang
- Tags: agent, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2605.25869v1

## One-Sentence Summary
Long-term memory is essential for persistent LLM agents, yet prevailing architectures store historical interactions as unstructured, flat text.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory is essential for persistent LLM agents, yet prevailing architectures store historical interactions as unstructured, flat text.

进一步看，论文的核心做法或实验重点可以概括为：This unconstrained storage induces provenance-role collapse, a critical failure mode where agents suffer from source-monitoring errors.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-term memory is essential for persistent LLM agents, yet prevailing architectures store historical interactions as unstructured, flat text. This unconstrained storage induces provenance-role collapse, a critical failure mode where agents suffer from source-monitoring errors. To resolve this cognitive vulnerability at the architectural level, we propose MemIR, a typed Memory Intermediate Representation that operationalizes source monitoring as a structural constraint. MemIR writes long-term memory into grounded atoms that separate raw evidence, retrieval cues, and truth-bearing claims, with factual authorization restricted to supported claim atoms. It then applies multi-route atomic projection and provenance-scoped utilization to transform heterogeneous retrieval hits into claim-centered candidate bundles and a normalized fact interface for answer generation. Experiments on LoCoMo and BEAM-100K demonstrate that MemIR consistently outperforms existing memory baselines, especially on tasks requiring source tracking, temporal grounding, and aggregation of fragmented evidence.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
