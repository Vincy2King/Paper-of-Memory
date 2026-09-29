# Self-Evolving Time-Series Forecasting Agents with Episodic Memory and Online Policy Learning

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.32689v1
- Published: 2026-09-26
- Updated: 2026-09-26
- Authors: Junyi Wang, Yilin Wang, Wen Wu, Chao Zhang
- Tags: agent, benchmark, context, episodic
- Categories: cs.LG
- URL: http://arxiv.org/abs/2609.32689v1

## One-Sentence Summary
LLM-based agents are increasingly used for time-series forecasting because they can organise contextual information, perform multi-step analysis, and guide the sequence of...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM-based agents are increasingly used for time-series forecasting because they can organise contextual information, perform multi-step analysis, and guide the sequence of actions required to complete forecasting tasks.

进一步看，论文的核心做法或实验重点可以概括为：Most existing agents focus only on the current forecasting instance.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.LG

## Abstract Snapshot
LLM-based agents are increasingly used for time-series forecasting because they can organise contextual information, perform multi-step analysis, and guide the sequence of actions required to complete forecasting tasks. Most existing agents focus only on the current forecasting instance. However, in real-world deployments, forecasting commonly operates online, with new forecasts issued from the currently available history as the forecast origin advances and the ground-truth targets of earlier instances progressively become available. These targets provide feedback on the actions taken in earlier instances, yet existing agents generally do not preserve or utilise this information to adapt their subsequent actions. To address this limitation, we introduce FASE, a Feedback-Aware Self-Evolving forecasting agent that converts such feedback into task-specific experience for subsequent forecasting instances. FASE combines episodic memory, which retrieves relevant completed instances, with online policy learning, which summarises the feedback accumulated across instances into ranking guidance. The proposed framework is evaluated on 29 dataset configurations selected from the GIFT-Eval benchmark. Across these 29 configurations, FASE attains the strongest aggregate point forecasting performance among the evaluated methods and reduces the normalised MAE by 9.1% relative to the best individual foundation model baseline. The results further indicate that the cumulative advantage of FASE increases as delayed feedback accumulates. Together, these findings demonstrate that FASE can continually self-evolve through feedback from completed forecasting instances without updating the parameters of the LLM.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
