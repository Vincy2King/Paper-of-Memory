# ForecastCompass: Guiding Agentic Forecasting with Adaptive Factor Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.30858v1
- Published: 2026-05-29
- Updated: 2026-05-29
- Authors: Yurui Chang, Yongkang Du, Yuanpu Cao, Jinghui Chen, Lu Lin
- Tags: agent, retrieval
- Categories: cs.LG
- URL: http://arxiv.org/abs/2605.30858v1

## One-Sentence Summary
Agentic forecasting is important for decision-making in dynamic environments, but it remains challenging because agents must reason from incomplete, time-limited evidence and...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agentic forecasting is important for decision-making in dynamic environments, but it remains challenging because agents must reason from incomplete, time-limited evidence and produce calibrated probabilities before...

进一步看，论文的核心做法或实验重点可以概括为：Memory provides a natural mechanism for transferring experience from resolved forecasts to future prediction tasks.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Agentic forecasting is important for decision-making in dynamic environments, but it remains challenging because agents must reason from incomplete, time-limited evidence and produce calibrated probabilities before outcomes are resolved. Memory provides a natural mechanism for transferring experience from resolved forecasts to future prediction tasks. However, existing agent-memory methods are not tailored to forecasting, as they typically store past interactions, reflections, or factual associations without explicitly representing reusable predictive factors or calibration knowledge. We propose ForecastCompass (FoCo), an adaptive factor-based memory framework for agentic forecasting. FoCo organizes forecasting experience with a hierarchical forecasting-task taxonomy, enabling retrieval task-relevant forecasting knowledge. It maintains two complementary memory components: factor memory, which captures reusable predictive dimensions, and reasoning memory, which encodes probability updating, uncertainty handling, and calibration principles. Using retrospective analyses as learning signals, FoCo iteratively revises memory through a verbalized memory-revision procedure, enabling the agent to accumulate transferable forecasting knowledge over time. Experiments on Prophet Arena and FutureX with GPT-5-mini and Gemini-2.5-Flash show that FoCo improves both probabilistic accuracy and calibration.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
