# CALM: Conflict-Aware Lifecycle Memory Governance for Long-Horizon Language Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.38573v1
- Published: 2026-10-28
- Updated: 2026-10-28
- Authors: Chang Li, Xianhao Ou, Xinyan Ma, Hao Li, Haoyuan Xu, Jiafeng Liang, Xiaohan Wang, Jiajun Chai, Guojun Yin, Ming Liu
- Tags: agent, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.38573v1

## One-Sentence Summary
A memory can be outdated for present-day reasoning yet indispensable for reconstructing the past.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：A memory can be outdated for present-day reasoning yet indispensable for reconstructing the past.

进一步看，论文的核心做法或实验重点可以概括为：Relevance-based retrieval overlooks this tension: semantic relevance, evidence-grounded validity, and query-specific eligibility are distinct.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：persistent memory, retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
A memory can be outdated for present-day reasoning yet indispensable for reconstructing the past. Relevance-based retrieval overlooks this tension: semantic relevance, evidence-grounded validity, and query-specific eligibility are distinct. We propose CALM, a conflict-aware lifecycle memory governance framework that decouples persistent memory preservation from query-time admission. CALM converts heterogeneous records into evidence-grounded memory cells, updates validity and lifecycle states using support, conflict, and dependency signals, and admits query-appropriate evidence through training-free or learned gating informed by temporal applicability. Across LongMemEval-S and LoCoMo with Qwen and GPT backbones, CALM outperforms state-of-the-art baselines, achieving the best overall accuracy. Compared with simple filtering and reranking, query-conditioned admission further improves evidence selection. Conflict-blocking and robustness analyses show CALM suppresses erroneous retrieved memories while retaining useful evidence. Historical-reconstruction experiments demonstrate that preserving superseded records supports accurate earlier-state reasoning without compromising current-state answers.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
