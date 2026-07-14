# The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.10608v1
- Published: 2026-07-12
- Updated: 2026-07-12
- Authors: Yixiong Chen, Xinyi Bai, Alan Yuille
- Tags: agent, benchmark, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.10608v1

## One-Sentence Summary
Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments.

进一步看，论文的核心做法或实验重点可以概括为：Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：memory augmented, memory-augmented, retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determines not only what memories should be retrieved, but also what models and control policies are needed to use them safely. To diagnose this process, we propose Entry--Propagation--Recovery (E-P-R), a trajectory-level framework that asks where memory first changes an action, whether that change carries forward, and whether the agent can recover after leaving a correct path. We instantiate E-P-R on WebArena and on MemTrapBench, a controlled benchmark we build to isolate these phases. We find that the main failure often begins at entry: agents adopt conflicting memory at the first exposed decision point even when it is task-wrong. Repeated exposure then amplifies this early error, while recovery after divergence is weak. Together, these effects create a compliance trap: across models, conflicting memory induces similar compliance rates, but once agents comply, their success rates collapse to a low floor. Stronger agents therefore suffer larger absolute damage because each compliance event erases more baseline capability. These results suggest that memory-augmented agents should be evaluated not only by retrieval quality or final success rate, but by how they consume memory throughout the trajectory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
