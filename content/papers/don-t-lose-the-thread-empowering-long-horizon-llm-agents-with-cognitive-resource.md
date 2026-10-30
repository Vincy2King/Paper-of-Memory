# Don't Lose the Thread: Empowering Long-Horizon LLM Agents with Cognitive Resource Self-Allocation

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.40350v1
- Published: 2026-10-29
- Updated: 2026-10-29
- Authors: Zheng Zhu, Xiaozhuan Liang, Xi Chen, Bei Yu, Jiaya Jia
- Tags: agent, benchmark, context
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.40350v1

## One-Sentence Summary
Agents powered by large language models (LLMs) have demonstrated remarkable progress in solving complex reasoning tasks.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agents powered by large language models (LLMs) have demonstrated remarkable progress in solving complex reasoning tasks.

进一步看，论文的核心做法或实验重点可以概括为：However, LLM agents often falter on long-horizon tasks due to cognitive overload, as their working memory becomes cluttered with expanding and irrelevant information, which dilutes their attention and hinders...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：working memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Agents powered by large language models (LLMs) have demonstrated remarkable progress in solving complex reasoning tasks. However, LLM agents often falter on long-horizon tasks due to cognitive overload, as their working memory becomes cluttered with expanding and irrelevant information, which dilutes their attention and hinders effective planning and reasoning. To mitigate this challenge, we introduce Cognitive Resource Self-Allocation (CORAL), a novel reasoning paradigm that empowers agents to proactively optimize their context. Implemented as an agent-callable working memory management toolset, CORAL allows an agent to checkpoint its task progress and verified facts, and adaptively initiate a new problem-solving episode by resetting cluttered context while preserving only the checkpointed information, enabling it to resume reasoning from a clean state. We further enhance the agent's checkpointing capabilities using a Multi-episode Agentic Reinforced Policy Optimization algorithm. On the GAIA benchmark, CORAL with an 8B model achieves 42.8% average accuracy, with particularly strong gains on the most challenging long-horizon tasks (Level 2 and Level 3). Crucially, these gains come at a substantially lower inference cost: CORAL consumes 6-7$\times$ fewer input tokens than a ReAct agent. It also generalizes to multi-hop Knowledge QA benchmarks and to the considerably harder BrowseComp, where it improves a strong proprietary agent by 8.0 points.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
