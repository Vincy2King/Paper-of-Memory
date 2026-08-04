# Shared Organizational Memory for Enterprise Coding Agents: System Design and Deployment Snapshot

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.00122v1
- Published: 2026-07-31
- Updated: 2026-07-31
- Authors: Harsh Rao Dhanyamraju, Leonidas Raghav
- Tags: agent, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.00122v1

## One-Sentence Summary
Enterprise coding agents rely on tools and retrieval, yet enterprise knowledge often remains outside public training data and formal documentation: internal DSLs, proprietary...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Enterprise coding agents rely on tools and retrieval, yet enterprise knowledge often remains outside public training data and formal documentation: internal DSLs, proprietary platforms, local conventions, recent...

进一步看，论文的核心做法或实验重点可以概括为：Existing knowledge interfaces expose stored resources but still depend on agents recognizing and explicitly recording lessons worth reusing, disconnecting capture from the coding workflow and leaving development...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Enterprise coding agents rely on tools and retrieval, yet enterprise knowledge often remains outside public training data and formal documentation: internal DSLs, proprietary platforms, local conventions, recent fixes, and tacit workflows. Existing knowledge interfaces expose stored resources but still depend on agents recognizing and explicitly recording lessons worth reusing, disconnecting capture from the coding workflow and leaving development experience repeatedly rediscovered. We report an ongoing production deployment of a shared organizational memory system that makes capture a platform-level part of coding work: it collects task-adjacent experience with contributor approval, curates it into reusable question-answer memories, gates obvious security and privacy risks, and retrieves memories for future agents. This short paper describes the deployed lifecycle and an operational snapshot. Effects on retrieval and coding tasks remain under evaluation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
