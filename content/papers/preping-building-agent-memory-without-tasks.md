# PREPING: Building Agent Memory without Tasks

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.13880v1
- Published: 2026-05-11
- Updated: 2026-05-11
- Authors: Yumin Choi, Sangwoo Park, Minki Kang, Jinheon Baek, Sung Ju Hwang
- Tags: agent
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2605.13880v1

## One-Sentence Summary
Agent memory is typically constructed either offline from curated demonstrations or online from post-deployment interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agent memory is typically constructed either offline from curated demonstrations or online from post-deployment interactions.

进一步看，论文的核心做法或实验重点可以概括为：However, regardless of how it is built, an agent faces a cold-start gap when first introduced to a new environment without any task-specific experience available.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Agent memory is typically constructed either offline from curated demonstrations or online from post-deployment interactions. However, regardless of how it is built, an agent faces a cold-start gap when first introduced to a new environment without any task-specific experience available. In this paper, we study pre-task memory construction: whether an agent can build procedural memory before observing any target-environment tasks, using only self-generated synthetic practice. Yet, synthetic interaction alone is insufficient, as without controlling what to practice and what to store, synthetic tasks become redundant, infeasible, and ultimately uninformative, and memory further degrades quickly due to unfiltered trajectories. To overcome this, we present Preping, a proposer-guided memory construction framework. At its core is proposer memory, a structured control state that shapes future practice. A Proposer generates synthetic tasks conditioned on this state, a Solver executes them, and a Validator determines which trajectories are eligible for memory insertion while also providing feedback to guide future proposals. Experiments on AppWorld, BFCL v3, and MCP-Universe show that Preping substantially improves over a no-memory baseline and achieves performance competitive with strong playbook-based methods built from offline or online experience, with deployment cost $2.99\times$ lower on AppWorld and $2.23\times$ lower on BFCL v3 than online memory construction. Further analyses reveal that the main benefit does not come from synthetic volume alone, but from proposer-side control over feasibility, redundancy, and coverage, combined with selective memory updates.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
