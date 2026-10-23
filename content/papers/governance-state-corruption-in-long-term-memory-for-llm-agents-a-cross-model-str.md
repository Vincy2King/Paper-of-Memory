# Governance-State Corruption in Long-Term Memory for LLM Agents: A Cross-Model Stress Test

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.30698v1
- Published: 2026-10-22
- Updated: 2026-10-22
- Authors: Bowen Liu, Youting Wang, Bonan Shen, Dingyan Shang
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.AI, cs.SE
- URL: http://arxiv.org/abs/2610.30698v1

## One-Sentence Summary
An LLM agent can retrieve a memory correctly yet use it incorrectly after its validity state changes.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：An LLM agent can retrieve a memory correctly yet use it incorrectly after its validity state changes.

进一步看，论文的核心做法或实验重点可以概括为：We study governance-state corruption: faults that alter which retained records enter model-visible context while stored content and tasks remain fixed.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI, cs.SE

## Abstract Snapshot
An LLM agent can retrieve a memory correctly yet use it incorrectly after its validity state changes. We study governance-state corruption: faults that alter which retained records enter model-visible context while stored content and tasks remain fixed. Across six providers, 731 benchmark-grounded bases yield 2,080 matched fault pairs. In offline control-plane checks, corruption changes the operative projection in 96.25% of pairs, while oracle-backed enforcement restores it in 100%. For downstream evaluation, a deterministically selected, non-probability LongMemEval/Memora panel resolves 298 of 300 matched triplets (238 distinct bases). Clean-minus-corrupted contrasts are 40.54 percentage points in LongMemEval binary correctness (95% base-cluster interval [30.32, 50.71]) and 30.60 points in rescaled Memora FAMA ([23.31, 37.69]); both sources also show recovery. OAKS Novel native option parity holds for all 6,714 resolved outputs. Full-cohort frozen-scorer corruption/recovery effects (-27.55/+27.51 points) remain descriptive proxies, not validated native semantic population effects. These bounded findings motivate evaluating memory control-state integrity alongside retrieval accuracy.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
