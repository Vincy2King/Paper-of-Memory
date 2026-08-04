# FedWorld: Scope-Aware Federation of Agent World Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.01561v1
- Published: 2026-08-03
- Updated: 2026-08-03
- Authors: Yuchao Hou
- Tags: agent
- Categories: cs.HC
- URL: http://arxiv.org/abs/2608.01561v1

## One-Sentence Summary
Large language model (LLM) agents learn world dynamics from local interaction experience to support subsequent planning and action selection.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents learn world dynamics from local interaction experience to support subsequent planning and action selection.

进一步看，论文的核心做法或实验重点可以概括为：However, the experience available to a single client is often incomplete, which motivates sharing knowledge across clients.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.HC

## Abstract Snapshot
Large language model (LLM) agents learn world dynamics from local interaction experience to support subsequent planning and action selection. However, the experience available to a single client is often incomplete, which motivates sharing knowledge across clients. Existing federated methods mainly aggregate model parameters, while agent memory-sharing methods commonly pool trajectories, memories, or rules without checking whether they remain valid for each client. This assumption is problematic because the same abstract action may produce different effects under different policies, environments, or exception conditions. Consequently, a rule supported by most clients may overwrite correct knowledge held by a minority client. To address this problem, we propose FEDWORLD, a scope-aware federated world-model protocol that exchanges structured abstract transition rules. Each client converts private transitions into normalized rules, and the server aligns related rules to identify each rule supporting and contradicting evidence across clients. The resulting evidence determines whether a rule is shared, cluster-specific, private, or unresolved. Each target client retains its local rules and accepts federated updates only for uncovered cases whose inferred scope is compatible; ambiguous rules are withheld. Experiments on $τ$-bench and ALFWorld show that FEDWORLD reduces negative transfer under conflicting dynamics while retaining useful cross-client transfer, leading to fewer state regressions, repeated actions, and excess steps, as well as higher task success.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
