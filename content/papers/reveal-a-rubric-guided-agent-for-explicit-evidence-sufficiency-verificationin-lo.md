# REVEAL: A Rubric-Guided Agent for Explicit Evidence Sufficiency Verificationin Long-Video Question Answering

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.08612v1
- Published: 2026-08-09
- Updated: 2026-08-09
- Authors: Caijun Yan, Yang Zhou, Meixing Shi, Haoran Sun, Yichen Li, Yuxiang Cai, Yankai Jiang
- Tags: agent, context, retrieval
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2608.08612v1

## One-Sentence Summary
Recently, retrieval-augmented and memory-augmented methods have emerged as two promising paradigms for long-video question answering.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recently, retrieval-augmented and memory-augmented methods have emerged as two promising paradigms for long-video question answering.

进一步看，论文的核心做法或实验重点可以概括为：However, existing methods typically rely on rigid, fixed-length temporal chunking (e.g., 10s) and static offline memory banks, which not only fragment coherent continuous events but also fail to adapt during real-time...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Recently, retrieval-augmented and memory-augmented methods have emerged as two promising paradigms for long-video question answering. However, existing methods typically rely on rigid, fixed-length temporal chunking (e.g., 10s) and static offline memory banks, which not only fragment coherent continuous events but also fail to adapt during real-time reasoning. Moreover, whether using multi-scale summaries or multimodal knowledge graphs, current approaches prioritize retrieval relevance while overlooking evidence sufficiency, often stopping to answer once only semantically relevant clues are retrieved, even when key temporal, causal, or fine-grained action evidence is still missing. To tackle these challenges, we propose REVEAL, a rubric-guided agent framework. As a foundation, we introduce an adaptive visual-similarity-based preprocessing pipeline that groups visually coherent adjacent frames into natural event units to construct an offline-online video memory---capturing global video context offline while dynamically maintaining question-conditioned memory online. Built upon this structured memory, REVEAL uses an automatically constructed rubric library to explicitly verify whether retrieved evidence satisfies sufficiency criteria, pinpoints missing clues upon verification failure, and directs targeted re-retrieval for complementary information. Without any extra training, REVEAL consistently outperforms both closed-source and open-source state-of-the-art methods across extensive experiments. These results show that explicitly verifying evidence sufficiency, rather than stopping at semantic relevance, retrieves the decisive clues that prior methods miss and yields more reliable long-video reasoning.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
