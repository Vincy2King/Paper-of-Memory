# Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.05686v1
- Published: 2026-05-07
- Updated: 2026-05-07
- Authors: Qiyao Liang, Risto Miikkulainen, Ila Fiete
- Tags: context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.05686v1

## One-Sentence Summary
Language models draw on two knowledge sources: facts baked into weights (parametric memory, PM) and information in context (working memory, WM).

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Language models draw on two knowledge sources: facts baked into weights (parametric memory, PM) and information in context (working memory, WM).

进一步看，论文的核心做法或实验重点可以概括为：We study two mechanistically distinct failure modes--conflict, when PM and WM disagree and interfere; and hallucination, when the queried fact was never learned.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：working memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Language models draw on two knowledge sources: facts baked into weights (parametric memory, PM) and information in context (working memory, WM). We study two mechanistically distinct failure modes--conflict, when PM and WM disagree and interfere; and hallucination, when the queried fact was never learned. Both produce confident output regardless, making output-based monitoring blind by design. We show both failures share a unified geometric account. In the hidden-state space of autoregressive generation, learned facts form attractor basins. Conflict is basin competition: WM disrupts convergence to the correct basin without raising output entropy. Hallucination is basin absence: the hidden state drifts freely when no memorized basin exists. The frozen LM head, designed for next-token prediction, cannot distinguish these cases and fires confidently either way. We verify this account in a controlled synthetic task--entity identifiers mapped to unique codes with PM installed via LoRA adapters--where ground truth is exact and component roles can be causally isolated through targeted adapter placement. Geometric margin--the hidden state's distance to the nearest memorized basin--reads this geometry directly and separates correct recall from hallucination far more cleanly than output entropy, with zero false refusals where entropy-based detection cannot avoid rejecting the vast majority of correct outputs. The separation holds on natural-language factual queries from the pretrained model with no adaptation, confirming attractor geometry is structural rather than a fine-tuning artifact. The fraction of confident hallucinations follows a scaling law $C = \exp(-c/\barΔ)$, growing with scale even as overall error rates fall. Hidden states reliably encode epistemic state; the frozen output head systematically erases it--and this erasure worsens with scale.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
