# LLMs Are Not Good Strategists, Yet Memory-Enhanced Agency Boosts Reasoning

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.12626v1
- Published: 2026-08-12
- Updated: 2026-08-12
- Authors: Yi Wu, Zhimin Hu
- Tags: agent, context, long-term
- Categories: cs.CL, cs.AI, cs.MA
- URL: http://arxiv.org/abs/2608.12626v1

## One-Sentence Summary
Strategic reasoning in Large Language Models (LLMs) within long-horizon environments is often limited by inconsistent subgoals.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Strategic reasoning in Large Language Models (LLMs) within long-horizon environments is often limited by inconsistent subgoals.

进一步看，论文的核心做法或实验重点可以概括为：In these settings, finite attention resources prevent the model from maintaining strategic coherence over thousands of steps.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term
- 检索关键词命中：episodic memory, working memory
- 来源分类信息：cs.CL, cs.AI, cs.MA

## Abstract Snapshot
Strategic reasoning in Large Language Models (LLMs) within long-horizon environments is often limited by inconsistent subgoals. In these settings, finite attention resources prevent the model from maintaining strategic coherence over thousands of steps. This limitation leads to strategic drift, where localized decisions fail to sustain a coherent trajectory across reasoning. To address this, we introduce EpicStar, a framework that enables agents to learn memory as policy to tackle long-horizon reasoning. Specifically, the agent maintains a bank of successful past episodes as a heuristic alongside a working memory to track short-term environmental changes. During inference, a dynamic gating mechanism determines whether to execute a retrieved action directly or to perform new reasoning through a contextual fusion of the retrieved episodes and current working memory. Utilizing StarCraft II as the testbed, we evaluated EpicStar against diverse opponent styles. It significantly outperforms baseline methods, achieving higher win rates while consuming an order of magnitude fewer tokens, and it maintains this advantage consistently across difficulty levels and opponent strategies. Our findings provide compelling evidence that structured cross-episode memory is essential for enabling LLM agents to perform robust, long-term strategic execution in dynamic, autonomous settings.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
