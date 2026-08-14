# When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.12888v1
- Published: 2026-08-13
- Updated: 2026-08-13
- Authors: Ruizhe Li, Licheng Zhang, Benfeng Xu, Mingxuan Du, Zheren Fu, Weidong Chen
- Tags: agent, context, conversation, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.12888v1

## One-Sentence Summary
Agent-memory systems increasingly buy retrieval quality with structure, transforming raw conversation histories into summaries, embeddings, trees, or knowledge graphs before any...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agent-memory systems increasingly buy retrieval quality with structure, transforming raw conversation histories into summaries, embeddings, trees, or knowledge graphs before any question is asked.

进一步看，论文的核心做法或实验重点可以概括为：We ask how much of that benefit comes from the structure itself, rather than from competent retrieval over the raw history.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, retrieval
- 检索关键词命中：agent memory, conversational memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Agent-memory systems increasingly buy retrieval quality with structure, transforming raw conversation histories into summaries, embeddings, trees, or knowledge graphs before any question is asked. We ask how much of that benefit comes from the structure itself, rather than from competent retrieval over the raw history. We present ReFind, an agent-controlled search interface that builds no semantic structure at all: it leaves the conversation archive unmodified, indexes it lexically at turn granularity, and combines a generic iterative keyword-search loop with four chat-native controls grounded in empirical refinding work: session-aware rank fusion, local context expansion, temporal narrowing, and skipping already-inspected sessions. A separate reasoning stage answers from the collected evidence. Across a broad suite of conversational-memory tasks (single- and multi-hop QA, event ordering, and fact consolidation), roughly 2,800 questions on precise-retrieval and fact-tracking capabilities evaluated under the incremental multi-turn setting of MemoryAgentBench, ReFind attains the highest mean accuracy (58.2) of any system compared, above the strongest graph- and tree-based memory systems (HippoRAG 2, 53.2), all under a GPT-4o-mini backbone matched to every reused baseline. Controlled comparisons to single-shot BM25, a matched generic-agentic BM25 control, component removals, and agentic dense/hybrid variants separately support the roles of agent control, chat-native controls, and lexical retrieval. On LongMemEval-S/M, the same interface reaches 93.2 +/- 3.3 and 89.3 +/- 6.0 with GPT-5-mini. The results indicate that for precise, evidence-grounded questions over chat archives, much of the benefit credited to elaborate memory structures is recoverable by giving an agent controllable search over the unmodified record, with no LLM-based index construction at all.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
