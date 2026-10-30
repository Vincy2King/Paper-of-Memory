# Judging Before Propagation: Task-Graph Contextual Integrity for Multi-Agent Privacy

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.39532v1
- Published: 2026-10-29
- Updated: 2026-10-29
- Authors: Hengyu Wu, Blaise Delattre, Yang Cao
- Tags: agent, benchmark, context
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2610.39532v1

## One-Sentence Summary
Multi-agent LLM systems increasingly rely on persistent memory and inter-agent communication.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multi-agent LLM systems increasingly rely on persistent memory and inter-agent communication.

进一步看，论文的核心做法或实验重点可以概括为：These capabilities create privacy risks that extend beyond individual interactions: a release appropriate in isolation may become inappropriate when combined with information previously disclosed to a recipient or...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Multi-agent LLM systems increasingly rely on persistent memory and inter-agent communication. These capabilities create privacy risks that extend beyond individual interactions: a release appropriate in isolation may become inappropriate when combined with information previously disclosed to a recipient or propagated to downstream agents along the planned workflow. Existing Contextual Integrity (CI) mechanisms for agentic systems typically rely on local judgments that assess each disclosure in isolation, with or without regard to the recipient's history, but do not account for how information propagates downstream. However, compliance at the current boundary does not guarantee appropriateness across the workflow. We introduce Task-Graph Contextual Integrity (TG-CI), to our knowledge the first task-graph-native formalization of Contextual Integrity for multi-agent systems. TG-CI represents a workflow as a Multi-Agent Task Graph (MATG) and extends CI from atomic transfers to stateful, graph-level information flows by jointly considering an item's intended propagation scope and recipients' evolving disclosure states. We operationalize TG-CI through propagation-scoped authorization under two complementary policies: Full-Scope, which requires admissibility across the complete downstream scope, and Auto-Region, which confines each item to its maximal admissible region using lightweight frontier gates. We further introduce MAPLE-Bench, a benchmark of 144 cases across four scenarios that jointly vary MATG topology, disclosure history, compromised-agent placement, and item-level privacy policies. In our primary experimental configuration, TG-CI reduces the mean unauthorized disclosure count by 85.8-94.1% relative to the Local-History CI baseline, while retaining 93.6-96.1% of the baseline's task accuracy, with the two enforcement policies providing complementary privacy--cost--utility trade-offs.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
