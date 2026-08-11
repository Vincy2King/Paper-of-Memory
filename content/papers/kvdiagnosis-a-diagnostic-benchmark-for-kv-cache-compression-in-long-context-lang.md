# KVDiagnosis: A Diagnostic Benchmark for KV-Cache Compression in Long-Context Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.09412v1
- Published: 2026-08-10
- Updated: 2026-08-10
- Authors: Chen Qiu, Ziwu Liu, Chao Fei, Guozhong Li, Panos Kalnis
- Tags: benchmark, compression, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.09412v1

## One-Sentence Summary
KV-cache compression reduces long-context memory, but aggregate task scores reveal neither which correct executions fail nor why.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：KV-cache compression reduces long-context memory, but aggregate task scores reveal neither which correct executions fail nor why.

进一步看，论文的核心做法或实验重点可以概括为：We present KVDiagnosis, a diagnostic dataset and benchmark with three contributions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, compression, context
- 检索关键词命中：context memory
- 来源分类信息：cs.AI

## Abstract Snapshot
KV-cache compression reduces long-context memory, but aggregate task scores reveal neither which correct executions fail nor why. We present KVDiagnosis, a diagnostic dataset and benchmark with three contributions. First, a 25-method taxonomy groups methods into five mechanism families and links them to eight verified implementations and their valid diagnostic measurements. Second, for every supported method setting, we evaluate all sources in each fixed split against a per-source FullCache control before selecting FullCache-correct/compressed-wrong (C-to-W) rows separately for each method-setting, so no compressor defines another's test set. Third, a common record format links paired outputs and run metadata to cache, likelihood, attention, and decoding measurements with explicit applicability states. On Qwen3-8B, four evidence-aware workloads yield 59 800 supported compressed runs over 2600 sources and 12 520 C-to-W rows. Under fixed diagnostic rules, 63.2% have low or partial measured/projected coverage. Only 19 rows (0.2%) combine high measured/projected coverage with strong likelihood drift; another 2,126 (17.0%) preserve structural position addressability, for which representation fidelity remains unknown, while showing the same drift. Against C-to-C success controls, all ten diagnostics separate failed from successful compression (stratified AUROC 0.684-0.871). Among 96 reproducible low-EAR failures, a controlled 4x evidence-attention boost repairs 29.2%, versus 6.3% under a count-matched sham intervention and 3.3% degradation on matched C-to-C controls. Code and data are available at https://github.com/ChosenQC/KVDiagnosis.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
