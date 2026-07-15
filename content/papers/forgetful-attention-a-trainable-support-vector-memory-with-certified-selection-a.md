# Forgetful Attention: A Trainable Support-Vector Memory with Certified Selection and Exact Unlearning

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.12204v1
- Published: 2026-07-13
- Updated: 2026-07-13
- Authors: Vishwajith Ramesh
- Tags: context, retrieval
- Categories: cs.LG
- URL: http://arxiv.org/abs/2607.12204v1

## One-Sentence Summary
Attention can be viewed as an online learner over context, yet existing test-time memories cannot certify that dropping a token leaves outputs unchanged or delete its influence...

## Introduction
这篇论文被纳入仓库，是因为它和 `context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Attention can be viewed as an online learner over context, yet existing test-time memories cannot certify that dropping a token leaves outputs unchanged or delete its influence outright.

进一步看，论文的核心做法或实验重点可以概括为：We introduce Support Vector Attention (SV-Attention), a max-margin memory whose weights are support coefficients of a one-class SVM with fixed box parameter C.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Attention can be viewed as an online learner over context, yet existing test-time memories cannot certify that dropping a token leaves outputs unchanged or delete its influence outright. We introduce Support Vector Attention (SV-Attention), a max-margin memory whose weights are support coefficients of a one-class SVM with fixed box parameter C. Its active-set partition gives reserve tokens exactly zero weight, certifying output-preserving eviction; a reversible incremental solver deletes a token to recover the state produced by retraining without it under the same C. In fp64 experiments, decrement and refit recover identical partitions whenever the optimum is unique, and their decision functions match to a median deviation of about 10^-9 (10^-13 on learned keys); the 10^-2 worst case is confined to ill-conditioned duplicates and remains below coefficient decay in every regime. The exact path reuses the maintained KKT inverse in a custom backward. Training uses a separate stabilized batched approximation and does not carry the exact-deletion certificate; it reaches 9,125 tokens/s on a 3.22M-parameter model, while remaining 35.8 times slower than an MPS softmax reference. At matched budgets, certified selection reaches 0.86 vs. 0.32 rare-item recall and retains 0.80 vs. 0.05 deterioration hours on real MIMIC-IV streams. We also demonstrate surgical forgetting, exact editing, patient-record deletion, and a forgettable retrieval memory over real sentence embeddings. On enwik8, the hybrid obtains 2.178 BPC vs. 2.383 for a matched-state sliding-window Transformer across seven seeds (8.6% paired improvement, p=0.001); a three-seed TinyStories result is directionally positive but not significant (p=0.057).

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
