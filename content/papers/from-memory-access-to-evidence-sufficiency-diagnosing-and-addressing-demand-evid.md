# From Memory Access to Evidence Sufficiency: Diagnosing and Addressing Demand--Evidence Misalignment

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.32088v1
- Published: 2026-11-24
- Updated: 2026-11-24
- Authors: Shiyao Liu, Yixing Fan, Ruqing Zhang, Xiaohui Yan, Jiafeng Guo, Xueqi Cheng
- Tags: long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.32088v1

## One-Sentence Summary
Long-term memory retrieval often returns query-relevant records, but relevance does not guarantee sufficient evidence: answering requires a set of records that jointly satisfies...

## Introduction
这篇论文被纳入仓库，是因为它和 `long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory retrieval often returns query-relevant records, but relevance does not guarantee sufficient evidence: answering requires a set of records that jointly satisfies a question's factual, relational,...

进一步看，论文的核心做法或实验重点可以概括为：We study this demand--evidence misalignment through MemPath, an interventional framework that diagnoses failures in memory access, demand coverage, and evidence utilization.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：long-term, retrieval
- 检索关键词命中：long-term memory, memory retrieval
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term memory retrieval often returns query-relevant records, but relevance does not guarantee sufficient evidence: answering requires a set of records that jointly satisfies a question's factual, relational, temporal, and state constraints. We study this demand--evidence misalignment through MemPath, an interventional framework that diagnoses failures in memory access, demand coverage, and evidence utilization. Guided by this diagnosis, we propose BiDE-Mem, which represents questions as typed demands and uses them to guide retrieval and evidence organization. We formalize demand--evidence support; in the evaluated compact path, it is conveyed through provenance-aware evidence organization and Reader guidance rather than a separate generative four-state verification step. On LoCoMo, BiDE-Mem improves accuracy by 6.23 percentage points over Mnemis; on LongMemEval, it achieves 91.80%, with strong multi-hop and temporal performance. Supplementary Qwen-Reader evaluations place it first among seven systems on LoCoMo and LongMemEval-S under two judging protocols. Ablations and evidence-level analyses show that demand representation, retrieval, and evidence presentation each contribute to answer quality.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
