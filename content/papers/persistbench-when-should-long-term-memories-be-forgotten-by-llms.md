# PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?

- Source: OpenReview
- Venue: ICML 2026 regular
- Paper ID: openreview:Z7Rhzk13NT
- Published: 2026-04-30
- Updated: 2026-06-24
- Authors: Sidharth Pulipaka, Oliver Chen, Manas Sharma, Taaha Saleem Bajwa, Vyas Raina, Ivaxi Sheth
- Tags: benchmark, context, conversation, long-term
- Categories: ICML.cc/2026/Conference/-/Submission
- URL: https://openreview.net/forum?id=Z7Rhzk13NT

## One-Sentence Summary
Conversational assistants are increasingly integrating long-term memory with large language models (LLMs).

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, conversation, long-term` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ICML 2026 regular` 这个 venue 相关。

从摘要来看，作者主要关注的是：Conversational assistants are increasingly integrating long-term memory with large language models (LLMs).

进一步看，论文的核心做法或实验重点可以概括为：This persistence of memories, e.g., the user is vegetarian, can enhance personalization in future conversations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ICML 2026 regular
- 高亮主题命中：benchmark, context, conversation, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：ICML.cc/2026/Conference/-/Submission

## Abstract Snapshot
Conversational assistants are increasingly integrating long-term memory with large language models (LLMs). This persistence of memories, e.g., the user is vegetarian, can enhance personalization in future conversations. However, the same persistence can also introduce safety risks that have been largely overlooked. Hence, we introduce \textbf{PersistBench} to measure the extent of these safety risks. We identify two long-term memory-specific risks: \textit{cross-domain leakage}, where LLMs inappropriately inject context from the long-term memories; and \textit{memory-induced sycophancy}, where stored long-term memories insidiously reinforce user biases. We evaluate 18 frontier and open-source LLMs on our benchmark. Our results reveal a surprisingly high failure rate across these LLMs - a median failure rate of $53\%$ on cross-domain samples and $97\%$ on sycophancy samples. To address this, our benchmark encourages the development of more robust and safer long-term memory usage in frontier conversational systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
