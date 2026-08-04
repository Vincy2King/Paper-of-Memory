# Stop When Memory Suffices: Evidence-Conditioned Progressive Execution for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.01285v1
- Published: 2026-08-02
- Updated: 2026-08-02
- Authors: Yidan Lin, Kaixiang Wang, Jiong Lou, Jie Li
- Tags: agent, context, long-term, retrieval
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2608.01285v1

## One-Sentence Summary
The continued development of LLMs toward persistent and adaptive intelligence increasingly requires long-term memory mechanisms that preserve and reuse information across...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：The continued development of LLMs toward persistent and adaptive intelligence increasingly requires long-term memory mechanisms that preserve and reuse information across interactions.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory systems either compress and structure histories for efficient access or perform deep research over broader trajectories.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
The continued development of LLMs toward persistent and adaptive intelligence increasingly requires long-term memory mechanisms that preserve and reuse information across interactions. Existing memory systems either compress and structure histories for efficient access or perform deep research over broader trajectories. The former lowers online cost but may omit temporal, causal, or cross-step dependencies, while the latter improves evidence coverage at substantial latency and inference cost. This raises a key question: can a memory system achieve strong answer quality while maintaining low online latency? We introduce Router-Mem, an evidence-conditioned progressive execution framework for long-horizon agent memory. Router-Mem first applies a shared low-cost retrieval prefix to obtain evidence. A lightweight sufficiency router then predicts whether the context supports early termination, which enable a single-token decision at inference time. It is trained with evidence-level supervision and rationale-conditioned representation distillation. When evidence is insufficient, Router-Mem reuses retrieval hits to expand memory blocks and perform deeper analysis and aggregation. Experiments on AMA-Bench and BEAM show that Router-Mem achieves 55.17\% and 38.77\% score while reducing average inference time by 27.3\% and 25.5\% compared with full memory execution.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
