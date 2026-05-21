# CALMem : Application-Layer Dual Memory for Conversational AI

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.20724v1
- Published: 2026-05-20
- Updated: 2026-05-20
- Authors: Rajendra Narayan Jena, Rajan Padmanabhan, Sankar Arumugam
- Tags: agent, context, conversation, episodic, retrieval
- Categories: cs.IR
- URL: http://arxiv.org/abs/2605.20724v1

## One-Sentence Summary
Large language models (LLMs) operate within fixed context windows that fundamentally limit conversational continuity.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models (LLMs) operate within fixed context windows that fundamentally limit conversational continuity.

进一步看，论文的核心做法或实验重点可以概括为：When context fills, compaction discards history irreversibly; when sessions end, all memory resets to zero.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, episodic, retrieval
- 检索关键词命中：episodic memory, memory augmented, memory-augmented
- 来源分类信息：cs.IR

## Abstract Snapshot
Large language models (LLMs) operate within fixed context windows that fundamentally limit conversational continuity. When context fills, compaction discards history irreversibly; when sessions end, all memory resets to zero. Existing solutions-larger context windows, retrieval-augmented generation for knowledge bases, and memory-augmented architectures such as MemGPT-either require model modification, impose provider lock-in, or do not address the compaction continuity problem. We present CALMem (Conversational Application-Layer Memory), an application-layer dual memory architecture that gives LLM-based conversational assistants virtually unbounded effective context without any modification to the underlying model. CALMem combines two complementary memory subsystems: an episodic memory layer built on sliding-window vector embeddings of conversation history, and a semantic memory layer of agent-writable structured facts. A token-budget-adaptive injection mechanism, called the MOIM (Message of Injected Memory), automatically retrieves and injects relevant past context each turn, scaling injection depth inversely with context pressure. A key contribution is intra-session retrieval: compacted away turns from the current session remain searchable, closing a gap unaddressed by prior work. The system is implemented as a pure application layer in a production Rust codebase, is provider-agnostic, and degrades to original LLM behaviour with zero overhead when disabled. We describe the architecture, design decisions, and performance characteristics, and analyse the trade-offs that guided each implementation choice.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
