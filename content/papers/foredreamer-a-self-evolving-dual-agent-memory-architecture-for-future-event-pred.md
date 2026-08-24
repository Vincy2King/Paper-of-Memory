# ForeDreamer: A Self-Evolving Dual-Agent Memory Architecture for Future Event Prediction

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.20920v1
- Published: 2026-08-21
- Updated: 2026-08-21
- Authors: Linhao Zhong, Zongze Du, Linyu Wu, Yu Bo, Hourong Li, Chenchen Jing, Hao Chen, Yuling Xi, Chunhua Shen
- Tags: agent, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.20920v1

## One-Sentence Summary
Open-web future event prediction requires agents to distill reliable signals from noisy, redundant, and incomplete evidence.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Open-web future event prediction requires agents to distill reliable signals from noisy, redundant, and incomplete evidence.

进一步看，论文的核心做法或实验重点可以概括为：Existing retrieval/memory mechanisms directly feed retrieved information to agents or rely on simple memory functions such as storing and reusing prior information for prediction, leaving them insufficient for open-...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory, retrieval memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Open-web future event prediction requires agents to distill reliable signals from noisy, redundant, and incomplete evidence. Existing retrieval/memory mechanisms directly feed retrieved information to agents or rely on simple memory functions such as storing and reusing prior information for prediction, leaving them insufficient for open-web forecasting. We propose to transform raw web evidence into structured memory before prediction, enabling agents to reason over distilled, question-specific evidence rather than noisy retrieval results. This paper presents ForeDreamer, a self-evolving dual-agent framework for managing memory over open-web evidence. ForeDreamer separates factual memory, a question-specific evidence state for the current forecast, from experiential memory, persistent agent experience accumulated across forecasting episodes. It uses a main agent for search and prediction, and a memory-processing subagent to convert search results into factual memory with dedicated tools. ForeDreamer further evolves experiential memory through two tracks, improving both forecasting decisions and factual-memory construction. Experiments on Prophet Arena and FutureX demonstrate the effectiveness of ForeDreamer. Project page: https://zhongzero.github.io/ForeDreamer

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
