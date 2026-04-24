# To Know is to Construct: Schema-Constrained Generation for Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.20117v1
- Published: 2026-04-22
- Updated: 2026-04-22
- Authors: Lei Zheng, Weinan Song, Daili Li, Yanming Yang
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2604.20117v1

## One-Sentence Summary
Constructivist epistemology argues that knowledge is actively constructed rather than passively copied.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Constructivist epistemology argues that knowledge is actively constructed rather than passively copied.

进一步看，论文的核心做法或实验重点可以概括为：Despite the generative nature of Large Language Models (LLMs), most existing agent memory systems are still based on dense retrieval.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Constructivist epistemology argues that knowledge is actively constructed rather than passively copied. Despite the generative nature of Large Language Models (LLMs), most existing agent memory systems are still based on dense retrieval. However, dense retrieval heavily relies on semantic overlap or entity matching within sentences. Consequently, embeddings often fail to distinguish instances that are semantically similar but contextually distinct, introducing substantial noise by retrieving context-mismatched entries. Conversely, directly employing open-ended generation for memory access risks "Structural Hallucination" where the model generates memory keys that do not exist in the memory, leading to lookup failures. Inspired by this epistemology, we posit that memory is fundamentally organized by cognitive schemas, and valid recall must be a generative process performed within these schematic structures. To realize this, we propose SCG-MEM, a schema-constrained generative memory architecture. SCG-MEM reformulates memory access as Schema-Constrained Generation. By maintaining a dynamic Cognitive Schema, we strictly constrain LLM decoding to generate only valid memory entry keys, providing a formal guarantee against structural hallucinations. To support long-term adaptation, we model memory updates via assimilation (grounding inputs into existing schemas) and accommodation (expanding schemas with novel concepts). Furthermore, we construct an Associative Graph to enable multi-hop reasoning through activation propagation. Experiments on the LoCoMo benchmark show that SCG-MEM substantially improves performance across all categories over retrieval-based baselines.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
