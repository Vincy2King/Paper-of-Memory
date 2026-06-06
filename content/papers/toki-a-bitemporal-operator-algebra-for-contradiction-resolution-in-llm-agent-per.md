# TOKI: A Bitemporal Operator Algebra for Contradiction Resolution in LLM-Agent Persistent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.06240v1
- Published: 2026-06-04
- Updated: 2026-06-04
- Authors: Ziming Wang
- Tags: agent
- Categories: cs.DB, cs.AI
- URL: http://arxiv.org/abs/2606.06240v1

## One-Sentence Summary
Persistent memory for an LLM agent is a write-heavy substrate: every belief update is a versioned write, and a new claim may contradict a stored one.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent memory for an LLM agent is a write-heavy substrate: every belief update is a versioned write, and a new claim may contradict a stored one.

进一步看，论文的核心做法或实验重点可以概括为：Production systems use four resolution heuristics (last-writer-wins, evidence-weighted merge, await-confirmation, per-rule policy), yet none declares the isolation level it assumes or the write-time anomalies it admits.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.DB, cs.AI

## Abstract Snapshot
Persistent memory for an LLM agent is a write-heavy substrate: every belief update is a versioned write, and a new claim may contradict a stored one. Production systems use four resolution heuristics (last-writer-wins, evidence-weighted merge, await-confirmation, per-rule policy), yet none declares the isolation level it assumes or the write-time anomalies it admits. We show that contradiction resolution is write-time concurrency control and make the missing contract explicit. TOKI types the four heuristics as one family of bitemporal operators over a dual-row schema, each with an isolation precondition and a provenance annotation that preserves the losing fact in an audit row. Four soundness theorems close the contract across isolation, schema, and provenance, lift the guarantees to operator pipelines, and extend the fold operators to n-ary conflict sets. A tightness companion proves that, within the relational schedule model, keyed logging of the adjudicating judge is necessary for replay consistency, which every audited baseline omits. A verdict matrix over eight systems localizes the gap: every baseline that keeps a language-model judge on the write path admits at least one of three write-time anomalies (replay inconsistency, belief-drift skew, audit erasure); a content-addressed engine-layer comparator avoids them only by removing the judge, and TOKI alone excludes all three while keeping it. On its one natural-workload slice the audit-row defence moves LoCoMo by 0.86, and ablating the typed memory layer removes 0.49 accuracy on 1,444 answerable LoCoMo questions; the cross-system comparison stays underpowered and claims no superiority. The contribution is the contract: a write-time correctness specification, proved sound across isolation, schema, and provenance, pinning the guarantee every production heuristic assumes but no deployed system makes explicit.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
