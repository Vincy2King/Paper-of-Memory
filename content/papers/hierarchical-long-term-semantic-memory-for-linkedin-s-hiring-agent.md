# Hierarchical Long-Term Semantic Memory for LinkedIn's Hiring Agent

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.26197v1
- Published: 2026-04-29
- Updated: 2026-04-29
- Authors: Zhentao Xu, Shangjing Zhang, Emir Poyraz, Yvonne Li, Ye Jin, Xie Lu, Xiaoyang Gu, Karthik Ramgopal, Praveen Kumar Bodigutla, Xiaofeng Wang
- Tags: agent, context, long-term, retrieval
- Categories: cs.IR, cs.LG
- URL: http://arxiv.org/abs/2604.26197v1

## One-Sentence Summary
Large Language Model (LLM) agents are increasingly used in real-world products, where personalized and context-aware user interactions are essential.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large Language Model (LLM) agents are increasingly used in real-world products, where personalized and context-aware user interactions are essential.

进一步看，论文的核心做法或实验重点可以概括为：A central enabler of such capabilities is the agent's long-term semantic memory system, which extracts implicit and explicit signals from noisy longitudinal behavioral data, stores them in a structured form, and...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.IR, cs.LG

## Abstract Snapshot
Large Language Model (LLM) agents are increasingly used in real-world products, where personalized and context-aware user interactions are essential. A central enabler of such capabilities is the agent's long-term semantic memory system, which extracts implicit and explicit signals from noisy longitudinal behavioral data, stores them in a structured form, and supports low-latency retrieval. Building industrial-grade long-term memory for LLM agents raises five challenges: scalability, low-latency retrieval, privacy constraints, cross-domain generalizability, and observability. We introduce the Hierarchical Long-Term Semantic Memory (HLTM) framework, which organizes textual data into a schema-aligned memory tree that captures semantic knowledge at multiple levels of granularity, enabling scalable ingestion, privacy-aware storage, low-latency retrieval, and transparent provenance; HLTM further incorporates an adaptation mechanism to generalize across diverse use cases. Extensive evaluations on LinkedIn's Hiring Assistant show that HLTM improves answer correctness and retrieval F1 significantly by more than 10%, while significantly advancing the Pareto frontier between query and indexing latency. HLTM has been deployed in LinkedIn's Hiring Assistant to power core personalization features in production hiring workflows.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
