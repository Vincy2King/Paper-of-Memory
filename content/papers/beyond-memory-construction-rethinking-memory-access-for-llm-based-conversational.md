# Beyond Memory Construction: Rethinking Memory Access for LLM-based Conversational Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.33226v1
- Published: 2026-09-27
- Updated: 2026-09-27
- Authors: Donghua Cai, Yongheng Deng, Yifei Wang, Zijun Shen, Ju Ren
- Tags: agent, context, conversation, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2609.33226v1

## One-Sentence Summary
Memory is a core component of conversational agents, enabling coherent and context-aware behavior over long interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory is a core component of conversational agents, enabling coherent and context-aware behavior over long interactions.

进一步看，论文的核心做法或实验重点可以概括为：Recent approaches commonly rely on LLM-based memory construction, where raw interactions are rewritten into structured memory units and later retrieved via a RAG pipeline.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, retrieval
- 检索关键词命中：conversational memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Memory is a core component of conversational agents, enabling coherent and context-aware behavior over long interactions. Recent approaches commonly rely on LLM-based memory construction, where raw interactions are rewritten into structured memory units and later retrieved via a RAG pipeline. While effective in controlled settings, we show that this paradigm breaks down in long-horizon, high-entropy conversations: memory construction becomes increasingly lossy and unstable as context length and information complexity grow, and incurs prohibitive cost due to repeated LLM invocation. To address these limitations, we propose Threader, a memory system that shifts the focus from memory construction to efficient, structure-aware access over raw interactions. Instead of rewriting interactions, Threader preserves them as first-class memory, organizes them into topic-coherent segments via lightweight incremental segmentation, and enables accurate retrieval through multi-view representation. At query time, it performs multi-signal retrieval that combines segment-level access with localized evidence matching, ensuring both completeness and coherence. Extensive experiments demonstrate that Threader consistently improves answer accuracy and evidence recall, while significantly reducing the memory construction overhead.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
