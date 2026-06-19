# PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.20047v1
- Published: 2026-06-18
- Updated: 2026-06-18
- Authors: Manu Ghulyani, Arunabh Singh, Karan Bharadwaj, Ankit Nath, Suranjan Goswami
- Tags: agent, compression, context, conversation, retrieval
- Categories: cs.IR
- URL: http://arxiv.org/abs/2606.20047v1

## One-Sentence Summary
Conversational and tool-using LLM agents operate over a context window that fills from several directions simultaneously.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Conversational and tool-using LLM agents operate over a context window that fills from several directions simultaneously.

进一步看，论文的核心做法或实验重点可以概括为：As a session proceeds, the agent accumulates user and assistant turns, entries drawn from a persistent memory store, and often largest of all, the verbatim outputs of tool calls such as file reads, search results, and...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression, context, conversation, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.IR

## Abstract Snapshot
Conversational and tool-using LLM agents operate over a context window that fills from several directions simultaneously. As a session proceeds, the agent accumulates user and assistant turns, entries drawn from a persistent memory store, and often largest of all, the verbatim outputs of tool calls such as file reads, search results, and API responses. Once the cumulative context exceeds the model's token budget, the framework must decide what to keep. The prevailing mechanism is recency truncation, sometimes paired with periodic summarization. This is topic-blind: a fact established early in a session is discarded simply because it is old, even when the current user query is about exactly that fact; conversely, verbose but irrelevant recent material is retained. Agents that must recall information across many turns, the defining case for memory, are precisely where recency truncation fails. Existing alternatives sit outside the agent's assembly step. Retrieval augmented generation fetches external documents into the prompt but does not arbitrate the agent's \emph{already-present} pooled context. Context-compression methods reduce token count by rewriting or pruning text, but operate query-blind and lossily. Neither treats memory entries, conversation turns, and tool outputs as a single candidate pool to be selected from by relevance at the moment the prompt is assembled.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
