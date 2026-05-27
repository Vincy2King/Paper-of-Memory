# Anticipate and Learn: Unleashing Idle-Time Compute in Proactive Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.25971v2
- Published: 2026-05-25
- Updated: 2026-05-26
- Authors: Haoyi Hu, Qirong Lyu, Xianghan Kong, Weiwen Liu, Jianghao Lin, Zixuan Guo, Yan Xu, Yasheng Wang, Weinan Zhang, Yong Yu
- Tags: agent, benchmark
- Categories: cs.CL, cs.IR, cs.MA
- URL: http://arxiv.org/abs/2605.25971v2

## One-Sentence Summary
While AI agents demonstrate remarkable capabilities in reasoning and tool use, they remain fundamentally reactive: they compute responses only after explicit user prompts.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：While AI agents demonstrate remarkable capabilities in reasoning and tool use, they remain fundamentally reactive: they compute responses only after explicit user prompts.

进一步看，论文的核心做法或实验重点可以概括为：This paradigm ignores a critical opportunity: the idle time between interactions is largely wasted, leaving agents unable to prepare for future user needs.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CL, cs.IR, cs.MA

## Abstract Snapshot
While AI agents demonstrate remarkable capabilities in reasoning and tool use, they remain fundamentally reactive: they compute responses only after explicit user prompts. This paradigm ignores a critical opportunity: the idle time between interactions is largely wasted, leaving agents unable to prepare for future user needs. To bridge this gap, we introduce ProAct, a proactive agent architecture that leverages idle-time compute to anticipate and fulfill likely upcoming user needs. By analyzing evolving dialogue history together with persistent memory, ProAct predicts upcoming needs and iteratively acquires information, allowing the agent to resolve knowledge gaps and prepare evidence before the user initiates a query. To rigorously evaluate proactive capabilities, we also introduce ProActEval, a comprehensive benchmark comprising 200 scenarios across 40 domains, featuring predictable need chains and diverse user cognitive profiles. Empirical results demonstrate significant advantages over reactive baselines. ProAct accelerates task completion by reducing required turns by 14.8%, decreases user effort by 11.7%, and cuts hallucination rates by 28.1% on ProActEval. Furthermore, MemBench evaluations confirm that ProAct achieves state-of-the-art reflective accuracy, underscoring its sustained and robust performance.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
