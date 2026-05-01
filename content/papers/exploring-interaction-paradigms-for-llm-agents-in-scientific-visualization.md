# Exploring Interaction Paradigms for LLM Agents in Scientific Visualization

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.27996v1
- Published: 2026-04-30
- Updated: 2026-04-30
- Authors: Jackson Vonderhorst, Kuangshi Ai, Haichao Miao, Shusen Liu, Chaoli Wang
- Tags: agent, benchmark, context
- Categories: cs.AI, cs.GR, cs.HC
- URL: http://arxiv.org/abs/2604.27996v1

## One-Sentence Summary
This paper examines how different types of large language model (LLM) agents perform on scientific visualization (SciVis) tasks, where users generate visualization workflows...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：This paper examines how different types of large language model (LLM) agents perform on scientific visualization (SciVis) tasks, where users generate visualization workflows from natural-language instructions.

进一步看，论文的核心做法或实验重点可以概括为：We compare three primary interaction paradigms, including domain-specific agents with structured tool use, computer-use agents, and general-purpose coding agents, by evaluating eight representative agents across 15...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI, cs.GR, cs.HC

## Abstract Snapshot
This paper examines how different types of large language model (LLM) agents perform on scientific visualization (SciVis) tasks, where users generate visualization workflows from natural-language instructions. We compare three primary interaction paradigms, including domain-specific agents with structured tool use, computer-use agents, and general-purpose coding agents, by evaluating eight representative agents across 15 benchmark tasks and measuring visualization quality, efficiency, robustness, and computational cost. We further analyze interaction modalities, including code scripts and model context protocol (MCP) or API calls for structured tool use, as well as command-line interfaces (CLI) and graphical user interfaces (GUI) for more general interaction, while additionally studying the effect of persistent memory in selected agents. The results reveal clear tradeoffs across paradigms and modalities. General-purpose coding agents achieve the highest task success rates but are computationally expensive, while domain-specific agents are more efficient and stable but less flexible. Computer-use agents perform well on individual steps but struggle with longer multi-step workflows, indicating that long-horizon planning is their primary limitation. Across both CLI- and GUI-based settings, persistent memory improves performance over repeated trials, although its benefits depend on the underlying interaction mode and the quality of feedback. These findings suggest that no single approach is sufficient, and future SciVis systems should combine structured tool use, interactive capabilities, and adaptive memory mechanisms to balance performance, robustness, and flexibility.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
