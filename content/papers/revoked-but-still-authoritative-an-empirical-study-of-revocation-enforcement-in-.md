# Revoked but Still Authoritative: An Empirical Study of Revocation Enforcement in Agent-Memory Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.08258v1
- Published: 2026-09-08
- Updated: 2026-09-08
- Authors: Yi Ting Shen, Kentaroh Toyoda, Alex Leung
- Tags: agent, retrieval
- Categories: cs.AI, cs.CR
- URL: http://arxiv.org/abs/2609.08258v1

## One-Sentence Summary
Long-running language-model agents depend on persistent memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-running language-model agents depend on persistent memory.

进一步看，论文的核心做法或实验重点可以概括为：Many agent-memory systems preserve history through soft revocation: a contradicted fact is marked invalid and retained rather than deleted.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory, persistent memory
- 来源分类信息：cs.AI, cs.CR

## Abstract Snapshot
Long-running language-model agents depend on persistent memory. Many agent-memory systems preserve history through soft revocation: a contradicted fact is marked invalid and retained rather than deleted. However, whether that mark is enforced at retrieval time is unexamined. In this paper, we measure five such systems: we load each with a revoked policy and its replacement, track whether the revoked fact is returned at retrieval and whether the agent then acts on it across nine policy scenarios and nine models, and score every trial under six defense conditions. We find that no system enforces revocation by default: the revoked fact is returned wherever the revocation label is visible to the retrieval layer, outranks its replacement, and leads agents to the unsafe action. Based on these findings, we develop a guard that sits between the agent and any memory backend and withholds records that are revoked or conflict with their replacement.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
