# SearchWiki: Learning to Build and Navigate Knowledge Wikis for Active Information Seeking

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.29953v1
- Published: 2026-08-30
- Updated: 2026-08-30
- Authors: Guransh Singh, Vishwajeet Kumar, Arkadeep Acharya, Adnan Qidwai, Jaydeep Sen, Sachindra Joshi
- Tags: agent, benchmark, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.29953v1

## One-Sentence Summary
Flat retrieval-augmented generation treats a corpus as a bag of chunks, discarding document hierarchy and cross document structure.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Flat retrieval-augmented generation treats a corpus as a bag of chunks, discarding document hierarchy and cross document structure.

进一步看，论文的核心做法或实验重点可以概括为：We introduce SearchWiki, a harness framework that synthesizes a corpus into a hierarchical, typed, navigable wiki and trains an agent, WikiResearcher-9B, to retrieve information through multi-turn tool use.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：cs.AI

## Abstract Snapshot
Flat retrieval-augmented generation treats a corpus as a bag of chunks, discarding document hierarchy and cross document structure. We introduce SearchWiki, a harness framework that synthesizes a corpus into a hierarchical, typed, navigable wiki and trains an agent, WikiResearcher-9B, to retrieve information through multi-turn tool use. The wiki organizes knowledge into three layers - document overviews, cross- document topic pages, and page-level source records; enabling progressive refinement of retrieval when initial lookup misses. We optimize the agent's navigation policy with on-policy reinforcement learning with a multi-component reward function balancing answer correctness, retrieval quality and trajectory efficiency. Evaluation on ViDoRe-V3 (8 domains), FinanceBench, and memory benchmarks (LoCoMo, LongMemEval, PersonaMem-v2) shows that WikiResearcher- 9B which is our RL-tuned Qwen 9B model, significantly outperforms same-size untrained baselines and exceeds or matches larger external models. SearchWiki paired with WikiResearcher-9B demonstrates that learned navigation over structured corpora is a superior alternative to flat retrieval.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
