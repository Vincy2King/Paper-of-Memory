# Beyond the Final Prompt: Measuring the Effect of Within-Conversation Context on AI Answers

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.02556v1
- Published: 2026-08-03
- Updated: 2026-08-03
- Authors: Benjamin Tannenbaum
- Tags: compression, context, conversation
- Categories: cs.IR
- URL: http://arxiv.org/abs/2608.02556v1

## One-Sentence Summary
An isolated final user message is often treated as the query in evaluations of AI systems.

## Introduction
这篇论文被纳入仓库，是因为它和 `compression, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：An isolated final user message is often treated as the query in evaluations of AI systems.

进一步看，论文的核心做法或实验重点可以概括为：In a conversation, however, the actionable request may be distributed across preceding turns.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression, context, conversation
- 检索关键词命中：persistent memory
- 来源分类信息：cs.IR

## Abstract Snapshot
An isolated final user message is often treated as the query in evaluations of AI systems. In a conversation, however, the actionable request may be distributed across preceding turns. We directly test whether that omitted within-conversation context changes answers. For each of 180 English multi-turn conversations sampled from a governed commercial corpus and the public PRISM dataset, we hold the final user message and requested answer model constant while generating three answers: one from the full role-labelled conversation, one from the final message alone, and one from the final message plus a prefix-only reconstruction capped at 160 words. A separately requested judge model evaluates answers under randomized labels. The prespecified primary endpoint is a material difference that could change what the user does, rather than a difference in style or detail. After inverse-probability weighting to the eligible cohorts, the full-conversation and isolated-final answers differ materially in 44.7% of cases (95% bootstrap CI 33.8% to 56.1%). Full-conversation answers score 0.49 points higher on a 0 to 4 request-satisfaction scale (0.32 to 0.67). Adding the compressed prefix reduces the material-difference rate to 30.8% (20.2% to 42.1%), a 13.9-point reduction (4.9% to 24.1%), and reduces the mean satisfaction gap to 0.01 points (-0.12 to 0.13). Yet compression is not equivalent to the complete dialogue context: almost one third of answers remain materially different. An order-swapped repeat on 48 cases yields 91.7% agreement and kappa = 0.83 for the primary decision. The study concerns preceding turns in the same conversation and does not test persistent memory across separate conversations.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
