# EP-Mem: Elastic Privacy Memory for Social Relationship-Aware LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.35233v1
- Published: 2026-09-28
- Updated: 2026-09-28
- Authors: Fengzhou Sun, Yuan Zhang, Xintong Yu, Jinyao Yan
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.35233v1

## One-Sentence Summary
Large language model (LLM) agents face critical privacy risks when acting as delegates in human-agent-human communication.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents face critical privacy risks when acting as delegates in human-agent-human communication.

进一步看，论文的核心做法或实验重点可以概括为：To prevent such breaches, agents must understand users' social relationships and adhere to context-dependent social information disclosure boundaries.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language model (LLM) agents face critical privacy risks when acting as delegates in human-agent-human communication. To prevent such breaches, agents must understand users' social relationships and adhere to context-dependent social information disclosure boundaries. Current studies on agent memory privacy focus on instantaneous interactions, leaving the long-term relational disclosure problem unexplored. In this paper, we propose EP-Mem, an Elastic Privacy Memory architecture that reframes privacy as user-owned boundary control across social roles. EP-Mem introduces (1) token-level memory driven by user-configurable a privacy policy that stratifies persons and events, combining domain-level default circulation rules with fact-level whitelist/blacklist exceptions; and (2) a pluggable sidecar with a privacy engine that aligns disclosure controls with memory across summary, detail, and boundary granularities, enforced throughout generation, storage, and retrieval. We construct EP-Bench, to our knowledge the first long-term multi-party benchmark with cross-session correlated events for policy-conditioned relational disclosure. Experiments show that EP-Mem achieves 94.0% privacy classification accuracy, improves disclosure-permission judgment from 22% to 68%, and reduces privacy leakage by 75.6%, while maintaining retrieval performance and cross-benchmark generalization.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
