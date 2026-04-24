# AAC: Admissible-by-Architecture Differentiable Landmark Compression for ALT

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.20744v1
- Published: 2026-04-22
- Updated: 2026-04-22
- Authors: An T. Le, Vien Ngo
- Tags: benchmark, compression
- Categories: cs.AI, cs.LG, cs.RO
- URL: http://arxiv.org/abs/2604.20744v1

## One-Sentence Summary
We introduce \textbf{AAC} (Architecturally Admissible Compressor), a differentiable landmark-selection module for ALT (A*, Landmarks, and Triangle inequality) shortest-path...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, compression` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We introduce \textbf{AAC} (Architecturally Admissible Compressor), a differentiable landmark-selection module for ALT (A*, Landmarks, and Triangle inequality) shortest-path heuristics whose outputs are admissible by...

进一步看，论文的核心做法或实验重点可以概括为：At deployment, the module reduces to classical ALT on a learned subset, composing end-to-end with neural encoders while preserving the classical toolchain.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, compression
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：cs.AI, cs.LG, cs.RO

## Abstract Snapshot
We introduce \textbf{AAC} (Architecturally Admissible Compressor), a differentiable landmark-selection module for ALT (A*, Landmarks, and Triangle inequality) shortest-path heuristics whose outputs are admissible by construction: each forward pass is a row-stochastic mixture of triangle-inequality lower bounds, so the heuristic is admissible for \emph{every} parameter setting without requiring convergence, calibration, or projection. At deployment, the module reduces to classical ALT on a learned subset, composing end-to-end with neural encoders while preserving the classical toolchain. The construction is the first differentiable instance of the compress-while-preserving-admissibility tradition in classical heuristic search. Under a matched per-vertex memory protocol, we establish that ALT with farthest-point-sampling landmarks (FPS-ALT) has provably near-optimal coverage on metric graphs, leaving at most a few percentage points of headroom for \emph{any} selector. AAC operates near this ceiling: the gap is $0.9$--$3.9$ percentage points on 9 road networks and ${\leq}1.3$ percentage points on synthetic graphs, with zero admissibility violations across $1{,}500+$ queries and all logged runs. At matched memory, AAC is also $1.2$--$1.5{\times}$ faster than FPS-ALT at the median query on DIMACS road networks, amortizing its offline cost within $170$--$1{,}924$ queries. A controlled ablation isolates the binding constraint: training-objective drift under default initialization, not architectural capacity; identity-on-first-$m$ initialization closes the expansion-count gap entirely. We release the module, a reusable matched-memory benchmarking protocol with paired two-one-sided-test (TOST) equivalence and pre-registration, and a reference compressed-differential-heuristics baseline.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
