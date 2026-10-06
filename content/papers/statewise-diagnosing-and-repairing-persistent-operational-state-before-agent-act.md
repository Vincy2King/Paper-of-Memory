# StateWise: Diagnosing and Repairing Persistent Operational State Before Agent Actions

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.05241v1
- Published: 2026-10-04
- Updated: 2026-10-04
- Authors: Yongyuan Peng, Zhou Feng, Tongying Wu, Jiahao Chen, Yuan Su, Chunyi Zhou, Tianyu Du, Shouling Ji
- Tags: agent
- Categories: cs.SE, cs.AI
- URL: http://arxiv.org/abs/2610.05241v1

## One-Sentence Summary
LLM agents combine reasoning, tool use, and persistent memory to support work across tasks by reusing stored operational records as premises for later actions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM agents combine reasoning, tool use, and persistent memory to support work across tasks by reusing stored operational records as premises for later actions.

进一步看，论文的核心做法或实验重点可以概括为：However, environmental or requirement changes can invalidate these records, while existing action review, provenance tracking, and clarification mechanisms may leave the underlying persistent state uncorrected.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.SE, cs.AI

## Abstract Snapshot
LLM agents combine reasoning, tool use, and persistent memory to support work across tasks by reusing stored operational records as premises for later actions. However, environmental or requirement changes can invalidate these records, while existing action review, provenance tracking, and clarification mechanisms may leave the underlying persistent state uncorrected. Our audit of coding-agent trajectories identifies candidate failure chains in which invalid records are reused, leading to task failures and unsafe modifications. We propose StateWise, a framework for diagnosing and repairing persistent operational state before action execution. StateWise uses record-level counterfactual replanning to identify decision-critical records, then establishes their current validity through reliability checks, read-only verification of machine-observable facts, and targeted clarification of developer-owned intent. Typed evidence grounding binds evidence to specific records and scopes, enabling persistent corrections with repair lineage. The agent then replans from the repaired state, followed by an independent state-action check before execution. We evaluate StateWise on 150 executable coding-agent cases across diverse runtime environments, workspace configurations, and repository settings, complemented by cross-model evaluations. Under corrupted persistent state, StateWise achieves 93.3% overall correctness, compared with 38.7% for the baseline agent, with no unsafe actions. Component ablations, multi-task experiments, and transfer evaluations further demonstrate effective recovery, persistent corrections, and transferability across repositories and tool interfaces.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
