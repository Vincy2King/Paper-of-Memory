# Masked by Consensus: Disentangling Privileged Knowledge in LLM Correctness

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.12373v4
- Published: 2026-04-14
- Updated: 2026-04-22
- Authors: Tomer Ashuach, Shai Gretz, Yoav Katz, Yonatan Belinkov, Liat Ein-Dor
- Tags: retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2604.12373v4

## One-Sentence Summary
Humans use introspection to evaluate their understanding through private internal states inaccessible to external observers.

## Introduction
这篇论文被纳入仓库，是因为它和 `retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Humans use introspection to evaluate their understanding through private internal states inaccessible to external observers.

进一步看，论文的核心做法或实验重点可以概括为：We investigate whether large language models possess similar privileged knowledge about answer correctness, information unavailable through external observation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.CL

## Abstract Snapshot
Humans use introspection to evaluate their understanding through private internal states inaccessible to external observers. We investigate whether large language models possess similar privileged knowledge about answer correctness, information unavailable through external observation. We train correctness classifiers on question representations from both a model's own hidden states and external models, testing whether self-representations provide a performance advantage. On standard evaluation, we find no advantage: self-probes perform comparably to peer-model probes. We hypothesize this is due to high inter-model agreement of answer correctness. To isolate genuine privileged knowledge, we evaluate on disagreement subsets, where models produce conflicting predictions. Here, we discover domain-specific privileged knowledge: self-representations consistently outperform peer representations in factual knowledge tasks, but show no advantage in math reasoning. We further localize this domain asymmetry across model layers, finding that the factual advantage emerges progressively from early-to-mid layers onward, consistent with model-specific memory retrieval, while math reasoning shows no consistent advantage at any depth.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
