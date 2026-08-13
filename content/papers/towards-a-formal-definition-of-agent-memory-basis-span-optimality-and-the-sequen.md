# Towards a Formal Definition of Agent Memory: Basis, Span, Optimality, and the Sequential Memory Problem

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.11654v1
- Published: 2026-08-12
- Updated: 2026-08-12
- Authors: Hongyao Tang
- Tags: agent, compression
- Categories: cs.LG
- URL: http://arxiv.org/abs/2608.11654v1

## One-Sentence Summary
Despite the wide deployment of memory in large-model agents, there is no unified formal account of what a memory is or when it is optimal.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Despite the wide deployment of memory in large-model agents, there is no unified formal account of what a memory is or when it is optimal.

进一步看，论文的核心做法或实验重点可以概括为：This paper takes a first step toward this account.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression
- 检索关键词命中：agent memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Despite the wide deployment of memory in large-model agents, there is no unified formal account of what a memory is or when it is optimal. This paper takes a first step toward this account. The central idea is that memory is a basis, knowledge is its span, and answerability is a coverage problem: an agent stores events extracted from a material; a generation operator turns any event set into the knowledge it entails; and a query is answerable exactly when some single item in the span covers it. The optimal memory is then the capacity-constrained maximizer of expected coverage, and its value traces a utility--capacity frontier, the common yardstick on which memory systems can be compared. Next, we consider noise in the memory and discuss coverage versus precision under it: a memory may store false claims, so the write policy must infer the truth of what it stores. Drawing an analogy with biological memory, which is formed continuously through ongoing experience, we formalize the continual agent-memory problem in a sequential MDP that covers multiple levels, where memory is the state, writing is the action, and the utility settled at query time is the delayed reward that drives learning. To make the framework concrete, we instantiate it on Homer's \emph{Odyssey}, turning the frontier, the compression zone, and the divergence of coverage from precision into concrete numbers. Finally, we position existing systems within the framework, making ``how good is a memory'' measurable and recasting the open problems of constructing and learning agent memory as concrete research questions.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
