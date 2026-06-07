# From Retrieval to Reconstruction: Constructing Evolvable Cognitive Memory for Long-term Dialogue

- Source: OpenReview
- Venue: ACL ARR 2026 March Submission
- Paper ID: openreview:DAfO4dwkEw
- Published: 2026-06-07
- Updated: 2026-06-07
- Authors: Unknown
- Tags: context, long-term, retrieval
- Categories: aclweb.org/ACL/ARR/2026/March/-/Submission
- URL: https://openreview.net/forum?id=DAfO4dwkEw

## One-Sentence Summary
Large Language Models (LLMs) serving as long-term personal companions require memory systems that support complex reasoning over extended dialogues.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, long-term, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 March Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Large Language Models (LLMs) serving as long-term personal companions require memory systems that support complex reasoning over extended dialogues.

进一步看，论文的核心做法或实验重点可以概括为：However, existing Retrieval-Augmented Generation (RAG) frameworks treat memory as passive storage, suffering from semantic collapse—where subjective beliefs and objective facts become indistinguishable—and rigid...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 March Submission
- 高亮主题命中：context, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：aclweb.org/ACL/ARR/2026/March/-/Submission

## Abstract Snapshot
Large Language Models (LLMs) serving as long-term personal companions require memory systems that support complex reasoning over extended dialogues. However, existing Retrieval-Augmented Generation (RAG) frameworks treat memory as passive storage, suffering from semantic collapse—where subjective beliefs and objective facts become indistinguishable—and rigid navigation that fails to connect dispersed information. We introduce CogMem, a cognitive memory architecture that reconstructs dialogue context through explicit structure. CogMem organizes memory via the PEC$^2$F (Person-Event-Concept-Claim-Fact) schema, using dedicated Claim nodes to separate subjective attributions from objective records and prevent information contamination. Rather than static retrieval, CogMem employs a deterministic controller with four cognitive operators (anchoring, traversal, intersection, evidence grounding) that dynamically navigate the graph based on query intent. Comprehensive evaluation on LoCoMo and LongMemEval shows that CogMem achieves state-of-the-art performance across all task categories, surpassing neural memory systems and graph retrieval methods.These results demonstrate that structured cognitive modeling significantly improves long-term memory accuracy and robustness compared to passive vector retrieval.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
