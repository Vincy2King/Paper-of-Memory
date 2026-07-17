# MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.14651v1
- Published: 2026-07-16
- Updated: 2026-07-16
- Authors: Jifeng Gao, Kang Xia, Yi Zhang, Xiaobin Hong, Mingkai Lin, Xingshen Wei, Wenzhong Li, Sanglu Lu
- Tags: agent, benchmark, context, retrieval
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2607.14651v1

## One-Sentence Summary
Persistent external memory enhances agent continuity but introduces persistent security vulnerabilities: adversarial content can be injected via standard interaction channels,...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent external memory enhances agent continuity but introduces persistent security vulnerabilities: adversarial content can be injected via standard interaction channels, retained across turns, and later distort...

进一步看，论文的核心做法或实验重点可以概括为：To address this challenge, we propose MemPoison, a comprehensive benchmark and analysis framework featuring 1227 hand-validated cases across four attack types, three injection channels, and three representative memory...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Persistent external memory enhances agent continuity but introduces persistent security vulnerabilities: adversarial content can be injected via standard interaction channels, retained across turns, and later distort downstream behavior. To address this challenge, we propose MemPoison, a comprehensive benchmark and analysis framework featuring 1227 hand-validated cases across four attack types, three injection channels, and three representative memory substrates, evaluated on seven open-weight and three closed-weight model families. We introduce a three-tier taxonomy: (L1) direct single-record corruption, (L2) compositional multi-record corruption and (L3) context-triggered dormant corruption. Our evaluations reveal a distinct defense frontier: while baseline write-time defenses, such as consistency checks, substantially suppress direct L1 attacks, they fail to reliably suppress L2 and L3 attacks. Through mechanistic influence decomposition (MID), we demonstrate structural blind spots in write-time defenses, which admit seemingly benign records that later become harmful through joint retrieval composition or trigger-conditioned activation. Our findings advocate for shifting from static filtering to adaptive, context-sensitive memory defense strategies.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
