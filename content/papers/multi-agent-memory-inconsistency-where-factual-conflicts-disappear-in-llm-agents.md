# Multi-Agent Memory Inconsistency: Where Factual Conflicts Disappear in LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.22245v1
- Published: 2026-11-17
- Updated: 2026-11-17
- Authors: Hejia Zhang, Zhongming Yu, Yimin Ding, Wei-Ting Chen, Hengjia Yu, Wentao Ni, Yijun Liu, Cong Xu, Xin Chen, Matrix Yao, Fan Zhao, Jishen Zhao
- Tags: agent, benchmark, context, retrieval
- Categories: cs.AI, cs.MA
- URL: http://arxiv.org/abs/2611.22245v1

## One-Sentence Summary
Multi-agent delegation lets LLM systems distribute evidence collection across workers with separate contexts.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multi-agent delegation lets LLM systems distribute evidence collection across workers with separate contexts.

进一步看，论文的核心做法或实验重点可以概括为：This creates a consistency challenge: facts retrieved by workers may be missing from the evidence available to the lead for a joint conclusion.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI, cs.MA

## Abstract Snapshot
Multi-agent delegation lets LLM systems distribute evidence collection across workers with separate contexts. This creates a consistency challenge: facts retrieved by workers may be missing from the evidence available to the lead for a joint conclusion. We introduce a benchmark and evidence-flow profiler for studying multi-agent memory inconsistency through controlled factual conflicts in Harvey LAB document-review tasks. Pooled across three models with comparable generation spending, requiring delegation increases retrieval of both conflicting claims from 50.2% to 68.7% relative to single-agent execution, yet conflict detection falls from 16.2% to 13.2%. Within this setting, workers report both claims for only 35.2% of retrieved pairs, and pooled matched comparisons show higher detection than single-agent execution when one worker reads both claims but lower detection when the claims are split across workers. Worker-to-lead handoffs are a central target for improving conflict detection in multi-agent LLMs.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
