# Large Language Models Do Not Always Need Readable Language

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.19857v1
- Published: 2026-06-18
- Updated: 2026-06-18
- Authors: Jiayi Zhu, Haoxuan Peng, Junxi Wang, Liang Ke, Chen Zhang, Linfeng Zhang
- Tags: agent, context
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2606.19857v1

## One-Sentence Summary
Large language models (LLMs) are commonly prompted and interfaced with human-readable natural language, even when the intended reader is another model.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models (LLMs) are commonly prompted and interfaced with human-readable natural language, even when the intended reader is another model.

进一步看，论文的核心做法或实验重点可以概括为：This paper investigates whether semantic information can be encoded in compact, non-standard textual forms that sacrifice human readability while remaining recoverable by LLMs.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Large language models (LLMs) are commonly prompted and interfaced with human-readable natural language, even when the intended reader is another model. This paper investigates whether semantic information can be encoded in compact, non-standard textual forms that sacrifice human readability while remaining recoverable by LLMs. We refer to this class of model-centric textual representations as BabelTele, approached here not as a fixed protocol but as an empirical probe into LLMs' capacity to generate and interpret such representations. Through readability diagnostics, model likelihood measures, human questionnaires, and downstream task evaluations, we find that BabelTele can substantially depart from ordinary natural language while preserving core semantics for instruction-tuned LLMs. As a task-agnostic representational paradigm, BabelTele demonstrates high information density, maintaining 99.5% semantic fidelity even when the text volume is condensed to 27.9% of its original length. We further evaluate its semantic robustness in cross-model transfer, agent memory, and multi-agent communication. Results suggest that BabelTele can reduce context overhead while generally maintaining reliable downstream performance, although its effectiveness depends on the compressor-reader pair and task setting. These findings indicate that human readability, natural-language typicality, and model-side semantic recoverability can be partially decoupled, opening a path toward model-native representations in future exploration of LLM systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
