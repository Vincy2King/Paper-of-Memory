# APDMem: Agent-Controlled Progressive Disclosure for Query-Adaptive Long-Term Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.02472v1
- Published: 2026-10-01
- Updated: 2026-10-01
- Authors: Chin-Lun Fu, Anagha Kulkarni, Hong Ni, Behrouz Madahian
- Tags: agent, context, conversation, long-term, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2610.02472v1

## One-Sentence Summary
Personalized LLM assistants must recover sparse evidence from long conversation histories across queries of varying complexity.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Personalized LLM assistants must recover sparse evidence from long conversation histories across queries of varying complexity.

进一步看，论文的核心做法或实验重点可以概括为：We introduce APDMem (Agent-controlled Progressive Disclosure Memory), a hierarchical long-term memory architecture that applies progressive disclosure to memory retrieval.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, long-term, retrieval
- 检索关键词命中：context memory, memory reasoning, memory retrieval
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Personalized LLM assistants must recover sparse evidence from long conversation histories across queries of varying complexity. We introduce APDMem (Agent-controlled Progressive Disclosure Memory), a hierarchical long-term memory architecture that applies progressive disclosure to memory retrieval. Rather than relying on a flat memory store or fixed retrieval granularity, APDMem represents conversation history as four progressively detailed layers: thematic summaries, personalized key facts, turn-level evidence notes, and raw messages. At inference time, a controller applies progressive disclosure to the memory hierarchy: it first reads high-level summaries and drills into finer evidence only when needed. This creates an adaptive cost-fidelity trade-off: simple queries can terminate early, while complex temporal, multi-hop, or exact-evidence queries trigger deeper inspection. A note synthesizer converts retrieved evidence into a query-focused structure that consolidates facts, orders events, and flags contradictions before final answer generation. Experiments on LongMemEval show that APDMem achieves strong performance for long-context memory reasoning while accessing only 8% of the total conversations.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
