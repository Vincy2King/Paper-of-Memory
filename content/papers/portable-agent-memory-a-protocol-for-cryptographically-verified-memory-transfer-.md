# Portable Agent Memory: A Protocol for Cryptographically-Verified Memory Transfer Across Heterogeneous AI Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.11032v1
- Published: 2026-05-10
- Updated: 2026-05-10
- Authors: Santhosh Kumar Ravindran
- Tags: agent, context, episodic
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2605.11032v1

## One-Sentence Summary
We present Portable Agent Memory, an open protocol and reference implementation for transferring persistent memory state across heterogeneous AI agents.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We present Portable Agent Memory, an open protocol and reference implementation for transferring persistent memory state across heterogeneous AI agents.

进一步看，论文的核心做法或实验重点可以概括为：Modern AI agents accumulate rich context -- episodic events,semantic knowledge, procedural skills, working state, and identity preferences -- but this context remains locked within vendor-specific runtimes.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, episodic
- 检索关键词命中：agent memory, persistent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
We present Portable Agent Memory, an open protocol and reference implementation for transferring persistent memory state across heterogeneous AI agents. Modern AI agents accumulate rich context -- episodic events,semantic knowledge, procedural skills, working state, and identity preferences -- but this context remains locked within vendor-specific runtimes. Portable Agent Memory addresses this through: (1) a five-component structured memory model with content-addressable entries linked by a Merkle-DAG provenance graph providing tamper-evidence; (2) capability-based access control enabling selective, scoped disclosure of memory segments; (3) an injection-resistant rehydration protocol that adapts recalled content to heterogeneous target models while mitigating indirect prompt injection; and (4) a JSON-first serialization format with optional CBOR compaction for efficient transport. We provide a Python SDK with 54 passing tests, agent skills for multiple platforms, and demonstrate cross-model memory transfer between GPT-4, Claude, Gemini, and Llama architectures. The protocol is open-source under Apache 2.0.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
