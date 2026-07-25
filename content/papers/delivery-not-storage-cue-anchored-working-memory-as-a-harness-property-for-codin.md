# Delivery, Not Storage: Cue-Anchored Working Memory as a Harness Property for Coding Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.20972v1
- Published: 2026-07-23
- Updated: 2026-07-23
- Authors: Swapnanil Saha
- Tags: agent, conversation
- Categories: cs.AI, cs.SE
- URL: http://arxiv.org/abs/2607.20972v1

## One-Sentence Summary
Coding agents ship with one kind of memory: documents.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Coding agents ship with one kind of memory: documents.

进一步看，论文的核心做法或实验重点可以概括为：Instruction files, plan artifacts, and auto-written memory directories are deliberately authored and deliberately retrieved: the agent must choose to write them and choose to read them back.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation
- 检索关键词命中：working memory
- 来源分类信息：cs.AI, cs.SE

## Abstract Snapshot
Coding agents ship with one kind of memory: documents. Instruction files, plan artifacts, and auto-written memory directories are deliberately authored and deliberately retrieved: the agent must choose to write them and choose to read them back. Human expertise runs on a second tier that never gets written down: situationally-bound operational facts (gotchas, locations, local conventions) encoded as a side effect of the work and retrieved involuntarily when the situation cues them. We argue this second tier is the load-bearing one for long-running agents and must be a harness property, not an agent choice. We contribute: (1) a two-tier design theory grounded in the cognitive literature on memory offloading, incidental encoding, and event-based prospective memory, each mapped to an architectural requirement; (2) a cue-anchored memory model where memories carry first-class trigger conditions over a composable vocabulary (path, symbol, semantic, event, temporal), evaluated deterministically by the harness, a composition no surveyed academic or shipped system provides; (3) a controlled evaluation on a real coding task showing that voluntary memory use is near zero even with a pre-seeded store (0 memory operations in 114 turns), that deterministic injection delivered in every seeded run with zero false alarms, and that 39% of intra-session re-reads re-buy content paid for before a compaction boundary; (4) a repeated-compaction decay probe: ten facts held only in conversation vanish at the first summary and stay absent from 106 of 108 compactions, and the deprived agent greps the harness's own session files to rebuild them, while the same facts injected from a harness-owned store arrive intact through all 138 compact-resumes as the final summary carries none. Delivery, not storage, is the product: the reliable memory channel for agents is the one the agent never has to think about.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
