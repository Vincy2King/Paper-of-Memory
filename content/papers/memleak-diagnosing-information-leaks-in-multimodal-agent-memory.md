# MemLeak: Diagnosing Information Leaks in Multimodal Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.29788v1
- Published: 2026-06-29
- Updated: 2026-06-29
- Authors: Kuan Wang, Chao Zhang
- Tags: agent, benchmark
- Categories: cs.LG
- URL: http://arxiv.org/abs/2606.29788v1

## One-Sentence Summary
When a multimodal AI agent is asked to forget a fact, current memory systems usually delete the text entry and report success.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：When a multimodal AI agent is asked to forget a fact, current memory systems usually delete the text entry and report success.

进一步看，论文的核心做法或实验重点可以概括为：We find that the fact can remain recoverable from retained user images, including images tagged to entirely different facts, because VLMs use implicit visual cues at inference time.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：agent memory
- 来源分类信息：cs.LG

## Abstract Snapshot
When a multimodal AI agent is asked to forget a fact, current memory systems usually delete the text entry and report success. We find that the fact can remain recoverable from retained user images, including images tagged to entirely different facts, because VLMs use implicit visual cues at inference time. We introduce the Information Provenance Graph (IPG), a taxonomy that classifies memory representations by deletion affordance. The IPG reveals that deletion fails through multiple channels. Our benchmark, MemLeak, measures this across a deletion cascade: direct probing of deletion-capable systems yields <1%, but retained correlated text enables 18.3% recovery, and retained images enable 12.0% recovery (0.0% blind baseline, 0.3% FPR) -- with 47% of image leaks not text-recoverable. Content-aware semantic deletion reduces the image residual to 2.0%. The residual appears across multiple VLMs, a production memory system, and real Unsplash-licensed photographs. Dual-annotator human validation (kappa = 0.88) confirms judge reliability.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
