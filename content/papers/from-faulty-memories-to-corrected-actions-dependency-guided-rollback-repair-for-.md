# From Faulty Memories to Corrected Actions: Dependency-Guided Rollback Repair for Memory-Augmented Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.10502v1
- Published: 2026-08-11
- Updated: 2026-08-11
- Authors: Caili Yu, Yiqi Wang, Jiaqi Zhang, Yiqun Duan, Mingkai Zheng, Zhangkai Wu, Kaize Shi, Taotao Cai
- Tags: agent, benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.10502v1

## One-Sentence Summary
Persistent memory lets language-model agents reuse information across sessions, but it also makes errors durable: a poisoned, stale, or misattributed record can alter reasoning,...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent memory lets language-model agents reuse information across sessions, but it also makes errors durable: a poisoned, stale, or misattributed record can alter reasoning, tool use, answers, and subsequent...

进一步看，论文的核心做法或实验重点可以概括为：Existing defenses mainly detect or delete suspicious memories, or revise the current response.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：memory augmented, memory-augmented, persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Persistent memory lets language-model agents reuse information across sessions, but it also makes errors durable: a poisoned, stale, or misattributed record can alter reasoning, tool use, answers, and subsequent memory writes. Existing defenses mainly detect or delete suspicious memories, or revise the current response. Deleting the source leaves already propagated claims, actions, and derived memories active, whereas resetting the store or replaying the full trace destroys benign state and repeats unnecessary computation. We therefore formulate \textbf{post-failure memory recovery: } \textit{given a failed execution and diagnosed faulty memories, recover both the answer and persistent state while retaining unaffected work.} Our \textbf{dependency-guided rollback repair} builds a typed memory-to-action graph from runtime provenance, traces explicit downstream dependencies, preserves candidates with independent trusted support, deactivates unsupported memory state, and selectively replays only answer-relevant affected computation. We evaluate this approach on a 150-case controlled benchmark spanning three tool-use domains and four memory failure types, and on a 50-case trajectory-derived stress test adapted from LongMemEval-V2. On the controlled benchmark, it achieves 85.3\% recovery versus 77.3\% for the best competing recovery method, removes all diagnosed faulty memories, preserves all benign memories, and requires only selective replay with modest LLM-call cost. On the adapted subset, it reaches 68.0\% recovery versus 54.0\% for the next best method, while also achieving the highest claim invalidation F1, 0.669 versus 0.603. Overall, the results do not imply uniformly better trace reconstruction, but show that dependency-guided rollback repair provides a strong recovery--cost trade-off while repairing faulty memory state and preserving benign memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
