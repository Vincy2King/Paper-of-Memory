# Post-Deterministic Distributed Systems: A New Foundation for Trustworthy Autonomous Infrastructure

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.01722v1
- Published: 2026-06-01
- Updated: 2026-06-01
- Authors: Jun He, Deying Yu
- Tags: agent
- Categories: cs.LG, cs.AI, cs.DC
- URL: http://arxiv.org/abs/2606.01722v1

## One-Sentence Summary
For decades, distributed systems have typically assumed that correct participants execute protocol-specified behavior with stable, externally defined, and deterministic semantics.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：For decades, distributed systems have typically assumed that correct participants execute protocol-specified behavior with stable, externally defined, and deterministic semantics.

进一步看，论文的核心做法或实验重点可以概括为：Classical theory has extensively parameterized network timing, communication topologies, and failure domains, but this participant model has remained comparatively fixed.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.LG, cs.AI, cs.DC

## Abstract Snapshot
For decades, distributed systems have typically assumed that correct participants execute protocol-specified behavior with stable, externally defined, and deterministic semantics. Classical theory has extensively parameterized network timing, communication topologies, and failure domains, but this participant model has remained comparatively fixed. The integration of autonomous reasoning engines, stochastic model-driven agents, and policy-driven actors into cloud control planes, incident response systems, and financial infrastructure challenges the universality of this assumption. These agents often produce divergent reasoning paths, distinct operational traces, and heterogeneous internal representations while achieving semantically equivalent and correct outcomes. In this paper, we introduce Post-Deterministic Distributed Systems (PDDS) as a research and engineering model for coordinating heterogeneous environments where deterministic code, stochastic models, and autonomous agents coexist. We show that classical distributed computing models form a zero-ambiguity special case of this participant-general model. We do not argue that deterministic systems disappear; rather, deterministic execution can no longer serve as the universal participant assumption for autonomous infrastructure. Finally, we outline five architectural pillars of post-deterministic infrastructure: Protocol-Driven Development, Verifiable Agentic Infrastructure, Autonomous State Control Planes, Semantic Quorum Assurance, and Epistemic State Replication. Epistemic State Replication extends persistence and consistency models from data visibility to knowledge visibility, enabling agentic memory, Verifiable Semantic Rollback, and coherence across reasoning participants. We also define a taxonomy of failure classes that arise in this setting.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
