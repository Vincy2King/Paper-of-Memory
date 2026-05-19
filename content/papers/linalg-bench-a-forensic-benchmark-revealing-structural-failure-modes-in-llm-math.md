# LinAlg-Bench: A Forensic Benchmark Revealing Structural Failure Modes in LLM Mathematical Reasoning

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.16675v1
- Published: 2026-05-15
- Updated: 2026-05-15
- Authors: Shradha Agarwal, Deepak Rajbhar, Tariq J
- Tags: benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.16675v1

## One-Sentence Summary
We introduce LinAlg-Bench, a diagnostic benchmark evaluating 10 frontier large language models on structured linear algebra computation across a strict dimensional gradient of...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We introduce LinAlg-Bench, a diagnostic benchmark evaluating 10 frontier large language models on structured linear algebra computation across a strict dimensional gradient of 3x3, 4x4, and 5x5 matrices.

进一步看，论文的核心做法或实验重点可以概括为：Spanning 9 task types and 660 SymPy-certified problems, the benchmark exhaustively evaluates 6,600 model outputs.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：working memory
- 来源分类信息：cs.AI

## Abstract Snapshot
We introduce LinAlg-Bench, a diagnostic benchmark evaluating 10 frontier large language models on structured linear algebra computation across a strict dimensional gradient of 3x3, 4x4, and 5x5 matrices. Spanning 9 task types and 660 SymPy-certified problems, the benchmark exhaustively evaluates 6,600 model outputs. Beyond binary accuracy, LinAlg-Bench introduces a three-stage automated forensic pipeline classifying 1,156 failures into ten primary error tags with fine-grained subtypes, revealing that LLM mathematical failure is not random but structurally constrained by algorithm type and matrix dimension. Our central finding is a sharp behavioral threshold at 4x4 scale: below it, models fail through execution errors -- sign tracking failures, arithmetic drift, and parity errors; above it, failure transitions to computational abandonment, with models fabricating responses through tool roleplay, constraint-consistent confabulation, and structured hallucination rather than attempting computation. This fabrication-to-abandonment transition is near-universal across all model tiers and architectures, suggesting a working memory limit rather than a knowledge gap, supported by three scale-emergent error types absent at 3x3 but present at 4x4 and 5x5. We further show that solution strategy rigidity is a near-perfect predictor of 5x5 determinant accuracy, document constraint-aware confabulation as a novel structured hallucination failure mode, and release all data, model outputs, error labels, and judge pipeline publicly.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
