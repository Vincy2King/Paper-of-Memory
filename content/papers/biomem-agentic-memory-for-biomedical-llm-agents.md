# BioMem: Agentic Memory for Biomedical LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.13426v1
- Published: 2026-11-10
- Updated: 2026-11-10
- Authors: Mingchen Li, Yongkang Xiao, Rumeng Li, Rui Zhang, Hong Yu
- Tags: agent, benchmark, context, conversation, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2611.13426v1

## One-Sentence Summary
Large language models (LLMs) have demonstrated considerable potential in biomedical applications, while agentic memory systems have emerged as a promising approach to preserving...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models (LLMs) have demonstrated considerable potential in biomedical applications, while agentic memory systems have emerged as a promising approach to preserving and utilizing information across tasks...

进一步看，论文的核心做法或实验重点可以概括为：However, a fundamental question remains: how effectively and reliably do these systems retain, retrieve, update, and utilize biomedical information?

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：agent memory, conversational memory, memory augmented, memory benchmark, memory benchmarks, memory retrieval
- 来源分类信息：cs.CL

## Abstract Snapshot
Large language models (LLMs) have demonstrated considerable potential in biomedical applications, while agentic memory systems have emerged as a promising approach to preserving and utilizing information across tasks and interactions. However, a fundamental question remains: how effectively and reliably do these systems retain, retrieve, update, and utilize biomedical information? In this study, we systematically investigate agentic memory in the biomedical domain, focusing on task effectiveness, retrieval quality, information fidelity, and long-term robustness. We evaluate five memory approaches across four LLMs in three representative settings: biomedical knowledge reasoning, clinical prediction, and long-term conversational memory. Our analyses reveal how memory construction, evidence relevance, and conversational history shape downstream biomedical performance, highlighting the distinct challenges of retrieving relevant information, preserving its fidelity, and effectively utilizing it for reasoning. Building on these findings, we introduce Hybrid Memory Retrieval and Utilization (HMRU), a training-free framework that jointly enhances evidence accessibility and task-aware utilization to improve biomedical reasoning and long-term conversational memory. HMRU achieves an average relative improvement of 8.6% across biomedical question-answering and conversational memory benchmarks, with additional gains in selected clinical prediction tasks. It further reduces conversational answer errors by 24.9% and closes 48.0% of the performance gap to full-context inference. Our findings provide a systematic characterization of biomedical agentic memory and practical insights into developing more effective and reliable memory-augmented LLM systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
