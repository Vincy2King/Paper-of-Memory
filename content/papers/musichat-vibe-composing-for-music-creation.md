# MusiChat: Vibe Composing for Music Creation

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.24873v1
- Published: 2026-07-27
- Updated: 2026-07-27
- Authors: Callie C. Liao, Duoduo Liao, Ellie L. Zhang
- Tags: conversation
- Categories: cs.AI, cs.SD
- URL: http://arxiv.org/abs/2607.24873v1

## One-Sentence Summary
Recent advances in AI music generation have enabled users to create complete musical pieces from natural-language prompts.

## Introduction
这篇论文被纳入仓库，是因为它和 `conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recent advances in AI music generation have enabled users to create complete musical pieces from natural-language prompts.

进一步看，论文的核心做法或实验重点可以概括为：However, most existing systems follow a prompt-and-regenerate paradigm, making iterative refinement difficult because users must repeatedly recreate compositions instead of directly evolving existing musical ideas.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：conversation
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI, cs.SD

## Abstract Snapshot
Recent advances in AI music generation have enabled users to create complete musical pieces from natural-language prompts. However, most existing systems follow a prompt-and-regenerate paradigm, making iterative refinement difficult because users must repeatedly recreate compositions instead of directly evolving existing musical ideas. We present MusiChat, a conversational vibe composing system that enables collaborative human-AI music creation through natural-language interaction and iterative refinement. At the core of MusiChat is a hierarchical controllable music generation framework that separates lyric-aligned musical structure generation from expressive surface realization, allowing flexible stylistic transformations and structure-preserving edits. The system integrates a large language model with a hybrid symbolic music engine through a memory-augmented architecture that maintains the active composition state and user history across interactions. A hybrid intent-routing mechanism further enables efficient interpretation of both precise musical edits and open-ended creative requests. Rather than regenerating compositions from scratch, MusiChat incrementally transforms an evolving musical artifact while preserving relevant musical structure and user intent. We evaluate MusiChat through objective analysis and human studies, achieving 95.31% and 100% accuracy for single- and multi-turn interactions, respectively, and obtaining like-to-dislike ratios of 2:1 for melody naturalness and 3:1 for musical quality. Our results demonstrate that MusiChat supports coherent multi-turn music authoring and interactive human-AI co-creation through a conversational interface.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
