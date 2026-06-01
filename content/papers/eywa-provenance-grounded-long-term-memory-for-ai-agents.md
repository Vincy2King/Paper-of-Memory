# Eywa: Provenance-Grounded Long-Term Memory for AI Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.30771v1
- Published: 2026-05-29
- Updated: 2026-05-29
- Authors: Resham Joshi
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2605.30771v1

## One-Sentence Summary
AI agents that persist across sessions need memory they can retrieve, audit, update, and erase.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：AI agents that persist across sessions need memory they can retrieve, audit, update, and erase.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory systems often collapse source evidence, extracted facts, retrieved context, and answer policy into one opaque prompt path, making failures difficult to diagnose: a wrong answer may come from missing...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
AI agents that persist across sessions need memory they can retrieve, audit, update, and erase. Existing memory systems often collapse source evidence, extracted facts, retrieved context, and answer policy into one opaque prompt path, making failures difficult to diagnose: a wrong answer may come from missing evidence, unsupported extraction, stale state, retrieval loss, or answer-model behavior. We present Eywa, a provenance-grounded memory architecture built around evidence before belief. Eywa stores immutable source evidence before deriving canonical facts, validates extracted memories against typed signals and source support, and retrieves bounded memory context through a deterministic multi-route read path with zero LLM calls inside retrieval. Retrieved context is returned separately from answer instructions, allowing the same memory substrate to be evaluated across frontier, budget, and local answer models. Under a frozen, artifact-recorded retrieval configuration, Eywa reaches 90.19% judge accuracy on the LoCoMo C1-C4 split with Claude Sonnet 4.6 write and QA roles. On LongMemEval-S, it reaches 88.2% retrieval-sufficiency accuracy. On BEAM, a 700-question technical-memory stress benchmark, it reaches 81.45% mean nugget score and 85.29% pass@score >= 0.5. Full per-question artifacts, including questions, gold answers, model answers, retrieved context, and labels, are published at https://eywa.to/research.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
