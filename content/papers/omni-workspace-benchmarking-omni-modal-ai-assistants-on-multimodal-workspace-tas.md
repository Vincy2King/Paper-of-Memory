# Omni-Workspace: Benchmarking Omni-Modal AI Assistants on Multimodal Workspace Tasks

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.19202v1
- Published: 2026-11-14
- Updated: 2026-11-14
- Authors: Yuhao Wang, Yucheng Zhao, Yiran Zhong, Feida Zhu, Hongcheng Liu, Qichao Wang, Ming Ma, Yu Wang
- Tags: agent, benchmark, context
- Categories: cs.CL
- URL: http://arxiv.org/abs/2611.19202v1

## One-Sentence Summary
Omni-modal agents are expected to move beyond multimodal understanding toward completing complex tasks in realistic multimodal environments.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Omni-modal agents are expected to move beyond multimodal understanding toward completing complex tasks in realistic multimodal environments.

进一步看，论文的核心做法或实验重点可以概括为：In these settings, information is distributed across heterogeneous files and modalities, with cross-file and cross-modal dependencies requiring agents to continually coordinate perception, reasoning, and tool use as...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：working memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Omni-modal agents are expected to move beyond multimodal understanding toward completing complex tasks in realistic multimodal environments. In these settings, information is distributed across heterogeneous files and modalities, with cross-file and cross-modal dependencies requiring agents to continually coordinate perception, reasoning, and tool use as newly gathered evidence informs subsequent actions. However, existing omni-modal benchmarks primarily focus on multimodal perception and understanding, leaving complex task completion through sustained interaction with multimodal workspaces underexplored. We introduce Omni-Workspace, a benchmark comprising 380 deep-research-style tasks across four multimodal workspace types and two difficulty levels. These tasks require agents to inspect and process workspace files, retrieve external information when needed, integrate evidence across files and modalities, and produce artifacts satisfying explicit requirements. Evaluating 18 representative models reveals limitations in long-horizon multimodal workspace execution, with the best model scoring only 65.93 on average. Further analysis identifies multimodal context inflation and task-state drift as recurring challenges. Motivated by these findings, we further propose OmniFocus, a lightweight approach combining multimodal working-memory management with explicit task-state tracking to improve performance and efficiency. Omni-Workspace advances the evaluation and development of omni-modal agents toward autonomous completion of complex tasks in multimodal workspaces.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
