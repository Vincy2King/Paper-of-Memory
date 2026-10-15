# MemCode: Discrete Semantic Representations for Long-Term Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.19472v1
- Published: 2026-10-14
- Updated: 2026-10-14
- Authors: Xin Li, Liang Hu, Duoqian Miao, Ming Peng, Qi Zhang
- Tags: agent, context, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.19472v1

## One-Sentence Summary
Long-term memory remains a fundamental bottleneck for large language model (LLM) agents across sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory remains a fundamental bottleneck for large language model (LLM) agents across sessions.

进一步看，论文的核心做法或实验重点可以概括为：Existing systems typically adopt a write-then-retrieve paradigm, storing context-dependent dialogue fragments and retrieving them via nearest-neighbor search in a continuous embedding space.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term memory remains a fundamental bottleneck for large language model (LLM) agents across sessions. Existing systems typically adopt a write-then-retrieve paradigm, storing context-dependent dialogue fragments and retrieving them via nearest-neighbor search in a continuous embedding space. This design yields unstable access units and systematically misses logically related but lexically distant evidence. We propose MemCode, a long-term agent memory framework that couples retrieval-oriented writing with discrete associative retrieval. MemCode rewrites dialogue into self-contained atomic memory units (AMUs), maps AMUs into a learnable codebook with isomorphic semantic quantization (ISQ), and uses codebook co-occurrence topology as a retrieval path complementary to vector search. For long-term memory stores, MemCode separates online atomic writes from asynchronous offline consolidation. On LongMemEval-S and LoCoMo with GPT-4o-mini and Qwen3-30B-A3B-Instruct-2507 backbones, MemCode achieves the best overall accuracy while keeping per-dialogue memory construction within roughly 40~130 seconds, making it 3~21 times faster than LightMem and over an order of magnitude faster than A-MEM and MemoryOS.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
