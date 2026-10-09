# MemoWM: How World Models Change What Agents Need to Remember

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.10778v1
- Published: 2026-10-07
- Updated: 2026-10-07
- Authors: Bingfan Zeng, Zhisheng Chen, Chenbo Sang, Zhengwei Xie, Jinpeng Wang, Xiangchen Guan, Rui Qian, Zheng Lu, Jingwei Song
- Tags: agent, benchmark, long-term
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2610.10778v1

## One-Sentence Summary
Long-term agents face growing storage demands as they accumulate experience.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term agents face growing storage demands as they accumulate experience.

进一步看，论文的核心做法或实验重点可以概括为：World models capture reusable regularities that can reduce the information stored for each experience.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term
- 检索关键词命中：agent memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Long-term agents face growing storage demands as they accumulate experience. World models capture reusable regularities that can reduce the information stored for each experience. We formulate the problem of memory allocation conditioned on a world model and introduce MemoWM, a framework that uses shared predictions to compress retained information and reconstruct omitted content. Its task-aware allocation rule balances the expected impact of reconstruction errors against storage cost, retaining information with downstream value beyond the predictive prior. Across five long-term agent-memory benchmarks, MemoWM achieves 42.42\% average answer accuracy, exceeding the strongest baseline by 2.62 percentage points, while reducing average experience-specific storage by 53.9\% relative to MIRIX, the most storage-efficient baseline. Further analysis shows that stronger world models reduce per-experience storage at comparable task quality. Accounting for model parameters reveals a trade-off between shared model capacity and recurring storage costs, with the capacity that minimizes total storage increasing as more interactions are retained. Our code is available at https://github.com/Feld-maxiu/MemoWM.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
