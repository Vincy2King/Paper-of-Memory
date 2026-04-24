# Automatic Ontology Construction Using LLMs as an External Layer of Memory, Verification, and Planning for Hybrid Intelligent Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.20795v1
- Published: 2026-04-22
- Updated: 2026-04-22
- Authors: Pavel Salovskii, Iuliia Gorshkova
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2604.20795v1

## One-Sentence Summary
This paper presents a hybrid architecture for intelligent systems in which large language models (LLMs) are extended with an external ontological memory layer.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：This paper presents a hybrid architecture for intelligent systems in which large language models (LLMs) are extended with an external ontological memory layer.

进一步看，论文的核心做法或实验重点可以概括为：Instead of relying solely on parametric knowledge and vector-based retrieval (RAG), the proposed approach constructs and maintains a structured knowledge graph using RDF/OWL representations, enabling persistent,...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
This paper presents a hybrid architecture for intelligent systems in which large language models (LLMs) are extended with an external ontological memory layer. Instead of relying solely on parametric knowledge and vector-based retrieval (RAG), the proposed approach constructs and maintains a structured knowledge graph using RDF/OWL representations, enabling persistent, verifiable, and semantically grounded reasoning. The core contribution is an automated pipeline for ontology construction from heterogeneous data sources, including documents, APIs, and dialogue logs. The system performs entity recognition, relation extraction, normalization, and triple generation, followed by validation using SHACL and OWL constraints, and continuous graph updates. During inference, LLMs operate over a combined context that integrates vector-based retrieval with graph-based reasoning and external tool interaction. Experimental observations on planning tasks, including the Tower of Hanoi benchmark, indicate that ontology augmentation improves performance in multi-step reasoning scenarios compared to baseline LLM systems. In addition, the ontology layer enables formal validation of generated outputs, transforming the system into a generation-verification-correction pipeline. The proposed architecture addresses key limitations of current LLM-based systems, including lack of long-term memory, weak structural understanding, and limited reasoning capabilities. It provides a foundation for building agent-based systems, robotics applications, and enterprise AI solutions that require persistent knowledge, explainability, and reliable decision-making.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
