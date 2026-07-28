# Keep It InMind: Benchmarking the Implicit-Association Blind Spot in Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.24368v1
- Published: 2026-07-27
- Updated: 2026-07-27
- Authors: Ruizhe Li, Mingxuan Du, Benfeng Xu, Zhendong Mao
- Tags: agent, benchmark, context, long-term
- Categories: cs.CL
- URL: http://arxiv.org/abs/2607.24368v1

## One-Sentence Summary
Long-term memory systems store what a user says in an external store and retrieve it when a related query arrives.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory systems store what a user says in an external store and retrieve it when a related query arrives.

进一步看，论文的核心做法或实验重点可以概括为：This interface rests on an assumption so natural that it is rarely stated: a memory that is needed will resemble the query that needs it.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-term memory systems store what a user says in an external store and retrieve it when a related query arrives. This interface rests on an assumption so natural that it is rarely stated: a memory that is needed will resemble the query that needs it. World knowledge breaks the assumption. A tree-nut allergy should change the answer to a macaron request through their almond-flour ingredient, yet the two texts share no cue a retriever can see. We call this failure mode the implicit-association blind spot and introduce InMind, a 125-task, expert-verified benchmark spanning ten life domains, with 113 tasks grounded in citable public sources. Its paired controls separate three explanations that existing evaluations conflate: the fact was never stored, the model lacks the bridging knowledge, or the fact was stored and never surfaced. The verdict is clean. With the decisive memory placed in context, the backbone answers 84.0 percent of indirect queries; when the same memory must be retrieved, six vector, graph, and agentic memory systems reach at most 14.4 percent, even though they recall the same facts on demand at up to 100 percent. An embedding with eight times the dimensionality raises answer-blind target recall for every system yet leaves the gap essentially intact. A minimal diagnostic probe that keeps memory visible before the query arrives recovers most of the gap, locating the failure in the query-conditioned interface itself and pointing to routing, deciding which facts must stay visible, as the open problem InMind is built to score.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
