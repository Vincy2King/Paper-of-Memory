# MemDerive: A Diagnostic Benchmark for Agent Memory over Evolving Data

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.25373v1
- Published: 2026-10-18
- Updated: 2026-10-18
- Authors: Sen Gao, Yongan Li, Han Chen, Bingsheng He, Ming Wu, Jason Zeng, Michael Heinrich, Shixuan Sun
- Tags: agent, benchmark, retrieval
- Categories: cs.DB, cs.AI, cs.CL, cs.IR
- URL: http://arxiv.org/abs/2610.25373v1

## One-Sentence Summary
Long-running agents rely on memory of their past interactions for task state, such as what has been completed and which conditions still hold.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-running agents rely on memory of their past interactions for task state, such as what has been completed and which conditions still hold.

进一步看，论文的核心做法或实验重点可以概括为：Such state is usually a derived state.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：agent memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.DB, cs.AI, cs.CL, cs.IR

## Abstract Snapshot
Long-running agents rely on memory of their past interactions for task state, such as what has been completed and which conditions still hold. Such state is usually a derived state. No record states it, and it must be computed by rules from multiple records of an evolving history. Existing memory benchmarks score only the final answer, with no reference for the intermediate states behind it. A wrong answer therefore cannot be traced to the state that was missed, and a state that silently became outdated goes undetected. We present MemDerive, a diagnostic benchmark for agent memory over evolving data. It specifies each scenario symbolically, derives exact gold answers with Datalog, records the gold derivation DAG and the supporting events of every query, and renders the history in natural language with fictional entities and distractors. Its 10 scenarios contain 4,692 events and 1,503 queries whose difficulty varies along access, evolution, and composition. On this ground truth, MemDerive evaluates answer reliability, diagnoses failures by probing the nodes of the gold derivation DAG, and tracks whether answers stay correct as events arrive. Our evaluation of four memory systems reveals failures that final-answer benchmarks hide. On derived state, every memory system falls behind simple BM25 retrieval, although the same answer model reaches 96.01% when given the supporting events. Most failures are ungathered, as a system holds the missing intermediate state but does not retrieve it for the question that needs it. Memory systems also rarely propagate implicit changes, which no new record states. These results suggest three principles for memory design. Gather inputs along the derivation, store rules with their versions, and maintain derived states through recorded dependencies.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
