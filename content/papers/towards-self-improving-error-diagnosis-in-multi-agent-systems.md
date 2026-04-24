# Towards Self-Improving Error Diagnosis in Multi-Agent Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.17658v1
- Published: 2026-04-19
- Updated: 2026-04-19
- Authors: Jiazheng Li, Emine Yilmaz, Bei Chen, Dieu-Thu Le
- Tags: agent, benchmark, context, episodic
- Categories: cs.MA, cs.CL
- URL: http://arxiv.org/abs/2604.17658v1

## One-Sentence Summary
Large Language Model (LLM)-based Multi-Agent Systems (MAS) enable complex problem-solving but introduce significant debugging challenges, characterized by long interaction...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large Language Model (LLM)-based Multi-Agent Systems (MAS) enable complex problem-solving but introduce significant debugging challenges, characterized by long interaction traces, inter-agent dependencies, and delayed...

进一步看，论文的核心做法或实验重点可以概括为：Existing diagnostic approaches often rely on expensive expert annotation or ''LLM-as-a-judge'' paradigms, which struggle to pinpoint decisive error steps within extended contexts.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.MA, cs.CL

## Abstract Snapshot
Large Language Model (LLM)-based Multi-Agent Systems (MAS) enable complex problem-solving but introduce significant debugging challenges, characterized by long interaction traces, inter-agent dependencies, and delayed error manifestation. Existing diagnostic approaches often rely on expensive expert annotation or ''LLM-as-a-judge'' paradigms, which struggle to pinpoint decisive error steps within extended contexts. In this paper, we introduce ErrorProbe, a self-improving framework for semantic failure attribution that identifies responsible agents and the originating error step. The framework operates via a three-stage pipeline: (1) operationalizing the MAS failure taxonomy to detect local anomalies, (2) performing symptom-driven backward tracing to prune irrelevant context, and (3) employing a specialized multi-agent team (Strategist, Investigator, Arbiter) to validate error hypotheses through tool-grounded execution. Crucially, ErrorProbe maintains a verified episodic memory that updates only when error patterns are confirmed by executable evidence, without the need for annotation. Experiments across the TracerTraj and Who&When benchmarks demonstrate that ErrorProbe significantly outperforms baselines, particularly in step-level localization, while the verified memory enables robust cross-domain transfer without retraining.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
