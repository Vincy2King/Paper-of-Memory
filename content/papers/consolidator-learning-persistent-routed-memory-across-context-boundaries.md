# Consolidator: Learning Persistent Routed Memory Across Context Boundaries

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.11701v1
- Published: 2026-08-12
- Updated: 2026-08-12
- Authors: Sungwoo Goo, Hwi-yeol Yun, Sangkeun Jung
- Tags: context, long-term
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2608.11701v1

## One-Sentence Summary
Copying short-term memory (STM) into a slower store can preserve state across a context boundary, but persistence alone does not ensure that the retained state influences...

## Introduction
这篇论文被纳入仓库，是因为它和 `context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Copying short-term memory (STM) into a slower store can preserve state across a context boundary, but persistence alone does not ensure that the retained state influences subsequent memory access.

进一步看，论文的核心做法或实验重点可以概括为：We test this distinction in a Phasor Memory Network (PMNet) using Consolidator, a shared slot-local operator that transforms routed STM before accumulating it into long-term memory (LTM), without replaying the source...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Copying short-term memory (STM) into a slower store can preserve state across a context boundary, but persistence alone does not ensure that the retained state influences subsequent memory access. We test this distinction in a Phasor Memory Network (PMNet) using Consolidator, a shared slot-local operator that transforms routed STM before accumulating it into long-term memory (LTM), without replaying the source tokens. After each consolidation, the KV cache and STM are cleared. The retained LTM can still be read and is also fed into the hierarchical router, thereby conditioning which explicit-memory slots subsequent inputs access. We evaluate this mechanism on a two-segment modulo-10 mapping task in which the second segment updates the mapping at the same memory address. Following a second consolidation and reset, a held-out query must recover the updated mapping from LTM. The backbone and memory interface are frozen, leaving only 12.35K Consolidator parameters trainable (0.041\% of a 29.95M model). Across five paired runs from the same STM-pretraining checkpoint, direct LTM routing raises updated-mapping recall from $44.38\pm1.94\%$ to $87.02\pm1.76\%$ ($+42.64\pm1.10$ percentage points), while immediate STM recall remains 89.90\% in both conditions; both train separate Consolidators and retain the same LTM read paths. Learned consolidation outperforms forced identity accumulation by $21.40\pm1.91$ percentage points without routing and $68.70\pm1.76$ with routing. Thus, on this task, consolidated LTM serves as both retrievable content and an access state that shapes subsequent slot selection.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
