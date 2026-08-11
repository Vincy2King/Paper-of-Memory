# Mitigating Over-Personalization in LLMs via Structured Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.08300v1
- Published: 2026-08-08
- Updated: 2026-08-08
- Authors: Hakeem Hannoon, Andrew Zhao, Mihir Narayan, Sharvin Goyal, Ivaxi Sheth
- Tags: context, conversation, long-term
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2608.08300v1

## One-Sentence Summary
Conversational assistants increasingly rely on persistent long-term memory to personalize responses across sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Conversational assistants increasingly rely on persistent long-term memory to personalize responses across sessions.

进一步看，论文的核心做法或实验重点可以概括为：However, when stored user information is reintroduced into the model context, it can also influence responses in inappropriate or unrelated settings.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, conversation, long-term
- 检索关键词命中：long-term memory, memory augmented, memory-augmented
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Conversational assistants increasingly rely on persistent long-term memory to personalize responses across sessions. However, when stored user information is reintroduced into the model context, it can also influence responses in inappropriate or unrelated settings. We study two such failure modes in memory-augmented LLMs: cross-domain leakage, where memories from one life domain affect responses in another, and memory-induced sycophancy, where stored user beliefs make models more likely to agree with the user rather than respond truthfully. We apply a simple inference-time modification to how memories are presented to the model, without changing the model or the memory contents. Across seven models on PersistBench, we compare the commonly used all-in context format, where memories are injected as an unstructured list, with structured formats that partition memories by domain. This simple modification consistently reduces cross-domain leakage while preserving utility, with our strongest method reducing leakage by $8.8\%$ on average relative to the baseline.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
