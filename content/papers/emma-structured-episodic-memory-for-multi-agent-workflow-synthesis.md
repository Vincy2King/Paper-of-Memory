# EMMA: Structured Episodic Memory for Multi-Agent Workflow Synthesis

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.35966v1
- Published: 2026-10-25
- Updated: 2026-10-25
- Authors: Ruijia Niu, Kaiwen Liu, Rose Yu, Kristina Klinkner
- Tags: agent, benchmark, context, episodic
- Categories: cs.MA, cs.AI
- URL: http://arxiv.org/abs/2610.35966v1

## One-Sentence Summary
Deploying LLM agents in specialized domains often require fine-grained task-specific procedures and knowledge a general model lacks, yet parameter training is costly and non-...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Deploying LLM agents in specialized domains often require fine-grained task-specific procedures and knowledge a general model lacks, yet parameter training is costly and non-interpretable, and hand-engineered agent...

进一步看，论文的核心做法或实验重点可以概括为：Episodic memory updates at context level, but single agent adaptation struggles to alleviate cross-task interference, especially with complex tasks such as multi-application navigation or data pool analysis.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.MA, cs.AI

## Abstract Snapshot
Deploying LLM agents in specialized domains often require fine-grained task-specific procedures and knowledge a general model lacks, yet parameter training is costly and non-interpretable, and hand-engineered agent systems shift the cost to expert labor. Episodic memory updates at context level, but single agent adaptation struggles to alleviate cross-task interference, especially with complex tasks such as multi-application navigation or data pool analysis. Although multi-agent evolution alleviates this problem, existing methods lack clear definitions on update rules and rely on the backbone model to decide where and how much the system changes. This ill-scoped evolution makes learning follow the backbone's structural preferences rather than the observed failures: one backbone accumulates skills while another spawns agents. We present EMMA (structured Episodic Memory for Multi-Agent workflow synthesis), which treats the configuration of a multi-agent system (controller routing memory, specialists inheriting a generalist prompt, and per-step procedural skills) as episodic memory. EMMA makes the ownership and admissibility of updates explicit: a reflector assigns each diagnosed failure to the scope owning its correction and proposes one edit within it, and backbone-independent guards keep every accepted edit scoped, incremental and bounded. Across KramaBench, AppWorld and BBEH with five backbones and four baselines (ACE, GEPA, EvoMAS and ADAS), EMMA attains the best overall performance on every benchmark, up to 32.5% over the strongest baseline, maintains consistent improvements across backbones, and uses 17-38% fewer training executions than the most efficient baseline.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
