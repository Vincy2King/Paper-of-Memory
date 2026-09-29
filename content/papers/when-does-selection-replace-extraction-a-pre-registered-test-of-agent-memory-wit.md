# When Does Selection Replace Extraction? A Pre-Registered Test of Agent Memory with a Typed Decision Model

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.34227v1
- Published: 2026-09-28
- Updated: 2026-09-28
- Authors: Rishabh Sharma, Rishika Lall
- Tags: agent, context, conversation
- Categories: cs.AI, cs.CL, cs.IR
- URL: http://arxiv.org/abs/2609.34227v1

## One-Sentence Summary
Does conversational memory need LLM-extracted facts, or is selecting the right raw turns enough?

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Does conversational memory need LLM-extracted facts, or is selecting the right raw turns enough?

进一步看，论文的核心做法或实验重点可以概括为：Published results disagree.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation
- 检索关键词命中：agent memory, conversational memory
- 来源分类信息：cs.AI, cs.CL, cs.IR

## Abstract Snapshot
Does conversational memory need LLM-extracted facts, or is selecting the right raw turns enough? Published results disagree. Extraction-based systems report gains from distilled facts. Recent studies find raw history with good ranking does as well, but disagree about whether ranking matters. We ran a pre-registered study on held-out LoCoMo conversations and LongMemEval. At a tight budget on LoCoMo, raw turns selected by a single call to Jev, a typed decision model, are non-inferior to an LLM-extraction memory (one-sided 95% bound -3.0 points against a -5-point margin). Blind human grading narrows the margin but does not change the result. Raw turns cost 3,061 times less to write, and the result holds with a second answer model. Within this study, reranking's gain shrinks as the budget grows. It adds 17.4 points on LoCoMo and 9.1 on LongMemEval when three of 30 candidates are kept. At generous budgets it adds 1.5 and 1.1, and extraction systems are more accurate. This suggests why published results disagree. At matched context, Jev selects as accurately as an LLM reranker (non-inferiority bound -2.0) at a third of the latency, and more accurately than a multi-call graph traversal. Reranking lowers correct abstention. Plans, code and graded answers are released.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
