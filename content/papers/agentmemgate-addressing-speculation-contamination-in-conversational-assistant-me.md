# AgentMemGate: Addressing Speculation Contamination in Conversational Assistant Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.07707v1
- Published: 2026-10-06
- Updated: 2026-10-06
- Authors: Chirag Sharma, Benjamin Fowlersmith, Karime Maamari
- Tags: agent, benchmark, conversation, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.07707v1

## One-Sentence Summary
Conversational AI assistants with long-term memory extract facts from user messages into a store consulted in later conversations.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Conversational AI assistants with long-term memory extract facts from user messages into a store consulted in later conversations.

进一步看，论文的核心做法或实验重点可以概括为：A stated plan can enter that store as fact: a user who might move to Seattle may be recorded as already living there.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, long-term
- 检索关键词命中：long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.AI

## Abstract Snapshot
Conversational AI assistants with long-term memory extract facts from user messages into a store consulted in later conversations. A stated plan can enter that store as fact: a user who might move to Seattle may be recorded as already living there. We call this speculation contamination. Final-state memory benchmarks miss this error because they do not probe intermediate state and include few unresolved speculations. We present AgentMemGate, a write-time gate for profile-store memory that classifies extracted statements as speculation, completed event, correction, or other. Speculations remain outside memory, with conditions governing later promotion or deletion. We also contribute a dataset of multi-session conversations in which plans are confirmed, abandoned, or left unresolved. On our 147-conversation held-out set, Mem0 and Graphiti assert unresolved plans as current state for 35.2% and 27.3% of pending plans. On the core benchmark, AgentMemGate eliminates all observed contamination relative to the identical ungated pipeline (87.5% to zero for the most exposed extraction style) and raises task accuracy from 65% to 95%. On the harder held-out set, gated contamination is 3.4% to 5.7% and task accuracy rises by 9 to 13 percentage points. Our analysis identifies field matching as the main remaining bottleneck: realistic speculations often match no profile field and never reach the gate. We release our datasets, prompts, and evaluation code.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
