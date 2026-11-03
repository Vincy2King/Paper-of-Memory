# Chain on Demand: Deferred Evidence Organization for Long-Term Conversational Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.02480v1
- Published: 2026-11-02
- Updated: 2026-11-02
- Authors: Di Lu, Zechen Li, Hao Xue
- Tags: conversation, long-term, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2611.02480v1

## One-Sentence Summary
Long-term conversational memory faces a timing mismatch: write-time summaries and graphs organize history before a future query is known, while independent retrieval can...

## Introduction
这篇论文被纳入仓库，是因为它和 `conversation, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term conversational memory faces a timing mismatch: write-time summaries and graphs organize history before a future query is known, while independent retrieval can allocate a limited evidence budget to redundant...

进一步看，论文的核心做法或实验重点可以概括为：We introduce Chain on Demand (CoD), a query-time evidence organization framework over an unchanged turn-level memory.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：conversation, long-term, retrieval
- 检索关键词命中：conversational memory, long-term memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Long-term conversational memory faces a timing mismatch: write-time summaries and graphs organize history before a future query is known, while independent retrieval can allocate a limited evidence budget to redundant or fragmented turns. We introduce Chain on Demand (CoD), a query-time evidence organization framework over an unchanged turn-level memory. Given a broad candidate pool, CoD constructs a temporary evidence chain by allocating a fixed anchor budget according to query relevance, lexical diversity relative to selected anchors, and newly covered query terms, followed by deterministic restoration of each selected anchor's same-session neighborhood. The resulting chain is used only for the current query, while the underlying conversational memory remains unchanged. In a paired comparison over all 1,986 LoCoMo questions, CoD achieves 82.2% accuracy on 1,540 non-adversarial questions and 76.3% on all 1,986 questions. On LongMemEval-S, one fixed configuration that indexes both user and assistant turns obtains 86.6% across all 500 questions. These results show that long-term memory can preserve the original conversation while deferring evidence organization until the information need is known.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
