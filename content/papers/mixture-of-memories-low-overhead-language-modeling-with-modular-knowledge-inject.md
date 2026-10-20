# Mixture-of-Memories: Low-Overhead Language Modeling with Modular Knowledge Injection

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.25425v1
- Published: 2026-10-18
- Updated: 2026-10-18
- Authors: Yifan Lu, Rubin Wei, Ziyun Zou, Junhong Liang, Haolin Yang, Xinlin Zhuang, Abhijit Das, Adinath Madhavrao Dukre, Shadab Khan, Zhouhan Lin, Imran Razzak
- Tags: retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.25425v1

## One-Sentence Summary
Large language models store substantial factual knowledge in their parameters, yet this knowledge is difficult to control, update, and reliably elicit at inference time.

## Introduction
这篇论文被纳入仓库，是因为它和 `retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models store substantial factual knowledge in their parameters, yet this knowledge is difficult to control, update, and reliably elicit at inference time.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory-augmented approaches typically rely on a single auxiliary mechanism, such as retrieval, parameter updates, or neural memory, and therefore apply the same form of correction to tokens with very...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CL

## Abstract Snapshot
Large language models store substantial factual knowledge in their parameters, yet this knowledge is difficult to control, update, and reliably elicit at inference time. Existing memory-augmented approaches typically rely on a single auxiliary mechanism, such as retrieval, parameter updates, or neural memory, and therefore apply the same form of correction to tokens with very different knowledge demands. We propose Mixture-of-Memories (MoM), a memory-augmented language modeling framework that separates routed neural memory from writable factual memory. MoM combines a frozen base LM with two neural memory experts: a latent memory that provides low-latency hidden-state corrections and a lexical memory that provides a token-space knowledge pathway. A lightweight Budget Router sets per-token mixture weights from uncertainty and disagreement features, replacing the fixed interpolation of prior memory modules. For post-hoc updates, an external explicit memory stays outside the router, because a router trained before facts are written learns to down-weight it; new facts are appended without retraining any component and used only when an answer-level gate accepts the retrieved fact. Experiments across language modeling, factual QA, update analysis, and efficiency show that MoM improves both predictive accuracy and updateability while retaining low inference overhead.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
