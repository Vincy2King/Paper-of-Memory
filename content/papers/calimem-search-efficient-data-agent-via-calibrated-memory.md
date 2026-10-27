# CaliMem: Search-Efficient Data Agent via Calibrated Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.34500v1
- Published: 2026-10-25
- Updated: 2026-10-25
- Authors: Hanze Li, Athan Z. Li, Feiyang Kang, Jiachen T. Wang, Yuhan Chen, Ruishan Liu, Ruoxi Jia
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.34500v1

## One-Sentence Summary
Data curation is a first-order design choice in machine learning, yet tailoring training data to a downstream model and task remains costly in labor, expertise, and compute.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Data curation is a first-order design choice in machine learning, yet tailoring training data to a downstream model and task remains costly in labor, expertise, and compute.

进一步看，论文的核心做法或实验重点可以概括为：Datasets are therefore often processed through fixed pipelines and reused across applications.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Data curation is a first-order design choice in machine learning, yet tailoring training data to a downstream model and task remains costly in labor, expertise, and compute. Datasets are therefore often processed through fixed pipelines and reused across applications. We show that this assumption is fragile: across 55 dataset--model tasks spanning biological domains, the same curation recipe can help one model while hurting another. Effective curation must adapt to the downstream setting, motivating automated search over data recipes. We first build an agentic system that searches for curation policies at deployment, improving data utility via \textit{test-time curation (TTC)}. Although achieving performance gains, its search is driven largely by recent feedback and remains local. Adding persistent memory helps the agent retain evidence across iterations and reveals a deeper problem: it forms claims that extend beyond the conditions in which they were observed, sometimes abandoning an entire strategy after a single unsuccessful trial. To address this problem, we introduce CaliMem, a calibrated-memory agentic loop that requires the agent to predict the outcome of each proposed policy before executing it. Comparing this prediction with the observed result gives the agent a \textit{reality check} on the claims behind its proposal. It uses the prediction error to retain supported claims, revise mistaken ones, and specify the conditions under which a conclusion holds. This makes the agent's beliefs testable, reduces overgeneralization, and supports more effective long-horizon exploration. Across biological and LLM post-training tasks, CaliMem consistently outperforms fixed curation baselines and published methods, and exceeds full-data training by up to 19.4\%. Code is open-sourced.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
