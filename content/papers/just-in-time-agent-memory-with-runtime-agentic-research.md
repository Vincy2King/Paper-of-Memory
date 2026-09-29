# Just-In-Time Agent Memory with Runtime Agentic Research

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.34385v1
- Published: 2026-09-28
- Updated: 2026-09-28
- Authors: Bingyu Yan, Chaofan Li, Hongjin Qian, Shuqi Lu, Chaozhuo Li, Zheng Liu
- Tags: agent, benchmark, context
- Categories: cs.CL, cs.AI, cs.IR, cs.LG
- URL: http://arxiv.org/abs/2609.34385v1

## One-Sentence Summary
Memory is critical for AI agents.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory is critical for AI agents.

进一步看，论文的核心做法或实验重点可以概括为：Many existing agent-memory systems follow an Ahead-of-Time (AOT) design, constructing memory before a specific request arrives.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL, cs.AI, cs.IR, cs.LG

## Abstract Snapshot
Memory is critical for AI agents. Many existing agent-memory systems follow an Ahead-of-Time (AOT) design, constructing memory before a specific request arrives. While this reduces online serving cost, such request-agnostic memory construction can discard fine-grained information that later becomes important. To address this limitation, we propose Just-In-Time Agent Memory (JAM), a trainable framework for query-conditioned context construction at runtime. A Memorizer preserves complete raw histories in a hierarchical page-store with compact navigational summaries, while a Researcher iteratively retrieves, inspects, and integrates evidence for each request. To train these memory-use behaviors, we introduce Memory-Gym, an evidence-grounded data synthesis pipeline covering nine task types across six domains, and optimize the Researcher through verified-trajectory supervised fine-tuning followed by Hint-guided Group Relative Policy Optimization. We demonstrate the effectiveness of JAM across a variety of benchmarks on agent memory and long-context processing, where it achieves stronger task performance than AOT-style memory systems while remaining substantially more efficient than prior trained agentic memory approaches. To support reproducibility and future research, we release our anonymized source code at https://github.com/VectorSpaceLab/general-agentic-memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
