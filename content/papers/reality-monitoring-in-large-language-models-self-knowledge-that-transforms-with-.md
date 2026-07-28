# Reality Monitoring in Large Language Models: Self-Knowledge That Transforms with Conversation Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.23927v1
- Published: 2026-07-27
- Updated: 2026-07-27
- Authors: Saurabh Ranjan, Konstantina Sokratous, Brian Odegaard
- Tags: benchmark, conversation, episodic
- Categories: cs.AI, cs.CL, cs.CY, q-bio.NC
- URL: http://arxiv.org/abs/2607.23927v1

## One-Sentence Summary
A conversational AI that cannot tell its own output from what a user said will treat its own mistakes as user-provided facts.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, conversation, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：A conversational AI that cannot tell its own output from what a user said will treat its own mistakes as user-provided facts.

进一步看，论文的核心做法或实验重点可以概括为：In humans, this capacity is called reality monitoring, and its failures are linked to hallucinations, delusions, and confabulation, yet whether LLMs possess it remains untested.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, conversation, episodic
- 检索关键词命中：conversational memory
- 来源分类信息：cs.AI, cs.CL, cs.CY, q-bio.NC

## Abstract Snapshot
A conversational AI that cannot tell its own output from what a user said will treat its own mistakes as user-provided facts. In humans, this capacity is called reality monitoring, and its failures are linked to hallucinations, delusions, and confabulation, yet whether LLMs possess it remains untested. Here we show, across two experiments and six LLMs, that source attribution depends on how conversational memory is structured: ceiling accuracy for self-generated content under minimal memory demands reverses to a fragile external-item advantage once episodic delay removes that shortcut. Feedback exposes two failures: in some models, internal and external judgments swap; in others, accuracy improves while confidence decouples from correctness, dissociations invisible to existing benchmarks. Across models, this pattern implicates active, not aggregate, parameter count. This suggests that as AI systems take on autonomous, multi-turn roles, evaluating what they know is not enough: tracking where that knowledge came from may matter equally.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
