# Memory Compression for High-Fanout Agent Sandboxes

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.11294v1
- Published: 2026-09-10
- Updated: 2026-09-10
- Authors: Mengming Li, Ceyu XU, Qijun Zhang, Jiangnan Yu, Xiangfeng Sun, Haohui Mai, Zhiyao Xie
- Tags: agent, compression
- Categories: cs.AI, cs.OS
- URL: http://arxiv.org/abs/2609.11294v1

## One-Sentence Summary
High-fanout agent workloads create a growing memory bottleneck because a single task may spawn many concurrent sandbox sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：High-fanout agent workloads create a growing memory bottleneck because a single task may spawn many concurrent sandbox sessions.

进一步看，论文的核心做法或实验重点可以概括为：Yet these sandboxes are far from independent: they originate from a shared template and execute related trajectories, exposing substantial template-relative and cross-sandbox memory redundancy.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression
- 检索关键词命中：memory compression
- 来源分类信息：cs.AI, cs.OS

## Abstract Snapshot
High-fanout agent workloads create a growing memory bottleneck because a single task may spawn many concurrent sandbox sessions. Yet these sandboxes are far from independent: they originate from a shared template and execute related trajectories, exposing substantial template-relative and cross-sandbox memory redundancy. Conventional memory compression is poorly matched to this setting in three fundamental dimensions: how to compress, because they fail to exploit similarity across non-identical sandbox pages; what to compress, because they control page-fault overhead through conservative page selection; and when to compress, because compression is either triggered by memory pressure or performed without awareness of agent execution phases. We present AgentZip, the first memory compression system designed specifically for AI-agent sandboxes. AgentZip introduces compression mechanisms that exploit both the template-relative and cross-sandbox redundancy. It broadens the compression scope to any page with a profitable representation and shifts overhead control from compression-time page selection to restore-time prefetching. It further aligns expensive compression with LLM waiting periods to avoid interfering with foreground tool execution. Across LLM training and inference workloads, AgentZip reduces sandbox-owned memory by up to 8.7x, compared with 2.1x for the Linux configuration. Restore prefetching and agent-execution-aware scheduling reduce the slowdown of aggressive compression from as high as 3.1x to 1.40x while retaining nearly all of its memory-saving benefit.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
