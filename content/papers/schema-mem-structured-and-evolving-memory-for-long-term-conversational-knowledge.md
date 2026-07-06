# Schema-Mem: Structured and Evolving Memory for Long-term Conversational Knowledge

- Source: OpenReview
- Venue: ACL ARR 2026 May Submission
- Paper ID: openreview:2Zp5AW2HRK
- Published: 2026-06-02
- Updated: 2026-07-06
- Authors: Unknown
- Tags: agent, context, conversation, long-term, retrieval
- Categories: aclweb.org/ACL/ARR/2026/May/-/Submission
- URL: https://openreview.net/forum?id=2Zp5AW2HRK

## One-Sentence Summary
Long-term conversational agents require memory systems that continuously acquire and maintain user-specific knowledge from unstructured dialogue histories.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, long-term` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 May Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Long-term conversational agents require memory systems that continuously acquire and maintain user-specific knowledge from unstructured dialogue histories.

进一步看，论文的核心做法或实验重点可以概括为：Existing LLM memory solutions often rely on flat text storage or coarse summaries, which suffer from redundancy and weak factual grounding, making it difficult to reason over evolving information in long-term...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 May Submission
- 高亮主题命中：agent, context, conversation, long-term, retrieval
- 检索关键词命中：conversational memory
- 来源分类信息：aclweb.org/ACL/ARR/2026/May/-/Submission

## Abstract Snapshot
Long-term conversational agents require memory systems that continuously acquire and maintain user-specific knowledge from unstructured dialogue histories. Existing LLM memory solutions often rely on flat text storage or coarse summaries, which suffer from redundancy and weak factual grounding, making it difficult to reason over evolving information in long-term interactions. To address this, we propose \textit{Schema-Mem}, a structured and evolving memory framework that represents conversational knowledge as fact-level schema units. Schema-Mem incrementally builds a connected memory graph by extracting key facts from each dialogue turn, linking related historical units through hybrid lexical–semantic search, and refining memory via LLM-based verification to resolve conflicts and incorporate new details. For question answering, it performs multi-source retrieval over schema units, linked contexts, and similar raw dialogues to provide grounded evidence for accurate responses. Extensive experiments on LoCoMo and LongMemEval show that Schema-Mem consistently outperforms strong baselines for long-term conversational memory and question answering.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
