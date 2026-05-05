# Effect-Transparent Governance for AI Workflow Architectures: Semantic Preservation, Expressive Minimality, and Decidability Boundaries

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.01030v1
- Published: 2026-05-01
- Updated: 2026-05-01
- Authors: Alan L. McCann
- Tags: memory
- Categories: cs.AI, cs.LO, cs.PL
- URL: http://arxiv.org/abs/2605.01030v1

## One-Sentence Summary
We present a machine-checked formalization of structurally governed AI workflow architectures and prove that effect-level governance can be imposed without reducing internal...

## Introduction
这篇论文被纳入仓库，是因为它和 `memory research` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We present a machine-checked formalization of structurally governed AI workflow architectures and prove that effect-level governance can be imposed without reducing internal computational expressivity.

进一步看，论文的核心做法或实验重点可以概括为：Using Interaction Trees in Rocq 8.19, we define a governance operator G that mediates all effectful directives, including memory access, external calls, and oracle (LLM) queries.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 检索关键词命中：memory reasoning
- 来源分类信息：cs.AI, cs.LO, cs.PL

## Abstract Snapshot
We present a machine-checked formalization of structurally governed AI workflow architectures and prove that effect-level governance can be imposed without reducing internal computational expressivity. Using Interaction Trees in Rocq 8.19, we define a governance operator G that mediates all effectful directives, including memory access, external calls, and oracle (LLM) queries. Our development compiles with 0 admitted lemmas and consists of 36 modules, ~12,000 lines of Rocq, and 454 theorems. We establishseven properties: (P1) governed Turing completeness, (P2) governed oracle expressivity, (P3) a decidability boundary in which governance predicates are total and closed under Boolean composition while semantic program properties remain non-trivial and undecidable by governance, (P4) goal preservation for permitted executions, (P5) expressive minimality of primitive capabilities (compute, memory, reasoning, external call, observability), (P6) subsumption asymmetry showing structural governance strictly subsumes content-level filtering, and (P7) semantic transparency: on all executions where governance permits, the governed interpretation is observationally equivalent (modulo governance-only events) to the ungoverned interpretation. Together, these results show that governance and computational expressivity are orthogonal dimensions: governance constrains the effect boundary of programs while remaining semantically transparent to internal computation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
