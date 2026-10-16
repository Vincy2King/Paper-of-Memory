# Hy-Memory-30B-A3B: Attributed Reinforcement Learning for Long-Term Memory Writing

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.22196v1
- Published: 2026-10-15
- Updated: 2026-10-15
- Authors: Tianxiang Fei, Jiazheng Kang, Mao Zheng, Xingyan He, Xiang Yu
- Tags: benchmark, context, long-term
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.22196v1

## One-Sentence Summary
External-memory systems extend language-model applications beyond a context window, but their quality depends critically on the model executing the write path: deciding what to...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：External-memory systems extend language-model applications beyond a context window, but their quality depends critically on the model executing the write path: deciding what to retain, how precisely to represent it,...

进一步看，论文的核心做法或实验重点可以概括为：Existing frameworks typically place a general-purpose large language model behind framework-specific prompts.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
External-memory systems extend language-model applications beyond a context window, but their quality depends critically on the model executing the write path: deciding what to retain, how precisely to represent it, and how new evidence should update persistent state. Existing frameworks typically place a general-purpose large language model behind framework-specific prompts. This raises serving cost, and a writer specialized for one protocol does not transfer directly to another; a unified model that can operate across established memory frameworks remains largely unexplored. We present Hy-Memory-30B-A3B, a compact long-term-memory writer trained across Mem0, MemOS, and Hy-Memory. Memory On-Policy Distillation teaches framework-specific write protocols on student-generated states; Memory RL then optimizes downstream answerability using dense per-chunk probes, attributed cross-chunk rewards, over-storage controls, and chunk-level GRPO. Carrying policy-written banks across windows keeps training aligned with deployment. On fixed 20% benchmark subsamples, Hy-Memory-30B-A3B ranks first on all four evaluated harnesses, including held-out EverMemOS, with a 55.49% macro average versus 54.62% for Claude Opus 5.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
