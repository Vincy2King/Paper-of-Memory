# Layered Mutability: Continuity and Governance in Persistent Self-Modifying Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.14717v2
- Published: 2026-04-16
- Updated: 2026-05-11
- Authors: Krti Tallam
- Tags: agent
- Categories: cs.AI, cs.CR, cs.CY, cs.LG
- URL: http://arxiv.org/abs/2604.14717v2

## One-Sentence Summary
Persistent language-model agents increasingly combine tool use, tiered memory, reflective prompting, and runtime adaptation.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent language-model agents increasingly combine tool use, tiered memory, reflective prompting, and runtime adaptation.

进一步看，论文的核心做法或实验重点可以概括为：In such systems, behavior is shaped not only by current prompts but by mutable internal conditions that influence future action.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI, cs.CR, cs.CY, cs.LG

## Abstract Snapshot
Persistent language-model agents increasingly combine tool use, tiered memory, reflective prompting, and runtime adaptation. In such systems, behavior is shaped not only by current prompts but by mutable internal conditions that influence future action. This paper introduces layered mutability, a framework for reasoning about that process across five layers: pretraining, post-training alignment, self-narrative, memory, and weight-level adaptation. The central claim is that governance difficulty rises when mutation is rapid, downstream coupling is strong, reversibility is weak, and observability is low, creating a systematic mismatch between the layers that most affect behavior and the layers humans can most easily inspect. I formalize this intuition with simple drift, governance-load, and hysteresis quantities, connect the framework to recent work on temporal identity in language-model agents, and report a preliminary ratchet experiment in which reverting an agent's visible self-description after memory accumulation fails to restore baseline behavior. In that experiment, the estimated identity hysteresis ratio is 0.68. The main implication is that the salient failure mode for persistent self-modifying agents is not abrupt misalignment but compositional drift: locally reasonable updates that accumulate into a behavioral trajectory that was never explicitly authorized.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
