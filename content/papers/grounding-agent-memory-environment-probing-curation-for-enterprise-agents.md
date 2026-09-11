# Grounding Agent Memory: Environment-Probing Curation for Enterprise Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.11060v1
- Published: 2026-09-10
- Updated: 2026-09-10
- Authors: Susheel Suresh, Hazel Mak, Sahil Bhatnagar, Chhaya Methani, Alejandro Gutierrez Munoz
- Tags: agent, context
- Categories: cs.AI, cs.SE
- URL: http://arxiv.org/abs/2609.11060v1

## One-Sentence Summary
Persistent memory is entering production-oriented agent platforms to help long-horizon agents accumulate experience across sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent memory is entering production-oriented agent platforms to help long-horizon agents accumulate experience across sessions.

进一步看，论文的核心做法或实验重点可以概括为：Yet a post-task curator agent restricted to completed trajectories can preserve errors, overgeneralize partial evidence, or retain stale knowledge.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：agent memory, persistent memory, retrieval memory
- 来源分类信息：cs.AI, cs.SE

## Abstract Snapshot
Persistent memory is entering production-oriented agent platforms to help long-horizon agents accumulate experience across sessions. Yet a post-task curator agent restricted to completed trajectories can preserve errors, overgeneralize partial evidence, or retain stale knowledge. We introduce environment-probing curation, a deployment-compatible extension that gives an existing asynchronous curator agent least-privilege, read-only world tools to check, scope, and refresh candidate memories. It requires no model retraining and leaves the task agent, retriever, memory representation, and production write authority unchanged. In a production-like GitHub Copilot (GHCP) harness built on its SDK, we compare stateless execution, full in-context learning, GHCP + Mem, and GHCP + Mem (w/ Env Probing) on CLBench database exploration and 90 adapted APEX management-consulting tasks. On CLBench, probing raises pass rate from 39% to 73% and pass-discounted reward from 8.60 to 22.60 while reducing queries from 8.8 to 4.7 per question and task-agent cost from \$3.38 to \$1.68. Across six APEX worlds, all 18 memory-versus-baseline mean reward comparisons are positive and task-agent tool calls fall by 16--75%; probing gives the best task-agent reward gain per dollar in five worlds. Probing also attains higher mean reward than GHCP + Mem on both Sonnet 4.6 and Opus 4.7 without schema drift. Environment probing therefore turns existing agent-memory curation into an environment-informed, auditable process while preserving a compact task-time interface.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
