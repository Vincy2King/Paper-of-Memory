# FIDES: Faithful Inference via Deep Evidence Signals for Retrieval-Memory Conflict in RAG

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.05644v1
- Published: 2026-06-04
- Updated: 2026-06-04
- Authors: Zhe Yu, Wenpeng Xing, Tiancheng Zhao, Mohan Li, Changting Lin, Meng Han
- Tags: benchmark, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.05644v1

## One-Sentence Summary
When retrieved evidence contradicts parametric memory, language models frequently ignore context and default to memorized priors -- a failure that undermines the core purpose of...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：When retrieved evidence contradicts parametric memory, language models frequently ignore context and default to memorized priors -- a failure that undermines the core purpose of retrieval augmentation.

进一步看，论文的核心做法或实验重点可以概括为：Contrastive decoding amplifies the context-conditioned output to suppress parametric bias, but existing methods rest on an implicit assumption that this bias is uniform across tokens.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
When retrieved evidence contradicts parametric memory, language models frequently ignore context and default to memorized priors -- a failure that undermines the core purpose of retrieval augmentation. Contrastive decoding amplifies the context-conditioned output to suppress parametric bias, but existing methods rest on an implicit assumption that this bias is uniform across tokens. A single global contrastive weight over-penalizes safe tokens while leaving genuinely conflicted ones insufficiently corrected. We identify token-level conflict concentration: retrieval-memory tension is sharply heterogeneous, concentrated on a small fraction of answer-critical decoding steps. This reframes contrastive decoding from how much contrast to apply to where to apply it. We propose FIDES (Faithful Inference via Deep Evidence Signals), a training-free decoder that reads three internal signals probing retrieval-memory conflict at complementary depths -- output surface, hidden representations, and prediction trajectory -- and fuses them to govern intervention strength at each decoding step. Across three benchmarks and six backbones -- four primary 7B/8B models and two scaling backbones up to 70B -- FIDES achieves the best context fidelity in all 18 settings, outperforming the strongest training-free baseline by +3 to +13 points. On the 70B scale, fidelity reaches 92-94% while F1 surges to 62-63%, demonstrating that token-level selectivity unlocks generation capability that coarse contrastive rules suppress.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
