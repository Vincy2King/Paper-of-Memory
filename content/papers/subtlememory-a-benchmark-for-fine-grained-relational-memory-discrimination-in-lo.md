# SubtleMemory: A Benchmark for Fine-Grained Relational Memory Discrimination in Long-Horizon AI Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.05761v1
- Published: 2026-06-04
- Updated: 2026-06-04
- Authors: Wenxuan Wang, Haoyu Sun, Fukuan Hou, Mingyang Song, Weinan Zhang, Yu Cheng, Yang Yang
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2606.05761v1

## One-Sentence Summary
Persistent AI assistants, such as OpenClaw, accumulate large collections of related memories over long-term interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent AI assistants, such as OpenClaw, accumulate large collections of related memories over long-term interactions.

进一步看，论文的核心做法或实验重点可以概括为：As these memories grow, they may reinforce one another, diverge across contexts, or directly conflict, making correct assistance depend on memory relations rather than isolated recall.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Persistent AI assistants, such as OpenClaw, accumulate large collections of related memories over long-term interactions. As these memories grow, they may reinforce one another, diverge across contexts, or directly conflict, making correct assistance depend on memory relations rather than isolated recall. Existing long-term memory benchmarks rarely probe how agents preserve and utilize such relations during downstream tasks. To address this gap, we introduce SubtleMemory, a benchmark for fine-grained relational memory discrimination in long-running AI agents. SubtleMemory constructs relation-controlled latent semantic artifacts whose variants instantiate complementary, nuanced, or contradictory relations, and embeds them into realistic user-agent histories, requiring agents to recover distributed relational structures during later queries and instructions. The benchmark contains 1,522 evaluation instances over 10 long histories, grounded in 1,090 relation-controlled memory-variant sets and spanning user-related and non-user-related queries. Evaluating six standalone memory systems, two Claw-style agents with native memory modules, and three Claw-style agents with plugin memory modules, we find that current systems remain weak on fine-grained relational memory discrimination. We further introduce diagnostic protocols that reveal distinct capability profiles across memory preservation, retrieval, and downstream reasoning stages.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
