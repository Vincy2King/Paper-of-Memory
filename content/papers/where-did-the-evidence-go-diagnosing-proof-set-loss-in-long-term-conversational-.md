# Where Did the Evidence Go? Diagnosing Proof-Set Loss in Long-Term Conversational Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.10170v1
- Published: 2026-11-06
- Updated: 2026-11-06
- Authors: Bogdan Roshchupkin, Maria Khodorchenko
- Tags: benchmark, context, conversation, long-term, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2611.10170v1

## One-Sentence Summary
Long-term conversational question answering can require several separated dialogue turns that support an answer only together.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term conversational question answering can require several separated dialogue turns that support an answer only together.

进一步看，论文的核心做法或实验重点可以概括为：We introduce EviCover, a retrieval approach designed to retain this complementary evidence.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：conversational memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Long-term conversational question answering can require several separated dialogue turns that support an answer only together. We introduce EviCover, a retrieval approach designed to retain this complementary evidence. It converts questions into observable evidence requirements, checks requirement coverage using retrieved source identifiers, and selects turns jointly. We track annotated support sets - the benchmark-labeled dialogue turns associated with each question - through retrieval, reranking, and final answer-generation context. We evaluate the baseline memory pipeline on generated, human-verified LoCoMo conversations and human-written REALTALK conversations, and examine EviCover on REALTALK's 108 multi-hop questions. Compared with the hybrid lexical/dense baseline, support-turn recall among 60 candidate turns rises from 0.526 to 0.575, and recall in the final ten-turn context rises from 0.349 to 0.379. The evidence funnel identifies separate discovery and selection failures, while paired answer evaluation shows that greater evidence recall does not yet establish a correctness gain. This analysis locates where complementary evidence is lost and distinguishes evidence retrieval from its use in answer generation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
