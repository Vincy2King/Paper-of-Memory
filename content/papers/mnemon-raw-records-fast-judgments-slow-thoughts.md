# Mnemon: Raw Records, Fast Judgments, Slow Thoughts

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.36059v1
- Published: 2026-09-28
- Updated: 2026-09-28
- Authors: Guangren Wang
- Tags: agent, context, conversation, long-term
- Categories: cs.CL, cs.AI, cs.IR
- URL: http://arxiv.org/abs/2609.36059v1

## One-Sentence Summary
Long-term memory lets an LLM assistant use a history it can no longer reread, and most memory systems build it by rewriting conversations into facts, graphs or typed memories at...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory lets an LLM assistant use a history it can no longer reread, and most memory systems build it by rewriting conversations into facts, graphs or typed memories at write time.

进一步看，论文的核心做法或实验重点可以概括为：We argue that the work of memory divides, as thinking does, into two systems.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL, cs.AI, cs.IR

## Abstract Snapshot
Long-term memory lets an LLM assistant use a history it can no longer reread, and most memory systems build it by rewriting conversations into facts, graphs or typed memories at write time. We argue that the work of memory divides, as thinking does, into two systems. Most of it is fast System 1 work: many small, independent yes/no judgments about records, such as whether a record is needed or no longer current, which a decision model makes by the dozen in a third of a second. Only a little is slow System 2 work: writing a few search queries, naming what the reply needs and composing the answer, which an LLM does well but slowly. We present Mnemon, a memory agent built on this division. It keeps conversations as raw, dated records; an LLM (System 2) plans searches over them, a decision model, Jev (System 1), judges what the searches return, and rules with explicit budgets turn the judgments into a small View for an unchanged answering model. A background pass consolidates each record once into topic timelines, value histories and standing instructions linked to the records, so that questions about a whole conversation reach evidence their own searches miss. Because nothing is decided about a record when it is written, the same agent can read any store that returns dated records. With gpt-4.1-mini answering, as in a public re-evaluation of 14 systems, Mnemon scores 91.7% on LoCoMo, the highest among them, and 83.8% on LongMemEval-S, from under 4k tokens of context per question, with the lowest effective cost index on LoCoMo. With a reasoning model answering, it reaches 92.2% on LoCoMo and 94.4% on LongMemEval-S, the latter on par with the best published results. From 100K to 10M tokens of history on BEAM, its cost per question grows by a factor of 1.11. On the same records, Jev separates gold evidence better than two LLMs and is 3-11 times faster.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
