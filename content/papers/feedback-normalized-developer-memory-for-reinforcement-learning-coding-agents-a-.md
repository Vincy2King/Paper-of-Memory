# Feedback-Normalized Developer Memory for Reinforcement-Learning Coding Agents: A Safety-Gated MCP Architecture

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.01567v1
- Published: 2026-05-02
- Updated: 2026-05-02
- Authors: Mehmet Iscan
- Tags: agent, benchmark, context, retrieval
- Categories: cs.SE, cs.CL, cs.LG
- URL: http://arxiv.org/abs/2605.01567v1

## One-Sentence Summary
Large language model (LLM) coding agents increasingly operate over repositories, terminals, tests, and execution traces across long software-engineering episodes.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) coding agents increasingly operate over repositories, terminals, tests, and execution traces across long software-engineering episodes.

进一步看，论文的核心做法或实验重点可以概括为：Persistent memory is useful, but static vector stores or generic retrieval-augmented generation (RAG) are insufficient for reinforcement-learning (RL) code development, where small details can alter Bellman targets,...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.SE, cs.CL, cs.LG

## Abstract Snapshot
Large language model (LLM) coding agents increasingly operate over repositories, terminals, tests, and execution traces across long software-engineering episodes. Persistent memory is useful, but static vector stores or generic retrieval-augmented generation (RAG) are insufficient for reinforcement-learning (RL) code development, where small details can alter Bellman targets, terminal masks, gradient flow, or validation claims. This paper presents RL Developer Memory, a local-first, Model Context Protocol (MCP)-native developer-memory architecture for RL coding agents. It treats memory selection as a logged contextual decision process: issue_match ranks candidates and records telemetry, issue_feedback maps raw labels to bounded rewards, and issue_record_resolution links verified resolutions to earlier retrieval events. A deterministic ranker remains deployed, while a contextual-bandit residual policy runs in shadow mode and can affect canary behavior only through conservative off-policy-evaluation (OPE) gates. RL/control memories require theory-to-code metadata and review-gated governance. The system is evaluated on a deterministic 200-case benchmark with RL algorithm bugs, hard negatives, review-gated RL/control cases, and low-risk failures. In the same-commit comparison, deterministic control and full shadow/OPE both achieve 80.0% expected-decision accuracy and 100.0% hard-negative suppression; the full configuration adds learning telemetry rather than accuracy gain. Static validation passed 11/11 checks; dynamic integration passed 10/10 cases. The evidence reports limits: active learned-policy deployment and official-client MCP interoperability are unsupported, live full-configuration latency regresses, and 40 residual non-RL failures remain. The contribution is an auditable memory-control architecture with explicit claim boundaries, not a universal coding-agent improvement claim.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
