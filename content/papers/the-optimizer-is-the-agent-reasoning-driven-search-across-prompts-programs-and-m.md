# The Optimizer Is the Agent: Reasoning-Driven Search across Prompts, Programs, and ML Workflows

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.06714v1
- Published: 2026-08-07
- Updated: 2026-08-07
- Authors: Junbo Li, Boyi Liu, Canwen Xu, Yite Wang, Yuxiong He, Zhangyang Wang, Qiang Liu, Zhewei Yao
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.06714v1

## One-Sentence Summary
Recent systems for optimizing prompts, programs, and ML workflows typically rely on explicit outer-loop controllers such as evolutionary search, bandits, or textual-gradient...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recent systems for optimizing prompts, programs, and ML workflows typically rely on explicit outer-loop controllers such as evolutionary search, bandits, or textual-gradient methods.

进一步看，论文的核心做法或实验重点可以概括为：We ask a fundamentally different question: how much of this search policy can be internalized by a single tool-using agent?

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Recent systems for optimizing prompts, programs, and ML workflows typically rely on explicit outer-loop controllers such as evolutionary search, bandits, or textual-gradient methods. We ask a fundamentally different question: how much of this search policy can be internalized by a single tool-using agent? We present ReASearch, a unified framework for reasoning-driven optimization in which the agent autonomously decides what to evaluate, how to diagnose failures, which edits to make, and when to verify or restart. Rather than serving only as a proposal generator guided by hand-designed heuristics, the agent actively analyzes outcomes, allocates budget, and refines its strategy over long horizons through persistent memory. With a shared agent loop and domain-specific tools, ReASearch instantiates the exact same scaffold to optimize prompts, programs, and ML workflows. Across 14 diverse tasks, it is competitive with and mostly better than specialized optimization systems, achieving gains of 2% to 40% over strong domain-specific baselines, and in some cases discovering solutions that improve on prior human best-known results. Crucially, we observe that complex search behaviors, which are typically implemented by explicit controllers, emerge naturally from the agent's reasoning process.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
