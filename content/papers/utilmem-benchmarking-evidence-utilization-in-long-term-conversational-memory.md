# UTILMEM: Benchmarking Evidence Utilization in Long-Term Conversational Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.30508v1
- Published: 2026-08-31
- Updated: 2026-08-31
- Authors: Peijun Qing, Fobo Shi, Soroush Vosoughi
- Tags: agent, benchmark, conversation, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.30508v1

## One-Sentence Summary
Long-term memory is increasingly important for conversational agents, yet existing benchmarks primarily measure memory through pointwise factual recall: whether a system can...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory is increasingly important for conversational agents, yet existing benchmarks primarily measure memory through pointwise factual recall: whether a system can recover isolated facts or event-level...

进一步看，论文的核心做法或实验重点可以概括为：Real-world memory use, however, often requires a more demanding capability: integrating distributed, implicit, and noisy evidence across extended interaction histories into coherent, task-oriented outputs.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, long-term, retrieval
- 检索关键词命中：conversational memory, long-term memory, memory augmented, memory benchmark, memory benchmarks, memory-augmented
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-term memory is increasingly important for conversational agents, yet existing benchmarks primarily measure memory through pointwise factual recall: whether a system can recover isolated facts or event-level details from prior interactions. Real-world memory use, however, often requires a more demanding capability: integrating distributed, implicit, and noisy evidence across extended interaction histories into coherent, task-oriented outputs. We call this capability memory utilization. Here, we introduce UtilMem, a diagnostic benchmark comprising 1,717 instances across five domains, designed to evaluate four underexplored aspects of memory utilization: reasoning over dense histories, identifying implicitly relevant memories, synthesizing distributed evidence into summaries, analyses, or plans, and resisting interference from semantically similar distractors. Evaluating a diverse set of retrieval-based and memory-augmented systems, we find that strong performance on conventional factual-memory benchmarks does not reliably translate into effective memory utilization. Moreover, retrieval alone is insufficient: even when relevant evidence is successfully recovered, systems frequently fail to integrate information across sessions or to distinguish useful evidence from plausible distractors. These findings expose a substantial gap between accessing stored information and using it effectively, and suggest that progress in long-term conversational memory will require architectures that explicitly support evidence integration and robustness to retrieval interference. Code is available at https://github.com/peijunallin/UtilMem.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
