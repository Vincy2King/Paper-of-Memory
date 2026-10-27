# Agent Memory as Recommendation: Recommender-System Design for Long-Term Memory of LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.34673v1
- Published: 2026-10-26
- Updated: 2026-10-26
- Authors: Xinyu Zhang, Weiwei Sun
- Tags: agent, context, long-term
- Categories: cs.IR, cs.AI, cs.CL
- URL: http://arxiv.org/abs/2610.34673v1

## One-Sentence Summary
Large language model (LLM) agents that serve users across many sessions must choose, for every request, the few stored memories that enter a limited context window.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents that serve users across many sessions must choose, for every request, the few stored memories that enter a limited context window.

进一步看，论文的核心做法或实验重点可以概括为：This choice largely decides whether the agent answers correctly, and it runs on every request at Web scale.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.IR, cs.AI, cs.CL

## Abstract Snapshot
Large language model (LLM) agents that serve users across many sessions must choose, for every request, the few stored memories that enter a limited context window. This choice largely decides whether the agent answers correctly, and it runs on every request at Web scale. This selection faces three challenges: a large and growing store, a per-request cost budget, and multi-session questions that need all of their evidence. Many memory systems build notes or graphs with hundreds to thousands of LLM calls per history, and each is designed on its own, so it is unclear which component yields the accuracy. These challenges mirror the properties of recommendation, so we formalize agent memory as budgeted slate recommendation, with the request as the user, stored memories as items and the context window as a slate. The formalization places memory systems in one design space of recommender cascades and factorizes accuracy into the completeness that each stage controls. Guided by it, we propose AgentMemRec, which adapts candidate generation, learning to rank and slate construction from recommender systems and selects memories without any LLM call. On multi-session questions of LongMemEval, AgentMemRec outperforms memory and context-selection methods, including A-Mem, HippoRAG 2, DynamicRAG and T-Mem, by 10 to 31 points of accuracy. It matches an LLM reranker that makes 64 calls per query at 3.2 times lower serving cost, and on LoCoMo it outperforms Mem0 and Zep without any LLM call at write time. The factorization attributes the gains to slates that more often hold all of the evidence, so recommender-system design offers an effective and efficient foundation for the long-term memory of LLM agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
