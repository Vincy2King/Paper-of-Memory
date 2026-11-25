# SAG-Mem-1.0 Technical Report

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.33124v1
- Published: 2026-11-24
- Updated: 2026-11-24
- Authors: Yuchao Wu, XingCheng Liang, Xuanze Wang, Yini Huang, Yue Wu
- Tags: benchmark, context, conversation, long-term, retrieval
- Categories: cs.CL, cs.IR
- URL: http://arxiv.org/abs/2611.33124v1

## One-Sentence Summary
Long-term conversational memory requires retrieving complementary facts scattered across dialogue sessions, including intermediate evidence with limited similarity to the...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term conversational memory requires retrieving complementary facts scattered across dialogue sessions, including intermediate evidence with limited similarity to the original question.

进一步看，论文的核心做法或实验重点可以概括为：Existing approaches often rely on derived memory representations or persistent relational structures, introducing construction costs and potentially losing source details.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：conversational memory
- 来源分类信息：cs.CL, cs.IR

## Abstract Snapshot
Long-term conversational memory requires retrieving complementary facts scattered across dialogue sessions, including intermediate evidence with limited similarity to the original question. Existing approaches often rely on derived memory representations or persistent relational structures, introducing construction costs and potentially losing source details. We present SAG-Mem, a conversational memory framework that preserves complete dialogue messages in non-overlapping chunks and discovers complementary evidence through query-time lexical expansion. Memory construction requires no model inference, using a lexical index without LLM-based extraction, summarization, or semantic relation construction. At query time, BM25 retrieves initial candidates, an evidence evaluator identifies useful chunks, and lexical cues from selected evidence guide an additional retrieval round. Retrieved dialogue is further annotated with calendar interpretations of supported relative-time expressions, preserving the original wording and temporal granularity. We also introduce SAG-Mem-Lite, an alternative configuration that replaces evidence scoring with embedding-based candidate scoring, achieving lower operational cost than Full Context and all memory-based baselines across both benchmarks with low query latency. On LoCoMo and LongMemEval, SAG-Mem achieves overall scores of 83.08 and 80.20, respectively, the highest among the evaluated methods on both benchmarks. On LongMemEval, it exceeds the strongest compared baseline by 7.20 points. SAG-Mem-Lite achieves scores of 77.09 and 77.20, respectively. These results support dialogue preservation and evidence-guided retrieval expansion as an effective design for long-term conversational memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
