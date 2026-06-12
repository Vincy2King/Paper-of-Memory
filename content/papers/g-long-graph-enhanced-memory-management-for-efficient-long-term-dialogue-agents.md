# G-Long: Graph-Enhanced Memory Management for Efficient Long-Term Dialogue Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.13115v1
- Published: 2026-06-11
- Updated: 2026-06-11
- Authors: Minjun Choi, Yoonjin Jang, Sangwon Youn, Youngjoong Ko
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2606.13115v1

## One-Sentence Summary
While Large Language Models (LLMs) have advanced open-domain dialogue systems, maintaining long-term consistency remains a challenge due to inherent limitations in long-context...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：While Large Language Models (LLMs) have advanced open-domain dialogue systems, maintaining long-term consistency remains a challenge due to inherent limitations in long-context reasoning and the inefficiency of...

进一步看，论文的核心做法或实验重点可以概括为：Existing approaches typically rely on either unstructured memory storage, which is prone to information loss, or computationally expensive LLMs that incur high latency.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
While Large Language Models (LLMs) have advanced open-domain dialogue systems, maintaining long-term consistency remains a challenge due to inherent limitations in long-context reasoning and the inefficiency of processing extensive raw text. Existing approaches typically rely on either unstructured memory storage, which is prone to information loss, or computationally expensive LLMs that incur high latency. To address these limitations, we propose G-Long, a graph-enhanced framework that utilizes a fine-tuned small Language Model (sLM) for structured triplet extraction and associative retrieval, significantly reducing operational costs. Furthermore, we introduce the novel attention-aware importance scoring mechanism that leverages the intrinsic cross-attention signals of a T5 summarizer to identify salient memories. Extensive experiments across diverse benchmarks demonstrate that G-Long achieves state-of-the-art performance in both response generation and memory retrieval, yielding performance gains of up to 9.8% in response quality on MSC and 40.8% in retrieval recall on LME, while significantly minimizing computational overhead.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
