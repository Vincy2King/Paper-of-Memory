# Episodic-to-Semantic Consolidation Without Identity Drift

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.01988v1
- Published: 2026-07-02
- Updated: 2026-07-02
- Authors: Xue Qin, Simin Luan, Cong Yang, Zhijun Li
- Tags: agent, context, episodic
- Categories: cs.AI, cs.RO
- URL: http://arxiv.org/abs/2607.01988v1

## One-Sentence Summary
Long-running adaptive intelligent agents face a structural tension between knowledge consolidation and information integrity.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-running adaptive intelligent agents face a structural tension between knowledge consolidation and information integrity.

进一步看，论文的核心做法或实验重点可以概括为：Memory consolidation is conventionally treated as an agent-changing operation: a model is fine-tuned, a prompt rewritten, a policy distilled, or a reflection appended to the context that governs future behaviour.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI, cs.RO

## Abstract Snapshot
Long-running adaptive intelligent agents face a structural tension between knowledge consolidation and information integrity. Memory consolidation is conventionally treated as an agent-changing operation: a model is fine-tuned, a prompt rewritten, a policy distilled, or a reflection appended to the context that governs future behaviour. In regulated autonomic deployment this is a liability because the agent operates under commitments and audit contracts that bind to a specific, cryptographically certified identity. We propose to treat consolidation not as a mutation of the planner or the identity manifest, but as a deterministic function f: M^ep -> M^sem over episodic memory whose output is a separately addressable semantic knowledge layer; the identity hash does not read M^sem, so consolidation updates knowledge without changing the agent's certified identity. We give a formal account of the agent representation, prove identity invariance through a structural lemma on the manifest's hash-input set, specify a deterministic aggregation algorithm whose outputs are auditable database rows with explicit confidence and supporting-event provenance, and validate the construction with synthetic experiments demonstrating per-field correctness, byte-equal identity across consolidation passes, and a mean 79.82% reduction in unproductive planner attempts (95% BCa CI [78.02%, 81.49%] across 10 seeds) against a calibrated Bayesian-shrunk baseline. The construction is a knowledge-update discipline for autonomic agents in which lessons accumulate as queryable facts while the agent's certified identity remains byte-equal across its operational lifetime, with an embodied service agent as the running case study.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
