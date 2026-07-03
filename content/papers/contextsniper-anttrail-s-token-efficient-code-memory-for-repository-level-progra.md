# ContextSniper: AntTrail's Token-Efficient Code Memory for Repository-Level Program Repair

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.01916v1
- Published: 2026-07-02
- Updated: 2026-07-02
- Authors: Chiwang Luk, Matin Mohammad Najafi, Zhifeng Jia, Wei Yang, Xiuchang Li, Jinwei Zhu, Yang Ren, Lei Chen, Gao Cong
- Tags: agent, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.01916v1

## One-Sentence Summary
Large language model agents can repair real repository issues, but they often spend large context budgets on whole-file reads, broad searches, and long terminal outputs where...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model agents can repair real repository issues, but they often spend large context budgets on whole-file reads, broad searches, and long terminal outputs where useful evidence is mixed with irrelevant...

进一步看，论文的核心做法或实验重点可以概括为：This paper presents ContextSniper, AntTrail's token-efficient code memory layer for repository-level program repair.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language model agents can repair real repository issues, but they often spend large context budgets on whole-file reads, broad searches, and long terminal outputs where useful evidence is mixed with irrelevant code and logs. This paper presents ContextSniper, AntTrail's token-efficient code memory layer for repository-level program repair. As the coding specialization of AntTrail's broader agent memory engine, ContextSniper implements the Sniper feature for precision evidence selection: it retrieves candidate code and runtime evidence, ranks it with hybrid retrieval signals, filters long outputs through an intention-aware context gate, and returns compact evidence packets while preserving recoverable source context outside the prompt. We evaluate ContextSniper on SWE-bench Lite with OpenClaw and Claude Code, using 50 task runs per host-agent condition. ContextSniper reduces total token use by 51.5% and logged cost by 36.4% for OpenClaw, and reduces total token use by 38.9% and estimated cost by 27.3% for Claude Code. Submitted-resolution rates decrease slightly, from 26.0% to 24.0% for OpenClaw and from 32.0% to 30.0% for Claude Code. ContextSniper's pilot testing scripts are open-sourced at https://github.com/Calluking/ContextSniper

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
