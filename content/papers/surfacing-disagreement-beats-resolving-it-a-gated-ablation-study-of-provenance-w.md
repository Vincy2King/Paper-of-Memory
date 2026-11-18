# Surfacing Disagreement Beats Resolving It: A Gated Ablation Study of Provenance-Weighted Memory for Multi-Agent Debate

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.22461v1
- Published: 2026-11-17
- Updated: 2026-11-17
- Authors: Ziaullah Khan, Abdul Rehman Khalid, Shrestha Nischal Lal, Nheng Vanchhay, Md Ariful Islam Mozumder, Hee-Cheol Kim
- Tags: agent, retrieval
- Categories: cs.MA, cs.CL
- URL: http://arxiv.org/abs/2611.22461v1

## One-Sentence Summary
Shared memory for multi-agent debate is usually built to resolve inconsistency: retrieval returns one winning fact and the disagreement disappears before any agent sees it.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Shared memory for multi-agent debate is usually built to resolve inconsistency: retrieval returns one winning fact and the disagreement disappears before any agent sees it.

进一步看，论文的核心做法或实验重点可以概括为：We ask whether that is correct.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.MA, cs.CL

## Abstract Snapshot
Shared memory for multi-agent debate is usually built to resolve inconsistency: retrieval returns one winning fact and the disagreement disappears before any agent sees it. We ask whether that is correct. In DebateGraph, four backends share one contract (read/write/snapshot), so five mechanisms from the agent-memory literature can be removed independently under a fixed budget, each gated on a pre-declared threshold. Across 39 runs one survives: preserving contradictions and passing the ranked conflict set to the debate, rather than collapsing it to a winner, improves F1 by +0.340 (95% CI [+0.267, +0.414]) and cuts attack success from 22 to 7 of 122 poisoned items (McNemar exact p=0.0003), at equal cost. Reaching it meant fixing a bottleneck in our harness: conflict sets are built only over retrieved edges, and our pre-declared cap left three quarters of planted contradictions unretrievable, first measuring the mechanism at +0.084. The effect replicates on two retrieval substrates and directionally on HotpotQA documents. No other mechanism survives, and two are worse than inert: once contradictions reach the prompt, a write trust-gate and the router's provenance features each cost accuracy (-0.075 and -0.096 F1). The gate fails structurally: poisoned objects are always entities the graph already contains, against 53% of gold, so groundedness scores the lie above a truthful first mention. We release the harness, attack set, and logs, and argue that silently reconciling memory is the assumption worth abandoning.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
