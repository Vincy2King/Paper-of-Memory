# Can an AI Assistant Really Forget? Auditable Deletion from Addressable Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.27539v4
- Published: 2026-07-30
- Updated: 2026-09-11
- Authors: Vishwajith Ramesh
- Tags: conversation
- Categories: cs.LG, cs.CL
- URL: http://arxiv.org/abs/2607.27539v4

## One-Sentence Summary
An assistant can stop repeating a fact without removing it from memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：An assistant can stop repeating a fact without removing it from memory.

进一步看，论文的核心做法或实验重点可以概括为：To study this difference, we install a support-vector gate in frozen Gemma 3 and record which stored keys and values belong to each exchange.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：conversation
- 检索关键词命中：conversational memory
- 来源分类信息：cs.LG, cs.CL

## Abstract Snapshot
An assistant can stop repeating a fact without removing it from memory. To study this difference, we install a support-vector gate in frozen Gemma 3 and record which stored keys and values belong to each exchange. A deletion request excludes the exchange's rows from the long-range readout and recalculates the gate on what remains. We check this operation against an independent refit, then compare it with running the model again on the conversation without the exchange. This second comparison matters because the exchange may already have influenced surviving memory rows. At 4B, the gated model passed checks for recall and feasible deletion on the same six of eight records admitted by the base model, at a perplexity cost under 2%. Admission fell at the smaller and larger checkpoints with the same configuration. The edited memory agreed closely with the local refit on the registered probes, and the model disclosed fewer deleted answers than when simply instructed to forget. However, an attack evaluated separately for each record could still distinguish edited memory from memory that never stored the record. Excluding an exchange's own rows therefore provides a way to edit and audit conversation memory, while leaving a measurable difference from rebuilding it without that exchange. Additional paired studies found no update-speed advantage for the current FP32 proxy and retained-answer matching below half in every tested condition.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
