# Memory-Managed Long-Context Attention: A Preliminary Study of Editable Request-Local Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.28876v1
- Published: 2026-06-27
- Updated: 2026-06-27
- Authors: Junyi Zou, Avrova Donz
- Tags: context, long-term
- Categories: cs.CL, cs.LG
- URL: http://arxiv.org/abs/2606.28876v1

## One-Sentence Summary
Long-context language models often conflate two different goals: compressing history into an efficient state, and maintaining reliable long-term memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-context language models often conflate two different goals: compressing history into an efficient state, and maintaining reliable long-term memory.

进一步看，论文的核心做法或实验重点可以概括为：Linear, recurrent, and sparse attention reduce the cost of processing long sequences, but they do not by themselves specify when a fact should be written, overwritten, protected from distractors, or discarded.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL, cs.LG

## Abstract Snapshot
Long-context language models often conflate two different goals: compressing history into an efficient state, and maintaining reliable long-term memory. Linear, recurrent, and sparse attention reduce the cost of processing long sequences, but they do not by themselves specify when a fact should be written, overwritten, protected from distractors, or discarded. We study memory-managed long-context attention, a research route that separates a fast recurrent or sparse backbone from explicit editable request-local memory slots and query-time sparse fallback. Across structured synthetic tasks, token/chunk/sequence bridges, generated natural language, and local frozen-model diagnostics, pure fixed-state or pure sparse methods fail some overwrite, version, anti-pollution, or no-write-signal cases, while a hybrid covers both routes. A small 2,097,152-token mechanism stress test reaches 50/50 pooled accuracy with 2-132 active chunks. A 2.74M-parameter minimal causal event-token model reaches 595/600 with lite write supervision, supporting proof of trainability rather than scale. A six-family frozen-hidden-state bridge reaches 1079/1080 controlled pointer accuracy, but it uses generator-provided integer key IDs and separately encoded canonical key strings; it is an oracle-metadata probe, not open-text entity resolution. Local non-leaderboard RULER 4K diagnostics remain close to full context, whereas a 33-record LongBench v1 16K subset shows that naive lexical selection is not general. The evidence separates three claims: controlled slot lifecycle is feasible, sparse fallback is needed when writes lack future-query signals, and learned open-domain selection remains the main architectural bottleneck. We do not claim a final generative architecture, global slot-trajectory convergence, or systems superiority.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
