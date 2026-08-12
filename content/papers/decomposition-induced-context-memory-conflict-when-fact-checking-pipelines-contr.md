# Decomposition-Induced Context-Memory Conflict: When Fact-Checking Pipelines Contradict Their Own Source Text

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.10627v1
- Published: 2026-08-11
- Updated: 2026-08-11
- Authors: Yu-Feng Yen
- Tags: context
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.10627v1

## One-Sentence Summary
Decompose-then-verify pipelines, including FActScore-style fact-checkers and long-form factuality evaluators, first split a passage into atomic claims before checking each one.

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Decompose-then-verify pipelines, including FActScore-style fact-checkers and long-form factuality evaluators, first split a passage into atomic claims before checking each one.

进一步看，论文的核心做法或实验重点可以概括为：Decomposition itself is treated as a neutral preprocessing step.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：context memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Decompose-then-verify pipelines, including FActScore-style fact-checkers and long-form factuality evaluators, first split a passage into atomic claims before checking each one. Decomposition itself is treated as a neutral preprocessing step. We show it is not: a decomposer can be induced to substitute its own parametric belief for what the source passage says, producing a claim that contradicts the text it was supposed to summarize faithfully. We call this Decomposition-Induced Context-Memory Conflict (DI-CC) and show it is mechanistically the same phenomenon as classical context-memory conflict, occurring inside a different pipeline stage than prior work has examined. A linear probe trained only on classical context-memory conflict data (NQ-Swap), never exposed to any decomposition output, significantly separates decomposition positions that produce DI-CC from faithful decompositions (AUC = 0.86-0.88, permutation p < 0.0005). An existing reference-free baseline, SelfCheckGPT-style self-consistency sampling, fails to detect DI-CC at all (AUC 0.51, chance-level), because DI-CC content is stably recoverable and recurs across resamples, unlike the variability self-consistency methods rely on. Context-aware decoding, a training-free mitigation from the classical setting, transfers to decomposition and suppresses DI-CC, but at a severe cost: many decompositions under coreference-heavy conditions fail to parse, often because the decomposer fabricates a different identity. We do not consider this mitigation deployment-ready. We further characterize the mechanism's boundaries: its natural occurrence rate is too sparss not manifest on naturally-occurring hallucinatedtext, and it requires a minimum model scale to detecablish DI-CC as a real, mechanistically grounded, andpartially treatable failure mode, with a scope we chhan overstate.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
