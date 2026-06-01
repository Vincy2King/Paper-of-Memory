# Beyond Static Dialogues: Benchmarking Realistic, Heterogeneous, and Evolving Long-Term Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.31086v1
- Published: 2026-05-29
- Updated: 2026-05-29
- Authors: Han Zhang, Zihao Tang, Xin Yu, Xiao Liu, Yeyun Gong, Haizhen Huang, Yan Lu, Weiwei Deng, Feng Sun, Qi Zhang, Hanfang Yang
- Tags: benchmark, context, long-term, retrieval
- Categories: cs.CL, cs.IR
- URL: http://arxiv.org/abs/2605.31086v1

## One-Sentence Summary
In existing memory benchmarks for Large Language Models (LLMs), the evaluated dialogue sessions often lack long-term semantic consistency, and the underlying personas tend to be...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：In existing memory benchmarks for Large Language Models (LLMs), the evaluated dialogue sessions often lack long-term semantic consistency, and the underlying personas tend to be flat and static.

进一步看，论文的核心做法或实验重点可以概括为：Furthermore, in real-world scenarios, interactions between users and assistants involve more diverse, heterogeneous data streams, such as documents and emails.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, long-term, retrieval
- 检索关键词命中：long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.CL, cs.IR

## Abstract Snapshot
In existing memory benchmarks for Large Language Models (LLMs), the evaluated dialogue sessions often lack long-term semantic consistency, and the underlying personas tend to be flat and static. Furthermore, in real-world scenarios, interactions between users and assistants involve more diverse, heterogeneous data streams, such as documents and emails. These shortcomings significantly limit the realism and effectiveness of current evaluations. To address these limitations, we introduce RHELM (Realistic, Heterogeneous, and Evolving Long-term Memory). Driven by meticulously crafted user profiles and a novel LOOP (pLan-rOllout-evOlve-Prune) module, we construct realistic dialogues across diverse interaction scenarios that exhibit dynamic temporal evolution and long-term coherence. Crucially, these dialogues are deeply integrated with heterogeneous external sources synchronized with the user's temporal event trajectory. The resulting benchmark encompasses challenging question-answer pairs spanning seven inquiry types, with each question mapping to at least one of 27 critical memory characteristics that we identify as essential yet underexplored in current research. Comprehensive experiments across full-context models, retrieval-augmented generation (RAG) methods, and representative memory frameworks reveal that contemporary approaches still expose critical weaknesses in complex, real-world settings, particularly in resolving multi-source aggregation and real-world contextual reasoning.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
