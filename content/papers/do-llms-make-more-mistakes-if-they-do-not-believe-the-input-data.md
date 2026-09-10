# Do LLMs Make More Mistakes If They Do Not Believe the Input Data?

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.09363v1
- Published: 2026-09-08
- Updated: 2026-09-08
- Authors: Peter Kochelka, Aleš Manuel Papáček, Vojtěch Dvořák, Ondřej Dušek
- Tags: context, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2609.09363v1

## One-Sentence Summary
Large language models (LLMs) are prone to hallucinating or misinterpreting facts, which impairs their usability in retrieval-augmented generation or data-to-text systems.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models (LLMs) are prone to hallucinating or misinterpreting facts, which impairs their usability in retrieval-augmented generation or data-to-text systems.

进一步看，论文的核心做法或实验重点可以概括为：We analyse how faithfulness of LLMs to provided context depends on how plausible they perceive the context to be (context-memory conflict).

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, retrieval
- 检索关键词命中：context memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Large language models (LLMs) are prone to hallucinating or misinterpreting facts, which impairs their usability in retrieval-augmented generation or data-to-text systems. We analyse how faithfulness of LLMs to provided context depends on how plausible they perceive the context to be (context-memory conflict). To better identify error patterns, we make use of the increased difficulty of non-English and low-resource language text generation and input data based on local knowledge, only partially captured in models' parametric knowledge. We let the models generate text in English, Czech, Slovak and Upper Sorbian from factual (FA), counterfactual (CFA) and fictional (FI) RDF triples containing local Czech and Slovak data. Contrary to our expectations, we observe only a weak context-memory conflict on the human-annotated sample. For Kimi K3 as an LLM judge, which agrees well with human annotations on the sample, counterfactual inputs receive only slightly lower faithfulness scores than factual ones (-0.05 on a 1-5 scale). We also find that a suboptimal choice of LLM judge would lead to overestimating the strength of the context-memory conflict.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
