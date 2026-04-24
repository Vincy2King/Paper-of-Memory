# Experience Compression Spectrum: Unifying Memory, Skills, and Rules in LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.15877v1
- Published: 2026-04-17
- Updated: 2026-04-17
- Authors: Xing Zhang, Guanghui Wang, Yanwei Cui, Wei Qiu, Ziyuan Li, Bing Zhu, Peiyang He
- Tags: agent, compression, context, episodic, retrieval
- Categories: cs.AI, cs.CL, cs.MA
- URL: http://arxiv.org/abs/2604.15877v1

## One-Sentence Summary
As LLM agents scale to long-horizon, multi-session deployments, efficiently managing accumulated experience becomes a critical bottleneck.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：As LLM agents scale to long-horizon, multi-session deployments, efficiently managing accumulated experience becomes a critical bottleneck.

进一步看，论文的核心做法或实验重点可以概括为：Agent memory systems and agent skill discovery both address this challenge -- extracting reusable knowledge from interaction traces -- yet a citation analysis of 1,136 references across 22 primary papers reveals a...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression, context, episodic, retrieval
- 检索关键词命中：agent memory, episodic memory
- 来源分类信息：cs.AI, cs.CL, cs.MA

## Abstract Snapshot
As LLM agents scale to long-horizon, multi-session deployments, efficiently managing accumulated experience becomes a critical bottleneck. Agent memory systems and agent skill discovery both address this challenge -- extracting reusable knowledge from interaction traces -- yet a citation analysis of 1,136 references across 22 primary papers reveals a cross-community citation rate below 1%. We propose the \emph{Experience Compression Spectrum}, a unifying framework that positions memory, skills, and rules as points along a single axis of increasing compression (5--20$\times$ for episodic memory, 50--500$\times$ for procedural skills, 1,000$\times$+ for declarative rules), directly reducing context consumption, retrieval latency, and compute overhead. Mapping 20+ systems onto this spectrum reveals that every system operates at a fixed, predetermined compression level -- none supports adaptive cross-level compression, a gap we term the \emph{missing diagonal}. We further show that specialization alone is insufficient -- both communities independently solve shared sub-problems without exchanging solutions -- that evaluation methods are tightly coupled to compression levels, that transferability increases with compression at the cost of specificity, and that knowledge lifecycle management remains largely neglected. We articulate open problems and design principles for scalable, full-spectrum agent learning systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
