# ZenBrain: A Neuroscience-Inspired 7-Layer Memory Architecture for Autonomous AI Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.23878v1
- Published: 2026-04-26
- Updated: 2026-04-26
- Authors: Alexander Bering
- Tags: agent, context, episodic
- Categories: cs.AI, cs.LG
- URL: http://arxiv.org/abs/2604.23878v1

## One-Sentence Summary
Despite a century of empirical memory research, existing AI agent memory systems rely on system-engineering metaphors (virtual-memory paging, flat LLM storage, Zettelkasten...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Despite a century of empirical memory research, existing AI agent memory systems rely on system-engineering metaphors (virtual-memory paging, flat LLM storage, Zettelkasten notes), none integrating principles of...

进一步看，论文的核心做法或实验重点可以概括为：We present ZenBrain, a multi-layer memory architecture integrating fifteen neuroscience models.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, episodic
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI, cs.LG

## Abstract Snapshot
Despite a century of empirical memory research, existing AI agent memory systems rely on system-engineering metaphors (virtual-memory paging, flat LLM storage, Zettelkasten notes), none integrating principles of consolidation, forgetting, and reconsolidation. We present ZenBrain, a multi-layer memory architecture integrating fifteen neuroscience models. It implements seven memory layers (working, short-term, episodic, semantic, procedural, core, cross-context) orchestrated by nine foundational algorithms (Two-Factor Synaptic Model, vmPFC-coupled FSRS, Simulation-Selection sleep, Bayesian confidence, and five more) plus six new Predictive Memory Architecture (PMA) components: a four-channel NeuromodulatorEngine, prediction-error-gated ReconsolidationEngine, TripleCopyMemory with divergent decay, four-dimensional PriorityMap with amygdala fast-path, StabilityProtector (NogoA/HDAC3 analogue), and MetacognitiveMonitor for bias detection. The 15-algorithm ablation reveals a cooperative survival network: under stress, 9 of 15 algorithms become individually critical (delta-Q up to -93.7%, Wilcoxon, 10 seeds, alpha=0.005). Simulation-Selection sleep achieves 37% stability improvement (p<0.005) with 47.4% storage reduction. TripleCopyMemory retains S(t)=0.912 at 30 days; PriorityMap reaches NDCG@10=0.997. Multi-layer routing beats a flat single-layer baseline by 20.7% F1 on LoCoMo (p<0.005) and 19.5% on MemoryArena (p=0.015). On LongMemEval-500, ZenBrain holds the highest mean rank on all 12 system-judge cells (4 systems x 3 LLM judges), three-judge mean J=0.545 vs letta=0.485, a-mem=0.414, mem0=0.394; all 9 pair-wise contrasts clear Bonferroni (alpha=0.05/18, min p=6.2e-31, d in [0.18, 0.52]). Under LongMemEval's binary judge, ZenBrain reaches 91.3% of oracle accuracy at 1/106th the per-query token budget. Open-source with 11,589 automated test cases.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
