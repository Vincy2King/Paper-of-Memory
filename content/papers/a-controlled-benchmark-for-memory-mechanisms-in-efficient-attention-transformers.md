# A Controlled Benchmark for Memory Mechanisms in Efficient-Attention Transformers

- Source: OpenReview
- Venue: FastML 2026 Conference Submission
- Paper ID: openreview:bdg8EIui6I
- Published: 2026-07-02
- Updated: 2026-07-02
- Authors: Rob Sneiderman
- Tags: benchmark, context
- Categories: FastML/2026/Conference/-/Submission
- URL: https://openreview.net/forum?id=bdg8EIui6I

## One-Sentence Summary
Efficient-attention transformers trade direct context access for compute, and a family of memory mechanisms is offered to recover what restricted attention drops.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `FastML 2026 Conference Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Efficient-attention transformers trade direct context access for compute, and a family of memory mechanisms is offered to recover what restricted attention drops.

进一步看，论文的核心做法或实验重点可以概括为：Reported gains are hard to trust: papers vary the mechanism, the backbone, the optimizer, the token budget, and the scale all at once, and they report a single aggregate perplexity that averages over positions where...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：FastML 2026 Conference Submission
- 高亮主题命中：benchmark, context
- 检索关键词命中：persistent memory
- 来源分类信息：FastML/2026/Conference/-/Submission

## Abstract Snapshot
Efficient-attention transformers trade direct context access for compute, and a family of memory mechanisms is offered to recover what restricted attention drops. Reported gains are hard to trust: papers vary the mechanism, the backbone, the optimizer, the token budget, and the scale all at once, and they report a single aggregate perplexity that averages over positions where local attention already suffices. This benchmark holds the backbone, data, optimizer, and token budget fixed across four memory mechanisms on a 286M-parameter GPT, varying only the memory system, and scores them with a position-resolved diagnostic rather than one aggregate number. The diagnostic is a positional context deficit map: the per-position bits-per-byte (BPB) gap between local and matched global attention, against which a mechanism’s per-position gain is measured. Across 42 training runs (three context lengths, up to four seeds each, paired by seed), only persistent memory tokens improve over the local baseline (−1.79 milli-BPB, paired p ≈ 0.012, Cohen’s dlarge); recurrent memory, test-time-training, and gated DeltaNet each hurt under a fixed budget. The deficit map shows persistent memory closes more than the full late-position deficit at the two longest contexts. Effects are small and single-scale; the contribution is the controlled protocol and the diagnostic, both architecture-agnostic and released as a plug-and-play harness.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
