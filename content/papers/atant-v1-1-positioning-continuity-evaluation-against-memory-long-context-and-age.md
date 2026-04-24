# ATANT v1.1: Positioning Continuity Evaluation Against Memory, Long-Context, and Agentic-Memory Benchmarks

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.10981v2
- Published: 2026-04-13
- Updated: 2026-04-19
- Authors: Samuel Sameer Tanguturi
- Tags: agent, benchmark, context
- Categories: cs.AI, cs.IR
- URL: http://arxiv.org/abs/2604.10981v2

## One-Sentence Summary
ATANT v1.0 (arXiv:2604.06710) defined continuity as a system property with 7 required properties and introduced a 10-checkpoint, LLM-free evaluation methodology validated on a...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：ATANT v1.0 (arXiv:2604.06710) defined continuity as a system property with 7 required properties and introduced a 10-checkpoint, LLM-free evaluation methodology validated on a 250-story corpus.

进一步看，论文的核心做法或实验重点可以概括为：Since publication, a recurring reviewer and practitioner question has concerned not the framework itself but its relationship to a wider set of memory evaluations: LOCOMO, LongMemEval, BEAM, MemoryBench, Zep's...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：agent memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.AI, cs.IR

## Abstract Snapshot
ATANT v1.0 (arXiv:2604.06710) defined continuity as a system property with 7 required properties and introduced a 10-checkpoint, LLM-free evaluation methodology validated on a 250-story corpus. Since publication, a recurring reviewer and practitioner question has concerned not the framework itself but its relationship to a wider set of memory evaluations: LOCOMO, LongMemEval, BEAM, MemoryBench, Zep's evaluation suite, Letta/MemGPT's evaluations, and RULER. This companion paper, v1.1, does not modify the v1.0 standard. It closes a related-work gap that v1.0 left brief under page limits. We show by structural analysis that none of these benchmarks measures continuity as defined in v1.0: of the 7 required properties, the median existing eval covers 1 property, the mean covers 0.43 when partial credit is scored at 0.5, and no eval covers more than 2. We provide a cell-by-cell property-coverage matrix, identify methodological defects specific to each benchmark (including an empty-gold scoring bug in the LOCOMO reference implementation that renders 23% of its corpus unscorable by construction), and publish our reference implementation's LOCOMO score (8.8%) alongside the structural reason that number is uninformative about continuity. We publish our 8.8% LOCOMO score alongside our 96% ATANT cumulative-scale score as a calibration pair: the 87-point divergence is evidence that the two benchmarks measure different properties, not that one system is an order of magnitude better than another. The position v1.1 takes is not adversarial: each benchmark measures a real capability. The claim is that none of them can adjudicate continuity, and conflating them with continuity evaluation has led the field to under-invest in the properties v1.0 names.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
