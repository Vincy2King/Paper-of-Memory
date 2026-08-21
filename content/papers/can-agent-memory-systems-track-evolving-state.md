# Can Agent Memory Systems Track Evolving State?

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.19652v1
- Published: 2026-08-20
- Updated: 2026-08-20
- Authors: Xinyi Fan, Miri Liu, Ruozhen Yang, Siru Ouyang, Jiawei Han
- Tags: agent, benchmark, context, conversation, retrieval
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2608.19652v1

## One-Sentence Summary
As LLM-based agents are deployed for longer and higher-stakes tasks, their memory systems continue to have crucial gaps.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：As LLM-based agents are deployed for longer and higher-stakes tasks, their memory systems continue to have crucial gaps.

进一步看，论文的核心做法或实验重点可以概括为：While existing memory benchmarks focus largely on recall-shaped tasks, we argue an effective memory system must track the evolving state of the world; as facts, constraints, and decisions are revised over a long...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, retrieval
- 检索关键词命中：agent memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
As LLM-based agents are deployed for longer and higher-stakes tasks, their memory systems continue to have crucial gaps. While existing memory benchmarks focus largely on recall-shaped tasks, we argue an effective memory system must track the evolving state of the world; as facts, constraints, and decisions are revised over a long interaction, answers must reflect the current state and not a superseded one. We define this capability as state tracking and instantiate it in StateMemBench, a benchmark of 234 multi-session scenarios spanning two conversation-length regimes. Its closed-pool grading scores whether an answer reflects the current state, the superseded state, or fails otherwise, separating state-tracking failures from other errors by construction. Our analysis shows that this task is challenging for existing memory systems, retrieval-augmented baselines, and long-context baselines. We then present StateMem, a state-first memory method that explicitly tracks supersession and relational dependencies, and show it improves current-state accuracy over the strongest same-backbone baseline by 1.8x (0.205 -> 0.363) on DeepSeek-V4-Flash and over the strongest memory system by 1.6x (0.149 -> 0.233) on Qwen-3.5-9B, while remaining competitive with the long-context baselines. Finally, we show the same state approach can be applied as a lightweight single-call wrapper over existing memory systems, lifting current-state accuracy by +32 to +67 points on StateMemBench across six memory and retrieval backends. A length- and cost-matched control attributes +15 to +32 of those points to state structure rather than added context.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
