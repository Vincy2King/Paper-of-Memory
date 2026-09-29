# Vestrum: Improving Agent Harnesses by Adapting Their Verification, Structure and Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.33822v1
- Published: 2026-09-27
- Updated: 2026-09-27
- Authors: Jayant Parashar, Eugene F. Douglass, William C. Bastian, Suchendra M. Bhandarkar
- Tags: agent, benchmark, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.33822v1

## One-Sentence Summary
An agent harness controls how a language model accesses information, uses tools, preserves memory, and checks its work.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：An agent harness controls how a language model accesses information, uses tools, preserves memory, and checks its work.

进一步看，论文的核心做法或实验重点可以概括为：Improving this software is costly when each evaluation requires a long interaction with an environment.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：cs.AI

## Abstract Snapshot
An agent harness controls how a language model accesses information, uses tools, preserves memory, and checks its work. Improving this software is costly when each evaluation requires a long interaction with an environment. We introduce Vestrum, a framework that turns failures in execution traces into scoped harness changes without training the task model. Its organizing overhypothesis is that tasks of a shared kind may exhibit recurring failures whose remedies transfer within that kind. Vestrum expresses failures as recognizable classes, proposes changes across verification, retrieval, decomposition, and knowledge synthesis, and screens their scope before evaluating them as a bundle. A persistent lessons file informs subsequent proposals. Across five settings and two baseline harnesses, the frozen harnesses improve held-out performance: UltraHorizon rises from 47.6 to 59.8 over GAM, Terminal-Bench 4 Hard from 63.7% to 70.3% of checks passed over Claude Code on eight held-out tasks at 1.03x test cost, and cell-type annotation agreement from 67.5% to 77.8% on held-out sections of one slide, alongside gains on LoCoMo and AMA-Bench. Across our searches, verification grounded in evidence helped both intermediate steps and final answers, at lower cost at intermediate steps, while critics asked to rebuild finished answers broke more than they repaired. On the three memory benchmarks, Vestrum also scores above the evaluated GEPA configurations in every paired evaluation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
