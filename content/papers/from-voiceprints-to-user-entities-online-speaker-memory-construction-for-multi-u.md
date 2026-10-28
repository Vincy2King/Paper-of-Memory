# From Voiceprints to User Entities: Online Speaker-Memory Construction for Multi-User Spoken Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.36713v1
- Published: 2026-10-27
- Updated: 2026-10-27
- Authors: Yucong Zhang, Cancan Li, Bo Xiao, Ke Zeng, Ming Li
- Tags: agent, benchmark, retrieval
- Categories: cs.SD, cs.AI, eess.AS
- URL: http://arxiv.org/abs/2610.36713v1

## One-Sentence Summary
Personalized spoken agents must identify speakers before accessing user-specific memory, yet memory benchmarks typically assume correctly attributed histories.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Personalized spoken agents must identify speakers before accessing user-specific memory, yet memory benchmarks typically assume correctly attributed histories.

进一步看，论文的核心做法或实验重点可以概括为：We argue that voiceprints are observations of identity, not identities themselves, and formulate online speaker-memory construction to maintain persistent user entities as acoustic evidence evolves.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：cs.SD, cs.AI, eess.AS

## Abstract Snapshot
Personalized spoken agents must identify speakers before accessing user-specific memory, yet memory benchmarks typically assume correctly attributed histories. We argue that voiceprints are observations of identity, not identities themselves, and formulate online speaker-memory construction to maintain persistent user entities as acoustic evidence evolves. We introduce EvoSpeakerMem, a training-free layer for causal speaker routing, selective acoustic-state updates, and identity-partitioned memory writes and retrieval through a replaceable text-memory backend. We also construct LoCoMo-ID, a spoken-memory benchmark with hidden speaker identities, speaker-sensitive queries, simulated recording-condition shifts, and four-speaker identity-confusion tests. On longitudinal SMIIP-TV, genuine-probe rejection under a frozen near-enrollment threshold rises from 29.8% to 55.6% over approximately one year. On LoCoMo-ID speaker-sensitive queries, gated updating improves identity-gated QA over fixed representations by 3.86 and 11.62 percentage points under clean and shifted conditions, respectively, with no wrong-user authorizations. The advantage persists in the four-speaker test. Yet reducing fragmentation and improving QA can coexist with incorrect cross-user links, revealing a fragmentation--contamination trade-off that QA alone cannot capture.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
