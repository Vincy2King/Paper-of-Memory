# MACBT: A Multi-Agent Cognitive Behavioral Therapy Decision Support System with Longitudinal Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.30939v1
- Published: 2026-09-25
- Updated: 2026-09-25
- Authors: De Jiang, Shuo Zhang, Weiwei Liao, Jianying Zhang, Chuanhui Yu, Hongen Liao, Kehong Yuan
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.30939v1

## One-Sentence Summary
Cognitive behavioral therapy (CBT) is an evidence-based first-line treatment for depression, yet its scale is constrained by the time clinicians spend on pre-session...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Cognitive behavioral therapy (CBT) is an evidence-based first-line treatment for depression, yet its scale is constrained by the time clinicians spend on pre-session preparation, post-session documentation, and...

进一步看，论文的核心做法或实验重点可以概括为：We present a clinician-facing AI decision-support system that combines a multi-agent CBT framework (MACBT) with a CBT-specific longitudinal memory module (CD Memory).

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Cognitive behavioral therapy (CBT) is an evidence-based first-line treatment for depression, yet its scale is constrained by the time clinicians spend on pre-session preparation, post-session documentation, and longitudinal cognitive-pathology tracking. We present a clinician-facing AI decision-support system that combines a multi-agent CBT framework (MACBT) with a CBT-specific longitudinal memory module (CD Memory). MACBT encodes the five-stage CBT workflow (assessment, Socratic questioning, cognitive restructuring, behavioral experiments, and treatment monitoring) into five collaborative agents. CD Memory tracks cognitive-distortion type, frequency, severity, and restructuring efficacy across sessions to generate pre-session pathology reports and intervention-priority recommendations. We construct a Chinese CBT dialogue corpus via dual-role large language model simulation and train a Qwen3-14B backbone with supervised fine-tuning and direct preference optimization. Evaluation with GPT-4 judges shows MACBT outperforms MeChat, SoulChat, PsyChat, and CPsyCounX in professionalism (2.62) and clinical authenticity (2.25). The full memory-augmented system further improves session quality by 12.6% and achieves a longitudinal mean of 2.29 on cross-session continuity, intervention progression, and personalization.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
