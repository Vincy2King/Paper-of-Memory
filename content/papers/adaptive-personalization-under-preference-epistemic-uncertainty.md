# Adaptive Personalization Under Preference Epistemic Uncertainty

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.40930v1
- Published: 2026-10-29
- Updated: 2026-10-29
- Authors: Priyanka Dey, Rajarshi Das, Vikas Bahirwani, Qi Zeng, Julia Kruk, Qi Qi
- Tags: benchmark, context, conversation, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.40930v1

## One-Sentence Summary
Human preferences change over time: an established preference may remain valid over time, become uncertain as context shifts, or be explicitly revised.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Human preferences change over time: an established preference may remain valid over time, become uncertain as context shifts, or be explicitly revised.

进一步看，论文的核心做法或实验重点可以概括为：Effective personalization requires conversational AI to adapt its response strategy to evolving preferences rather than relying on passive memory retrieval.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, conversation, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.CL

## Abstract Snapshot
Human preferences change over time: an established preference may remain valid over time, become uncertain as context shifts, or be explicitly revised. Effective personalization requires conversational AI to adapt its response strategy to evolving preferences rather than relying on passive memory retrieval. We formalize this capability as adaptive personalization under epistemic uncertainty. A human preference study further confirms that people favor state-contingent response strategies as preference uncertainty changes. To evaluate whether language models mirror this adaptation, we create a multilingual benchmark spanning 250 personas, 5 languages, and 25K conversational turns that decouples strategy selection from response execution. Across eight closed- and open-weight models, we uncover a recognition-generation gap: models reliably identify appropriate strategies when selecting among candidate options, but collapse during open-ended generation, suffering a 35-46% drop in strategy calibration. Crucially, this failure is systematic: models default to exploit-first behavior, over-relying on existing preferences regardless of preference epistemic uncertainty. We show this failure is addressable: while prompting interventions fail, targeted training that supervises models' internal strategy representations toward state-conditional human preferences narrows the user acceptability generalization gap by a third on out-of-distribution personas and conversational styles.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
