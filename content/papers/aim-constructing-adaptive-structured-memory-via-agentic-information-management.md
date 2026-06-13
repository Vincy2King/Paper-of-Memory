# AIM: Constructing Adaptive Structured Memory via Agentic Information Management

- Source: OpenReview
- Venue: ACL ARR 2026 May Submission
- Paper ID: openreview:qFBAlgwkzb
- Published: 2026-06-02
- Updated: 2026-06-12
- Authors: Unknown
- Tags: agent, benchmark, long-term
- Categories: aclweb.org/ACL/ARR/2026/May/-/Submission
- URL: https://openreview.net/forum?id=qFBAlgwkzb

## One-Sentence Summary
Long-term memory remains a critical bottleneck for LLM agents in managing historical user interactions and task-related resources.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 May Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Long-term memory remains a critical bottleneck for LLM agents in managing historical user interactions and task-related resources.

进一步看，论文的核心做法或实验重点可以概括为：Existing approaches typically rely on flat, predefined memory structures that lack adaptability and sophisticated reasoning capabilities.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 May Submission
- 高亮主题命中：agent, benchmark, long-term
- 检索关键词命中：agent memory, long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：aclweb.org/ACL/ARR/2026/May/-/Submission

## Abstract Snapshot
Long-term memory remains a critical bottleneck for LLM agents in managing historical user interactions and task-related resources. Existing approaches typically rely on flat, predefined memory structures that lack adaptability and sophisticated reasoning capabilities. To address this, we propose \textbf{Agentic Information Management (AIM)}, a novel framework that leverages the LLM's inherent code generation and reasoning abilities to dynamically construct and manage structured memory. Unlike existing summarize-then-retrieve paradigms, AIM regards agent memory as an information management problem. AIM employs an agent to dynamically organize heterogeneous sources into well-defined structured representations. Furthermore, recognizing the limitations of existing memory benchmarks, which often use non-agentic, LLM-generated dialogues, we introduce VibeCodeMem, a high-quality, human-annotated long-horizon QA dataset. It spans realistic working sessions with a coding agent across four software applications and 16 diverse features. Experiments using both open-source and proprietary LLMs demonstrate that AIM consistently outperforms strong baselines, achieving a 10.53\% absolute improvement on LoCoMo and 2.07\% on VibeCodeMem with the Claude-4.5-haiku model. Our results highlight the promise of agentic, self-structured memory for long-term agent capabilities. Our code and data will be released upon acceptance.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
