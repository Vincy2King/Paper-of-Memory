# Activation-Guided Neuron Intervention to Induce Alzheimer's-Related Computational Language Phenotypes in a Large Language Model

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.03067v1
- Published: 2026-08-04
- Updated: 2026-08-04
- Authors: Rui He, Ercong Nie, Hong Jiang, Iris E. Sommer, Philipp Homan, Wolfram Hinzen
- Tags: working memory
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.03067v1

## One-Sentence Summary
Changes in spontaneous speech provide an early signal of cognitive dysfunction in Alzheimer's disease (AD) that large language models (LLMs) can detect.

## Introduction
这篇论文被纳入仓库，是因为它和 `working memory` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Changes in spontaneous speech provide an early signal of cognitive dysfunction in Alzheimer's disease (AD) that large language models (LLMs) can detect.

进一步看，论文的核心做法或实验重点可以概括为：However, detection alone cannot establish whether the underlying model representations contribute functionally to behavior.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：working memory
- 检索关键词命中：working memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Changes in spontaneous speech provide an early signal of cognitive dysfunction in Alzheimer's disease (AD) that large language models (LLMs) can detect. However, detection alone cannot establish whether the underlying model representations contribute functionally to behavior. We introduce an activation-guided intervention framework using Qwen3-8B. The framework identifies feed-forward neurons with higher activation rates for AD than control transcripts and modulates their output contributions during generation by scaling the corresponding down-projection weights. This yielded nine edited variants differing in intervention direction, magnitude, and scope. The original and edited models completed the same 12-turn neuropsychological battery, assessed through blinded human ratings and computational linguistic measures. Amplifying AD-associated neurons produced graded impairments in story recall, verbal fluency, working memory, procedural discourse, scene construction, and coreference resolution. Attenuation largely preserved performance and selectively improved several outcomes. Amplification also reduced lexical surprisal, idea density, syntactic complexity, and discourse quantity, broadly paralleling changes reported in human AD speech. These findings show that neurons identified solely from clinical language differences can influence behavior across multiple cognitive domains, providing proof of concept for an AD-related computational phenotype and a controlled framework for experimentally examining links between language and broader cognitive dysfunction.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
