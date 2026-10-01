# Memory Is a Derivation: The Distributed-Evidence Paradox in Long-Term Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.36130v1
- Published: 2026-09-28
- Updated: 2026-09-28
- Authors: Hongjun Liu, Chen Zhao
- Tags: agent, compression, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.36130v1

## One-Sentence Summary
Long-running LLM agents compress past interactions into persistent memories that may be reused as premises for later tasks.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-running LLM agents compress past interactions into persistent memories that may be reused as premises for later tasks.

进一步看，论文的核心做法或实验重点可以概括为：This creates a distinct derivation problem: whether the memory actually follows from what the interaction history supports.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression, long-term
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-running LLM agents compress past interactions into persistent memories that may be reused as premises for later tasks. This creates a distinct derivation problem: whether the memory actually follows from what the interaction history supports. Relevant evidence may be scattered across earlier interactions, while compression can introduce relations or event status that the history never established. A valid memory may therefore appear unsupported because its citations omit relevant evidence, while individually supported facts may be composed into a stronger statement the history never established. We characterize this problem through three coupled requirements: (1) Evidence scope; (2) Compositional validity; (3) Admission reliability. We therefore ask whether the interaction history available at write time supports what enters persistent memory. We introduce DerivAudit, a framework for auditing whether a memory is actually supported by the history available when it was written. The audit separates three questions: whether supporting evidence lies beyond writer-provided citations, whether the composed memory introduces unsupported meaning, and how write-time admission decisions affect later memory use. Across two natural memory corpora, audits using broader pre-write history recover support for nearly 60% of memories that appear unsupported from citations alone, while 17-21% remain unsupported after expansion. Yet broader evidence does not by itself make admission reliable: unsupported memories are still frequently admitted across verification models, and evidence expansion alone worsens it on two backbones.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
