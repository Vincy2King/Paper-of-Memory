# Decoupled Analysis-Judging: An Automated Creativity Evaluator Using LLMs in Complex Multi-step Creativity Tasks

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.03432v1
- Published: 2026-09-03
- Updated: 2026-09-03
- Authors: Xiangyu Wang, Jin Wu, Xiaoyu Li, Chanjin Zheng, Yifeng Zhou
- Tags: context
- Categories: cs.CL
- URL: http://arxiv.org/abs/2609.03432v1

## One-Sentence Summary
Automated evaluation of creativity tasks remains challenging for LLM-as-a-Judge, as LLM is susceptible to biases such as verbosity bias and leniency bias.

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Automated evaluation of creativity tasks remains challenging for LLM-as-a-Judge, as LLM is susceptible to biases such as verbosity bias and leniency bias.

进一步看，论文的核心做法或实验重点可以概括为：Such limitations are particularly evident in Contextually-Grounded and Procedurally-Structured Tasks (CGPST), a complex multi-step creativity task where inter-step dependencies, highly subjectivity, and wide scoring...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CL

## Abstract Snapshot
Automated evaluation of creativity tasks remains challenging for LLM-as-a-Judge, as LLM is susceptible to biases such as verbosity bias and leniency bias. Such limitations are particularly evident in Contextually-Grounded and Procedurally-Structured Tasks (CGPST), a complex multi-step creativity task where inter-step dependencies, highly subjectivity, and wide scoring ranges lead to more unstable and biased judgments. Existing approaches either rely on task-specific training or directly apply LLM-as-a-Judge, both of which struggle to ensure reliable evaluation under such complexity. To bridge these gaps, we propose CreaEval, an automated creativity evaluator for CGPST that decouples typical LLM-as-a-Judge into analysis and judging. Correspondingly, CreaEval involves two critical phases: Memory-augmented Analysis, a SoT-LLM converts multi-step responses into structured evaluation evidence, incorporating cross-step memory; and Evidence-based Judging, a Judge-LLM uses the extracted evidence for judging without accessing raw responses. Comprehensive experiments show that CreaEval achieves an average performance improvement of 22.74% over the second-best baselines across CGPST and two classic simple creativity tasks, demonstrating its generalizability. The code is available at https://github.com/Jaong/CreaEval.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
