# Action Conditioned Bisimulation For GUI Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.38778v1
- Published: 2026-09-30
- Updated: 2026-09-30
- Authors: Hongbo Zhang, Liuyang Song, Quanquan Li, Daqian Yang, Yan Wen, Zhengtao Yao
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.38778v1

## One-Sentence Summary
An agent that remembers what it did on a web page must decide when two pages count as the same.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：An agent that remembers what it did on a web page must decide when two pages count as the same.

进一步看，论文的核心做法或实验重点可以概括为：Memories built on observation similarity merge pages that look alike but behave differently, and GUIs are full of such pages: two tabs of one widget or two rows of one menu answer the same click differently.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
An agent that remembers what it did on a web page must decide when two pages count as the same. Memories built on observation similarity merge pages that look alike but behave differently, and GUIs are full of such pages: two tabs of one widget or two rows of one menu answer the same click differently. We define the merge rule as an action-conditioned bisimulation over the empirical predictive state graph a frozen agent fills as it acts. Two states merge only when their shared actions lead to agreeing outcomes and successor blocks under an affordance label. Observation similarity never enters the rule, and nothing is trained. It replaces the merge rule of an existing outcome-value memory, so a closed-loop comparison isolates it. On MiniWoB++ it raises success rate over a memoryless agent, while a control taking identical exploratory detours, the prior successor-representation merge, and the same criterion without action conditioning change nothing.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
