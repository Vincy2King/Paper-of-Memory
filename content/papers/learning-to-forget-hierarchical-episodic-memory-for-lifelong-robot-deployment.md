# Learning to Forget -- Hierarchical Episodic Memory for Lifelong Robot Deployment

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.11306v2
- Published: 2026-04-13
- Updated: 2026-05-05
- Authors: Leonard Bärmann, Joana Plewnia, Alex Waibel, Tamim Asfour
- Tags: episodic, long-term
- Categories: cs.RO, cs.AI
- URL: http://arxiv.org/abs/2604.11306v2

## One-Sentence Summary
Robots must verbalize their past experiences when users ask "Where did you put my keys?" or "Why did the task fail?" Yet maintaining life-long episodic memory (EM) from...

## Introduction
这篇论文被纳入仓库，是因为它和 `episodic, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Robots must verbalize their past experiences when users ask "Where did you put my keys?" or "Why did the task fail?" Yet maintaining life-long episodic memory (EM) from continuous multimodal perception quickly exceeds...

进一步看，论文的核心做法或实验重点可以概括为：We present H$^2$-EMV, a framework enabling humanoids to learn what to remember through user interaction.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：episodic, long-term
- 检索关键词命中：episodic memory
- 来源分类信息：cs.RO, cs.AI

## Abstract Snapshot
Robots must verbalize their past experiences when users ask "Where did you put my keys?" or "Why did the task fail?" Yet maintaining life-long episodic memory (EM) from continuous multimodal perception quickly exceeds storage limits and makes real-time query impractical, calling for selective forgetting that adapts to users' notions of relevance. We present H$^2$-EMV, a framework enabling humanoids to learn what to remember through user interaction. Our approach incrementally constructs hierarchical EM, selectively forgets using language-model-based relevance estimation conditioned on learned natural-language rules, and updates these rules given user feedback about forgotten details. Evaluations on simulated household tasks and 20.5-hour-long real-world recordings from ARMAR-7 demonstrate that H$^2$-EMV maintains question-answering accuracy while reducing memory size by 45% and query-time compute by 35%. Critically, performance improves over time - accuracy increases 70% in second-round queries by adapting to user-specific priorities - demonstrating that learned forgetting enables scalable, personalized EM for long-term human-robot collaboration.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
