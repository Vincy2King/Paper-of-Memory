# The Right Memory in the Wrong Context: Verifying Retrieval Admissibility in Long-Term Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.07309v1
- Published: 2026-10-05
- Updated: 2026-10-05
- Authors: Zi Wang, Xingqiao Wang, Emmanuel Addai, Devika Ambekar, Xiaowei Xu
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.AI, cs.IR, cs.MA
- URL: http://arxiv.org/abs/2610.07309v1

## One-Sentence Summary
Long-term-memory agents can retrieve relevant information that is inadmissible for the current request because it belongs to another principal, violates policy, or reflects an...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term-memory agents can retrieve relevant information that is inadmissible for the current request because it belongs to another principal, violates policy, or reflects an incompatible lifecycle state.

进一步看，论文的核心做法或实验重点可以概括为：Recall and final-answer accuracy do not reveal this: a route can appear safe by missing required evidence, while a correct answer may follow inadmissible prompt exposure.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.AI, cs.IR, cs.MA

## Abstract Snapshot
Long-term-memory agents can retrieve relevant information that is inadmissible for the current request because it belongs to another principal, violates policy, or reflects an incompatible lifecycle state. Recall and final-answer accuracy do not reveal this: a route can appear safe by missing required evidence, while a correct answer may follow inadmissible prompt exposure. We introduce a retrieval-admissibility verification framework that assigns each memory-query pair one of three statuses (admissible, inadmissible, or unresolved), compares routes at matched required-evidence recall with bounds for unresolved cases, and tracks memory IDs through prompt exposure while linking exposure to target-level disclosure. We evaluate its stages on separate, non-pooled populations. A post-hoc top-20 reanalysis of frozen rankings from two public long-term-memory benchmarks, RHELM and MemOps, covers 3,767 queries. All released anchors lie within trusted query namespaces; with within-namespace scores unchanged, off-namespace filtering cannot lower their ranks. Top-20 anchor recall increases from 0.432 to 0.533, 80% recall feasibility from 0.237 to 0.311, and exact similarity evaluations decrease by 98.3%. In a frozen 72-case development diagnostic, a released-metadata reference preserves required evidence, whereas neither text-only verifier detects violations under the 1% required-anchor false-denial limit. Across 1,523 paired benchmark-native cases, namespace routing is associated with judged-accuracy gains of 0.053-0.068 across three readers; recall also changes, so this comparison is observational. In 16 controlled exposure scenarios, only one of four reader-specific 95% confidence intervals excludes zero for relevant-inadmissible literal disclosure (+0.156, 95% CI [0.031, 0.312]). Results motivate separate verification of candidate support, admissibility, prompt exposure, and answer disclosure.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
