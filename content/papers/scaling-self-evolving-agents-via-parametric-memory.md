# Scaling Self-Evolving Agents via Parametric Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.04536v1
- Published: 2026-06-03
- Updated: 2026-06-03
- Authors: Tao Ren, Weiyao Luo, Hui Yang, Rongzhi Zhu, Xiang Huang, Yuchuan Wu, Bingxue Chou, Jieping Ye, Jiafeng Liang, Yongbin Li, Yijie Peng
- Tags: agent, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.04536v1

## One-Sentence Summary
Existing memory-augmented LLM agents store past experience exclusively in prompt space, as textual summaries or retrieved passages, while keeping model parameters frozen...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Existing memory-augmented LLM agents store past experience exclusively in prompt space, as textual summaries or retrieved passages, while keeping model parameters frozen throughout a rollout.

进一步看，论文的核心做法或实验重点可以概括为：Such agents can \emph{look up} what they have seen but cannot \emph{learn from} it: their policy is unchanged by experience, and any information dropped from the context is permanently lost.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Existing memory-augmented LLM agents store past experience exclusively in prompt space, as textual summaries or retrieved passages, while keeping model parameters frozen throughout a rollout. Such agents can \emph{look up} what they have seen but cannot \emph{learn from} it: their policy is unchanged by experience, and any information dropped from the context is permanently lost. We introduce \texttt{TMEM}, a self-evolving parametric memory framework in which the agent not only compresses history into explicit memory but also absorbs distilled supervision into fast LoRA weights $Δ_t$ via lightweight online updates, genuinely altering its future behavior within a single episode. We formalize this as an agentic decision process with fast-weight rollout dynamics: actions are sampled from $π_{θ_0+Δ_t}$, while extraction actions produce supervision that updates $Δ_t$ for subsequent decisions. This view makes the extraction policy directly optimizable by RL: training $θ_0$ improves not only task actions but also the quality of the data used for online LoRA adaptation. We further propose SVD-based initialization of the LoRA subspace to accelerate online convergence. Experiments on LoCoMo, LongMemEval-S, multi-objective search, and CL-Bench show that \texttt{TMEM} consistently outperforms summary-based and retrieval-based baselines across different model scales.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
