# FlowEdit: Associative Memory for Lifelong Pronunciation Adaptation in Flow-Matching TTS

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.20518v1
- Published: 2026-06-18
- Updated: 2026-06-18
- Authors: Harshit Singh, Ayush Pratap Singh, Nityanand Mathur
- Tags: benchmark, episodic
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.20518v1

## One-Sentence Summary
Flow-matching text-to-speech systems achieve remarkable zero-shot quality but remain static after deployment: pronunciation errors on out-of-vocabulary proper nouns persist...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Flow-matching text-to-speech systems achieve remarkable zero-shot quality but remain static after deployment: pronunciation errors on out-of-vocabulary proper nouns persist unless the model is retrained.

进一步看，论文的核心做法或实验重点可以概括为：We introduce FlowEdit, a life-long adaptation framework for frozen flow-matching TTS that learns pronunciation corrections as latent conditioning edits rather than weight updates.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Flow-matching text-to-speech systems achieve remarkable zero-shot quality but remain static after deployment: pronunciation errors on out-of-vocabulary proper nouns persist unless the model is retrained. We introduce FlowEdit, a life-long adaptation framework for frozen flow-matching TTS that learns pronunciation corrections as latent conditioning edits rather than weight updates. When corrective feedback is provided, FlowEdit optimizes a token-level perturbation in the text embedding space, then stores the correction in a Modern Hopfield Network serving as content-addressable episodic memory. At inference, corrections are retrieved via soft attention with a similarity gate, enabling fuzzy morphological matching. On our curated benchmark of 312 multilingual proper nouns across 18 language families, FlowEdit reduces target-word Phoneme Error Rate by 92.7% relative to the zero-shot baseline while maintaining identical general-speech quality. Corrections complete in approximately 15 seconds on a single GPU.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
