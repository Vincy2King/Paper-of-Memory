# Taking the PULSE of Enterprise Workflows: Evaluating Persistent Project-State Understanding

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.28374v1
- Published: 2026-11-20
- Updated: 2026-11-20
- Authors: Jiexin Ding, Lin Ai, Adam Davies, Scott Counts
- Tags: agent, benchmark, context, retrieval
- Categories: cs.CL, cs.AI, cs.SE
- URL: http://arxiv.org/abs/2611.28374v1

## One-Sentence Summary
Enterprise agents must maintain an up-to-date understanding of work distributed across heterogeneous artifacts, evolving over time, and unevenly visible to different collaborators.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Enterprise agents must maintain an up-to-date understanding of work distributed across heterogeneous artifacts, evolving over time, and unevenly visible to different collaborators.

进一步看，论文的核心做法或实验重点可以概括为：We formulate this challenge as persistent project-state understanding (PPSU) and introduce PULSE, a benchmark of 1,573 questions over 30 enterprise project histories.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CL, cs.AI, cs.SE

## Abstract Snapshot
Enterprise agents must maintain an up-to-date understanding of work distributed across heterogeneous artifacts, evolving over time, and unevenly visible to different collaborators. We formulate this challenge as persistent project-state understanding (PPSU) and introduce PULSE, a benchmark of 1,573 questions over 30 enterprise project histories. PULSE constructs deterministic, time-indexed project state and documented collaborator views from source-linked records, and evaluates three families of questions: open loops, project evolution, and view gaps. Across retrieval agents, graph- and memory-augmented retrieval, long-context, and oracle conditions, we find substantial headroom for current systems. Retrieval and extraction account for the largest share of the gap, but providing explicit project state on top of gold evidence yields further substantial gains, showing that PPSU cannot be reduced to retrieval alone. Further analysis shows that questions requiring information to be reconciled across multiple parts of the project history remain difficult even when the relevant evidence is provided, while project-state synthesis and perspective conditioning remain persistent challenges. These results motivate enterprise agents that explicitly maintain and reconcile temporally grounded state across sources, actors, and time.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
