# EvolveMem:Self-Evolving Memory Architecture via AutoResearch for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.13941v1
- Published: 2026-05-13
- Updated: 2026-05-13
- Authors: Jiaqi Liu, Xinyu Ye, Peng Xia, Zeyu Zheng, Cihang Xie, Mingyu Ding, Huaxiu Yao
- Tags: agent, benchmark, long-term, retrieval
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2605.13941v1

## One-Sentence Summary
Long-term memory is essential for LLM agents that operate across multiple sessions, yet existing memory systems treat retrieval infrastructure as fixed: stored content evolves...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory is essential for LLM agents that operate across multiple sessions, yet existing memory systems treat retrieval infrastructure as fixed: stored content evolves while scoring functions, fusion...

进一步看，论文的核心做法或实验重点可以概括为：We argue that truly adaptive memory requires co-evolution at two levels: the stored knowledge and the retrieval mechanism that queries it.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Long-term memory is essential for LLM agents that operate across multiple sessions, yet existing memory systems treat retrieval infrastructure as fixed: stored content evolves while scoring functions, fusion strategies, and answer-generation policies remain frozen at deployment. We argue that truly adaptive memory requires co-evolution at two levels: the stored knowledge and the retrieval mechanism that queries it. We present EvolveMem, a self-evolving memory architecture that exposes its full retrieval configuration as a structured action space optimized by an LLM-powered diagnosis module. In each evolution round, the module reads per-question failure logs, identifies root causes, and proposes targeted configuration adjustments; a guarded meta-analyzer applies them with automatic revert-on-regression and explore-on-stagnation safeguards. This closed-loop self-evolution realizes an AutoResearch process: the system autonomously conducts iterative research cycles on its own architecture, replacing manual configuration tuning. Starting from a minimal baseline, the process converges autonomously, discovering effective retrieval strategies including entirely new configuration dimensions not present in the original action space. On LoCoMo, EvolveMem outperforms the strongest baseline by 25.7% relative and achieves a 78.0% relative improvement over the minimal baseline. On MemBench, EvolveMem exceeds the strongest baseline by 18.9% relative. Evolved configurations transfer across benchmarks with positive rather than catastrophic transfer, indicating that the self-evolution process captures universal retrieval principles rather than benchmark-specific heuristics. Code is available at https://github.com/aiming-lab/SimpleMem.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
