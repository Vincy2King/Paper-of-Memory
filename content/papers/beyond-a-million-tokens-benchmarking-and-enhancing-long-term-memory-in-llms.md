# Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs

- Source: OpenReview
- Venue: ICLR 2026 Poster
- Paper ID: openreview:y59hf5lrMn
- Published: 2026-01-26
- Updated: 2026-04-11
- Authors: Mohammad Tavakoli, Alireza Salemi, Carrie Ye, Mohamed Abdalla, Hamed Zamani, J Ross Mitchell
- Tags: benchmark, context, conversation, episodic, long-term, retrieval
- Categories: ICLR.cc/2026/Conference/-/Submission
- URL: https://openreview.net/forum?id=y59hf5lrMn

## One-Sentence Summary
Evaluating the abilities of large language models (LLMs) for tasks that require long-term memory and thus long-context reasoning, for example in conversational settings, is...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, conversation, episodic` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ICLR 2026 Poster` 这个 venue 相关。

从摘要来看，作者主要关注的是：Evaluating the abilities of large language models (LLMs) for tasks that require long-term memory and thus long-context reasoning, for example in conversational settings, is hampered by the existing benchmarks, which...

进一步看，论文的核心做法或实验重点可以概括为：This paper introduces a comprehensive solution to these challenges.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ICLR 2026 Poster
- 高亮主题命中：benchmark, context, conversation, episodic, long-term, retrieval
- 检索关键词命中：episodic memory, long-term memory, working memory
- 来源分类信息：ICLR.cc/2026/Conference/-/Submission

## Abstract Snapshot
Evaluating the abilities of large language models (LLMs) for tasks that require long-term memory and thus long-context reasoning, for example in conversational settings, is hampered by the existing benchmarks, which often lack narrative coherence, cover narrow domains, and only test simple recall-oriented tasks. This paper introduces a comprehensive solution to these challenges. First, we present a novel framework for automatically generating long (up to 10M tokens), coherent, and topically diverse conversations, accompanied by probing questions targeting a wide range of memory abilities. From this, we construct BEAM, a new benchmark comprising 100 conversations and 2,000 validated questions. Second, to enhance model performance, we propose LIGHT–a framework inspired by human cognition that equips LLMs with three complementary memory systems: a long-term episodic memory, a short-term working memory, and a scratchpad for accumulating salient facts. Our experiments on BEAM reveal that even LLMs with 1M token context windows (with and without retrieval-augmentation) struggle as dialogues lengthen. In contrast, LIGHT consistently improves performance across various models, achieving an average improvement of 3.5%–12.69% over the strongest baselines, depending on the backbone LLM. An ablation study further confirms the contribution of each memory component.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
