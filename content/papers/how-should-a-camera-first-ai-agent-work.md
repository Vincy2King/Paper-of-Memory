# How Should a Camera-First AI Agent Work?

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.14772v1
- Published: 2026-10-10
- Updated: 2026-10-10
- Authors: Xiaofan Wu, Xi Zeng, Miaoxia Chen, Peishan Chen, Shuyan Li, Chen Wang, Jiyun Yao, Hanyong Zhong, Jiahao Zhu
- Tags: agent
- Categories: cs.AI, cs.HC, cs.LO
- URL: http://arxiv.org/abs/2610.14772v1

## One-Sentence Summary
Camera-first agents must act on the visual world as it unfolds.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Camera-first agents must act on the visual world as it unfolds.

进一步看，论文的核心做法或实验重点可以概括为：We argue that the central obstacle for future camera-first agents is not recognition ability - multimodal models (vision-language and live/streaming alike) generalize well through language and remain the right tool...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：working memory
- 来源分类信息：cs.AI, cs.HC, cs.LO

## Abstract Snapshot
Camera-first agents must act on the visual world as it unfolds. We argue that the central obstacle for future camera-first agents is not recognition ability - multimodal models (vision-language and live/streaming alike) generalize well through language and remain the right tool for semantic reasoning - but time. Many visual targets are ephemeral: they appear, are query-relevant, and leave within a short window. Binding memory to the same end-to-end path as reasoning means that by the time a monolithic pipeline completes, the evidence is gone. We formalize this as Ephemeral-Target Interaction (ETI) and a Perceptual Deadline Contract separating a hard memory deadline from a soft reasoning deadline, grounded in the bounded, passive nature of sensory and working memory. We propose a two-deadline architecture: an always-on, bounded, non-semantic fast path; an active remembering mechanism that commits a moment to durable memory before it is overwritten (event-driven in v1); and a deferred deliberation layer (multimodal model + tools). We instantiate the contract on real MOT17 track windows, a consistency check, and calibrate the single-path baseline from measured frontier-model latency: even a short answer takes 1.2-9.3 s, and an agentic identify-and-search longer. Answers can be late; evidence cannot be missed.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
