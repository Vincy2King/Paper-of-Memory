# Eviction as Estimation: A Fixed-Lag Smoothing View of Test-Time Memory, and When Measuring Beats Accumulating

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.24667v1
- Published: 2026-07-27
- Updated: 2026-07-27
- Authors: Maruthi Vemula, Neeraj Praneeth Gajula
- Tags: benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.24667v1

## One-Sentence Summary
A language model with a bounded working memory must repeatedly decide which stored items to keep.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：A language model with a bounded working memory must repeatedly decide which stored items to keep.

进一步看，论文的核心做法或实验重点可以概括为：Every deployed method decides the moment an item arrives, from the past (StreamingLLM, H2O) or from a guess about the future (SnapKV).

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：working memory
- 来源分类信息：cs.AI

## Abstract Snapshot
A language model with a bounded working memory must repeatedly decide which stored items to keep. Every deployed method decides the moment an item arrives, from the past (StreamingLLM, H2O) or from a guess about the future (SnapKV). We recast the choice as an estimation problem on a hidden signal, whether an item will be reused, placing existing methods on one axis, the commit lag $H$: online filters and learned predictors commit at $H=0$, while Belady's offline optimum sits where the whole future is known. The missing regime in between, fixed-lag smoothing, waits a bounded number of steps, observes which items a correct near-future prediction attended to, and only then commits. This measurement, demonstrated utility, turns Belady's unobservable future request into something we read off the model itself. We instantiate it as a training-free policy, RMM, a strict generalization of H2O that reduces to it exactly when the measurement is uniform. In controlled settings where reuse is endogenous and separated in time, demonstrated utility identifies used memory far better than accumulated attention, and a small bounded memory behaves like a much larger one. But on independent third-party benchmarks, run inside NVIDIA's KVPress harness against its own SnapKV, H2O, and StreamingLLM implementations, the advantage mostly disappears: RMM is on par with H2O for single-turn question answering and loses to both H2O and SnapKV in a streaming multi-turn setting. The cause is simple: on natural text the model is correct about most tokens, so weighting attention by correctness barely changes it, and demonstrated utility collapses onto accumulated attention unless reuse is sharp and endogenous, which standard benchmarks do not exercise. Our contribution is the framework and an honest map of when measuring beats accumulating, not a new state of the art.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
