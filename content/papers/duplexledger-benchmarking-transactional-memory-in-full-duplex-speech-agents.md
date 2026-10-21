# DuplexLedger: Benchmarking Transactional Memory in Full-Duplex Speech Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.27581v1
- Published: 2026-10-20
- Updated: 2026-10-20
- Authors: Yuxuan Li, Xiangchen Guan, Kunrong Li, Jin Wang, Kaiwen Luo, Yang Xiao, Yufei Guo, Zhisheng Chen, Liang Lin, Kun Wang
- Tags: agent, benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.27581v1

## One-Sentence Summary
Full-duplex speech agents must update persistent memory while listening and speaking, yet it remains unclear which events should be stored, revised, or excluded.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Full-duplex speech agents must update persistent memory while listening and speaking, yet it remains unclear which events should be stored, revised, or excluded.

进一步看，论文的核心做法或实验重点可以概括为：Existing benchmarks isolate interaction timing from memory outcomes, obscuring the state transitions behind a correct answer.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Full-duplex speech agents must update persistent memory while listening and speaking, yet it remains unclear which events should be stored, revised, or excluded. Existing benchmarks isolate interaction timing from memory outcomes, obscuring the state transitions behind a correct answer. We introduce DuplexLedger, a bilingual benchmark of 1,094 persistent sessions aligning four full-duplex scenarios with event-level Write/Update/Ignore/Retain supervision, explicit pre/post memory states, and 6,564 same-session questions and checks. Evaluating five full-duplex models reveals an interaction-memory gap: no system combines strong boundary control with coherent final-state memory, and the best final-state fact coverage is 2.01%. We propose ACT-Mem, an 8.92M-parameter sidecar comprising an event controller, a versioned transactional ledger, and a typed retriever coupled with a frozen MiniCPM-o 4.5 backbone. On 219 held-out sessions, ACT-Mem increases latest-value accuracy from 4.11% to 8.68% while reducing stale assertions and distractor adoption. It improves interaction boundaries but slows interruption stopping. These results motivate selective, auditable full-duplex memory rather than indiscriminate transcript retention. Code is available at https://github.com/lyx-researcher/DuplexLedger.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
