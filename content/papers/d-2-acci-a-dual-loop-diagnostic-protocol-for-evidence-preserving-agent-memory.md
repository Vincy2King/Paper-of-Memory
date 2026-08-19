# D$^2$ACCI: A Dual-Loop Diagnostic Protocol for Evidence-Preserving Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.17756v1
- Published: 2026-08-18
- Updated: 2026-08-18
- Authors: Xule Liu, Yijun Liu, Chao Li, Shao Kun
- Tags: agent, benchmark, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.17756v1

## One-Sentence Summary
Memory is a key capability of LLM agents.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory is a key capability of LLM agents.

进一步看，论文的核心做法或实验重点可以概括为：Persistent memory extends this across sessions---enabling recall, revision, and personalization.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：agent memory, memory retrieval, persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Memory is a key capability of LLM agents. Persistent memory extends this across sessions---enabling recall, revision, and personalization. Yet its multi-stage pipeline (ingestion, retrieval, filtering, generation) makes failures difficult to localize: end-to-end evaluation reveals that an error occurred, but not which stage caused it. Existing evaluations often report aggregate performance without paired statistical comparisons, slice-level non-regression checks, or stage-level diagnostic traces. We propose D$^2$ACCI (Diagnostic-Driven Artifact-based Closed-loop Controlled Iteration), a dual-loop protocol whose outer diagnostic gate promotes, feature-flags, or rejects memory interventions based on paired evidence, protected-slice monitoring, and trace-level localizability. We further introduce DCR, a graded observability metric that measures whether failures remain localizable, and D$^2$ACCI-Eval, a reusable artifact for gate replay. We instantiate the protocol in MemStack and evaluate on three public benchmarks, achieving 93.59% on LoCoMo, 90.93% on LongMemEval, and 57.20% on PersonaMem-V2. Five paired ablations show that supplement extraction, session-memory retrieval, and Forget Guard yield statistically significant gains (+1.9 to +3.7pp, all p $\le$ .003). In contrast, BM25/RRF is retained as a monitored feature flag---a distinction invisible to aggregate-only evaluation. A diagnostic audit shows enriched traces substantially improve root-cause agreement over result-only relabeling. Diagnostic artifacts reach 98--100% DCR@3 versus 0% for results-only logs. These results establish that robust memory-system iteration demands traceable, statistically grounded, and regression-aware evidence---exactly the gap D$^2$ACCI fills.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
