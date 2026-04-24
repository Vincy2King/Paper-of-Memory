# EngramaBench: Evaluating Long-Term Conversational Memory with Structured Graph Retrieval

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.21229v1
- Published: 2026-04-23
- Updated: 2026-04-23
- Authors: Julian Acuna
- Tags: benchmark, context, conversation, long-term, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2604.21229v1

## One-Sentence Summary
Large language model assistants are increasingly expected to retain and reason over information accumulated across many sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model assistants are increasingly expected to retain and reason over information accumulated across many sessions.

进一步看，论文的核心做法或实验重点可以概括为：We introduce EngramaBench, a benchmark for long-term conversational memory built around five personas, one hundred multi-session conversations, and one hundred fifty queries spanning factual recall, cross-space...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：conversational memory, retrieval memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Large language model assistants are increasingly expected to retain and reason over information accumulated across many sessions. We introduce EngramaBench, a benchmark for long-term conversational memory built around five personas, one hundred multi-session conversations, and one hundred fifty queries spanning factual recall, cross-space integration, temporal reasoning, adversarial abstention, and emergent synthesis. We evaluate Engrama, a graph-structured memory system, against GPT-4o full-context prompting and Mem0, an open-source vector-retrieval memory system. All three use the same answering model (GPT-4o), isolating the effect of memory architecture. GPT-4o full-context achieves the highest composite score (0.6186), while Engrama scores 0.5367 globally but is the only system to score higher than full-context prompting on cross-space reasoning (0.6532 vs. 0.6291, n=30). Mem0 is cheapest but substantially weaker (0.4809). Ablations reveal that the components driving Engrama's cross-space advantage trade off against global composite score, exposing a systems-level tension between structured memory specialization and aggregate optimization.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
