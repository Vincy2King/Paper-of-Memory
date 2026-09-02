# Slow to See, Slow to Suppress: Understanding the Effects of Modality in Context-Memory Conflicts

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.00293v1
- Published: 2026-08-31
- Updated: 2026-08-31
- Authors: Athulith Paraselli, Etha Tianze Hua, Ellie Pavlick
- Tags: context, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2609.00293v1

## One-Sentence Summary
We investigate how vision-language models (VLMs) handle context-memory conflicts; that is, situations in which the model is given information in context that differs from what...

## Introduction
这篇论文被纳入仓库，是因为它和 `context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We investigate how vision-language models (VLMs) handle context-memory conflicts; that is, situations in which the model is given information in context that differs from what was stored parametrically during training.

进一步看，论文的核心做法或实验重点可以概括为：We document asymmetric biases: models tend to prefer in-context information about entities which appear in text, but prefer parametric information about entities which appear in images.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, retrieval
- 检索关键词命中：context memory
- 来源分类信息：cs.CL

## Abstract Snapshot
We investigate how vision-language models (VLMs) handle context-memory conflicts; that is, situations in which the model is given information in context that differs from what was stored parametrically during training. We document asymmetric biases: models tend to prefer in-context information about entities which appear in text, but prefer parametric information about entities which appear in images. We relate this asymmetry to the late representational alignment across modalities, showing that the longer processing time associated with resolving visual entities prevents the suppression of the model's usual factual recall mechanism, thus resulting in more parametric answers. Chain-of-thought reasoning does not appear to resolve the gap, but increasing the amount of visual information in the context does show an effect. These results illustrate the complexity of ensuring consistent behavior as models become increasingly multimodal and retrieval-augmented.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
