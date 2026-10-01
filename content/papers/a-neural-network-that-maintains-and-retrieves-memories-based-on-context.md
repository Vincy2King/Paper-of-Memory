# A neural network that maintains and retrieves memories based on context

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.37791v1
- Published: 2026-09-29
- Updated: 2026-09-29
- Authors: Hayoung Song, JeongJun Park, Qihong Lu, Giacomo Vedovati, Monica D. Rosenberg, Zachariah M. Reagh, ShiNung Ching
- Tags: context, episodic, long-term, retrieval
- Categories: cs.AI, cs.NE
- URL: http://arxiv.org/abs/2609.37791v1

## One-Sentence Summary
Every day, people continuously infer situational context and adjust the way they understand and remember the world.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, episodic, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Every day, people continuously infer situational context and adjust the way they understand and remember the world.

进一步看，论文的核心做法或实验重点可以概括为：Context, signaled by the prefrontal cortex, is known to modulate working memory and episodic memory, but the algorithmic understanding of this modulation remains limited.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, episodic, long-term, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.AI, cs.NE

## Abstract Snapshot
Every day, people continuously infer situational context and adjust the way they understand and remember the world. Context, signaled by the prefrontal cortex, is known to modulate working memory and episodic memory, but the algorithmic understanding of this modulation remains limited. Here, we train a recurrent neural network (RNN), augmented with an episodic memory buffer, to infer context using Bayesian inference as it continuously makes predictions of upcoming scenes while watching naturalistic movies. When the inferred context modulates the RNN's recurrent connectivity (the basis of working memory) in a low-rank manner, the model's activity patterns best match neural responses in human participants who watched the same movies during fMRI. Context also modulates episodic memory retrieval, such that the model retrieves memories based on not only content similarity but also context similarity. This is implemented as a key-value system with self-attention, designed to additionally encode context and retrieve context-congruent memories. The resulting model not only better resembles human brain representations but also learns to retrieve memories like humans much faster than a model without context modulation. Together, our findings suggest a computational mechanism by which context modulates information maintenance and long-term memory retrieval in naturalistic environments.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
