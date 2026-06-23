# Nous: A Predictive World Model for Long-Term Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.22030v1
- Published: 2026-06-20
- Updated: 2026-06-20
- Authors: Pranav Singh
- Tags: agent, benchmark, conversation, long-term
- Categories: cs.AI, cs.CL, cs.IR, cs.LG
- URL: http://arxiv.org/abs/2606.22030v1

## One-Sentence Summary
We present Nous, a novel agent memory architecture grounded in the principle that knowledge is prediction, not storage.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We present Nous, a novel agent memory architecture grounded in the principle that knowledge is prediction, not storage.

进一步看，论文的核心做法或实验重点可以概括为：Rather than persisting facts as database records, vector embeddings, or knowledge-graph triples, Nous maintains a predictive world model: a collection of categorical probability distributions, called dimensions, one...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, long-term
- 检索关键词命中：agent memory, conversational memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.AI, cs.CL, cs.IR, cs.LG

## Abstract Snapshot
We present Nous, a novel agent memory architecture grounded in the principle that knowledge is prediction, not storage. Rather than persisting facts as database records, vector embeddings, or knowledge-graph triples, Nous maintains a predictive world model: a collection of categorical probability distributions, called dimensions, one per entity-attribute pair observed in conversation. Each incoming observation is scored by its information-theoretic surprise S = -log2 P(obs | D), and the distribution is updated via a closed-form Bayesian posterior. The primary stored artifact is the delta, a record of the shift from prior to posterior belief, rather than the fact itself. Forgetting emerges naturally as entropy decay toward the uniform distribution, and identity resolution is handled through mutual information between entity dimension sets. Evaluated on the LoCoMo long-term conversational memory benchmark across ten conversations (1,540 questions) using GPT-4o-mini as backbone, Nous achieves F1 of 63.50 (single-hop), 55.32 (multi-hop), 58.57 (temporal), and 62.50 (open-domain). Against A-MEM's self-reported GPT-4o-mini numbers, Nous shows substantial gains in three of four categories, though we note that independent citations of A-MEM's results disagree with each other on category assignment, a reproducibility issue we discuss openly rather than resolve unilaterally. We additionally compare against BeliefMem, a concurrently developed system built on the same core premise of belief-based rather than deterministic memory; on the same benchmark and backbone, Nous's self-reported numbers exceed BeliefMem's self-reported numbers on all four categories, though we flag several uncontrolled differences between the two evaluation pipelines that prevent this from being a fully controlled comparison. Nous requires no external vector database or graph engine.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
