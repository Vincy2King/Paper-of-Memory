# ReTeach: Building a Self-Teacher through Multi-Round Reflection and Retry

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.11529v1
- Published: 2026-10-08
- Updated: 2026-10-08
- Authors: Yafeng Tang, Hao Li, Hongsheng Yu, Qiang Fu
- Tags: benchmark, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.11529v1

## One-Sentence Summary
Self-distillation can improve reasoning without a separately trained, more capable teacher, but its effectiveness depends on how the self-teacher gains an advantage over the...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Self-distillation can improve reasoning without a separately trained, more capable teacher, but its effectiveness depends on how the self-teacher gains an advantage over the student.

进一步看，论文的核心做法或实验重点可以概括为：Conditioning the teacher on reference answers or solutions can provide such an advantage, but this information may be unavailable.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Self-distillation can improve reasoning without a separately trained, more capable teacher, but its effectiveness depends on how the self-teacher gains an advantage over the student. Conditioning the teacher on reference answers or solutions can provide such an advantage, but this information may be unavailable. Reflection offers a way to derive explicit error diagnoses and revision guidance from self-generated attempts, yet existing reflection-based methods often combine it with reference information, rich task feedback, or persistent memory. We introduce ReTeach, a Reflective self-distillation framework that constructs its self-Teacher through multi-round reflection and retry using only self-generated attempts and outcome-level verification. Starting from an unsuccessful student rollout, the teacher alternates explicit reflection with renewed attempts until success or the retry budget is exhausted, without reference answers or solutions, external diagnostic feedback, or cross-example memory. Each failed retry informs subsequent reflection, while successful correction provides outcome-level evidence for the potential utility of the resulting teacher context. An outcome-aware selection and weighting strategy distinguishes initially correct, reflection-corrected, and unresolved examples, assigning separate weights to their category-normalized distillation losses. Through on-policy distillation, the student matches the teacher's context-conditioned token-level predictive distributions at prefixes of its own rollouts, transferring the benefits of iterative correction while retaining single-pass inference. Across six benchmarks spanning mathematical reasoning, science question answering, and tool use, ReTeach improves average accuracy over GRPO by 1.39 percentage points.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
