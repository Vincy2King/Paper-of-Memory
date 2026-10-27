# Adaptive Memory Index Evolution for Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.34977v1
- Published: 2026-10-26
- Updated: 2026-10-26
- Authors: Yuntong Hu, Tongli Su, Yuanfu Sun, Shuo Ma, Qiaoyu Tan, Liang Zhao
- Tags: agent, benchmark, retrieval
- Categories: cs.LG
- URL: http://arxiv.org/abs/2610.34977v1

## One-Sentence Summary
Long-horizon agents continually accumulate experience, yet retaining a memory does not guarantee access when it is needed.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon agents continually accumulate experience, yet retaining a memory does not guarantee access when it is needed.

进一步看，论文的核心做法或实验重点可以概括为：Existing systems can adapt both memory content and access; we isolate persistent access updates as a separately controlled adaptation layer.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：agent memory, persistent memory, retrieval memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Long-horizon agents continually accumulate experience, yet retaining a memory does not guarantee access when it is needed. Existing systems can adapt both memory content and access; we isolate persistent access updates as a separately controlled adaptation layer. We formulate this target as Memory Index Evolution and instantiate it with Adaptive Memory Index Evolution (AMIE), a lightweight plug-in layer that evolves per-memory access state from deployment retrievals without modifying stored content or retraining the host memory system. AMIE distils a semantic teacher's keep/suppress judgments into a retrieval-conditioned policy and accumulates its selective actions into bounded state that reweights subsequent host retrievals. Surprisingly, even a zero-call policy that simply accumulates retrieval frequency can match or outperform semantic policies in several settings, revealing retrieval traffic itself as a strong signal for access adaptation, while learned selectivity improves robustness when frequently retrieved memories remain useful. Across five retrieval-based hosts and three benchmarks, trained AMIE improves downstream F1 or accuracy in all 15 comparisons, by 0.70--3.37 percentage points (up to 25% relative), and improves retrieval in all 10 comparisons. Controlled analyses show that persistent competitor suppression can expose previously unseen evidence, while suppressing repeatedly useful memories creates the complementary failure mode. Together, these results establish persistent memory access as a practical adaptation layer, distinct from the content it serves, in retrieval-based agent memory systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
