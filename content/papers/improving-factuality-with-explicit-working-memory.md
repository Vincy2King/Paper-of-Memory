# Improving Factuality with Explicit Working Memory

- Source: OpenReview
- Venue: ACL 2025
- Paper ID: openreview:V1RoKB0Sir
- Published: 2025-06-01
- Updated: 2026-04-15
- Authors: Mingda Chen, Yang Li, Karthik Padthe, Rulin Shao, Alicia Yi Sun, Luke Zettlemoyer, Gargi Ghosh, Wen-tau Yih
- Tags: retrieval
- Categories: OpenReview.net/Archive/-/Direct_Upload
- URL: https://openreview.net/forum?id=V1RoKB0Sir

## One-Sentence Summary
Large language models can generate factually inaccurate content, a problem known as hallucination.

## Introduction
这篇论文被纳入仓库，是因为它和 `retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL 2025` 这个 venue 相关。

从摘要来看，作者主要关注的是：Large language models can generate factually inaccurate content, a problem known as hallucination.

进一步看，论文的核心做法或实验重点可以概括为：Recent works have built upon retrieved-augmented generation to improve factuality through iterative prompting but these methods are limited by the traditional RAG design.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL 2025
- 高亮主题命中：retrieval
- 检索关键词命中：working memory
- 来源分类信息：OpenReview.net/Archive/-/Direct_Upload

## Abstract Snapshot
Large language models can generate factually inaccurate content, a problem known as hallucination. Recent works have built upon retrieved-augmented generation to improve factuality through iterative prompting but these methods are limited by the traditional RAG design. To address these challenges, we introduce EWE (Explicit Working Memory), a novel approach that enhances factuality in long-form text generation by integrating a working memory that receives real-time feedback from external resources. The memory is refreshed based on online fact-checking and retrieval feedback, allowing EWE to rectify false claims during the generation process and ensure more accurate and reliable outputs. Our experiments demonstrate that Ewe outperforms strong baselines on four fact-seeking long-form generation datasets, increasing the factuality metric, VeriScore, by 2 to 6 points absolute without sacrificing the helpfulness of the responses. Further analysis reveals that the design of rules for memory updates, configurations of memory units, and the quality of the retrieval datastore are crucial factors for influencing model performance.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
