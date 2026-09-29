# Before Answering: Evidence Sufficiency under Size-Matched Memory Construction

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.32269v1
- Published: 2026-09-26
- Updated: 2026-09-26
- Authors: Joyanta Jyoti Mondal, Md. Shifatul Ahsan Apurba, Mridul Banik, Md Masud Al Mahmud, Ibne Farabi Shihab
- Tags: agent, benchmark
- Categories: cs.CL, cs.LG
- URL: http://arxiv.org/abs/2609.32269v1

## One-Sentence Summary
Agents that answer questions from compressed or retrieved memory must recognize when the evidence a query needs is no longer in memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agents that answer questions from compressed or retrieved memory must recognize when the evidence a query needs is no longer in memory.

进一步看，论文的核心做法或实验重点可以概括为：Benchmarks for this task usually create insufficient-evidence examples by deleting supporting passages.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：memory benchmark, memory benchmarks, retrieval memory
- 来源分类信息：cs.CL, cs.LG

## Abstract Snapshot
Agents that answer questions from compressed or retrieved memory must recognize when the evidence a query needs is no longer in memory. Benchmarks for this task usually create insufficient-evidence examples by deleting supporting passages. We show that this construction leaks the label through memory size: on MuSiQue, a classifier that only counts paragraphs reaches an area under the ROC curve (AUROC) of $0.979$ for detecting unsafe memory, higher than the lexical estimator we initially evaluated. We propose a size-matched construction that provably removes this shortcut, and use it to study MemSafe, an estimator that cross-encodes the query with each memory unit and aggregates the units with a set transformer. Across three multi-hop question answering datasets and five seeds, MemSafe reaches $0.968$ and $0.983$ AUROC on MuSiQue and HotpotQA, $0.26$ to $0.39$ above a lexical baseline, while the third dataset, 2WikiMultiHopQA, is saturated. A frozen pretrained cross-encoder with a logistic head already closes $41\%$ of the MuSiQue gap between the lexical baseline and MemSafe. At the same time, MemSafe degrades more than a weak baseline on the unanswerable questions released with MuSiQue, reaches only $0.639$ AUROC on SQuAD~2.0, and needs several thousand clinical training examples before it outperforms a feature-based estimator. Used as a gate for a 7B reader, it reduces the error rate on answered questions from $0.850$ to $0.631$ at $5\%$ coverage, outperforming both reader confidence and, on average, the ground-truth integrity label, although a 7B LLM judge is the better gate at $10\%$ coverage. These results indicate that the way insufficient evidence is constructed matters as much as the estimator that detects it.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
