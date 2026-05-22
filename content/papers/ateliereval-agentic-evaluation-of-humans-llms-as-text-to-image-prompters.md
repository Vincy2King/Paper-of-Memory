# AtelierEval: Agentic Evaluation of Humans & LLMs as Text-to-Image Prompters

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.22645v1
- Published: 2026-05-21
- Updated: 2026-05-21
- Authors: Hanjun Luo, Zhimu Huang, Sylvia Chung, Yiran Wang, Yingbin Jin, Jialin Li, Jiang Li, Xinfeng Li, Hanan Salam
- Tags: agent, benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.22645v1

## One-Sentence Summary
Text-to-image (T2I) systems increasingly rely on upstream prompters, either humans or multimodal large language models (MLLMs), to translate user intent into detailed prompts.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Text-to-image (T2I) systems increasingly rely on upstream prompters, either humans or multimodal large language models (MLLMs), to translate user intent into detailed prompts.

进一步看，论文的核心做法或实验重点可以概括为：Yet current benchmarks fix the prompt and only evaluate T2I models, leaving the prompting proficiency of this upstream component entirely unmeasured.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Text-to-image (T2I) systems increasingly rely on upstream prompters, either humans or multimodal large language models (MLLMs), to translate user intent into detailed prompts. Yet current benchmarks fix the prompt and only evaluate T2I models, leaving the prompting proficiency of this upstream component entirely unmeasured. We introduce AtelierEval, the first unified benchmark that quantifies prompting proficiency across 360 expert-crafted tasks. Grounded in a cognitive view, it spans three task categories and instantiates tasks using a taxonomy of real-world challenges, with a dual interface for both humans and MLLMs. To enable scalable and reliable evaluation, we propose AtelierJudge, a skill-based, memory-augmented agentic evaluator. It produces subjective and objective scores for prompt-image pairs, achieving a Spearman correlation of 0.79 with human experts, approaching human performance. Extensive experiments benchmark 8 MLLMs against 48 human users across 4 T2I backends, validate AtelierEval as a robust diagnostic tool, and reveal the superiority of mimicry over planning, advocating for an image-augmented direction for future prompters. Our work is released to support future research.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
