# Learning When to Remember: Risk-Sensitive Contextual Bandits for Abstention-Aware Memory Retrieval in LLM-Based Coding Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.27283v1
- Published: 2026-04-30
- Updated: 2026-04-30
- Authors: Mehmet Iscan
- Tags: agent, context, retrieval
- Categories: cs.CL, cs.AI, cs.LG
- URL: http://arxiv.org/abs/2604.27283v1

## One-Sentence Summary
Large language model (LLM)-based coding agents increasingly rely on external memory to reuse prior debugging experience, repair traces, and repository-local operational knowledge.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM)-based coding agents increasingly rely on external memory to reuse prior debugging experience, repair traces, and repository-local operational knowledge.

进一步看，论文的核心做法或实验重点可以概括为：However, retrieved memory is useful only when the current failure is genuinely compatible with a previous one; superficial similarity in stack traces, terminal errors, paths, or configuration symptoms can lead to...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：agent memory, memory retrieval, retrieval memory
- 来源分类信息：cs.CL, cs.AI, cs.LG

## Abstract Snapshot
Large language model (LLM)-based coding agents increasingly rely on external memory to reuse prior debugging experience, repair traces, and repository-local operational knowledge. However, retrieved memory is useful only when the current failure is genuinely compatible with a previous one; superficial similarity in stack traces, terminal errors, paths, or configuration symptoms can lead to unsafe memory injection. This paper reframes issue-memory use as a selective, risk-sensitive control problem rather than a pure top-k retrieval problem. We introduce RSCB-MC, a risk-sensitive contextual bandit memory controller that decides whether an agent should use no memory, inject the top resolution, summarize multiple candidates, perform high-precision or high-recall retrieval, abstain, or ask for feedback. The system stores reusable issue knowledge through a pattern-variant-episode schema and converts retrieval evidence into a fixed 16-feature contextual state capturing relevance, uncertainty, structural compatibility, feedback history, false-positive risk, latency, and token cost. Its reward design penalizes false-positive memory injection more strongly than missed reuse, making non-injection and abstention first-class safety actions. In deterministic smoke-scale artifacts, RSCB-MC obtains the strongest non-oracle offline replay success rate, 62.5%, while maintaining a 0.0% false-positive rate. In a bounded 200-case hot-path validation, it reaches 60.5% proxy success with 0.0% false positives and a 331.466 microseconds p95 decision latency. The results show that, for coding-agent memory, the key question is not only which memory is most similar, but whether any retrieved memory is safe enough to influence the debugging trajectory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
