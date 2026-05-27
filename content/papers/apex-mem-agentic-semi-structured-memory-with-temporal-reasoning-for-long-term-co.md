# APEX-MEM: Agentic Semi-Structured Memory with Temporal Reasoning for Long-Term Conversational AI

- Source: OpenReview
- Venue: ACL 2026
- Paper ID: openreview:Rub55frimD
- Published: 2026-05-01
- Updated: 2026-05-26
- Authors: Pratyay Banerjee, Masud Moshtaghi, Amita Misra, Shivashankar Subramanian, Ankit Chadha
- Tags: agent, context, conversation, long-term, retrieval
- Categories: OpenReview.net/Archive/-/Direct_Upload
- URL: https://openreview.net/forum?id=Rub55frimD

## One-Sentence Summary
Large language models still struggle with reliable long-term conversational memory: simply enlarging context windows or applying naive retrieval often introduces noise and...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, long-term` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL 2026` 这个 venue 相关。

从摘要来看，作者主要关注的是：Large language models still struggle with reliable long-term conversational memory: simply enlarging context windows or applying naive retrieval often introduces noise and destabilizes responses.

进一步看，论文的核心做法或实验重点可以概括为：We present APEX-MEM, a conversational memory system that combines three key innovations: (1) a property graph which uses domain-agnostic ontology to structure conversations as temporally grounded events in an entity-...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL 2026
- 高亮主题命中：agent, context, conversation, long-term, retrieval
- 检索关键词命中：conversational memory
- 来源分类信息：OpenReview.net/Archive/-/Direct_Upload

## Abstract Snapshot
Large language models still struggle with reliable long-term conversational memory: simply enlarging context windows or applying naive retrieval often introduces noise and destabilizes responses. We present APEX-MEM, a conversational memory system that combines three key innovations: (1) a property graph which uses domain-agnostic ontology to structure conversations as temporally grounded events in an entity-centric framework, (2) append-only storage that preserves the full temporal evolution of information, and (3) a multi-tool retrieval agent that understands and resolves conflicting or evolving information at query time, producing a compact and contextually relevant memory summary. This retrieval-time resolution preserves the full interaction history while suppressing irrelevant details. APEX-MEM achieves 88.88% accuracy on LOCOMO's Question Answering task and 86.2% on LongMemEval, outperforming state-of-the-art session-aware approaches and demonstrating that structured property graphs enable more temporally coherent long-term conversational reasoning.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
