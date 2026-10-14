# Can Agents Forget When Asked? A Benchmark for Memory Unlearning in LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.18052v1
- Published: 2026-10-13
- Updated: 2026-10-13
- Authors: Bofan Xie, Chaokun Wang, Guanchen Ge, Songyao Wang, Fang Niu, Hang Zhang, Wei Wang
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.18052v1

## One-Sentence Summary
Long-term memory has become a core component of large language model (LLM) agents.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory has become a core component of large language model (LLM) agents.

进一步看，论文的核心做法或实验重点可以概括为：As agents accumulate personal information over long-term use, users increasingly ask them to delete sensitive or outdated facts.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term memory has become a core component of large language model (LLM) agents. As agents accumulate personal information over long-term use, users increasingly ask them to delete sensitive or outdated facts. A memory system should honor such requests. It should remove exactly what was requested and keep the rest of its memory intact. However, existing memory benchmarks evaluate only memory writing, retrieval, and organization, so whether agents can forget at the user's explicit request remains under-evaluated. To address this gap, we propose Bemula, the first benchmark dedicated to memory unlearning. It comprises 50 multi-session dialogue instances, 135 forget requests of six types, and 1,742 test questions. Each dialogue has a control version without the requests, so that only systems that have stored the target can earn credit for forgetting. Across the paired versions, five test suites measure storage, removal of the requested information, preservation of unrelated memories, relearning of similar facts, and resistance to extraction attacks. On Bemula, we evaluate six mainstream memory systems under three backbone LLMs, together with the Full Context LLM on two of them. The results are negative. Across all evaluated systems and backbones, no system passes more than 1.5% of forget requests end to end, and most pass none at all. These systems either leave the requested information extractable under simple attacks or delete far more than requested. Memory unlearning therefore remains an open challenge for agent memory design. We release our data and code at https://github.com/Nboxff/bemula-benchmark.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
