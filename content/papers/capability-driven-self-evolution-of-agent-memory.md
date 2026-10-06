# Capability-Driven Self-Evolution of Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.06361v1
- Published: 2026-10-05
- Updated: 2026-10-05
- Authors: Yaoqi Chen, Yuru Feng, Qianxi Zhang, Baotong Lu, Jianan Lu, Zhirui Wang, Shusen Xu, Zewen Jin, Zengzhong Li, Cheng Li, Qi Chen
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.06361v1

## One-Sentence Summary
Memory self-evolution uses task feedback to iteratively improve executable memory programs that store and retrieve information from past interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory self-evolution uses task feedback to iteratively improve executable memory programs that store and retrieve information from past interactions.

进一步看，论文的核心做法或实验重点可以概括为：Existing approaches typically adopt holistic evolution, deriving revision directions from mixed feedback and judging progress by overall performance.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Memory self-evolution uses task feedback to iteratively improve executable memory programs that store and retrieve information from past interactions. Existing approaches typically adopt holistic evolution, deriving revision directions from mixed feedback and judging progress by overall performance. This can obscure optimization directions and hide capability-specific gains offset by regressions elsewhere, leaving promising directions underexplored. We introduce capability-driven evolution, which extends search guidance from overall performance to individual capability dimensions, preserving promising revisions and expanding exploration beyond the boundaries of holistic evolution. We propose PrisMem, which uses dependency-aware capability selection to prioritize targets with potential cross-capability benefits and history-guided diagnosis to refine capability specialists. Trace-guided integration compares evaluated programs on paired differential cases, using their behavioral differences to consolidate complementary gains into a unified memory program. Experiments show that PrisMem outperforms the strongest baselines by 10.54 and 7.83 percentage points on BEAM-1M and LongMemEval-M, respectively, demonstrating its effectiveness on million-token histories.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
