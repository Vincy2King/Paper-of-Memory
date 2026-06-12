# Ontology Memory-Augmented ASR Correction for Long Text-Speech Interleaved Conversations

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.13464v1
- Published: 2026-06-11
- Updated: 2026-06-11
- Authors: Xinxin Li, Huiyao Chen, Meishan Zhang, Yunxin Li, Zulong Chen, Zhibo Ren, Xiaoqing Dong Baotian Hu, Min Zhang
- Tags: context, conversation
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2606.13464v1

## One-Sentence Summary
Automatic speech recognition (ASR) correction has traditionally focused on isolated utterances or short local contexts.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Automatic speech recognition (ASR) correction has traditionally focused on isolated utterances or short local contexts.

进一步看，论文的核心做法或实验重点可以概括为：However, as text and speech become increasingly interleaved in long interactions, ASR correction requires conversation-level contextual evidence.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, conversation
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Automatic speech recognition (ASR) correction has traditionally focused on isolated utterances or short local contexts. However, as text and speech become increasingly interleaved in long interactions, ASR correction requires conversation-level contextual evidence. Existing ASR correction methods often rely on the current hypothesis or concatenate raw dialogue history. In such contexts, sparse correction evidence can be difficult to locate amid redundancy and noise. Addressing these challenges, we propose an ontology memory-augmented ASR correction framework for long text-speech interleaved conversations. The framework organizes preceding interaction history into a dynamically updatable ontology memory, where entities, terminology, surface variants, potential ASR confusions, and semantic relations are stored as retrievable nodes for context-grounded correction. To evaluate this setting, we construct RAMC-Corr, a dataset derived from MAGIC-RAMC for long-range ASR correction with grounded context. Experiments on RAMC-Corr show that our method improves over direct correction in 9 out of 10 paired backbone-setting combinations and encourages more selective and evidence-grounded corrections for context-dependent ASR errors.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
