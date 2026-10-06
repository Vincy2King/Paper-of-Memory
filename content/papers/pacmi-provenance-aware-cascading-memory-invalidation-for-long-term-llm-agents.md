# PACMI: Provenance-Aware Cascading Memory Invalidation for Long-Term LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.05732v1
- Published: 2026-10-05
- Updated: 2026-10-05
- Authors: Yiqi Wang, Jiaqi Liu, Jiaqi Zhang, Zhangkai Wu, Yiqun Duan, Mingkai Zheng, Taotao Cai
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.LG, cs.IR
- URL: http://arxiv.org/abs/2610.05732v1

## One-Sentence Summary
LLM agents rely on long-term memory to retain and reuse information when performing tasks over long horizons.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM agents rely on long-term memory to retain and reuse information when performing tasks over long horizons.

进一步看，论文的核心做法或实验重点可以概括为：Existing methods provide limited support for handling memories that become outdated as new observations or domain evidence arrive.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.LG, cs.IR

## Abstract Snapshot
LLM agents rely on long-term memory to retain and reuse information when performing tasks over long horizons. Existing methods provide limited support for handling memories that become outdated as new observations or domain evidence arrive. Such outdated memories may remain semantically relevant, continue to affect dependent records, and retain value as historical evidence. This calls for two capabilities: dependency tracking to identify downstream effects and historical preservation to retain useful past records. We propose Provenance-Aware Cascading Memory Invalidation (PACMI), a framework that represents memories and new evidence in a provenance graph with typed dependency edges. PACMI assigns records to a four-state validity lattice, propagates validity changes to dependent memories, and uses the resulting states for retrieval and stale-premise detection. We also introduce a diagnostic benchmark with 100 cases and 300 queries across five domains. The evaluation separates node, context-, and answer-level performance. PACMI achieves the highest final-answer accuracy on this benchmark, and its paired difference from the strongest baseline is significant under an exact McNemar test. The premise checker achieves perfect precision, recall, and F 1 on the controlled query distribution. Cascading propagation primarily improves memorystate correctness: removing it increases final-answer errors from 3 to 11, but the paired difference does not reach the 0.05 significance threshold. Code and data will be made publicly available.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
