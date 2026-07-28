# MemChain: Learning Interpretable Memory Traces for Memory-Augmented LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.24097v1
- Published: 2026-07-27
- Updated: 2026-07-27
- Authors: Yiwen Ma, Songjun Tu, Qichao Zhang, Dong Li, Linjing Li, Dongbin Zhao
- Tags: agent, context, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.24097v1

## One-Sentence Summary
Memory-augmented LLM agents typically answer queries by retrieving relevant memories and feeding them directly to an answer model.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-augmented LLM agents typically answer queries by retrieving relevant memories and feeding them directly to an answer model.

进一步看，论文的核心做法或实验重点可以概括为：This retrieval-as-evidence paradigm assumes retrieved memories are already suitable for reasoning, leaving the answer model to resolve redundancy, conflicts, and weak relevance while incurring substantial context...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term, retrieval
- 检索关键词命中：long-term memory, memory augmented, memory-augmented, retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Memory-augmented LLM agents typically answer queries by retrieving relevant memories and feeding them directly to an answer model. This retrieval-as-evidence paradigm assumes retrieved memories are already suitable for reasoning, leaving the answer model to resolve redundancy, conflicts, and weak relevance while incurring substantial context overhead in long-term memory tasks. We propose MemChain, a trainable post-retrieval memory policy that transforms retrieved candidates into answer-facing active memory, represented as a compact and grounded evidence context. Given a user query and retrieved candidates, MemChain first generates a question-conditioned evidence plan, then constructs an ordered grounded evidence trace that organizes retrieved memories according to their semantic roles and dependencies, and finally executes explicit memory actions to produce a concise evidence context for answer generation. To train the mediator, we introduce a two-stage learning framework. Supervised trace learning first teaches the policy to generate structurally valid plans, traces, actions, and evidence contexts. We then propose Trace-Guided Memory Policy Optimization (TMPO), a reinforcement learning objective that optimizes the memory policy using downstream answer quality while jointly encouraging trace grounding, evidence support, structural validity, and answer stability across multiple rollouts. Experiments on LoCoMo and LongMemEval-S demonstrate that MemChain consistently achieves state-of-the-art performance across both closed-source and open-weight frozen answer models while substantially reducing the memory context passed to the answer model.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
