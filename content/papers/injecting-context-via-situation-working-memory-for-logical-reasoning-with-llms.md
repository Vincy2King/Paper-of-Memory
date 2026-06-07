# Injecting Context via Situation Working Memory for Logical Reasoning with LLMs

- Source: OpenReview
- Venue: ACL ARR 2026 January Submission
- Paper ID: openreview:fADr5Hv8v0
- Published: 2026-03-20
- Updated: 2026-06-07
- Authors: Unknown
- Tags: context
- Categories: aclweb.org/ACL/ARR/2026/January/-/Submission
- URL: https://openreview.net/forum?id=fADr5Hv8v0

## One-Sentence Summary
Recent advances in large language models (LLMs) have improved logical reasoning by injecting formal logic or explicit structured representations.

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 January Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Recent advances in large language models (LLMs) have improved logical reasoning by injecting formal logic or explicit structured representations.

进一步看，论文的核心做法或实验重点可以概括为：However, such methods often lose track of \textit{what is true now} in multi-step reasoning, failing to maintain a coherent global state and its logical consequences.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 January Submission
- 高亮主题命中：context
- 检索关键词命中：working memory
- 来源分类信息：aclweb.org/ACL/ARR/2026/January/-/Submission

## Abstract Snapshot
Recent advances in large language models (LLMs) have improved logical reasoning by injecting formal logic or explicit structured representations. However, such methods often lose track of \textit{what is true now} in multi-step reasoning, failing to maintain a coherent global state and its logical consequences. Motivated by Situation Model Theory in cognitive psychology, which views comprehension as constructing and updating a mental model of events along key dimensions (time, space, causality, intention, protagonist), we propose Situation Working Memory (SituW), a cognitively inspired method for contextual reasoning in LLMs. SituW first builds a situation representation by decomposing text along these five dimensions, then guides LLM inference with this evolving state. Keeping an explicit, dynamically updated situation memory instead of a static logical form encourages globally consistent reasoning over the situation model rather than raw text. Evaluated in both supervised and unsupervised settings, SituW improves accuracy by 23.3%p and 15.93%p while reducing “uncertain” predictions, suggesting that explicit situation modeling supports more globally consistent LLM reasoning.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
