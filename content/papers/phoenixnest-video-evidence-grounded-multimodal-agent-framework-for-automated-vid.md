# PhoenixNest-Video: Evidence-Grounded Multimodal Agent Framework for Automated Video Interview Assessment

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.02231v1
- Published: 2026-09-02
- Updated: 2026-09-02
- Authors: Fan Yuxuan, Huang Miaojun, Zhang Haimei, Wu Jingshen, Liu Hao
- Tags: agent, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.02231v1

## One-Sentence Summary
Interview assessment requires per-criterion judgments grounded in behavioral evidence, yet surging applicant volumes have made human-only evaluation costly and inconsistent,...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Interview assessment requires per-criterion judgments grounded in behavioral evidence, yet surging applicant volumes have made human-only evaluation costly and inconsistent, while existing AI approaches yield opaque...

进一步看，论文的核心做法或实验重点可以概括为：We introduce PhoenixNest-Video, an evidence-grounded multimodal agent framework for automated video interview assessment.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：working memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Interview assessment requires per-criterion judgments grounded in behavioral evidence, yet surging applicant volumes have made human-only evaluation costly and inconsistent, while existing AI approaches yield opaque scores without traceable rationale. We introduce PhoenixNest-Video, an evidence-grounded multimodal agent framework for automated video interview assessment. It builds a semantic video graph as structured working memory, performs rubric-conditioned retrieval with cross-modal verification across visual, audio, and textual streams, and produces per-criterion scores anchored to the candidate's materials. A Scorer trained via Rubrics-based Reinforcement Learning with dual rewards for rubric alignment and score-level differentiation internalizes the discriminative structure of multi-level rubrics. PhoenixNest-Video attains 91.50\% grade-level accuracy on VInterview-2025, outperforming substantially larger proprietary models. A compact, rubric-grounded agent therefore scores candidates in closer agreement with an expert panel than direct prompting of much larger models, and exposes the evidence behind each score for human review.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
