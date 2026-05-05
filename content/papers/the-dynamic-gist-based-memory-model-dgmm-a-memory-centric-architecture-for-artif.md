# The Dynamic Gist-Based Memory Model (DGMM): A Memory-Centric Architecture for Artificial Intelligence

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.02106v1
- Published: 2026-05-04
- Updated: 2026-05-04
- Authors: Terry Dorsey, Kevin Huggins
- Tags: context, episodic, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.02106v1

## One-Sentence Summary
Contemporary artificial intelligence systems achieve strong performance through large-scale parameterization, retrieval augmentation, and training on extensive static corpora.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Contemporary artificial intelligence systems achieve strong performance through large-scale parameterization, retrieval augmentation, and training on extensive static corpora.

进一步看，论文的核心做法或实验重点可以概括为：Despite these advances, they continue to face limitations in persistent memory, temporal grounding, provenance, and interpretability.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, episodic, retrieval
- 检索关键词命中：persistent memory, working memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Contemporary artificial intelligence systems achieve strong performance through large-scale parameterization, retrieval augmentation, and training on extensive static corpora. Despite these advances, they continue to face limitations in persistent memory, temporal grounding, provenance, and interpretability. These challenges are especially pronounced in large language models, where experience is encoded implicitly in fixed parameters, limiting the ability to preserve, inspect, and reinterpret past interactions over time. This paper establishes a memory-centric architectural foundation for artificial intelligence in which experience is represented explicitly and persistently to support temporal grounding, provenance, and interpretability. It proposes an alternative to parameter-centric approaches by treating memory as a first-class, structured substrate for reasoning. We introduce the Dynamic Gist-Based Memory Model (DGMM), an architecture in which experience is represented as an evolving, graph-structured episodic-semantic memory. DGMM encodes experience as interconnected conceptual structures grounded in time, source, and interaction context, and defines selective, cue-conditioned recall as the mechanism for constructing working memory. A formal schema and architectural invariants are provided based on additive memory growth and recall-conditioned interpretation. The results specify properties of DGMM, including episodic persistence, locality of cue-conditioned surprise, and contextual variability without structural modification of stored memory. DGMM provides a coherent architectural theory in which memory is explicit and persistent, supporting evolving interpretation without retraining and enabling interpretable, context-aware, and temporally grounded AI systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
