# What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.03354v1
- Published: 2026-05-05
- Updated: 2026-05-05
- Authors: Xutao Mao, Jinman Zhao, Gerald Penn, Cong Wang
- Tags: agent, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.03354v1

## One-Sentence Summary
Agent memory failures are silent: an LLM-based agent can produce a fluent response even when it fails to extract, retain, or retrieve the information needed across sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agent memory failures are silent: an LLM-based agent can produce a fluent response even when it fails to extract, retain, or retrieve the information needed across sessions.

进一步看，论文的核心做法或实验重点可以概括为：The write-manage-read loop describes the external pipeline of these systems but leaves open which internal computations implement each stage.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Agent memory failures are silent: an LLM-based agent can produce a fluent response even when it fails to extract, retain, or retrieve the information needed across sessions. The write-manage-read loop describes the external pipeline of these systems but leaves open which internal computations implement each stage. Tracing internal feature circuits across the Qwen-3 family (0.6B--14B) and two memory frameworks (mem0 and A-MEM), we report three findings. First, control is detectable before content: routing circuitry is causally active at 0.6B, while content circuitry produces no detectable signal until 4B under our tracing setup, creating a deployment regime where small models route with apparent competence but silently fail at extraction and grounding. Second, within the content group, Write and Read share a late-layer hub that operates as a context-grounding substrate already present in the base model; only memory framing recruits a functional grounding direction on this substrate, and the hub transfers across both frameworks. Third, emergence does not imply steerability: although the content circuit becomes detectable at 4B, it becomes reliably steerable only at 8B, indicating that detection and intervention have distinct scale thresholds. As a practical implication, the feature-space separation between the two circuit groups enables per-operation failure localization at 76.2% accuracy without supervision, providing a stage-level diagnostic for otherwise silent agent-memory failures.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
