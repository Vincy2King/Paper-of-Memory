# SCM: Sleep-Consolidated Memory with Algorithmic Forgetting for Large Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.20943v1
- Published: 2026-04-22
- Updated: 2026-04-22
- Authors: Saish Sachin Shinde
- Tags: benchmark, context, conversation
- Categories: cs.LG
- URL: http://arxiv.org/abs/2604.20943v1

## One-Sentence Summary
We present SCM (Sleep-Consolidated Memory), a research preview of a memory architecture for large language models that draws on neuroscientific principles to address a...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We present SCM (Sleep-Consolidated Memory), a research preview of a memory architecture for large language models that draws on neuroscientific principles to address a fundamental limitation in current systems: the...

进一步看，论文的核心做法或实验重点可以概括为：Existing approaches rely on truncating context windows, growing vector databases without bound, or tiered storage systems that lack consolidation and forgetting mechanisms.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, conversation
- 检索关键词命中：working memory
- 来源分类信息：cs.LG

## Abstract Snapshot
We present SCM (Sleep-Consolidated Memory), a research preview of a memory architecture for large language models that draws on neuroscientific principles to address a fundamental limitation in current systems: the absence of persistent, structured, and biologically plausible memory. Existing approaches rely on truncating context windows, growing vector databases without bound, or tiered storage systems that lack consolidation and forgetting mechanisms. SCM implements five core components inspired by human memory: a limited-capacity working memory, multi-dimensional importance tagging, offline sleep-stage consolidation with distinct NREM and REM phases, intentional value-based forgetting, and a computational self-model enabling introspection. Across a standardized benchmark suite of eight tests, the prototype achieves perfect recall accuracy over ten-turn conversations while reducing memory noise by 90.9% through adaptive forgetting. Memory search latency remains below one millisecond even with hundreds of stored concepts. This work establishes the architectural foundations for memory systems that consolidate, prioritize, and forget, offering a testable platform for advancing LLM memory research.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
