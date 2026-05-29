# Towards Verifiable Multimodal Deep Research: A Multi-Agent Harness for Interleaved Report Generation

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.29861v1
- Published: 2026-05-28
- Updated: 2026-05-28
- Authors: Chenghao Zhang, Guanting Dong, Yufan Liu, Tong Zhao, Zhicheng Dou
- Tags: agent, benchmark
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2605.29861v1

## One-Sentence Summary
Large Language Models (LLMs) have advanced autonomous agents from deep search, which retrieves concise factual answers, to deep research, which synthesizes scattered evidence...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large Language Models (LLMs) have advanced autonomous agents from deep search, which retrieves concise factual answers, to deep research, which synthesizes scattered evidence into long-form reports.

进一步看，论文的核心做法或实验重点可以概括为：However, verifiable multimodal deep research remains challenging due to open-ended synthesis without deterministic ground truth and the need to interleave textual arguments with visual evidence.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：working memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Large Language Models (LLMs) have advanced autonomous agents from deep search, which retrieves concise factual answers, to deep research, which synthesizes scattered evidence into long-form reports. However, verifiable multimodal deep research remains challenging due to open-ended synthesis without deterministic ground truth and the need to interleave textual arguments with visual evidence. We propose \textsc{Ptah}, a multi-agent harness for interleaved report generation. \textsc{Ptah} orchestrates the lifecycle from user query to rendered web report through planning, research, and writing stages, where specialized agents construct visual-aware plans, collect claim-grounded evidence, maintain source-aligned images in a \textit{Visual Working Memory}, and compose reports through declarative multimodal tool use. A verifier agent serves as the harness's acceptance function, enforcing factual grounding, citation fidelity, and cross-modal consistency throughout the workflow. We further introduce \textsc{Ptah}Eval, an evaluation protocol that augments existing benchmarks with image-level and presentation-level assessments. Experiments on deep research benchmarks show that \textsc{Ptah} produces more reliable, visually informative, and usable human-facing multimodal reports than strong baselines.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
