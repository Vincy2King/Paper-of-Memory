# Agentsensus: Consensus-Compressed Shared Memory for Multi-Agent Story Worlds

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.32297v1
- Published: 2026-09-26
- Updated: 2026-09-26
- Authors: Yu Pan
- Tags: agent, long-term
- Categories: cs.AI, cs.CL, cs.MA
- URL: http://arxiv.org/abs/2609.32297v1

## One-Sentence Summary
A agentic story world is a dynamic system simulating who learned what, when, and from whom -- yet the standard design gives each character a private memory stream.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：A agentic story world is a dynamic system simulating who learned what, when, and from whom -- yet the standard design gives each character a private memory stream.

进一步看，论文的核心做法或实验重点可以概括为：A shared event is therefore stored once per witness, large duplication will be incurred in terms of storage.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI, cs.CL, cs.MA

## Abstract Snapshot
A agentic story world is a dynamic system simulating who learned what, when, and from whom -- yet the standard design gives each character a private memory stream. A shared event is therefore stored once per witness, large duplication will be incurred in terms of storage. We present Agentsensus, a story-world simulation framework in which there is an unified long-term memory. Records of the same event merge into one owned by all its witnesses, and semantically relevant memory records are linked. We evaluate on four worlds -- two classical Chinese novels, Hamlet, and a real-world conflict timeline -- run for 40 to 80 rounds against three per-character memory designs under an equal-granularity protocol. Agentsensus writes 22-44% fewer entries than the closest baseline and is the only design whose memory becomes shared (14-28% of records held by more than one character, some by 10) and linked (94-99%), at judged simulation quality indistinguishable or even better than the baselines. An ablation attributes this to the merge itself: disabling it multiplies the store by 3.1x and takes sharing to exactly zero. Sharing also compounds with the horizon rather than saturating early, rising 6% to 9% to 14% as one world is re-run at 10, 20 and 40 rounds.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
