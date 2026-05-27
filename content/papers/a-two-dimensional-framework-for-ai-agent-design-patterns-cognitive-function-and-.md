# A Two-Dimensional Framework for AI Agent Design Patterns: Cognitive Function and Execution Topology

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.13850v2
- Published: 2026-03-16
- Updated: 2026-05-24
- Authors: Jia Huang, Joey Tianyi Zhou
- Tags: agent
- Categories: cs.AI, cs.MA, cs.SE
- URL: http://arxiv.org/abs/2605.13850v2

## One-Sentence Summary
Existing frameworks for LLM-based agent architectures describe systems from a single perspective: industry guides (Anthropic, Google, LangChain) focus on execution topology --...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Existing frameworks for LLM-based agent architectures describe systems from a single perspective: industry guides (Anthropic, Google, LangChain) focus on execution topology -- how data flows -- while cognitive science...

进一步看，论文的核心做法或实验重点可以概括为：Neither axis alone disambiguates architecturally distinct systems: the same Orchestrator-Workers topology can implement Plan-and-Execute, Hierarchical Delegation, or Adversarial Verification -- three patterns with...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：memory reasoning
- 来源分类信息：cs.AI, cs.MA, cs.SE

## Abstract Snapshot
Existing frameworks for LLM-based agent architectures describe systems from a single perspective: industry guides (Anthropic, Google, LangChain) focus on execution topology -- how data flows -- while cognitive science surveys focus on cognitive function -- what the agent does. Neither axis alone disambiguates architecturally distinct systems: the same Orchestrator-Workers topology can implement Plan-and-Execute, Hierarchical Delegation, or Adversarial Verification -- three patterns with fundamentally different failure modes and design trade-offs. We propose a two-dimensional classification that combines (1) a Cognitive Function axis with seven categories (Perception, Memory, Reasoning, Action, Reflection, Collaboration, Governance) and (2) an Execution Topology axis with six structural archetypes (Chain, Route, Parallel, Orchestrate, Loop, Hierarchy). The resulting 7x6 matrix identifies 28 named patterns, 15 with original names. We demonstrate orthogonality through systematic cross-axis analysis, define eight representative patterns in detail, and validate descriptive coverage across four real-world domains (financial lending, legal due diligence, network operations, healthcare triage). Cross-domain analysis yields five empirical laws of pattern selection governing the relationship between environmental constraints (time pressure, action authority, failure cost asymmetry, volume) and architectural choices. The framework provides a principled, framework-neutral, and model-agnostic vocabulary for AI agent architecture design.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
