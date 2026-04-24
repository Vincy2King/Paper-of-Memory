# Architecture Matters More Than Scale: A Comparative Study of Retrieval and Memory Augmentation for Financial QA Under SME Compute Constraints

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.17979v1
- Published: 2026-04-20
- Updated: 2026-04-20
- Authors: Jianan Liu, Jing Yang, Xianyou Li, Weiran Yan, Yichao Wu, Penghao Liang, Mengwei Yuan
- Tags: benchmark, conversation, long-term, retrieval
- Categories: cs.IR
- URL: http://arxiv.org/abs/2604.17979v1

## One-Sentence Summary
The rapid adoption of artificial intelligence (AI) and large language models (LLMs) is transforming financial analytics by enabling natural language interfaces for reporting,...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, conversation, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：The rapid adoption of artificial intelligence (AI) and large language models (LLMs) is transforming financial analytics by enabling natural language interfaces for reporting, decision support, and automated reasoning.

进一步看，论文的核心做法或实验重点可以概括为：However, limited empirical understanding exists regarding how different LLM-based reasoning architectures perform across realistic financial workflows, particularly under the cost, accuracy, and compliance constraints...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, conversation, long-term, retrieval
- 检索关键词命中：long-term memory, memory augmented, memory-augmented
- 来源分类信息：cs.IR

## Abstract Snapshot
The rapid adoption of artificial intelligence (AI) and large language models (LLMs) is transforming financial analytics by enabling natural language interfaces for reporting, decision support, and automated reasoning. However, limited empirical understanding exists regarding how different LLM-based reasoning architectures perform across realistic financial workflows, particularly under the cost, accuracy, and compliance constraints faced by small and medium-sized enterprises (SMEs). SMEs typically operate within severe infrastructure constraints, lacking cloud GPU budgets, dedicated AI teams, and API-scale inference capacity, making architectural efficiency a first-class concern. To ensure practical relevance, we introduce an explicit SME-constrained evaluation setting in which all experiments are conducted using a locally hosted 8B-parameter instruction-tuned model without cloud-scale infrastructure. This design isolates the impact of architectural choices within a realistic deployment environment. We systematically compare four reasoning architectures: baseline LLM, retrieval-augmented generation (RAG), structured long-term memory, and memory-augmented conversational reasoning across both FinQA and ConvFinQA benchmarks. Results reveal a consistent architectural inversion: structured memory improves precision in deterministic, operand-explicit tasks, while retrieval-based approaches outperform memory-centric methods in conversational, reference-implicit settings. Based on these findings, we propose a hybrid deployment framework that dynamically selects reasoning strategies to balance numerical accuracy, auditability, and infrastructure efficiency, providing a practical pathway for financial AI adoption in resource-constrained environments.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
