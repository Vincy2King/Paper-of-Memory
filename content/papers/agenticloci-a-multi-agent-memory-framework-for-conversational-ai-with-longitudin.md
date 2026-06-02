# AgenticLOCI: A Multi-Agent Memory Framework for Conversational AI with Longitudinal Personalization

- Source: OpenReview
- Venue: ACL ARR 2026 May Submission
- Paper ID: openreview:iUinLcItGF
- Published: 2026-06-02
- Updated: 2026-06-02
- Authors: Unknown
- Tags: agent, benchmark, context, conversation, long-term, retrieval
- Categories: aclweb.org/ACL/ARR/2026/May/-/Submission
- URL: https://openreview.net/forum?id=iUinLcItGF

## One-Sentence Summary
Long-term conversational AI requires two distinct capabilities: remembering what was discussed and adapting to how a user's preferences evolve over time.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 May Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Long-term conversational AI requires two distinct capabilities: remembering what was discussed and adapting to how a user's preferences evolve over time.

进一步看，论文的核心做法或实验重点可以概括为：We argue these operate on different timescales and require separate but interoperable architectures.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 May Submission
- 高亮主题命中：agent, benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：aclweb.org/ACL/ARR/2026/May/-/Submission

## Abstract Snapshot
Long-term conversational AI requires two distinct capabilities: remembering what was discussed and adapting to how a user's preferences evolve over time. We argue these operate on different timescales and require separate but interoperable architectures. AgenticLOCI is a five-agent framework built on this premise: session retrieval fuses a semantic LLM ranker (Engram, STM) with a keyword-lobe scorer (Hippo, LTM) via Reciprocal Rank Fusion, while personalization is maintained through a versioned deliberation-state memory that accumulates empirically grounded decision-episode snapshots across interactions. We evaluate on three benchmarks using Qwen 2.5-7B-Instruct. On LoCoMo, the AgenticLOCI Backbone achieves F1 = 0.342 versus BM25 = 0.285 while consuming 7.3× fewer input tokens per item. On LongMemEval-S, item-level analysis confirms that Engram and Hippo solve architecturally distinct sub-problems; at 7B scale Hippo's keyword precision leads, a reversal expected to resolve at larger model sizes where LLM ranking is more reliable. On PersonaMem, all configurations perform within a narrow band, establishing that memory benefit is conditional on context-budget pressure. The longitudinal personalization layer is evaluated on a synthetic mobility benchmark with known user trajectories, achieving restraint of 0.976 and move-precision of 0.583 against an ablation baseline. We demonstrate the full framework as a personalized urban mobility assistant for an anonymized German city.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
