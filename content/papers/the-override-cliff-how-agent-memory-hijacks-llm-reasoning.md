# The Override Cliff: How Agent Memory Hijacks LLM Reasoning

- Source: OpenReview
- Venue: ACL ARR 2026 May Submission
- Paper ID: openreview:mNtrAwNwyD
- Published: 2026-06-02
- Updated: 2026-07-02
- Authors: Unknown
- Tags: agent, benchmark, retrieval
- Categories: aclweb.org/ACL/ARR/2026/May/-/Submission
- URL: https://openreview.net/forum?id=mNtrAwNwyD

## One-Sentence Summary
When instruction-tuned LLMs store past experience in retrieval-augmented memory, much of memory's measured influence in our evaluation flows through verbatim answer copying...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 May Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：When instruction-tuned LLMs store past experience in retrieval-augmented memory, much of memory's measured influence in our evaluation flows through verbatim answer copying rather than higher-level reasoning.

进一步看，论文的核心做法或实验重点可以概括为：Across $1{,}866$ controlled experiments spanning three model families, multi-episode agent tasks, and three external conflict benchmarks, removing concrete answer bindings sharply reduces override on the strongest-...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 May Submission
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：aclweb.org/ACL/ARR/2026/May/-/Submission

## Abstract Snapshot
When instruction-tuned LLMs store past experience in retrieval-augmented memory, much of memory's measured influence in our evaluation flows through verbatim answer copying rather than higher-level reasoning. Across $1{,}866$ controlled experiments spanning three model families, multi-episode agent tasks, and three external conflict benchmarks, removing concrete answer bindings sharply reduces override on the strongest-conflict tasks and attenuates it on more naturalistic benchmarks. Override strength changes at a concentrated boundary we term the *override cliff*: between answer-level and paraphrase-level memory content, override drops $4.5\times$ on average in a single specificity step. On NQ-Swap, removing the swapped entity reduces override to zero on both tested models, and the cliff replicates on two frontier API models with full closed-book filtering (GPT-4o-mini $1.6\times$; Claude Haiku 4.5 $1.8\times$), with attenuated but persistent effect. On $\tau$-bench, a real agent benchmark with deterministic evaluation, verbatim tool-call memories cause $20.6\%$ stale parameter copying vs. $6.3\%$ for strategy-only memories ($p{=}0.017$, cliff ratio $3.3\times$), even when the agent performs fresh tool lookups. Logit probes are consistent with a ${\sim}5\times$ token-level amplification at this boundary, and paraphrased or summarized memories often avoid the strongest override failures.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
