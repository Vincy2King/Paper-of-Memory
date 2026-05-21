# MemConflict: Evaluating Long-Term Memory Systems Under Memory Conflicts

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.20926v1
- Published: 2026-05-20
- Updated: 2026-05-20
- Authors: Zhen Tao, Jinxiang Zhao, Peng Liu, Dinghao Xi, Yanfang Chen, Wei Xu, Zhiyu Li
- Tags: agent, benchmark, context, conversation, long-term, retrieval
- Categories: cs.IR
- URL: http://arxiv.org/abs/2605.20926v1

## One-Sentence Summary
Long-term memory systems enable conversational agents based on large language models (LLMs) to retain, retrieve, and apply user-specific information across multi-session...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory systems enable conversational agents based on large language models (LLMs) to retain, retrieve, and apply user-specific information across multi-session interactions.

进一步看，论文的核心做法或实验重点可以概括为：However, existing evaluations mainly assess outcome-level performance or temporal updating, providing limited insight into how systems retrieve and rank temporally valid, factually correct, and contextually applicable...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：long-term memory, memory retrieval, retrieval memory
- 来源分类信息：cs.IR

## Abstract Snapshot
Long-term memory systems enable conversational agents based on large language models (LLMs) to retain, retrieve, and apply user-specific information across multi-session interactions. However, existing evaluations mainly assess outcome-level performance or temporal updating, providing limited insight into how systems retrieve and rank temporally valid, factually correct, and contextually applicable memory evidence under conflicting alternatives. To address this gap, we propose MemConflict, a diagnostic framework that treats memory validity as a query-conditioned fitness-for-use problem. MemConflict formalizes dynamic, static, and conditional conflicts over temporal validity, factual correctness, and contextual applicability. It simulates controlled long-horizon histories from structured user profiles, introduces cross-session conflicts, and injects semantically similar distractors to create competition among memory candidates. The resulting multi-session dialogue benchmark supports black-box evaluation of final answers and white-box analysis of supporting-memory retrieval and ranking. Experiments on six representative long-term memory systems show uneven strengths across conflict types, with answer correctness often diverging from memory retrieval and ranking. Sensitivity analyses reveal that longer histories, distractors, implicit queries, and larger conflict distances degrade performance. Diagnostics show failures from missing supporting memories and ineffective use of retrieved memories. Collectively, MemConflict advances principled long-term memory governance through retrieval-aware, conflict-aware reliability assessment.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
