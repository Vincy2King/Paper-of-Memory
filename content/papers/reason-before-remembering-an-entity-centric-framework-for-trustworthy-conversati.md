# Reason Before Remembering: An Entity-Centric Framework for Trustworthy Conversational Memory

- Source: OpenReview
- Venue: ACL ARR 2026 August Submission
- Paper ID: openreview:oobq0Zs3mc
- Published: 2026-08-04
- Updated: 2026-08-29
- Authors: Unknown
- Tags: context, conversation, retrieval
- Categories: aclweb.org/ACL/ARR/2026/August/-/Submission
- URL: https://openreview.net/forum?id=oobq0Zs3mc

## One-Sentence Summary
Conversational memory in AI systems becomes crucial for coherent interactions through prolonged conversations.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, conversation, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 August Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Conversational memory in AI systems becomes crucial for coherent interactions through prolonged conversations.

进一步看，论文的核心做法或实验重点可以概括为：State-of-the-art techniques mainly aim at improving memory by context expansion, using retrieval, or external memory.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 August Submission
- 高亮主题命中：context, conversation, retrieval
- 检索关键词命中：conversational memory
- 来源分类信息：aclweb.org/ACL/ARR/2026/August/-/Submission

## Abstract Snapshot
Conversational memory in AI systems becomes crucial for coherent interactions through prolonged conversations. State-of-the-art techniques mainly aim at improving memory by context expansion, using retrieval, or external memory. However, most methods assume that any entity mention should be immediately mapped to one interpretation. This often leads to premature commitments, memory confirmation bias, hallucinations in the conversation, and accumulation of wrong conversational state. This paper states that conversational memory should not hide ambiguity, but should represent it explicitly as part of the reasoning process. This paper proposes an Entity-Centric Conversational Memory Framework that views entity linking as a process of explicit belief management, instead of a deterministic one. It maintains the space of interpretations of entities that includes both correct and incorrect hypotheses, such as $\mathrm{UNKNOWN}$ hypothesis, processes heterogeneous conversational evidence via belief update, detects ambiguity, and performs one of three actions: Commit, Clarify, or Delay. By doing so, the framework separates entity reasoning from memory updates, allowing to write to memory only when certain. The experiments conducted on ConEL conversational entity linking dataset show that the proposed framework reaches $99.0\%$ commit precision providing explicit control over the precision-coverage trade-off. The analysis shows several properties of conversational memory and brings important architectural insights to light: the existence of memory confirmation bias, the importance of treating $\mathrm{UNKNOWN}$ as an active competing hypothesis, and the limitations of fixed ambiguity thresholds on different entity types.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
