# MNIST-PRO: MNIST is Back as a Partially Observable World for AI Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.31022v1
- Published: 2026-08-31
- Updated: 2026-08-31
- Authors: Vernon Toh, Navonil Majumder, Zhengyuan Liu, Nancy F. Chen, Soujanya Poria
- Tags: agent, benchmark
- Categories: cs.AI, cs.CV
- URL: http://arxiv.org/abs/2608.31022v1

## One-Sentence Summary
AI agents in partially observable environments need to coordinate active sensing with working memory to maintain an evolving perceptual state.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：AI agents in partially observable environments need to coordinate active sensing with working memory to maintain an evolving perceptual state.

进一步看，论文的核心做法或实验重点可以概括为：However, existing benchmarks struggle to isolate this perceptual-state construction and interpretation capability because they introduce physical and control complexities.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：working memory
- 来源分类信息：cs.AI, cs.CV

## Abstract Snapshot
AI agents in partially observable environments need to coordinate active sensing with working memory to maintain an evolving perceptual state. However, existing benchmarks struggle to isolate this perceptual-state construction and interpretation capability because they introduce physical and control complexities. We address this with MNIST-PRO, a benchmark that isolates agentic perception by converting MNIST digit recognition into a sequential, glimpse-based search task with lookback constraints. We evaluate ten multimodal models across four memory representations, including raw visual history, textual states, structured metric grid maps, and a consolidated visual canvas. While models excel under full observability, partial observability exposes a clear performance gap. We identify three distinct bottlenecks. First, perceptual-state construction and interpretation present a challenge, as agents struggle to integrate fragmented glimpses. Second, agents often stop exploring before they see the full sequence. Third, models often fail to revise early, incorrect beliefs even when faced with subsequent contradictory evidence. These results show that simply acquiring visual evidence is not enough. Agents must also be able to build and update a reliable perceptual state.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
