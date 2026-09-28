# Probing Stability-Plasticity Tradeoffs in Agent Memory through Cognitive Experimental Paradigms

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.30558v1
- Published: 2026-09-24
- Updated: 2026-09-24
- Authors: Jiaqi Ding, Guorong Wu
- Tags: agent, long-term
- Categories: cs.CL, cs.AI, cs.LG
- URL: http://arxiv.org/abs/2609.30558v1

## One-Sentence Summary
Agent memory systems are increasingly used to maintain long-term user preferences, task states and evolving facts, but current evaluations often collapse memory behavior into...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agent memory systems are increasingly used to maintain long-term user preferences, task states and evolving facts, but current evaluations often collapse memory behavior into final-answer accuracy.

进一步看，论文的核心做法或实验重点可以概括为：We introduce MemProbe, a cognitive-science-inspired framework for diagnosing stability-plasticity tradeoffs in agent memory.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL, cs.AI, cs.LG

## Abstract Snapshot
Agent memory systems are increasingly used to maintain long-term user preferences, task states and evolving facts, but current evaluations often collapse memory behavior into final-answer accuracy. We introduce MemProbe, a cognitive-science-inspired framework for diagnosing stability-plasticity tradeoffs in agent memory. The framework is motivated by a core insight from cognitive memory research: memory is reconstructive and shaped by interference, source reliability, reinforcement, and reactivation. MemProbe turns this insight into four reusable experimental paradigms (interference, misinformation, consolidation strength, and reconsolidation window) that manipulate when a memory should be updated, preserved, or treated as uncertain. It further decomposes correctness into behavioral profiles that reveal how systems update, preserve, attribute, and temporally organize information. We instantiate these paradigms in a 56-episode diagnostic suite and evaluate six incremental memory systems under a unified protocol. Results show that systems with similar aggregate scores exhibit distinct behavioral profiles. MemProbe provides such a diagnostic lens, turning aggregate performance into interpretable profiles of memory maintenance over time. Code is available at https://github.com/jq-ding/MemProbe.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
