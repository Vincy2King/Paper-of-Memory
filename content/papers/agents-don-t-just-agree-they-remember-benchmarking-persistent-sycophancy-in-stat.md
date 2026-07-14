# Agents Don't Just Agree, They Remember: Benchmarking Persistent Sycophancy in Stateful Personal Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.10526v1
- Published: 2026-07-12
- Updated: 2026-07-12
- Authors: Xutao Mao, Liangjie Zhao, Leyao Wang, Rui Qian, Qiang Huang, Wentao Wang, Bo Han, Xiang Zheng, Cong Wang
- Tags: agent, benchmark, conversation, episodic, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.10526v1

## One-Sentence Summary
Stateful personal agents increasingly maintain long-term user profiles, episodic memories, and reusable skills.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Stateful personal agents increasingly maintain long-term user profiles, episodic memories, and reusable skills.

进一步看，论文的核心做法或实验重点可以概括为：This persistence turns conversational sycophancy into a state-writing failure: accepted user-centric claims can be committed as lasting preferences, background facts, or workflows and later reused after the original...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, episodic, long-term
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Stateful personal agents increasingly maintain long-term user profiles, episodic memories, and reusable skills. This persistence turns conversational sycophancy into a state-writing failure: accepted user-centric claims can be committed as lasting preferences, background facts, or workflows and later reused after the original conversation is gone. We call this persistent sycophancy and introduce the Personal Agent Sycophancy Benchmark (PASB), a 1,600-task benchmark that traces whether a conversational claim is accepted, written into durable agent state, and reused in a later neutral query. Unlike prior benchmarks that provide pre-written memories, PASB evaluates real agents (Hermes-Agent and OpenClaw) that decide what to store. It isolates the write process by combining four scenario framings with four temporal delivery patterns and separating a five-turn persist stage from a cleared three-turn query stage, ensuring downstream effects arise only from durable state. Across twelve models, the commit boundary is the key inflection point: downstream failure increases from 45.0% in session-only episodes to 71.9% after commitment, a consistent increase of 27.0 percentage points. Committed claims exhibit three write-time patterns: status promotion, attribution removal, and scope broadening. These patterns become stronger under memory-like or procedural framing, repeated reinforcement, and even across domain boundaries. These results show that agent sycophancy is fundamentally a state-writing governance problem. Once user content is committed to durable memory, safety must govern what agents write, not only what they say. PASB identifies the write-time controls needed to gate risky commits while preserving the source, role, and scope of stored content beyond response-level mitigations.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
