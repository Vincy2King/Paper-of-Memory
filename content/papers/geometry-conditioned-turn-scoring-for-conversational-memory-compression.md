# Geometry-Conditioned Turn Scoring for Conversational Memory Compression

- Source: OpenReview
- Venue: GroundLM Findings
- Paper ID: openreview:XqFFt1fHk2
- Published: 2026-08-30
- Updated: 2026-08-30
- Authors: Pranav Kompally, Sibi Chakkaravarthy S
- Tags: benchmark, compression, context, conversation
- Categories: EMNLP/2026/Workshop/GroundLM/-/Submission
- URL: https://openreview.net/forum?id=XqFFt1fHk2

## One-Sentence Summary
Compressing long multi-turn conversations requires deciding not only how to compress context, but which signal should rank memory candidates under a fixed budget.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, compression, context, conversation` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `GroundLM Findings` 这个 venue 相关。

从摘要来看，作者主要关注的是：Compressing long multi-turn conversations requires deciding not only how to compress context, but which signal should rank memory candidates under a fixed budget.

进一步看，论文的核心做法或实验重点可以概括为：We study a sparse keep/compress/drop (KCD) codec and compare geometric, semantic, and hybrid scoring signals across conversational memory regimes.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：GroundLM Findings
- 高亮主题命中：benchmark, compression, context, conversation
- 检索关键词命中：conversational memory, memory compression
- 来源分类信息：EMNLP/2026/Workshop/GroundLM/-/Submission

## Abstract Snapshot
Compressing long multi-turn conversations requires deciding not only how to compress context, but which signal should rank memory candidates under a fixed budget. We study a sparse keep/compress/drop (KCD) codec and compare geometric, semantic, and hybrid scoring signals across conversational memory regimes. On a stress-test benchmark designed to expose support-turn failures, a geometry-scored codec substantially outperforms a semantic signal swap inside the same codec. On MSC (1,000 conversations), we show that geometry-based compression methods substantially outperform LongLLMLingua on geometric fidelity (ΔL2 ≈ +130) while LongLLMLingua modestly improves answer NLL---a geometry-behavior divergence confirming that behavioral metrics alone are insufficient to evaluate memory compression. Among KCD signal variants on MSC (1,000 conversations, Qwen2.5-1.5B), query-conditioned geometry achieves the best combination of geometric fidelity and behavioral quality simultaneously: at budget 0.50 it reduces logit L2 by 109.4 units versus semantic KCD (p<0.001, conversation-level) while also achieving best answer NLL across all budgets. On LongMemEval-S (100 full-length conversations), all KCD variants significantly improve behavioral quality over uniform compression. A Llama-3.2-3B cross-model check shows that the geometry signal advantage is model-family-dependent: semantic compression dominates geometry compression on behavior across all budgets for Llama-3B (p≤0.01, conversation-level). The paper's central claim is that geometry-behavior divergence is real and consequential, and that query-conditioned geometry is the signal that best resolves it on Qwen2.5 models.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
