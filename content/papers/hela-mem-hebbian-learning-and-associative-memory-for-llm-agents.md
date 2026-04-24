# HeLa-Mem: Hebbian Learning and Associative Memory for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.16839v1
- Published: 2026-04-18
- Updated: 2026-04-18
- Authors: Jinchang Zhu, Jindong Li, Cheng Zhang, Jiahong Liu, Menglin Yang
- Tags: agent, context, conversation, episodic, long-term
- Categories: cs.CL
- URL: http://arxiv.org/abs/2604.16839v1

## One-Sentence Summary
Long-term memory is a critical challenge for Large Language Model agents, as fixed context windows cannot preserve coherence across extended interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory is a critical challenge for Large Language Model agents, as fixed context windows cannot preserve coherence across extended interactions.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory systems represent conversation history as unstructured embedding vectors, retrieving information through semantic similarity.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, episodic, long-term
- 检索关键词命中：episodic memory, long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-term memory is a critical challenge for Large Language Model agents, as fixed context windows cannot preserve coherence across extended interactions. Existing memory systems represent conversation history as unstructured embedding vectors, retrieving information through semantic similarity. This paradigm fails to capture the associative structure of human memory, wherein related experiences progressively strengthen interconnections through repeated co-activation. Inspired by cognitive neuroscience, we identify three mechanisms central to biological memory: association, consolidation, and spreading activation, which remain largely absent in current research. To bridge this gap, we propose HeLa-Mem, a bio-inspired memory architecture that models memory as a dynamic graph with Hebbian learning dynamics. HeLa-Mem employs a dual-level organization: (1) an episodic memory graph that evolves through co-activation patterns, and (2) a semantic memory store populated via Hebbian Distillation, wherein a Reflective Agent identifies densely connected memory hubs and distills them into structured, reusable semantic knowledge. This dual-path design leverages both semantic similarity and learned associations, mirroring the episodic-semantic distinction in human cognition. Experiments on LoCoMo demonstrate superior performance across four question categories while using significantly fewer context tokens. Code is available on GitHub: https://github.com/ReinerBRO/HeLa-Mem

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
