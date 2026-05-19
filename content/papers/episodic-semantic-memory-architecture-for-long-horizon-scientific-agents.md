# Episodic-Semantic Memory Architecture for Long-Horizon Scientific Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.17625v1
- Published: 2026-05-17
- Updated: 2026-05-17
- Authors: Nikola Milosevic
- Tags: agent, context, episodic, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.17625v1

## One-Sentence Summary
As Large Language Models (LLMs) evolve into persistent scientific collaborators, context window saturation has emerged as a critical bottleneck.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, episodic, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：As Large Language Models (LLMs) evolve into persistent scientific collaborators, context window saturation has emerged as a critical bottleneck.

进一步看，论文的核心做法或实验重点可以概括为：Scientific workflows involving iterative data analysis and hypothesis refinement rapidly saturate even extended contexts with dense technical content, while monolithic approaches suffer from quadratic cost scaling and...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, episodic, long-term, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
As Large Language Models (LLMs) evolve into persistent scientific collaborators, context window saturation has emerged as a critical bottleneck. Scientific workflows involving iterative data analysis and hypothesis refinement rapidly saturate even extended contexts with dense technical content, while monolithic approaches suffer from quadratic cost scaling and cognitive degradation. We evaluate a Dual Process Memory Architecture that decouples immediate episodic needs (constant 10-message window) from long-term consolidated knowledge (growing at approximately 3 tokens/message). Unlike prior social agent memory systems, our domain-specific consolidation addresses contradictory parameter evolution, multi-hop reasoning across experimental phases, and precise technical fact retention. Through large-scale evaluation spanning 15,000 messages with cross-model validation across six LLMs from three families (OpenAI, Anthropic, Google), totaling 1,440 queries, we establish three key findings. First, while full-context models fail at 10,000 messages due to context overflow, our system maintains 70-85% accuracy with 1-2 second latency using 62% fewer tokens (45,434 vs 120,000+ limit). Second, cross-model validation reveals architecture-level trade-offs independent of specific LLMs: Dual Process excels at numeric/temporal queries (65-90% accuracy) while RAG excels at historical retrieval (60-85%), suggesting complementary deployment strategies. Third, we identify a "Sim-to-Real" gap where synthetic tests maintain constant memory but realistic workflows exhibit linear growth (about 3 tokens/message), with consolidation quality emerging as the primary scalability bottleneck. The architecture successfully manages profiles with 14,000+ scientific facts (125k tokens), demonstrating that domain-specific memory consolidation enables sustained operation beyond full-context limits.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
