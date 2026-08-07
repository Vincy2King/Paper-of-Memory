# Activity Frames: Deterministic Screen-Activity Compilation for Agent Memory and Replay

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.05784v1
- Published: 2026-08-06
- Updated: 2026-08-06
- Authors: Nossa Iyamu
- Tags: agent, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.05784v1

## One-Sentence Summary
Computer-use agents pay full frontier inference to re-derive routines their user has already performed, because an agent's memory today records what the user said, not what the...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Computer-use agents pay full frontier inference to re-derive routines their user has already performed, because an agent's memory today records what the user said, not what the user did.

进一步看，论文的核心做法或实验重点可以概括为：We compile passively captured screen activity into agent memory with a deterministic, zero-model pipeline: it segments a local capture stream into typed activity frames, bounded episodes carrying application, site,...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Computer-use agents pay full frontier inference to re-derive routines their user has already performed, because an agent's memory today records what the user said, not what the user did. We compile passively captured screen activity into agent memory with a deterministic, zero-model pipeline: it segments a local capture stream into typed activity frames, bounded episodes carrying application, site, timing, input volume, and evidence pointers back to the raw rows, with no model in the loop, so the output is byte-identical, cacheable, and mechanically auditable. On one professional's single-user corpus of 128,756 frames over 51 active days, the compiler reduces a day of raw capture to a prompt-ready context block 86x smaller in 68 ms, and an agent reading that block answers questions about the day at 98.4% accuracy (Wilson 95% CI 91.7-99.7%) against an independent oracle, versus 66-80% for an LLM summary of the same capture, a mid-tier model reading the block matching a frontier one. The same compiler doubles as a demand-side cost instrument. Read off passive, pre-delegation human activity rather than agent rollouts, it supplies two parameters that agent-cost models assume but, to our knowledge, have not measured: the Routine Overhead Ratio R and the routine recurrence h. We report first values of R, a modeled upper bound, at 60-343x, and a delegable recurrence of 9.0% in-sample and 7.7% out-of-sample, for a realistic all-fleet token ceiling near 8%; a compiled routine replays deterministically with the model out of the loop, demonstrated live at zero model tokens on a guard-matched hit. Schema, compiler, and evaluation harness are open.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
