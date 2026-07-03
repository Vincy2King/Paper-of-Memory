# Learning User-Aware Recall: Personalized Retrieval in Long-Term Conversational Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.00017v2
- Published: 2026-05-28
- Updated: 2026-07-02
- Authors: ZhiShu Jiang, Haibo Liu, Xin Shen, Guanqiang QI, Chenxi Miao, Weikang Li, Liwei Qian, Xin Pei, Jizhou Huang
- Tags: agent, conversation, episodic, long-term, retrieval
- Categories: cs.IR, cs.AI, cs.CL
- URL: http://arxiv.org/abs/2607.00017v2

## One-Sentence Summary
Long-term conversational agents are expected to remember past interactions, but memory is useful only when the right evidence is recalled for the right user.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, episodic, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term conversational agents are expected to remember past interactions, but memory is useful only when the right evidence is recalled for the right user.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory-augmented LLM agents have made progress in building compact memory banks, yet retrieval is still often driven by query-centered similarity or fixed ranking rules, leaving user-conditioned relevance...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, episodic, long-term, retrieval
- 检索关键词命中：conversational memory, memory retrieval
- 来源分类信息：cs.IR, cs.AI, cs.CL

## Abstract Snapshot
Long-term conversational agents are expected to remember past interactions, but memory is useful only when the right evidence is recalled for the right user. Existing memory-augmented LLM agents have made progress in building compact memory banks, yet retrieval is still often driven by query-centered similarity or fixed ranking rules, leaving user-conditioned relevance underexplored. To address this gap, we propose Profile-guided Personalized Retrieval Optimization (PPRO), a retrieval-centric framework that makes memory retrieval both user-aware and optimizable. PPRO builds episodic and semantic memory banks from dialogue histories and derives a user profile from accumulated memories. The profile serves as an explicit personalized prior in memory ranking, allowing retrieval to account for stable user attributes, preferences, and relationships. PPRO further trains a query rewriter with Group Relative Policy Optimization, using both evidence retrieval quality and downstream answer quality as feedback while keeping the memory banks and answer model fixed. Experiments on LoCoMo and LongMemEval-S show consistent gains over training-free memory systems and training-based baselines. Ablation studies further show that both profile-guided ranking and retrieval-oriented rewriting contribute substantially to performance, highlighting retrieval optimization as a key factor in personalized long-term memory use.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
