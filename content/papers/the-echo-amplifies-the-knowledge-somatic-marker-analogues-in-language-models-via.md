# The Echo Amplifies the Knowledge: Somatic Marker Analogues in Language Models via Emotion Vector Re-Injection

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.08611v1
- Published: 2026-05-09
- Updated: 2026-05-09
- Authors: Jared Glover
- Tags: context, episodic
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.08611v1

## One-Sentence Summary
Current language model memory systems store what happened but not how it felt.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Current language model memory systems store what happened but not how it felt.

进一步看，论文的核心做法或实验重点可以概括为：This distinction -- between semantic memory (knowing about a past event) and episodic memory (re-experiencing it) -- was identified by Tulving as the difference between noetic and autonoetic consciousness.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Current language model memory systems store what happened but not how it felt. This distinction -- between semantic memory (knowing about a past event) and episodic memory (re-experiencing it) -- was identified by Tulving as the difference between noetic and autonoetic consciousness. Damasio demonstrated that humans with intact knowledge but absent emotional markers exhibit impaired decision-making. We bridge this gap for language models. Using Gemma 3 1B-IT with pretrained Gemma Scope 2 sparse autoencoders, we identify 310 emotion-exclusive features at layer 22 with psychologically valid geometry. We construct distinctive-feature emotion vectors during experience and partially re-inject them during recall, triggered by context similarity at layer 7. We test four conditions paralleling Damasio's framework: A (no memory), B (semantic labels), C (emotion echo), and BC (semantic + echo). For emotional orientation, the echo alone steepens the threat-safety gradient: the regression slope of threat rating on contextual similarity is 0.80 for C vs 0.56 for A ($p$=0.011, permutation test). For decisions, the echo amplifies knowledge into action: BC=80% good choices vs B=52% ($z$=+2.60, $p$<0.01), while the echo alone has no effect (C=22%, n.s.). The echo changes how the model feels independently, but changes what it does only when combined with knowledge -- replicating Damasio's core finding. The echo amplifies knowledge. It does not replace it.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
