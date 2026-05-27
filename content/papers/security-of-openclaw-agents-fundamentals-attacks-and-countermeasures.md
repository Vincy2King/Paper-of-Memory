# Security of OpenClaw Agents: Fundamentals, Attacks, and Countermeasures

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.25435v1
- Published: 2026-05-25
- Updated: 2026-05-25
- Authors: Yuntao Wang, Jianle Ba, Han Liu, Yanghe Pan, Jintao Wei, Zhou Su, Tom H. Luan, Linkang Du
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.25435v1

## One-Sentence Summary
The rapid evolution of large language model (LLM)-driven autonomous agents has given rise to OpenClaw, a new class of open-source agent frameworks that operate as continuously...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：The rapid evolution of large language model (LLM)-driven autonomous agents has given rise to OpenClaw, a new class of open-source agent frameworks that operate as continuously running, skill-augmented systems with...

进一步看，论文的核心做法或实验重点可以概括为：Such capabilities enable OpenClaw agents to autonomously execute complex, multi-step tasks and interact seamlessly with external applications, but simultaneously introduce a substantially enlarged attack surface.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
The rapid evolution of large language model (LLM)-driven autonomous agents has given rise to OpenClaw, a new class of open-source agent frameworks that operate as continuously running, skill-augmented systems with persistent memory, multi-channel interaction, and high degrees of autonomy. Such capabilities enable OpenClaw agents to autonomously execute complex, multi-step tasks and interact seamlessly with external applications, but simultaneously introduce a substantially enlarged attack surface. In particular, the combination of high-privilege operations and persistent memory exposes OpenClaw agents to various emerging threats, including skill poisoning, cognitive manipulation, multi-agent cascading failures, and supply-chain vulnerabilities. In this survey, we present a comprehensive study of the security landscape of OpenClaw agents. We first examine the general architecture and key characteristics that distinguish OpenClaw agents from traditional AI agent systems. We categorize existing security and privacy threats into a layered framework and analyze how vulnerabilities arise during agent reasoning, action execution, and external interaction. Representative defense mechanisms are also reviewed to draw the current defense landscape. Finally, several unresolved issues related to the reliability and trustworthiness of OpenClaw ecosystems are discussed.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
