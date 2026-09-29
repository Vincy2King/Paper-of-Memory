# The Epistemics of Agent Memory: Measuring, and Governing, the Consolidation Decision in Long-Horizon LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.33013v1
- Published: 2026-09-26
- Updated: 2026-09-26
- Authors: Sasank Annapureddy, Anjaneya Prasad Thamatani
- Tags: agent, benchmark, compression, episodic, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.33013v1

## One-Sentence Summary
Long-horizon LLM agents must convert accumulated experience into durable memory, deciding what to keep, compress, abstract into reusable skills and rules, or forget.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon LLM agents must convert accumulated experience into durable memory, deciding what to keep, compress, abstract into reusable skills and rules, or forget.

进一步看，论文的核心做法或实验重点可以概括为：We report a four-phase research program on this consolidation problem whose central finding is a shift in what is measured: from how much an agent remembers, to whether its consolidation decisions are any good, to...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, episodic, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-horizon LLM agents must convert accumulated experience into durable memory, deciding what to keep, compress, abstract into reusable skills and rules, or forget. We report a four-phase research program on this consolidation problem whose central finding is a shift in what is measured: from how much an agent remembers, to whether its consolidation decisions are any good, to whether those decisions can be trusted. Phase 1 learns episodic boundaries from agent traces by downstream utility; an honest near-miss (oracle correlation 0.691 vs a 0.70 bar) whose lasting output is a three-gate anti-leakage protocol. Phase 2 learns when to promote experience and to which abstraction level under a token budget, achieving a verified +22.7% task-success improvement with 7x compression, but exposing a degenerate-forgetting failure and a distribution-shift failure mode we name lambda-prevalence coupling. Phase 3 introduces ConsolidationBench, an oracle-by-construction benchmark that scores consolidation decisions against a known optimum on three non-circular axes; production retrieval systems retain information yet score zero on cross-level transfer. Phase 4 introduces governed consolidation: the decision wrapped in poison-resistance, reversibility, and auditability guarantees with a quality gate. Governance is statistically distinct from the quality score ($r^2 = 0.43$; partial $r = 0.27$; identical-quality policies differ threefold in governance), so the contribution survives independently of the metric's external validity. On that question we report a resolved negative: after a graded-reuse redesign removed a structural ceiling, a two-benchmark study with 2,532 real answer cells finds the quality score does not predict real transfer accuracy (pooled Spearman $ρ= -0.24$, n = 12, CI spanning zero). An adversarial self-critique pass cleared the final claim set with zero surviving overclaims.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
