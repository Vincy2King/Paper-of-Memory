# Distractor-Aware Truncation: Disentangling Context-Length Effects from Signal Loss in Long-Context LLM Benchmarks

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.03297v1
- Published: 2026-08-04
- Updated: 2026-08-04
- Authors: Mohsen Arjmandi
- Tags: benchmark, context, retrieval
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2608.03297v1

## One-Sentence Summary
A standard claim in the literature on retrieval-augmented and memory-augmented language models is that shorter context is better when the relevant information is preserved.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：A standard claim in the literature on retrieval-augmented and memory-augmented language models is that shorter context is better when the relevant information is preserved.

进一步看，论文的核心做法或实验重点可以概括为：We test this claim by running every sample of two long-context benchmarks -- BABILong and GraphWalks (BFS) -- at four context-retention fractions (100%, 75%, 50%, 25%) under two truncation protocols.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
A standard claim in the literature on retrieval-augmented and memory-augmented language models is that shorter context is better when the relevant information is preserved. We test this claim by running every sample of two long-context benchmarks -- BABILong and GraphWalks (BFS) -- at four context-retention fractions (100%, 75%, 50%, 25%) under two truncation protocols. The first is the naive protocol implicitly used in much prior work: drop content from the middle of the prompt. The second is distractor-aware: identify the task-relevant content for each sample and drop only the rest. We evaluate three sizes of the Claude family (Haiku 4.5, Sonnet 4.6, Opus 4.7) and, to test cross-provider generality, GPT-5.5 from a different provider; we apply the same protocol to two further benchmarks (MRCR v2, Oolong). Under naive truncation, score collapses monotonically (paired Wilcoxon, Holm-corrected p_adj < 0.05 in all eight BABILong and GraphWalks cells). Under the distractor-aware protocol -- which preserves the signal by construction -- performance is preserved or improves: the two smaller Claude models show statistically significant gains on BABILong, while the larger models (Opus 4.7 and GPT-5.5) sit at their full-context ceiling. The naive collapse and its distractor-aware recovery replicate on GPT-5.5, ruling out a single-provider artifact. The mechanism is direct: under the naive protocol the answer-bearing content survives in fewer than 1% of samples at 25% retention; under the distractor-aware protocol it is preserved by construction. The naive protocol is therefore not a measurement of context-window effects; it is a measurement of how often middle-removal happens to spare the answer. We conclude that future studies of context-length effects must specify how they distinguish signal from distractor, or they are at best ambiguous between two opposite hypotheses.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
