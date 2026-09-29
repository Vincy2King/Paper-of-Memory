# Learning What to Recall: Adaptive Multi-Cue Episodic Memory for World Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.34677v1
- Published: 2026-09-28
- Updated: 2026-09-28
- Authors: Beomsu Kim, Chieh-Hsin Lai, Bac Nguyen, Amir Bar, Jong Chul Ye, Yuki Mitsufuji
- Tags: context, episodic, retrieval
- Categories: cs.LG, cs.AI, cs.CV
- URL: http://arxiv.org/abs/2609.34677v1

## One-Sentence Summary
World models predict future observations from current experience and actions, yet prediction can depend on observations seen far in the past.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：World models predict future observations from current experience and actions, yet prediction can depend on observations seen far in the past.

进一步看，论文的核心做法或实验重点可以概括为：Episodic memory preserves past observations for later recall; however, as memory accumulates, it raises a fundamental question: which memories are useful for the current prediction, and which available retrieval cues...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, episodic, retrieval
- 检索关键词命中：episodic memory
- 来源分类信息：cs.LG, cs.AI, cs.CV

## Abstract Snapshot
World models predict future observations from current experience and actions, yet prediction can depend on observations seen far in the past. Episodic memory preserves past observations for later recall; however, as memory accumulates, it raises a fundamental question: which memories are useful for the current prediction, and which available retrieval cues should be trusted to find them? This is challenging because fixed criteria based on recency, pose overlap, or visual similarity can be unreliable across environments and queries. We propose Future-Aware Recall (FAR), a framework that learns episodic recall from future-aware predictive supervision and adaptive multi-cue scoring. During training, FAR measures predictive utility by the conditional log-likelihood of the realized future given recalled context, approximated by negative diffusion prediction loss, and uses it to train a retriever that remains future-blind at inference. The retriever learns cue-specific relevance and automatically determines which available retrieval cues, such as time, pose, vision, and audio, to trust for each query when selecting memories. Across three complementary settings, FAR outperforms hand-designed recall even with the same retrieval cues, automatically adapts which available cues to trust, and recalls the right history as the world changes. Together, these results establish FAR as a flexible, principled approach to episodic memory access in world models.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
