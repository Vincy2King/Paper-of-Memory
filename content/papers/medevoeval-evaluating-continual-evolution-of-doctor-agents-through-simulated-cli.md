# MedEvoEval: Evaluating Continual Evolution of Doctor Agents through Simulated Clinical Episodes

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.28900v1
- Published: 2026-06-27
- Updated: 2026-06-27
- Authors: Hui Zhang
- Tags: agent, benchmark, retrieval
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2606.28900v1

## One-Sentence Summary
Doctor agents are moving beyond single-turn answer generation toward evolving clinical decision systems.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Doctor agents are moving beyond single-turn answer generation toward evolving clinical decision systems.

进一步看，论文的核心做法或实验重点可以概括为：Within an outpatient episode, they acquire evidence, use examination and consultation resources, and decide when to finalize a diagnosis and management plan.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Doctor agents are moving beyond single-turn answer generation toward evolving clinical decision systems. Within an outpatient episode, they acquire evidence, use examination and consultation resources, and decide when to finalize a diagnosis and management plan. Across episodes, their behavior may change through memory, retrieval, reflection, or other update mechanisms. Current evaluations only partially cover this setting. Fixed-input medical QA benchmarks score final answers from complete inputs, whereas many interactive benchmarks still focus on individual encounters or fixed runs, providing limited support for evaluating how episode-level decisions interact with cross-episode experience. We introduce MedEvoEval, an executable longitudinal evaluation framework based on action-gated simulated outpatient episodes. Each source case is converted into role-specific patient, examination, and manager views; evidence is revealed only through valid actions; and each episode records a structured trace that links observations, actions, final outputs, manager scores, and optional experience write-back. We release a runnable E&D artifact with 700 processed episodes, provenance notes, schemas, an episode runner, scoring scripts, configurations, example logs, analysis code, and trajectory- and step-level derivatives. Experiments show that episode traces expose process costs hidden by final-answer scoring, show how MDT-style consultation reallocates resources, and support longitudinal analyses of memory maturation, held-out transfer, update-stage response, and backward retention. Together, these results show that MedEvoEval provides a concrete basis for evaluating whether doctor agents improve through experience, transfer useful behavior, and retain earlier capabilities over time.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
