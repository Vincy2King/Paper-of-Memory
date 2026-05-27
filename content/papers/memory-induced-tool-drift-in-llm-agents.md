# Memory-Induced Tool-Drift in LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.24941v1
- Published: 2026-05-24
- Updated: 2026-05-24
- Authors: Mahavir Dabas, Jihyun Jeong, Ming Jin, Ruoxi Jia
- Tags: agent, benchmark, context, long-term
- Categories: cs.CR, cs.LG
- URL: http://arxiv.org/abs/2605.24941v1

## One-Sentence Summary
Modern LLM agents combine long-term memory for personalization with tool-calling interfaces for taking actions in the world -- a combination underpinning contemporary production...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Modern LLM agents combine long-term memory for personalization with tool-calling interfaces for taking actions in the world -- a combination underpinning contemporary production systems.

进一步看，论文的核心做法或实验重点可以概括为：We study a previously unexamined failure of this combination: when personality-driven biases stored in memory (cost-consciousness, impatience, risk tolerance, etc.) silently affect tool calls in contexts where they...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CR, cs.LG

## Abstract Snapshot
Modern LLM agents combine long-term memory for personalization with tool-calling interfaces for taking actions in the world -- a combination underpinning contemporary production systems. We study a previously unexamined failure of this combination: when personality-driven biases stored in memory (cost-consciousness, impatience, risk tolerance, etc.) silently affect tool calls in contexts where they are not applicable. We call this memory-induced tool-drift and operationalize it through MEMDRIFT, a benchmark of 105 scenarios spanning five bias dimensions and seven professional domains, generated through an automated adversarial pipeline. Across seven frontier models -- including those with extended reasoning -- biased memories raise deflection scores (a judge-scored measure of parameter deviation from unbiased baselines) by up to $+3.6$ points on a 1--5 scale. Tool-drift persists when memory management is handled by three production memory architectures. The phenomenon affects real-world tools: scanning 6{,}062 tools across 288 verified MCP servers, we flag 608 with susceptible parameters and confirm tool-drift on a validated subset. Mechanistically, biased memories act as implicit steering vectors, pushing activations along the same latent directions as explicit behavioral instructions. They also redistribute attention from task-relevant context toward memory entries with surface-level keyword overlap to the target parameter. Standard defenses -- prompt-based relevance instructions and memory filters -- reduce drift but do not eliminate it. As agents take increasingly consequential actions on a user's behalf, memory-induced tool-drift represents a systematic vulnerability that current safeguards do not address, motivating dedicated defenses at the intersection of memory management and tool-call generation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
