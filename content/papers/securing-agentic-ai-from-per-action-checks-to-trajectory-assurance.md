# Securing Agentic AI: From Per-Action Checks to Trajectory Assurance

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.01558v1
- Published: 2026-08-03
- Updated: 2026-08-03
- Authors: Alireza Lotfi, Subangkar Karmaker Shanto, Imtiaz Karim, Elisa Bertino
- Tags: agent
- Categories: cs.AI, cs.CR, cs.MA
- URL: http://arxiv.org/abs/2608.01558v1

## One-Sentence Summary
Autonomous agents are increasingly used to execute consequential tasks in environments governed by operational constraints, organizational policies, regulatory requirements, and...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Autonomous agents are increasingly used to execute consequential tasks in environments governed by operational constraints, organizational policies, regulatory requirements, and technical standards.

进一步看，论文的核心做法或实验重点可以概括为：Their safety is therefore determined not by the correctness of individual actions, but by whether their overall behavior remains consistent with the rules and invariants of the systems in which they operate.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.AI, cs.CR, cs.MA

## Abstract Snapshot
Autonomous agents are increasingly used to execute consequential tasks in environments governed by operational constraints, organizational policies, regulatory requirements, and technical standards. Their safety is therefore determined not by the correctness of individual actions, but by whether their overall behavior remains consistent with the rules and invariants of the systems in which they operate. As large language model (LLM)-based agents become more autonomous and increasingly delegate tasks across organizational boundaries, securing them evolves from a single challenge into a broad and interconnected landscape spanning the entire agentic stack. At the single-agent level, untrusted inputs through prompts, memory, retrieved knowledge, and tool interfaces create attack surfaces. In multi-agent settings, delegation and communication introduce challenges related to identity, trust, capability control, and decision transparency, while the underlying model routing and execution control plane remains vulnerable to manipulation and to unverified model provenance. Perhaps the most fundamental challenge is behavioral containment: sequences of individually permissible actions may collectively violate system-level constraints and safety invariants. At the broader level, supply-chain integrity, provenance, accountability, and end-to-end observability remain largely open problems. A common principle unifies these directions: security must become a verifiable property of the architectures, protocols, and runtimes that govern agent behavior, rather than an optional layer of guidance. Charting these challenges provides a roadmap toward trustworthy autonomous agent deployment.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
