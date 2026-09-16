# GeoSkill:Experience-Driven Hierarchical Skill Learning with Collaborative Revision forGeospatialAgents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.13667v1
- Published: 2026-09-12
- Updated: 2026-09-12
- Authors: Han Luo, Xian Xu, Yinhe Liu, Yanfei Zhong
- Tags: agent, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.13667v1

## One-Sentence Summary
Geospatial agents are increasingly expected to support recurring and evolving analytical tasks rather than execute isolated workflows.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Geospatial agents are increasingly expected to support recurring and evolving analytical tasks rather than execute isolated workflows.

进一步看，论文的核心做法或实验重点可以概括为：In such settings, effective agents must distill prior execution experience into reusable geospatial procedural knowledge to guide future planning and tool use.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Geospatial agents are increasingly expected to support recurring and evolving analytical tasks rather than execute isolated workflows. In such settings, effective agents must distill prior execution experience into reusable geospatial procedural knowledge to guide future planning and tool use. However, existing memory-augmented paradigms struggle to summarize both long-horizon tool-chain orchestration experience and tool-level invocation constraints in geospatial analysis, while directly relying on LLM self-reflection to update experience often leads to misattribution and unreliable revisions. To address these challenges, we propose GeoSkill, an experience-driven hierarchical skill learning framework for geospatial agents. GeoSkill comprises two core components: (i) a Hierarchical Skill Bank (HSB), consisting of a Planning Skill Bank and a Tool Skill Bank, which respectively distill high-level task-planning experience and tool usage constraints, enabling structured representation and cross-task reuse of historical execution experience; and (ii) a Collaborative Trace-driven Skill Revision (CTSR) mechanism, where Judge, Critic, and Refiner collaboratively perform error identification, skill-level defect localization, and targeted modification, preventing misattributed and unreliable revisions from polluting the skill bank. GeoSkill learns and validates skills from historical executions during development, and freezes the skill bank for retrieval-only guidance on unseen tasks during deployment. Extensive experiments on EarthBench and ThinkGeo demonstrate that GeoSkill effectively transforms historical execution experience into reusable hierarchical skills, improving both end-to-end task accuracy and tool-execution reliability in geospatial tasks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
