# When Users Don't Ask: Benchmarking Context-Driven Memory Retrieval in Conversational Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.03467v1
- Published: 2026-09-03
- Updated: 2026-09-03
- Authors: Wen-Yu Chang, Yun-Nung Chen
- Tags: agent, benchmark, context, conversation, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2609.03467v1

## One-Sentence Summary
Large language models (LLMs) are increas- ingly deployed as long-horizon conversational agents, motivating growing interest in mem- ory systems.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models (LLMs) are increas- ingly deployed as long-horizon conversational agents, motivating growing interest in mem- ory systems.

进一步看，论文的核心做法或实验重点可以概括为：However, existing benchmarks primarily evaluate memory through QA-style probing rather than in-situ conversational usage.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, retrieval
- 检索关键词命中：memory benchmark, memory benchmarks, memory retrieval
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Large language models (LLMs) are increas- ingly deployed as long-horizon conversational agents, motivating growing interest in mem- ory systems. However, existing benchmarks primarily evaluate memory through QA-style probing rather than in-situ conversational usage. We introduce LOCOMO-CONV, a conversa- tional memory benchmark derived from Lo- CoMo with four query styles: dialog, implicit, counterfactual, and composed. Across five rep- resentative memory systems, we evaluate both retrieval recall and end-to-end response qual- ity. Our experiments show that conversational framing exposes substantial retrieval gaps over- looked by QA benchmarks, especially on im- plicit and composed queries, which multi-facet query rewriting narrows for raw-turn mem- ory but not abstractive memory. We further find that strong retrieval does not fully trans- late into response quality, and that implicit queries exhibit silent grounding, where mem- ory improves contextual grounding without ex- plicitly surfacing the gold fact. These results point to reasoning-based memory elaboration as a promising direction, and we release aux- iliary supportive_memory annotations captur- ing conversationally useful context beyond the original gold evidence.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
