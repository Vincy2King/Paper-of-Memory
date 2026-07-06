# Before It Persists: Write-Time Defense for Multimodal Agent Memory

- Source: OpenReview
- Venue: SCALE@ICML2026 Poster
- Paper ID: openreview:6lJ6J3dDOx
- Published: 2026-05-15
- Updated: 2026-07-05
- Authors: Agam Pandey
- Tags: agent, benchmark, retrieval
- Categories: ICML.cc/2026/Workshop/SCALE/-/Submission
- URL: https://openreview.net/forum?id=6lJ6J3dDOx

## One-Sentence Summary
Persistent memory makes multimodal agents more capable, but it also creates a new attack surface: once unsupported content is written into memory, later retrieval and...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `SCALE@ICML2026 Poster` 这个 venue 相关。

从摘要来看，作者主要关注的是：Persistent memory makes multimodal agents more capable, but it also creates a new attack surface: once unsupported content is written into memory, later retrieval and consolidation can reuse it as if it were reliable...

进一步看，论文的核心做法或实验重点可以概括为：We study write-time defense for multimodal agent memory.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：SCALE@ICML2026 Poster
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：agent memory, persistent memory
- 来源分类信息：ICML.cc/2026/Workshop/SCALE/-/Submission

## Abstract Snapshot
Persistent memory makes multimodal agents more capable, but it also creates a new attack surface: once unsupported content is written into memory, later retrieval and consolidation can reuse it as if it were reliable state. We study write-time defense for multimodal agent memory. Our system, SAGE-Mem, separates transient evidence from durable belief : observations may be stored as evidence, but they are promoted to belief only when they are sufficiently supported, independent, and non-conflicting. This targets a gap left by retrieval-time defenses, which act only after poisoned content has already entered memory. We evaluate on LoCoMo-Adv, an adversarial multimodal extension of LoCoMo-10, and on MM-BrowseComp-Adv, a multimodal browsing benchmark covering answer-overwrite, OCR, vision-caption, and visual-prompt attacks. On LoCoMo-Adv, at a conservative operating point, SAGE-Mem eliminates observed write admission and retrieval contamination relative to a retrieval-time baseline, but reduces benign completion under attack (0.460 vs. 0.642). On the canonical browsing overwrite setting, BrowseGuard, a browsing-specific write policy built on the same principle, blocks all 388 direct and paraphrased overwrite attempts while keeping attacked utility near its clean level (0.155 vs. 0.160). On the broader five-attack browsing suite, extending the same guarded write policy across browser, OCR, and caption channels reduces Write ASR from 0.2552 to 0.0369 and Retrieval ASR from 0.5636 to 0.3694. Overall, the results suggest that for memory-bearing agents, robustness should be evaluated not only at retrieval, but also at the point where observations become persistent state.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
