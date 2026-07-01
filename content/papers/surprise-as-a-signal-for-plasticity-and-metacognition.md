# Surprise as a Signal for Plasticity and Metacognition

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.31495v1
- Published: 2026-06-30
- Updated: 2026-06-30
- Authors: Louis Mouchon
- Tags: episodic
- Categories: cs.AI, cs.LG
- URL: http://arxiv.org/abs/2606.31495v1

## One-Sentence Summary
We study a single idea across two settings: that a prediction-error signal, computed by a small predictor over the latent space of a frozen encoder, can serve both as a gate on...

## Introduction
这篇论文被纳入仓库，是因为它和 `episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We study a single idea across two settings: that a prediction-error signal, computed by a small predictor over the latent space of a frozen encoder, can serve both as a gate on plasticity and as a substrate for...

进一步看，论文的核心做法或实验重点可以概括为：In the first system, a non-parametric episodic memory writes a new concept only when this surprise is high, and a periodic offline replay phase consolidates recent traces into a slow linear readout.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI, cs.LG

## Abstract Snapshot
We study a single idea across two settings: that a prediction-error signal, computed by a small predictor over the latent space of a frozen encoder, can serve both as a gate on plasticity and as a substrate for metacognition. In the first system, a non-parametric episodic memory writes a new concept only when this surprise is high, and a periodic offline replay phase consolidates recent traces into a slow linear readout. On a continual stream of 1000 ImageNet classes with a frozen DINOv2 or I-JEPA backbone, the consolidation phase recovers 17.7 points of retention on the oldest classes for DINOv2 and 51.3 points for I-JEPA (single-seed runs), and an ablation shows that replaying only a recent window is worse than no replay at all. In few-shot evaluation the same memory reaches 91.6% on 5-way 1-shot mini-ImageNet, above a task-specific baseline, while a harder 500-way regime exposes the true difficulty. In the second system, the same surprise signal, computed in a shared text-image space, modulates the behaviour of a vision-language model: it answers assertively when a concept is known, hedges when it is partially familiar, and refuses to identify the object and asks for an explanation when it is novel, learning the concept from a single user utterance. The external detector separates known from novel concepts at an AUROC of 0.966 (95% CI +/-0.024), far above the model's own verbalised confidence (0.618), while its token-level confidence sits below chance under greedy decoding; after a sleep phase that empties the fast store, the system recalls 99.2% of fifty taught facts from the consolidated store while a base model recovers none. We report both systems as proof-of-concept, with explicit limitations, and position the second against recent episodic-memory and personalised-VLM work.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
