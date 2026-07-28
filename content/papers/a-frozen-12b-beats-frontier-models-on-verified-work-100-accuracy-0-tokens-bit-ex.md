# A Frozen 12B Beats Frontier Models on Verified Work: 100% Accuracy, 0 Tokens, Bit-Exact, Forever

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.23806v1
- Published: 2026-07-26
- Updated: 2026-07-26
- Authors: Sietse Schelpe
- Tags: benchmark, context, retrieval
- Categories: cs.CL, cs.AI, cs.IR, cs.LG, cs.PF
- URL: http://arxiv.org/abs/2607.23806v1

## One-Sentence Summary
Improving a language model today means retraining it: enormous compute, a new opaque model each cycle, non-deterministic output.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Improving a language model today means retraining it: enormous compute, a new opaque model each cycle, non-deterministic output.

进一步看，论文的核心做法或实验重点可以概括为：We take the opposite path: the model stays frozen, and a persistent memory of verified solutions grows beside it.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CL, cs.AI, cs.IR, cs.LG

## Abstract Snapshot
Improving a language model today means retraining it: enormous compute, a new opaque model each cycle, non-deterministic output. We take the opposite path: the model stays frozen, and a persistent memory of verified solutions grows beside it. Once a problem family is solved and has passed an independent verification step that never consults the answer key, every new instance of that family is answered at zero generation tokens, bit-exact, deterministically. Across 180 fresh instances spanning nine problem families, four architectures from four vendors - dense and mixture-of-experts - each score 180/180 at zero generation tokens per answer: execution-bound capability decoupled from parameter scaling. A negative control attributes the capability fully to the memory: emptied, it solves nothing. The same verify-before-store contract holds for open-ended reasoning: 88/88 consistency-gated acceptances across all four models, machine-checked formal proof, and reasoning-method transfer at 77/80. Memory selection takes 1.4 microseconds; a full reuse completes in 6-23 ms at 36 mWh. Approximate similarity retrieval selects the wrong item 94.3% of the time on a 4,500-item verified store where exact addressing makes zero errors. The store also serves as working context at a scale no shipped engine matches: a 6,000,000-token movable window on a single 46 GB GPU at flat memory, where vLLM stops at 30,399 tokens and SGLang silently truncates past 32,000. On published benchmarks, frontier models remain far ahead of any 12B at raw from-scratch reasoning; on everything this system has solved and verified, the comparison inverts: a frontier API call pays a fresh generation pass on every query, forever, while verified reuse costs zero tokens and returns the identical bits every time. A public testbench with free, rate-limited access accompanies this report: https://corbenic-galahad-bench.hf.space

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
