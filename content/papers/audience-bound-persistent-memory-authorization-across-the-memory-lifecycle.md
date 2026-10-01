# Audience-Bound Persistent Memory: Authorization Across the Memory Lifecycle

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.36373v1
- Published: 2026-09-28
- Updated: 2026-09-28
- Authors: Sibo Liu
- Tags: agent, context, conversation, retrieval
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2609.36373v1

## One-Sentence Summary
A personal language agent that acts for its owner across private and shared conversations can learn a fact from one audience and later place it in the context it assembles for...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：A personal language agent that acts for its owner across private and shared conversations can learn a fact from one audience and later place it in the context it assembles for another.

进一步看，论文的核心做法或实验重点可以概括为：We study authorization before context across the whole memory lifecycle.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
A personal language agent that acts for its owner across private and shared conversations can learn a fact from one audience and later place it in the context it assembles for another. We study authorization before context across the whole memory lifecycle. Each memory item carries the audience present when it was recorded; derived items are partitioned by audience, receive the intersection of their sources' audiences, or are suppressed; an audience widens only by an explicit, object-specific grant; and an item enters a model attempt only when every current viewer belongs to one of its authorized audiences, with unresolved viewers failing closed to public-only. Under explicit identity, provenance and complete-mediation assumptions, this admission is sound and policy-complete on the exact assembled context, enforced by exclusion rather than by model behavior. We realize it in two independently persisted reference architectures, a flat store and a relationship graph, and, descriptively, in a native agent-memory runtime. In a prospectively frozen confirmation over 10,000 multi-party histories, no forbidden item entered any architecture's context, whereas unscoped retrieval exposed forbidden items in 82% of its contexts. Entitled recall matched policy-equivalent baselines exactly and exceeded unscoped retrieval by 0.30 Recall@5, with a Holm-confirmed advantage that grows with distractors. No architecture produced a wrong-principal substitution, but unscoped substitutions were too rare to establish the prespecified joint decision.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
