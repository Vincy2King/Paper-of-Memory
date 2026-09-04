# MemoryLACE: Memory Lifecycle-Aware Consolidation and Evidence Retrieval

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.03201v1
- Published: 2026-09-02
- Updated: 2026-09-02
- Authors: Meriem Yacoubi, Pia Schmidt, Nenad Petrovic, Ahmed Frikha, Martin Kirchhoff, Alois Knoll
- Tags: agent, long-term, retrieval
- Categories: cs.CL, cs.LG
- URL: http://arxiv.org/abs/2609.03201v1

## One-Sentence Summary
Long-term LLM agents must preserve information across interactions while distinguishing repeated evidence, historical states, updates, and unresolved contradictions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term LLM agents must preserve information across interactions while distinguishing repeated evidence, historical states, updates, and unresolved contradictions.

进一步看，论文的核心做法或实验重点可以概括为：Existing textual memory systems retrieve semantically relevant memories efficiently but often leave these relationships implicit, whereas richer structured approaches model them through global graphs, hierarchical...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：long-term memory, memory reasoning, retrieval memory
- 来源分类信息：cs.CL, cs.LG

## Abstract Snapshot
Long-term LLM agents must preserve information across interactions while distinguishing repeated evidence, historical states, updates, and unresolved contradictions. Existing textual memory systems retrieve semantically relevant memories efficiently but often leave these relationships implicit, whereas richer structured approaches model them through global graphs, hierarchical abstractions, or reflection at greater complexity. We introduce MemoryLACE (MemLACE), a lightweight memory framework that explicitly models the lifecycle of textual evidence through sparse merge, supersession, and contradiction relations while preserving atomic natural-language memories and their provenance. Rather than retrieving memories independently, MemLACE reconstructs relation-aware evidence units that expose current, historical, supporting, and conflicting evidence for downstream reasoning. Across BEAM and StructMemEval, using open-weight and proprietary LLM backbones, MemLACE achieves the highest overall performance in same-backbone comparisons while reducing end-to-end runtime on BEAM by 66.6% relative to Hindsight, the strongest reported reflective-memory baseline. Ablation studies identify lifecycle expansion and temporal awareness as the principal contributors to these gains. Together, the results demonstrate that explicitly modeling the local lifecycle of textual evidence is sufficient to substantially improve long-term memory reasoning without requiring comprehensive knowledge graphs or global reflection.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
