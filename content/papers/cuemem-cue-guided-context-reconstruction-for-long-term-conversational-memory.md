# CueMem: Cue-Guided Context Reconstruction for Long-Term Conversational Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.12354v1
- Published: 2026-09-11
- Updated: 2026-09-11
- Authors: Changjian Wang, Rongzhen Li, Weili Guan, Shuming Shi, Quan Lu, Ning Jiang
- Tags: agent, context, conversation, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2609.12354v1

## One-Sentence Summary
Long-term conversational agents must answer user queries by recalling information from extended dialogue histories, yet directly using the full history is costly and often...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term conversational agents must answer user queries by recalling information from extended dialogue histories, yet directly using the full history is costly and often unreliable, while compressed memory units may...

进一步看，论文的核心做法或实验重点可以概括为：Motivated by the reconstructive view of autobiographical memory, we propose CueMem, a cue-guided framework that treats extracted memory records as retrieval cues rather than self-contained evidence and reconstructs...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, long-term, retrieval
- 检索关键词命中：conversational memory, long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-term conversational agents must answer user queries by recalling information from extended dialogue histories, yet directly using the full history is costly and often unreliable, while compressed memory units may lose fine-grained evidence needed for question answering. Motivated by the reconstructive view of autobiographical memory, we propose CueMem, a cue-guided framework that treats extracted memory records as retrieval cues rather than self-contained evidence and reconstructs query-relevant dialogue context from their source turns. During memory construction, CueMem extracts fine-grained memory cues from dialogue turns and links each cue to its source turn. At query time, it retrieves query-relevant cues, maps them to source-turn anchors, and expands from these anchors over a turn graph that captures temporal proximity and semantic relatedness, reconstructing a compact evidence context from the original dialogue for LLM answer generation. Experiments on LoCoMo and LongMemEval show that CueMem consistently outperforms representative long-term memory baselines. Further analyses show that graph-based context reconstruction helps recover supporting dialogue evidence while reducing query-time input tokens and latency compared with the full-history LLM setting. These results highlight retrieval cues as an effective alternative to self-contained memory evidence for long-term conversational question answering.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
