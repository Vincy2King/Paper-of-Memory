# PDEU-Bench: Benchmarking the Personalized Planning Lifecycle of Tool-Calling LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.34930v1
- Published: 2026-09-28
- Updated: 2026-09-28
- Authors: Huayi Lai, Shichao Song, Qingchen Yu, Simin Niu, Mengwei Wang, Hanyu Wang, Xun Liang
- Tags: agent, benchmark, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.34930v1

## One-Sentence Summary
Large language model (LLM) agents are evolving from tool-calling systems that execute isolated instructions into task-oriented agents that pursue user goals through sustained,...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents are evolving from tool-calling systems that execute isolated instructions into task-oriented agents that pursue user goals through sustained, multi-step interactions.

进一步看，论文的核心做法或实验重点可以概括为：However, existing benchmarks for personalized tool use largely assess isolated calls or reactive execution, leaving unclear whether agents can formulate, execute, and revise an explicit plan while preserving user...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language model (LLM) agents are evolving from tool-calling systems that execute isolated instructions into task-oriented agents that pursue user goals through sustained, multi-step interactions. However, existing benchmarks for personalized tool use largely assess isolated calls or reactive execution, leaving unclear whether agents can formulate, execute, and revise an explicit plan while preserving user preferences throughout long-term interaction. To address this gap, we introduce \textbf{PDEU-Bench} (\textbf{P}ersonalized plan \textbf{D}efinition, plan \textbf{E}xecution, and plan \textbf{U}pdate \textbf{Bench}mark), a benchmark for evaluating the complete planning lifecycle of personalized tool-using agents. PDEU-Bench comprises 214 long-horizon interaction tasks spanning 12 everyday domains and 94 tools, with stage-specific assessments of preference adherence and plan quality. Extensive evaluations of 15 representative open-source and closed-source LLMs reveal a pronounced gap between local tool execution and dynamic planning: LLMs can often instantiate preferences in individual calls, yet struggle to construct coherent plan definition and plan update. We further evaluate mainstream personalization and memory-augmentation methods. Although these methods improve particular stages, none of the evaluated methods reliably propagates user preferences throughout the complete lifecycle, and their gains frequently fail to transfer to subsequent execution. Fine-grained error analysis further reveals that preference omissions and conflicts persist throughout the planning lifecycle, highlighting the need for future research to parameterize LLMs with preference-aware information retrieval and memory capabilities. We provide the relevant code and data in the appendix to support future research.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
