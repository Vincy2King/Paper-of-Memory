# STARK: Moving towards Personalized Agents That Truly Learn and Remember

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.25705v1
- Published: 2026-11-19
- Updated: 2026-11-19
- Authors: Aryan Jain, Abhishek Jha, Anish Nediyanchath, Promod Yenigalla
- Tags: agent, benchmark, context, episodic, long-term
- Categories: cs.CL, cs.AI, cs.IR
- URL: http://arxiv.org/abs/2611.25705v1

## One-Sentence Summary
Long-term memory is essential for personalized agentic systems that interact with users over long time periods, yet current architectures only capture what happened while...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory is essential for personalized agentic systems that interact with users over long time periods, yet current architectures only capture what happened while leaving the reasoning of why it happened to be...

进一步看，论文的核心做法或实验重点可以概括为：These events can, however, convey not only what a user experienced but also how that experience shaped their behavioral patterns.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, episodic, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL, cs.AI, cs.IR

## Abstract Snapshot
Long-term memory is essential for personalized agentic systems that interact with users over long time periods, yet current architectures only capture what happened while leaving the reasoning of why it happened to be derived later by underlying LLMs.%, and silo knowledge within individual users. These events can, however, convey not only what a user experienced but also how that experience shaped their behavioral patterns. We introduce STARK, a dual-graph memory architecture which treats these events not just as nodes but also as edges between behavioral insights. STARK maintains an Episodic Graph which records interactions as temporally, causally, and semantically linked episodes; and an Insight Graph which represents LLM-extracted behavioral signals scored by how many events support them, connected by the very events that led to them. At inference, behavioral knowledge is retrieved directly from insight nodes grounded by event-as-edges, eliminating repeated episodic traversal. The event-as-edge structure also naturally enables projecting the knowledge graph into a relational embedding space where cross-user transfer becomes possible under shared contextual circumstances, allowing the system to infer missing insights for cold-start users. Evaluations show that STARK improves by 1.48 judge score on LongMemEval information extraction and 0.93 on LoCoMo open domain questions over state of the art. On the public LongLaMP abstract-generation benchmark, cross-user transfer improves open-ended judge scores by 0.7 points and ROUGE-L by 3 at 5% graph sparsity.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
