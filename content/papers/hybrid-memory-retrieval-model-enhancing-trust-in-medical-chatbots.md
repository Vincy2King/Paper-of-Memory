# Hybrid Memory-Retrieval Model: Enhancing Trust in Medical Chatbots

- Source: OpenReview
- Venue: ACL ARR 2025 May Submission
- Paper ID: openreview:paddqFWkLB
- Published: 2025-07-29
- Updated: 2026-07-02
- Authors: Unknown
- Tags: context, conversation, long-term, retrieval
- Categories: aclweb.org/ACL/ARR/2025/May/-/Submission
- URL: https://openreview.net/forum?id=paddqFWkLB

## One-Sentence Summary
Medical chatbots powered by large language models (LLMs) face two critical challenges: hallucination, where the model produces plausible but incorrect responses, and loss of...

## Introduction
这篇论文被纳入仓库，是因为它和 `context, conversation, long-term, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2025 May Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Medical chatbots powered by large language models (LLMs) face two critical challenges: hallucination, where the model produces plausible but incorrect responses, and loss of context in multi-turn conversations.

进一步看，论文的核心做法或实验重点可以概括为：These issues undermine reliability and trust in healthcare settings.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2025 May Submission
- 高亮主题命中：context, conversation, long-term, retrieval
- 检索关键词命中：long-term memory, memory retrieval
- 来源分类信息：aclweb.org/ACL/ARR/2025/May/-/Submission

## Abstract Snapshot
Medical chatbots powered by large language models (LLMs) face two critical challenges: hallucination, where the model produces plausible but incorrect responses, and loss of context in multi-turn conversations. These issues undermine reliability and trust in healthcare settings. This paper introduces a hybrid memory-retrieval architecture designed to enhance factual grounding and conversational coherence. The system integrates a dual-retriever pipeline (BM25 and MedCPT) with long-term memory retrieval using ChromaDB. Retrieved documents and past interactions are fused via Reciprocal Rank Fusion and provided as input to a compact language model (Phi-2) for response generation. A fallback mechanism is employed when insufficient context is available to reduce hallucinated responses. Evaluation on the MedQuAD dataset demonstrates high semantic alignment (BERTScore F1 = 0.8644), improved fluency, and significantly faster response times compared to baseline retrieval-augmented models. These results support the effectiveness of combining structured memory with selective retrieval to develop more trustworthy medical dialogue systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
