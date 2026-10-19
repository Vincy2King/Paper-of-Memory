# Beyond Marginal Influence: Interaction-Aware Memory Selection for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.23266v1
- Published: 2026-10-16
- Updated: 2026-10-16
- Authors: BHVSP Subrahmanyam, Neeraj Choudhary
- Tags: agent, benchmark, compression, retrieval
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2610.23266v1

## One-Sentence Summary
LLM-agent memory selection often uses retrieval rankings based on record relevance or individual influence.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM-agent memory selection often uses retrieval rankings based on record relevance or individual influence.

进一步看，论文的核心做法或实验重点可以概括为：Such rankings cannot identify sufficient subsets under redundant or jointly necessary evidence.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, retrieval
- 检索关键词命中：agent memory, memory compression
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
LLM-agent memory selection often uses retrieval rankings based on record relevance or individual influence. Such rankings cannot identify sufficient subsets under redundant or jointly necessary evidence. We study per-decision memory sufficiency: selecting a small subset that preserves full-memory behavior. To separate search error from model error, we introduce JointCoreBench, a benchmark with nine interaction families, six workflow domains, natural-language decisions, and exact sufficient-set oracles, and JointCore, a relevance cost-ordered group-deletion baseline that tests blocks before individual records. On 6,912 exact conditions, cost-ordered JointCore recovers a minimum-cost sufficient set in 100.0% of cases, reduces subset evaluations from 30.00 to 11.13 (62.9%), and achieves 87.8% active-memory savings. Across four 12B-70B model families and 432 tasks per model, its unweighted mean is 10.28 versus 16.00 model queries and 50.6% versus 43.1% minimum-cost recovery relative to cost aware singleton deletion. Both methods preserve full-memory behavior under the deterministic primary interface. Tests with physical deletion, UNKNOWN masks, PENDING sentinels, counterfactual values, and alternative labels identify interface dependent behavior. JointCore is an efficient benchmark baseline; the study does not establish deployment-ready memory compression.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
