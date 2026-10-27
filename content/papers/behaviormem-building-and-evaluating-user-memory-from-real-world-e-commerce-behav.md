# BehaviorMem: Building and Evaluating User Memory from Real-World E-Commerce Behavior Streams

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.34790v1
- Published: 2026-10-26
- Updated: 2026-10-26
- Authors: Sizhe Wang, Xinghao Fang, Rui Qiu, Zhenjia Ma, Dagui Chen, Kun Kuang, Hongcheng Guo
- Tags: agent, benchmark, long-term
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.34790v1

## One-Sentence Summary
User memory helps personalized systems build on their understanding of users over time.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：User memory helps personalized systems build on their understanding of users over time.

进一步看，论文的核心做法或实验重点可以概括为：In e-commerce, users convey their preferences and needs through both explicit language and implicit interactions with products.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
User memory helps personalized systems build on their understanding of users over time. In e-commerce, users convey their preferences and needs through both explicit language and implicit interactions with products. We study memory built from logs of these interactions, examining how it can \emph{remember} concrete evidence and established interests, and use that evidence to \emph{infer} underlying needs and preferences that inform judgments beyond well-observed product domains. Existing memory methods primarily target language-based interactions, and evaluations offer limited real behavioral data and limited separation of these capabilities. This leaves open how to jointly support and separately evaluate remembering and inference from behavioral logs. We formulate the problem of continual behavioral user memory around these joint requirements and develop a dedicated evaluation framework and memory method to address them. \textbf{BehaviorMemBench} is a benchmark built from real e-commerce logs covering 1{,}194 users and 17{,}462 behavioral batches over more than three years, with automatic future-behavior labels and a task-independent memory interface to separately evaluate remembering and inference under a common protocol. \textbf{BehaviorMem} is a memory design that organizes explicit behavioral facts and inferred user characteristics across long-term and short-term scopes in a two-axis state, with evidence-grounded formation, continual maintenance, and query-independent readout. Experiments across two builders and two task readers show that BehaviorMem leads the evaluated agentic memories on remember and infer, and reveal different method rankings across the two capabilities and competitive statistical baselines. Validation on a public dataset further supports its usefulness for downstream tasks based on behavioral histories.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
