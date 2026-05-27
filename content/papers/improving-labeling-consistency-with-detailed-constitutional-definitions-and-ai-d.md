# Improving Labeling Consistency with Detailed Constitutional Definitions and AI-Driven Evaluation

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.24247v1
- Published: 2026-05-22
- Updated: 2026-05-22
- Authors: Konstantin Berlin, Adam Swanda
- Tags: conversation
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2605.24247v1

## One-Sentence Summary
Many automated labeling pipelines classify inputs into categories defined by a written specification, content moderation being a prominent use case.

## Introduction
这篇论文被纳入仓库，是因为它和 `conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Many automated labeling pipelines classify inputs into categories defined by a written specification, content moderation being a prominent use case.

进一步看，论文的核心做法或实验重点可以概括为：Simple category definitions are not detailed enough for labelers to produce the accurate, consistent golden labels these pipelines require.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：conversation
- 检索关键词命中：working memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Many automated labeling pipelines classify inputs into categories defined by a written specification, content moderation being a prominent use case. Simple category definitions are not detailed enough for labelers to produce the accurate, consistent golden labels these pipelines require. One solution is to write a prescriptive definition that settles enough real boundary cases that labelers cannot disagree with the written interpretation. In practice, definitions at that level of detail exceed what a human annotator can hold in working memory, so annotators fall back on intuition and the labels drift from the written rules, regressing on accuracy and consistency. We propose and demonstrate the efficacy of an AI-driven workflow in which AI helps write a per-category constitution that defines the label in enough detail to cover edge cases, and a frontier LLM interprets it on each input to produce the golden label more consistently and accurately than humans reading the same document. We evaluate on three content moderation categories (harassment, hate speech, non-violent crime) and show that the approach reduces cross-model inconsistency by up to 57x compared to paragraph definitions, with cross-model disagreement diagnosing specification gaps and the human responsible for high-level decisions about what each category should mean rather than individual labeling calls. For the safety evaluation, we introduce a dual-axis formulation scoring intent and content independently over the full conversation, so downstream consumers can act on either axis or both.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
