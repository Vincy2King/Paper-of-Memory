# DMF: A Deterministic Memory Framework for Conversational AI Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.03463v1
- Published: 2026-06-02
- Updated: 2026-06-02
- Authors: Matteo Stabile, Enrico Zimuel
- Tags: agent, benchmark, compression, context, conversation
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2606.03463v1

## One-Sentence Summary
Conversational AI agents require memory systems that are both scalable and semantically coherent across long interaction horizons.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Conversational AI agents require memory systems that are both scalable and semantically coherent across long interaction horizons.

进一步看，论文的核心做法或实验重点可以概括为：Existing approaches rely predominantly on large language model (LLM)-based summarisation at write time, which introduces non-determinism, escalating token costs, and opacity in pruning decisions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, context, conversation
- 检索关键词命中：memory compression
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Conversational AI agents require memory systems that are both scalable and semantically coherent across long interaction horizons. Existing approaches rely predominantly on large language model (LLM)-based summarisation at write time, which introduces non-determinism, escalating token costs, and opacity in pruning decisions. We present the Deterministic Memory Framework (DMF), a CPU-first approach that replaces generative memory compression with a fully deterministic pipeline grounded in classical NLP analysis, vector geometry, and mathematical scoring. DMF assigns each conversational interaction a Survival Score $Ω$ computed from deterministic content signals, conversational cues, and structured provenance, combined through a logistic projection. An interaction-count decay law, denoted as $Ω_{\mathrm{eff}}(Δn)$, governs how relevance evolves as new turns arrive, where $Δn$ is the number of newer interactions rather than wall-clock time, preserving full determinism. We present the mathematical formulation of DMF, its structured recall pipeline, the pruning decision procedure, and the evaluation protocol. Experiments are conducted on a purpose-built benchmark using the LoCoMo and LongMemEval datasets. We compare DMF against Mem0, a popular memory layer for AI agents. DMF achieves comparable accuracy while using zero tokens to prepare the memory context and 5x to 242x fewer tokens over the entire conversation. These results show that it is possible to eliminate LLM calls from the memory-management loop, reducing token costs to nearly zero and enabling deterministic memory systems for conversational AI agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
