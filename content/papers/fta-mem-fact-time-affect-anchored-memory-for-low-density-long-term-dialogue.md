# FTA-Mem: Fact-Time-Affect Anchored Memory for Low-Density Long-Term Dialogue

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.16303v1
- Published: 2026-08-17
- Updated: 2026-08-17
- Authors: Chang Liu, Shuyi Zhang, Changsheng Ma, Yongfeng Tao, Minqiang Yang, Bin Hu
- Tags: agent, benchmark, context, long-term
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.16303v1

## One-Sentence Summary
Long-term emotional-support agents require memory mechanisms for personalized understanding across sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term emotional-support agents require memory mechanisms for personalized understanding across sessions.

进一步看，论文的核心做法或实验重点可以概括为：However, emotional-support dialogue is often low-density: turns are incomplete, evidence is scattered, and user states evolve over time.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-term emotional-support agents require memory mechanisms for personalized understanding across sessions. However, emotional-support dialogue is often low-density: turns are incomplete, evidence is scattered, and user states evolve over time. Existing memory methods usually rely on fixed units, such as turn-level notes or session summaries, which may lose details or introduce redundant noise. We propose FTA-Mem, a structured memory framework for low-density long-term dialogue. FTA-Mem uses Boundary-preserving Window Segmentation (BWS) to form coherent situation fragments, and constructs Fact-Time-Affect Memory Units (FTA Units) that jointly encode factual content, temporal grounding, and affective context. Retrieved units are then synthesized into structured context for answer generation. Experiments on ES-MemEval and LoCoMo show that FTA-Mem improves overall long-term memory question answering across benchmarks with different information-density characteristics. On ES-MemEval, FTA-Mem achieves 0.3871 F1 and 0.6668 BERTScore. Further analysis shows that situation-level FTA construction better balances evidence preservation and construction cost than coarse session-level or overly fine-grained turn-pair construction, providing an effective granularity trade-off for long-term dialogue memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
