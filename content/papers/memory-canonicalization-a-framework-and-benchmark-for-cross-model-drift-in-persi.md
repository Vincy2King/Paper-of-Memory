# Memory Canonicalization: A Framework and Benchmark for Cross-Model Drift in Persistent LLM Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.05124v1
- Published: 2026-10-04
- Updated: 2026-10-04
- Authors: Amit Vadnere, Aishwarya Lonarkar
- Tags: agent, benchmark, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.05124v1

## One-Sentence Summary
Persistent memory for Large Language Models (LLMs) has matured rapidly: systems such as MemGPT/Letta, Mem0, and Zep now provide agents with tiered, temporally-aware, model-...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent memory for Large Language Models (LLMs) has matured rapidly: systems such as MemGPT/Letta, Mem0, and Zep now provide agents with tiered, temporally-aware, model-agnostic external storage, while the Model...

进一步看，论文的核心做法或实验重点可以概括为：A less addressed problem is that an identical stored memory object, retrieved by two different LLMs under otherwise identical conditions, may not be interpreted the same way, factually or emotionally.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Persistent memory for Large Language Models (LLMs) has matured rapidly: systems such as MemGPT/Letta, Mem0, and Zep now provide agents with tiered, temporally-aware, model-agnostic external storage, while the Model Context Protocol (MCP) standardizes access to memory servers. A less addressed problem is that an identical stored memory object, retrieved by two different LLMs under otherwise identical conditions, may not be interpreted the same way, factually or emotionally. This paper proposes memory canonicalization: a write-time pipeline that detects ambiguity, conditional structure, and emotional loading in a raw memory object and rewrites it into an explicit, structurally disambiguated canonical form, with emotional valence represented as a separate field rather than inferred from tone. We formalize the pipeline, define a companion Cross-Model Semantic Drift / Emotional Consistency Score benchmark (CMSC-E), and report results from a three-arm pilot using 176 synthetic memory objects and three downstream model families. We find an uncorrected improvement in cross-model emotional consistency for fully canonicalized memory relative to raw memory (+0.050, 95% bootstrap CI [0.013, 0.086], paired t-test p = 0.010), but this result does not survive Bonferroni, Holm, or Benjamini-Hochberg correction across the six comparisons tested. None of the factual-drift (CMSD) comparisons reach significance at any correction level. We report these results as exploratory rather than confirmatory and outline needed follow-up work, including larger samples, independent judge models, human-validated rendering, and preregistration.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
