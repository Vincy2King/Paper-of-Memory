# Jacobian-Causal Memory Control for Persistent Memory in Language Model Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.08779v1
- Published: 2026-11-05
- Updated: 2026-11-05
- Authors: Marvin Danig
- Tags: benchmark, retrieval
- Categories: cs.AI, cs.CL, cs.LG
- URL: http://arxiv.org/abs/2611.08779v1

## One-Sentence Summary
Persistent-memory systems choose not only which records are retrieved but which prior information can alter current inference.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent-memory systems choose not only which records are retrieved but which prior information can alter current inference.

进一步看，论文的核心做法或实验重点可以概括为：We propose Jacobian-causal memory control (JCMC), which represents each authorized memory intervention by a predicted influence signature in a shared behavioral measurement space, selects interventions against a...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI, cs.CL, cs.LG

## Abstract Snapshot
Persistent-memory systems choose not only which records are retrieved but which prior information can alter current inference. We propose Jacobian-causal memory control (JCMC), which represents each authorized memory intervention by a predicted influence signature in a shared behavioral measurement space, selects interventions against a target effect and side-effect budget, and compares predicted with observed effects before retaining or rolling back the intervention. Under explicit smoothness and bounded-estimation assumptions, we prove a quadratic local-approximation bound, characterize the target effects reachable by a set of signatures, bound selection regret under signature error, and bound non-additive interactions between simultaneous memories. The paper reports no benchmark measurements; it defines a paired counterfactual estimator and an evaluation protocol comparing JCMC with relevance, graph, and policy-filtered retrieval baselines. The central claim is narrowed or falsified if those simpler baselines match effect targeting, side-effect control, and rollback utility under equal model, memory, policy, and cost budgets.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
