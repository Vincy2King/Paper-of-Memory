# Shared Selective Persistent Memory for Agentic LLM Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.09493v1
- Published: 2026-07-10
- Updated: 2026-07-10
- Authors: Sanjana Pedada, Aditya Dhavala, Neelraj Patil
- Tags: agent, context, conversation
- Categories: cs.AI, cs.MA, cs.SE
- URL: http://arxiv.org/abs/2607.09493v1

## One-Sentence Summary
Agentic LLM systems that generate code through multi-turn tool use face a fundamental context problem: each session starts from zero, discarding the configuration choices,...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agentic LLM systems that generate code through multi-turn tool use face a fundamental context problem: each session starts from zero, discarding the configuration choices, domain constraints, data schemas, and tool-...

进一步看，论文的核心做法或实验重点可以概括为：Naively persisting entire conversation histories is token-inefficient and counterproductive: irrelevant context degrades generation quality.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI, cs.MA, cs.SE

## Abstract Snapshot
Agentic LLM systems that generate code through multi-turn tool use face a fundamental context problem: each session starts from zero, discarding the configuration choices, domain constraints, data schemas, and tool-use patterns that made previous sessions productive. Naively persisting entire conversation histories is token-inefficient and counterproductive: irrelevant context degrades generation quality. We introduce shared selective persistent memory, an architecture that identifies and retains four categories of reusable context (task specifications, data schemas, tool configurations, and output constraints) while discarding session-specific reasoning traces. Crucially, this memory is shared: workspaces encapsulating selective memory can be transferred across users with role-based access control, enabling collaborative reuse without redundant specification. We implement it in a deployed collaborative workspace platform where LLM agents produce, edit, and maintain git-versioned artifacts (dashboards, reports, and data-driven documents) from heterogeneous sources (CSV, SQL, REST APIs, and MCP servers). A complementary zero-token data refresh mechanism decouples generated programs from runtime data, enabling artifact reuse without re-invocation. Across three enterprise scenarios, shared selective persistent memory achieves 96% task completion (vs. 79% without memory and 71% with full history). Zero-token refresh eliminates LLM re-invocation for recurring updates (14x task-time reduction), while summary-driven generation cuts per-invocation token cost by 97x versus raw data injection. A replication on four public datasets confirms generalizability, with zero-token refresh succeeding in 12/12 trials. Notably, naive full-history persistence actively degrades completion by biasing the agent with stale traces, while selective memory outperforms both extremes.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
