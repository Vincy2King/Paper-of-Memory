# MemLeak: Cross-User Semantic Leakage in Multi-Tenant AI Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.04195v1
- Published: 2026-10-03
- Updated: 2026-10-03
- Authors: Priyanka Mudgal, Kai Zhao, Guilin Zhang, Andy Olsen, Ezekiel Miller, Xu Chu, Aletta Johanna Blanken
- Tags: agent, long-term, retrieval
- Categories: cs.AI, cs.LG
- URL: http://arxiv.org/abs/2610.04195v1

## One-Sentence Summary
Personal AI agents in enterprise multi-tenant deployments share a common vector store for long-term memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Personal AI agents in enterprise multi-tenant deployments share a common vector store for long-term memory.

进一步看，论文的核心做法或实验重点可以概括为：Shared embedding spaces create a surface for cross-user memory leakage: a user's query can retrieve semantically adjacent memories belonging to another user through ordinary cosine-similarity retrieval, without any...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.AI, cs.LG

## Abstract Snapshot
Personal AI agents in enterprise multi-tenant deployments share a common vector store for long-term memory. Shared embedding spaces create a surface for cross-user memory leakage: a user's query can retrieve semantically adjacent memories belonging to another user through ordinary cosine-similarity retrieval, without any exploit. We formalize this as cross-user admissibility failure and evaluate it across six experiments, plus follow-up ablations, under both sparse (TF-IDF) and production-faithful (MiniLM-L6-v2) retrieval. Non-adversarial, incidental leakage reaches 70--100\% under pooled {same-team} retrieval; adversarially crafted memories achieve 90--100\% top-$k$ placement, exceeding weaker keyword-based attacker baselines, with score lifts of $+0.416$ to $+0.511$ under production-faithful dense retrieval (Config B); and end-to-end response contamination reaches 5.00/5 under a production retrieval path and 4.67/5 with Claude Sonnet~4.5, with contaminated responses often scoring as helpful or more helpful than clean ones, a gap validated against human judgment. Among three architectural mitigations, only hard post-retrieval ownership gating consistently restores the clean baseline (1.00/5) across {two generation models, at a measured latency overhead of roughly 1.4~ms per query.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
