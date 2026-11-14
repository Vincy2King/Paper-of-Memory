# MemCredit: From Relevance to Utility for Decision-Time Memory in Long-Horizon Web Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.15600v1
- Published: 2026-11-11
- Updated: 2026-11-11
- Authors: Quanjiang Guo, Sijie Wang, Qianyang Zhu, Ben Zhang, Jinchuan Zhang, Ke Yan, Zhao Kang
- Tags: agent, compression, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.15600v1

## One-Sentence Summary
Large language model (LLM) agents increasingly operate over long Web interaction histories, making memory management critical for reliable and efficient decision making.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents increasingly operate over long Web interaction histories, making memory management critical for reliable and efficient decision making.

进一步看，论文的核心做法或实验重点可以概括为：Existing methods primarily optimize storage, retrieval, or compression, but the memories most semantically relevant to the current state are not necessarily those that most improve the agent's action.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language model (LLM) agents increasingly operate over long Web interaction histories, making memory management critical for reliable and efficient decision making. Existing methods primarily optimize storage, retrieval, or compression, but the memories most semantically relevant to the current state are not necessarily those that most improve the agent's action. We introduce MemCredit, a decision-centric memory framework that shifts memory selection from semantic relevance to decision utility. MemCredit estimates the state-, reference-context-, and policy-conditional marginal contribution of individual memories through controlled counterfactual interventions, and distills these intervention-derived credits into a lightweight utility estimator. At inference time, semantic relevance is used only for high-recall candidate generation, while predicted utility arbitrates which memories are retained under a fixed token budget, without modifying the underlying agent policy or requiring additional environment interaction. We evaluate MemCredit on ALFWorld and WebShop against representative memory baselines. On ALFWorld, MemCredit achieves 86.57 SR@50 under a 500-token historical-memory budget, compared with 65.67% for BM25 retrieval. Counterfactual analysis further shows that memory utility is sparse, strongly state dependent, and poorly captured by semantic relevance. These results suggest that decision utility provides a more effective principle than relevance alone for long-horizon agent memory management.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
