# ReWork: Efficient Iterative Reasoning with Working Memory

- Source: OpenReview
- Venue: COLM 2026 ER Workshop
- Paper ID: openreview:cNK4KZzHH2
- Published: 2026-08-07
- Updated: 2026-08-11
- Authors: Haoyu He, Yong Cao, Andreas Geiger
- Tags: working memory
- Categories: colmweb.org/COLM/2026/Workshop/Efficient_Reasoning/-/Submission
- URL: https://openreview.net/forum?id=cNK4KZzHH2

## One-Sentence Summary
Hard reasoning problems yield to iteration: a model drafts a candidate solution, then repeatedly revises it.

## Introduction
这篇论文被纳入仓库，是因为它和 `working memory` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `COLM 2026` 这个 venue 相关。

从摘要来看，作者主要关注的是：Hard reasoning problems yield to iteration: a model drafts a candidate solution, then repeatedly revises it.

进一步看，论文的核心做法或实验重点可以概括为：Two group of revision methods coexist in the literature: latent recursion deepens the computation in the latent space, and diffusion revises the predictions over denoising steps.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：COLM 2026 ER Workshop
- 高亮主题命中：working memory
- 检索关键词命中：working memory
- 来源分类信息：colmweb.org/COLM/2026/Workshop/Efficient_Reasoning/-/Submission

## Abstract Snapshot
Hard reasoning problems yield to iteration: a model drafts a candidate solution, then repeatedly revises it. Two group of revision methods coexist in the literature: latent recursion deepens the computation in the latent space, and diffusion revises the predictions over denoising steps. Iteration of either kind places two competing demands on model state, which must maintain the partial solution built so far yet and keep the plasticity to change wherever that solution is wrong. A recurrent network that carries a single hidden state forward asks one representation to serve both demands: persistence protects progress but establishes stale computation, while plasticity enables correction but erases what is already built. To mitigate this, we introduce ReWork with refreshing working memory for latent recurrence. To split the two demands into two states with different lifetimes a token-aligned sensory memory persists across latent recursions and holds the evolving answer, while compact working memory reads that answer, integrates global evidence, writes an update back, and is refreshed for the next recurrence. By nesting the latent recurrence and discrete diffusion, ReWork re-estimates every token across denoising steps, and latent recursion refines the sensory memory within each latent recurrence. Experiments on Maze-Hard show that a 36.8M-parameter ReWork solves 82.0\% of mazes exactly compared to size-matched token-aligned recurrent model (72.8\%), while costing under 48\% of the attention a token-aligned update would use. On Sudoku-Extreme the same separation nearly triples exact solve (60.4\% against 21.1\%). Exact accuracy grows along both loops and equal-compute allocations are not interchangeable, so recursion and denoising act as complementary axes of test-time compute, and a learned halting rule removes about half of the recurrent computation at unchanged accuracy. An iterative reasoner, these results suggest, should couple a persistent sensory memory with disposable working memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
