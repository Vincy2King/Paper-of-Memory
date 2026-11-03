# EvoRec: A Unified Self-Evolving Agentic Recommender with Dynamic Reflection Trees

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.01977v1
- Published: 2026-11-01
- Updated: 2026-11-01
- Authors: Mengting Li, Long Zhang, Hao Jiang, Sheng Yu, Fei Pan, Peng Jiang
- Tags: agent, long-term, retrieval
- Categories: cs.IR
- URL: http://arxiv.org/abs/2611.01977v1

## One-Sentence Summary
Conventional recommender systems rely on fixed cascaded pipelines, limiting their ability to adapt to evolving user needs and feedback.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Conventional recommender systems rely on fixed cascaded pipelines, limiting their ability to adapt to evolving user needs and feedback.

进一步看，论文的核心做法或实验重点可以概括为：Existing agentic recommenders introduce reasoning and tool use but often lack end-to-end decision control and systematic failure reflection.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：working memory
- 来源分类信息：cs.IR

## Abstract Snapshot
Conventional recommender systems rely on fixed cascaded pipelines, limiting their ability to adapt to evolving user needs and feedback. Existing agentic recommenders introduce reasoning and tool use but often lack end-to-end decision control and systematic failure reflection. We propose EvoRec, a unified agentic recommendation framework that combines autonomous decision-making with reflection-driven self-evolution. A Need Agent infers user needs from long-term, short-term, and working memory. A Planning Agent adaptively allocates retrieval budgets between Behavior Continuation and Need Satisfaction, selects retrieval tools, and sets ranking-fusion weights. An Acting Executor executes the plan and records decision traces. Following user feedback, a Dynamic Reflection Tree identifies failures in need inference, planning, or previous repairs, proposes personalized corrections, and validates them through replay. Verified repairs update working memory and are distilled into reusable cross-user strategies, enabling continual improvement without parameter updates. Experiments on a Kuaishou local-services advertising dataset show a 15.7% Hit@50 improvement over the strongest baseline. Hierarchical reflection further improves Hit@50 by 13.1% among users with prior repairs. In a seven-day online A/B test, nearline EvoRec increases advertising revenue by 4.6% and CTCVR by 3.5%, with a 14.5% revenue gain for high-intent users. These results demonstrate the effectiveness of reflection-driven self-evolution in industrial-scale recommendation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
