# What Is This Memory Useful For? Measuring Task-Conditioned Utility in Long-Term Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.03930v1
- Published: 2026-11-02
- Updated: 2026-11-02
- Authors: Chih-Hsuan Yang, Anjir Ahmed Chowdhury, Feng Yan, Rajeev Thakur
- Tags: agent, benchmark, compression, context, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.03930v1

## One-Sentence Summary
A stored experience may answer one future question and offer little help with another.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：A stored experience may answer one future question and offer little help with another.

进一步看，论文的核心做法或实验重点可以概括为：We measure this task-conditioned utility rather than assigning each memory a single importance score.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, context, long-term, retrieval
- 检索关键词命中：agent memory, memory compression
- 来源分类信息：cs.AI

## Abstract Snapshot
A stored experience may answer one future question and offer little help with another. We measure this task-conditioned utility rather than assigning each memory a single importance score. A task-blind writer stores a memory without seeing the later task; a frozen reader then answers that task with and without the memory, using identical filler. A cost ledger records the resources used to form, store and expose the memory. On single-call factual-recall tasks built from LongMemEval-V2 web-agent memories, the same memory helps more when it contains information needed for the answer. Its mean paired reward gain on these answer-bearing task pairs exceeds that on matched-control pairs by $+0.33$ (95% interval $+0.21$ to $+0.46$). The tested task-blind summaries and structured records yield smaller gains than Raw, including at fixed total context; a budget sweep is consistent with retention of answer-bearing content contributing to the difference. The bearing--control contrast remains positive in a new session with randomized memory position and under a second reader, although individual memory--task labels change. Generic retrieval performs above chance but misses most screen-defined answer-bearing memories. The factual-recall gains do not extend to the tested software-engineering and scientific-coding benchmarks, where even raw memories have no measurable effect. We provide a public, versioned Conditional Memory Utility Dataset of paired measurements and costs. The practical takeaway is to evaluate memory compression by the task utility it preserves alongside its costs. Task-conditioned measurements make this comparison possible; their stability must also be checked.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
