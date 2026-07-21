# RECON: Benchmarking Agent Memory for Compositional Reasoning over Long Contexts

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.16716v1
- Published: 2026-07-18
- Updated: 2026-07-18
- Authors: Mihir Shriniwas Arya
- Tags: agent, benchmark, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.16716v1

## One-Sentence Summary
Large language models and LLM-based agents are widely used as personal chat assistants, enterprise copilots, and autonomous workflow agents.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models and LLM-based agents are widely used as personal chat assistants, enterprise copilots, and autonomous workflow agents.

进一步看，论文的核心做法或实验重点可以概括为：In all these applications, memory (the ability to retain, access, and reason over information accumulated over long contexts and multiple interactions) plays a crucial role in determining the reliability of any agent.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：agent memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language models and LLM-based agents are widely used as personal chat assistants, enterprise copilots, and autonomous workflow agents. In all these applications, memory (the ability to retain, access, and reason over information accumulated over long contexts and multiple interactions) plays a crucial role in determining the reliability of any agent. We introduce RECON (Reasoning over Extended Contexts with Obfuscated Narratives), a benchmark for evaluating compositional reasoning over long contexts. RECON spans 24 case files across three domains (criminal, medical, and financial), each ranging from 50k to 100k tokens, and tests agents on six memory intensive tasks: reconstructing multi-hop evidence chains, propagating cascading invalidations, resolving source conflicts, counterfactual reasoning, satisfying temporal constraints, and temporal fact retrieval. Recent memory benchmarks evaluate whether agents can retrieve scattered facts or detect if a fact has changed whereas RECON evaluates what happens after the change, whether agents can trace which downstream conclusions are affected, which survive through independent support, and how alternative timelines would have unfolded. Our evaluation reveals substantial limitations across current architectures: even the strongest non-Oracle system reaches only 22.4% Accuracy, with retrieval and reasoning each surfacing as challenges.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
