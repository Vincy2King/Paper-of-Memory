# AGL-1: The Enterprise AI Governance Layer as a Control Plane for Trusted Enterprise Intelligence

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.03516v1
- Published: 2026-07-03
- Updated: 2026-07-03
- Authors: Roopam W. Sure
- Tags: agent, context, retrieval
- Categories: cs.SE, cs.AI, cs.CY
- URL: http://arxiv.org/abs/2607.03516v1

## One-Sentence Summary
Enterprise artificial intelligence is moving from isolated experimentation toward operational dependency across copilots, retrieval-augmented generation systems, autonomous...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Enterprise artificial intelligence is moving from isolated experimentation toward operational dependency across copilots, retrieval-augmented generation systems, autonomous agents, and AI-enabled business workflows.

进一步看，论文的核心做法或实验重点可以概括为：As this transition accelerates, the primary enterprise challenge is no longer only model access or inference scale.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.SE, cs.AI, cs.CY

## Abstract Snapshot
Enterprise artificial intelligence is moving from isolated experimentation toward operational dependency across copilots, retrieval-augmented generation systems, autonomous agents, and AI-enabled business workflows. As this transition accelerates, the primary enterprise challenge is no longer only model access or inference scale. It is governed intelligence operations: the ability to enforce authorization, preserve contextual lineage, control persistent memory, detect stale or conflicting knowledge, constrain agentic execution, and produce audit-ready evidence across distributed AI estates. This paper introduces AGL-1, the Enterprise AI Governance Layer, as a vendor-neutral reference model for the control plane that should operate across foundation models, retrieval systems, orchestration frameworks, enterprise memory, policy engines, observability systems, tools, APIs, and business applications. Building on governed knowledge-system principles introduced in GKS-5, AGL-1 generalizes the governance problem from retrieval-specific controls to full AI execution-path governance. It identifies recurring failure modes such as unauthorized retrieval, stale grounding, unmanaged memory, weak provenance, policy drift, fragmented observability, and uncontrolled autonomous execution. It then defines seven governance domains: identity-aware retrieval, policy enforcement, provenance management, memory governance, knowledge integrity monitoring, agentic execution control, and trust observability. The central claim is that durable enterprise value from AI will increasingly depend on the ability to govern intelligence at scale. In complex enterprises, trust is not a property of the model alone. It is a property of the system around the model: identity, knowledge, policy, memory, tools, human oversight, and evidence working together as a managed control plane.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
