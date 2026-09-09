# Where to Look and What to Use: Retrieve-Localize-Generate for Long-Term Conversational Memory Question Answering

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.07093v1
- Published: 2026-09-07
- Updated: 2026-09-07
- Authors: Yifan Wang, Xinkui Lin, Yongxiu Xu, Shen Gao, Ruochen Yang, Kun Huang, Yubin Wang, Jie Wu, Wei Liu, Jian Luan, Hongbo Xu, Shuo Shang
- Tags: benchmark, context, conversation, long-term, retrieval
- Categories: cs.CL, cs.IR
- URL: http://arxiv.org/abs/2609.07093v1

## One-Sentence Summary
Retrieval-augmented generation (RAG) enables large language models (LLMs) to answer questions by accessing external knowledge and has been widely adopted for long-term...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Retrieval-augmented generation (RAG) enables large language models (LLMs) to answer questions by accessing external knowledge and has been widely adopted for long-term conversational memory question answering.

进一步看，论文的核心做法或实验重点可以概括为：However, existing methods suffer from two key challenges: (1) fragmented evidence scattered across temporally distant sessions, and (2) noisy content within retrieved sessions that triggers the lost-in-the-middle effect.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：conversational memory
- 来源分类信息：cs.CL, cs.IR

## Abstract Snapshot
Retrieval-augmented generation (RAG) enables large language models (LLMs) to answer questions by accessing external knowledge and has been widely adopted for long-term conversational memory question answering. However, existing methods suffer from two key challenges: (1) fragmented evidence scattered across temporally distant sessions, and (2) noisy content within retrieved sessions that triggers the lost-in-the-middle effect. To address these challenges, we propose MemLoc, a unified Retrieve-Localize-Generate framework for long-term conversational memory QA. For retrieval, MemLoc decomposes each session into multi-granularity memory units and performs query routing via an inner-memory graph with entropy-based granularity selection. It further models cross-session semantic and temporal dependencies through a cross-memory graph, enabling coarse-to-fine retrieval of top-K relevant memory candidates. For localization, we introduce a reasoning-based evidence locator trained with Self-reflective Hint Policy Optimization (SHPO), which performs progressive refinement by extracting query-relevant fragments within memory units to suppress noise and reranking across candidates to remove redundancy, producing a compact evidence set with lightweight location IDs. For generation, these IDs act as precise grounding signals that guide the LLM to the correct memory positions, mitigating the lost-in-the-middle effect while preserving original contextual integrity. Extensive experiments on four benchmarks demonstrate that MemLoc achieves state-of-the-art retrieval accuracy and response quality while maintaining efficiency. Our code is available at: https://github.com/Nikol-coder/MemLoc.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
