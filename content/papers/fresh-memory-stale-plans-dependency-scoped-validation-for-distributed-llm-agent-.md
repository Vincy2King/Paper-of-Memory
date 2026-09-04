# Fresh Memory, Stale Plans: Dependency-Scoped Validation for Distributed LLM-Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.03340v1
- Published: 2026-09-03
- Updated: 2026-09-03
- Authors: Evan Chen, Shiqiang Wang, Christopher G. Brinton
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.03340v1

## One-Sentence Summary
Distributed LLM-agent teams can read the latest shared facts and still act on an obsolete plan.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Distributed LLM-agent teams can read the latest shared facts and still act on an obsolete plan.

进一步看，论文的核心做法或实验重点可以概括为：A planner may derive an action from requirement $r_3$, another agent may commit $r_4$, and an executor may receive $r_4$ without replacing the plan derived from $r_3$.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Distributed LLM-agent teams can read the latest shared facts and still act on an obsolete plan. A planner may derive an action from requirement $r_3$, another agent may commit $r_4$, and an executor may receive $r_4$ without replacing the plan derived from $r_3$. We call this \emph{stale-plan execution}: state freshness does not establish that the plan authorizing an action remains valid. We introduce PlanFence, a dependency-scoped action-validation protocol. Plans cite the exact public records they used, and an executor validates only the records that can affect the pending external action, replanning once or blocking when validation is incomplete. In 30 controlled live workflows with a post-plan revision, a freshness-only executor acts on the obsolete plan in every task, whereas PlanFence completes all tasks without an invalid action. Controlled replay reveals two conditional boundaries: proactive synchronization yields lower coordination stall at low churn, while PlanFence avoids repeated update-path coordination as churn grows and avoids validating unrelated state as the shared keyspace grows. These are controlled safety and systems-cost results, not general task-accuracy gains.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
