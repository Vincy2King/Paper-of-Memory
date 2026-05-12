# Mela: Test-Time Memory Consolidation based on Transformation Hypothesis

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.10537v1
- Published: 2026-05-11
- Updated: 2026-05-11
- Authors: Lungchuan Chen
- Tags: context, episodic, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2605.10537v1

## One-Sentence Summary
Memory consolidation, the process by which transient experiences are transformed into stable, structured representations, is a foundational organizing principle in the human...

## Introduction
这篇论文被纳入仓库，是因为它和 `context, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory consolidation, the process by which transient experiences are transformed into stable, structured representations, is a foundational organizing principle in the human brain, yet it remains largely unexplored as...

进一步看，论文的核心做法或实验重点可以概括为：In this work, we leverage established neuroscientific theories of memory consolidation and cross-frequency coupling to propose the Hierarchical Memory Module (HMM), a neural memory architecture composed of two...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, episodic, retrieval
- 检索关键词命中：memory augmented, memory retrieval, memory-augmented
- 来源分类信息：cs.CL

## Abstract Snapshot
Memory consolidation, the process by which transient experiences are transformed into stable, structured representations, is a foundational organizing principle in the human brain, yet it remains largely unexplored as a design principle for modern sequence models. In this work, we leverage established neuroscientific theories of memory consolidation and cross-frequency coupling to propose the Hierarchical Memory Module (HMM), a neural memory architecture composed of two functionally distinct sub-modules that operate at different update frequencies. Inspired by the transformation hypothesis, the low-frequency sub-module produces high-level representations that capture abstract, gist-level knowledge, while the high-frequency sub-module produces fine-grained representations that preserve richer episodic detail. The final memory output is dynamically reconstructed as a context-dependent combination of both representations, analogous to the reconstructive nature of human memory retrieval. We integrate HMM into a Transformer-based language decoder to form Mela, a family of memory-augmented language models that perform online memory consolidation at test time. To further exploit the multi-granularity memory representations produced by HMM, we introduce MemStack, a method that distributes different levels of memory features across the early layers of the decoder without introducing additional tokens. Experiments on language modeling demonstrate that Mela outperforms Transformer baselines across all the model sizes. Moreover, with the pretrained context length fixed at 4K, Mela maintains performance on significantly longer contexts, whereas Transformer baselines degrade rapidly beyond their training length. Extensive ablation studies validate the contribution of each component and provide guidance for practical configuration.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
