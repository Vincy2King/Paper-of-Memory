# REINS: A Self-Evolving Agent Harness for Real-Time Trajectory Planning

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.10748v1
- Published: 2026-11-07
- Updated: 2026-11-07
- Authors: Zhihong Cui, Hengyu Liu, Haoran Tang, Shijun Liu, Amir Taherkordi, Tor Skeie
- Tags: agent, benchmark
- Categories: cs.RO, cs.AI
- URL: http://arxiv.org/abs/2611.10748v1

## One-Sentence Summary
Agent harnesses -- runtime scaffolds that wrap an LLM's reasoning loop with tool dispatch, verification, and persistent memory -- have become the standard substrate for...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agent harnesses -- runtime scaffolds that wrap an LLM's reasoning loop with tool dispatch, verification, and persistent memory -- have become the standard substrate for deploying LLMs as autonomous agents, as...

进一步看，论文的核心做法或实验重点可以概括为：In trajectory planning, however, this paradigm has not taken hold: existing LLM-based trajectory planning methods either keep the LLM in the decision loop, exceeding the millisecond-level control budget, or offload it...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：cs.RO, cs.AI

## Abstract Snapshot
Agent harnesses -- runtime scaffolds that wrap an LLM's reasoning loop with tool dispatch, verification, and persistent memory -- have become the standard substrate for deploying LLMs as autonomous agents, as demonstrated by Claude Code and Codex in software engineering. In trajectory planning, however, this paradigm has not taken hold: existing LLM-based trajectory planning methods either keep the LLM in the decision loop, exceeding the millisecond-level control budget, or offload it to offline rules or training-time supervision -- leaving the runtime planner non-evolving. Intermediate hybrids still lack the verification-and-consolidation loop that makes harnesses reliable. We ask: what runtime harness would let an LLM planner meet real-time constraints while self-evolving into a deployable one? We propose REINS, a harness built on three LLM-planner couplings: LLM outputs are (i) grounded to a learned variable-level dynamics model, (ii) verified via calibrated predicates and forward rollout, and (iii) consolidated into an indexed rule memory that serves future scenes in O(log n) without re-invoking the LLM. The harness closes a self-evolution loop: familiar scenes resolve by memory lookup; novel scenes invoke the LLM, whose verified outputs enrich the memory. Without modifying LLM weights, REINS attains 98%+ compliance, nearly 50% collision reduction, and 1.9-4.6 ms latency on simulated and real-world benchmarks at the tactical decision layer, with LLM invocation rate monotonically declining as memory matures. Code: https://github.com/ZhihongCui/REINS

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
