# When Memory Updates but Behavior Does Not: Repairing Implicit Stale Dependencies in Personalized Agent Responses

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.01619v1
- Published: 2026-08-03
- Updated: 2026-08-03
- Authors: Haofei Sun, Lin He
- Tags: agent, benchmark, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.01619v1

## One-Sentence Summary
Memory-augmented agents can know that a user's stored state is outdated and still plan around the old value.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-augmented agents can know that a user's stored state is outdated and still plan around the old value.

进一步看，论文的核心做法或实验重点可以概括为：The STALE benchmark calls this the implicit policy adaptation (IPA) gap.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：agent memory, memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Memory-augmented agents can know that a user's stored state is outdated and still plan around the old value. The STALE benchmark calls this the implicit policy adaptation (IPA) gap. We identify one structural contributor: draft-anchored verification checks what a response says, and in an open-ended response the stale dependency is usually unsaid. StateAuditor therefore audits in the opposite direction, from stored state to draft. An LLM proposes candidate old-to-new transitions from timestamped evidence; deterministic code pins each quotation to a single entry, checks that the new evidence really is newer, and lets only these verified transitions trigger repair. What is verified is provenance and chronology - not semantic supersession. On STALE's full protocol (400 scenarios, 50-session histories, one independent response per query), strict single-query VTA scores .736 against .686 for our locked predecessor under the same judge: a +5.0-point paired gain (95% CI [+2.9, +7.2]) coming almost entirely from IPA and premise resistance (PR). The benchmark's own judge, from a third model family, reproduces the gain (.738 vs. .680). On an independent cross-family preference-evolution benchmark (HorizonBench), the full draft-audit-repair pipeline over a gold-derived structured store raises current-preference accuracy (user-clustered p<.01), though a matched control shows most of this external gain is the draft-side audit itself; a harder authored lifecycle set gives no gain, bounding the claim while false invalidation stays controlled. On STALE, by contrast, a matched control (same evidence, adapter, and call budget) scores only .692 (+0.6 over the predecessor, n.s.), attributing the STALE gain to the transition machinery rather than added context or calls. We make no claim about general-purpose agent memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
