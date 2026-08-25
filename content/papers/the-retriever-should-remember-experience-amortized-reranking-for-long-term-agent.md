# The Retriever Should Remember: Experience-Amortized Reranking for Long-Term Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.22767v1
- Published: 2026-08-24
- Updated: 2026-08-24
- Authors: Qi Feng, Chris Ding, Jicong Fan
- Tags: agent, conversation, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.22767v1

## One-Sentence Summary
Long-term language-model agents accumulate memories across interactions, but their retrievers typically do not accumulate retrieval experience.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term language-model agents accumulate memories across interactions, but their retrievers typically do not accumulate retrieval experience.

进一步看，论文的核心做法或实验重点可以概括为：Semantic retrieval is efficient, but embedding similarity does not always reflect whether a memory contains evidence relevant to the current query.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, long-term, retrieval
- 检索关键词命中：agent memory, conversational memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term language-model agents accumulate memories across interactions, but their retrievers typically do not accumulate retrieval experience. Semantic retrieval is efficient, but embedding similarity does not always reflect whether a memory contains evidence relevant to the current query. Large language model (LLM) rerankers provide stronger query-conditioned relevance scores, yet stateless reranking repeatedly scores a large candidate pool and discards these scores after each query. We introduce EARM, an experience-amortized reranking framework that treats previously acquired LLM relevance scores as reusable retrieval experience. EARM stores sparse query--memory relevance scores in an online matrix, learns their shared structure through causal matrix completion, and combines a small set of newly observed scores with estimated scores to rerank the remaining candidates. The scoring budget decreases as experience accumulates, changing LLM reranking from a repeated per-query expense into a retrieval capability learned over an agent's lifetime. Experiments on long-term conversational memory show that mixed observed-and-estimated reranking improves answer accuracy over semantic retrieval by up to 6.62% and remains effective when only 17.5% of candidates receive direct LLM relevance scores, thereby substantially reducing the inference overhead of LLM reranking. These results motivate a broader view of agent memory: a long-lived agent should remember not only past content, but also how that content has proved useful for retrieval.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
