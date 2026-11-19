# MemoSync: Co-Managing Developer-Agent Metamemory Across Contexts

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.24165v1
- Published: 2026-11-18
- Updated: 2026-11-18
- Authors: Baiqiao Zhang, Junze Li, Chunyang Luo, Yuying Tang, Wenshuo Zhang, Shiyuan Piao, Dingdong Liu, Shuai Ma, Xiaojuan Ma
- Tags: agent, context
- Categories: cs.HC, cs.SE
- URL: http://arxiv.org/abs/2611.24165v1

## One-Sentence Summary
AI coding agents increasingly manage what context carries across sessions and projects, but developers have limited visibility into what these agents store, retrieve, and apply.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：AI coding agents increasingly manage what context carries across sessions and projects, but developers have limited visibility into what these agents store, retrieve, and apply.

进一步看，论文的核心做法或实验重点可以概括为：This opacity creates a metamemory problem: the developer's meta-level judgments about what should be remembered are separated from the agent's object-level memory operations, disrupting the monitoring and control that...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：agent memory
- 来源分类信息：cs.HC, cs.SE

## Abstract Snapshot
AI coding agents increasingly manage what context carries across sessions and projects, but developers have limited visibility into what these agents store, retrieve, and apply. This opacity creates a metamemory problem: the developer's meta-level judgments about what should be remembered are separated from the agent's object-level memory operations, disrupting the monitoring and control that keep the two levels aligned. We conducted a formative study with 12 developers and identified what they want to monitor and control across four dimensions of agent memory use. Based on these findings, we designed MemoSync, a co-management system that treats agent memory as a shared, operable representation: the agent proposes memory candidates and reports which items it uses, and the developer reviews, edits, and scopes them. In a between-subjects study (N=132) against two baselines, MemoSync participants achieved significantly higher task performance and the highest mean developer-agent memory alignment. In an exploratory mediation analysis, the alignment advantage was primarily driven by improved monitoring accuracy. Despite performing substantially more monitoring and control actions, participants reported no increase in perceived workload. A week-long deployment with nine developers showed that memory monitoring and control fit into everyday development work. MemoSync is open-sourced at https://github.com/SLEEPYBQ/MemoSync.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
