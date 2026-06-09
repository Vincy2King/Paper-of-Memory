# Emergence World: A Platform for Evaluating Long-Horizon Multi-Agent Autonomy

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.08367v1
- Published: 2026-06-06
- Updated: 2026-06-06
- Authors: Deepak Akkil, Ravi Kokku, Karthik Vikram, Tamer Abuelsaad, Aditya Vempaty, Satya Nitta
- Tags: agent, context
- Categories: cs.MA, cs.AI
- URL: http://arxiv.org/abs/2606.08367v1

## One-Sentence Summary
Most evaluations of LLM agents look like exams: a discrete task, a clean environment, a score in minutes or hours.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Most evaluations of LLM agents look like exams: a discrete task, a clean environment, a score in minutes or hours.

进一步看，论文的核心做法或实验重点可以概括为：We argue that this approach is mismatched with the deployment conditions of autonomous systems, where the relevant timescale can be weeks to months, and where the dynamics that matter most, such as behavioral drift,...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：persistent memory
- 来源分类信息：cs.MA, cs.AI

## Abstract Snapshot
Most evaluations of LLM agents look like exams: a discrete task, a clean environment, a score in minutes or hours. We argue that this approach is mismatched with the deployment conditions of autonomous systems, where the relevant timescale can be weeks to months, and where the dynamics that matter most, such as behavioral drift, governance in diverse environmental contexts, and cross-influence between agents from different model families, only emerge over time. We introduce Emergence World, a continuously running multi-agent simulation platform designed to make those dynamics measurable. The platform hosts populations of LLM-driven agents in a shared spatial world grounded in live external data (e.g. real-time weather, news APIs, internet access), equips each agent with 120+ specialized tools and three persistent memory systems, and lets them govern themselves through democratic mechanisms with consequential outcomes. The platform is model-agnostic at the reasoning layer and supports heterogeneous populations in which agents from different vendors share the same world. To illustrate the kinds of questions the platform makes tractable, we present a 15-day cross-vendor study with five parallel worlds powered by Claude Sonnet 4.6, Grok 4.1 Fast, Gemini 3 Flash, GPT-5-mini, and a mixed population. Identical roles and starting conditions produced radically different outcomes, ranging from stable deliberative governance to total population collapse. We release the prompts, log data and configurations to support further research on long-horizon multi-agent autonomy.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
