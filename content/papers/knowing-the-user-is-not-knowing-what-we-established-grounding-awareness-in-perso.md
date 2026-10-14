# Knowing the User Is Not Knowing What We Established: Grounding Awareness in Personal Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.18684v1
- Published: 2026-10-13
- Updated: 2026-10-13
- Authors: Jiajun Chen, Xinyue Chen, Yicheng Jiang, Hua Shen
- Tags: agent, benchmark, retrieval
- Categories: cs.AI, cs.HC, cs.LG
- URL: http://arxiv.org/abs/2610.18684v1

## One-Sentence Summary
Personal-agent memory has largely focused on learning what users know, prefer, and want.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Personal-agent memory has largely focused on learning what users know, prefer, and want.

进一步看，论文的核心做法或实验重点可以概括为：However, knowing the user does not necessarily mean knowing what the user and the agent have established together.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：agent memory, persistent memory
- 来源分类信息：cs.AI, cs.HC, cs.LG

## Abstract Snapshot
Personal-agent memory has largely focused on learning what users know, prefer, and want. However, knowing the user does not necessarily mean knowing what the user and the agent have established together. An assistant's proposal should not become an authorized instruction merely because it is remembered. We introduce Grounding Awareness, the ability to distinguish accepted, unacknowledged, revised, and scoped arrangements when selecting actions. We develop a controlled benchmark to test whether agents can tell the difference between proposals users have accepted and those they have not, and whether they apply accepted arrangements only where appropriate. Across multiple agents and memory systems, we find that strong memory performance does not ensure Grounding Awareness. More surprisingly, providing more complete user information can increase execution of unacknowledged proposals, while persistent memory can cause agents to treat these proposals as if they were user instructions. We trace these failures through memory writing, retrieval, and action selection. Finally, we introduce Grounding Layer, a lightweight, training-free extension that explicitly tracks grounding status and checks consequential actions, substantially improving agent behavior without modifying models or memory systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
