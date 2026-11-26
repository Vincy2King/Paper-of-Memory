# HoMe: Toward Practical Harness Optimization of Memory Systems for AI Assistants

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.34624v1
- Published: 2026-11-25
- Updated: 2026-11-25
- Authors: Yifei Xu, Li Yu, Zhaoyang Liu, Ce Wang, Sen Huang, Yanyan Shen, Yun Lin, Linpeng Huang, Hong Mei
- Tags: agent, benchmark, retrieval
- Categories: cs.AI, cs.LG
- URL: http://arxiv.org/abs/2611.34624v1

## One-Sentence Summary
The behavior of memory systems for long-running AI assistants is governed by a harness, which consists of the code, prompts, and configurations for memory construction,...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：The behavior of memory systems for long-running AI assistants is governed by a harness, which consists of the code, prompts, and configurations for memory construction, maintenance, retrieval, and answer generation.

进一步看，论文的核心做法或实验重点可以概括为：However, optimizing the harness of a memory system remains largely manual, and unrestricted editing alone does not ensure structural improvements.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：memory benchmarks
- 来源分类信息：cs.AI, cs.LG

## Abstract Snapshot
The behavior of memory systems for long-running AI assistants is governed by a harness, which consists of the code, prompts, and configurations for memory construction, maintenance, retrieval, and answer generation. However, optimizing the harness of a memory system remains largely manual, and unrestricted editing alone does not ensure structural improvements. In this paper, we introduce HoMe, an evaluation-driven framework that iteratively evaluates candidate harnesses and derives each new candidate from any previously evaluated harness by editing any part of it. HoMe combines session-level memory versioning with execution traces to identify shared failure mechanisms across cases and localize them to the responsible sessions and harness components. It encourages early structural exploration through candidate gating and reduces evaluation cost through smoke tests, adaptive sampling, and the reuse of constructed memory. We validate HoMe with the open-source memory system ReMe on two large-scale long-horizon memory benchmarks, LongMemEval-S and BEAM. With six formal candidate evaluations per benchmark, after a full initial evaluation, HoMe discovers harnesses that improve end-task performance over the originally strong harness while consuming far fewer query-time tokens. The code is available at https://github.com/agentscope-ai/ReMe.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
