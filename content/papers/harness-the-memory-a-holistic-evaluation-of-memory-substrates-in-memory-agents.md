# Harness the Memory: A Holistic Evaluation of Memory Substrates in Memory Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.15008v1
- Published: 2026-08-15
- Updated: 2026-08-15
- Authors: Wei-Chieh Huang, Weizhi Zhang, Yuchen Wu, Yankai Chen, Eric Hanchen Jiang, Wooseong Yang, Yiwei Yang, Henry Peng Zou, Hanrong Zhang, Ying Nian Wu, Haolun Wu, Kai-Wei Chang, Philip S. Yu, Xue Liu, Aylin Caliskan
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.15008v1

## One-Sentence Summary
Memory is becoming core infrastructure for long-horizon LLM agents, yet existing evaluations offer limited guidance on which memory substrate, namely the underlying medium in...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory is becoming core infrastructure for long-horizon LLM agents, yet existing evaluations offer limited guidance on which memory substrate, namely the underlying medium in which memory is represented and stored,...

进一步看，论文的核心做法或实验重点可以概括为：We present a controlled harness evaluation of memory substrates for memory-augmented agents, covering dense and sparse indices, text records, structural stores, hierarchical stores, refinement-based memories,...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory, memory augmented, memory-augmented
- 来源分类信息：cs.CL

## Abstract Snapshot
Memory is becoming core infrastructure for long-horizon LLM agents, yet existing evaluations offer limited guidance on which memory substrate, namely the underlying medium in which memory is represented and stored, should be used under different operating regimes. We present a controlled harness evaluation of memory substrates for memory-augmented agents, covering dense and sparse indices, text records, structural stores, hierarchical stores, refinement-based memories, parametric updates, and activation-compatible context mechanisms. Across three backbone models and four benchmark suites spanning user-centric question answering and agent-centric decision-making, we instrument 26 performance and efficiency metrics under a unified harness. Our results show that no single substrate consistently dominates: broad retrieval benefits long-context factual QA, while excessive retrieval can harm sequential decision-making by shifting attention away from action-critical context. Scalability introduces a further routing axis, as substrates that perform well at moderate history lengths can become costly or brittle at longer horizons. These findings motivate substrate routing as a necessary component of adaptive agent memory systems and provide empirical guidance for designing efficient, reliable, and regime-aware long-term memory for LLM agents. Code will be made available upon acceptance.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
