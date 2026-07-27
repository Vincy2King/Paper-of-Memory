# IFCMemoryBench: Evaluating Long-Term Memory of LLM-Based Agents in BIM Information Retrieval

- Source: OpenReview
- Venue: Agentic AI Evaluation and Trustworthiness KDD2026
- Paper ID: openreview:v4j9bz4wRS
- Published: 2026-07-27
- Updated: 2026-07-27
- Authors: Changyu Du, Alexander Vosseler, Filippo Mazza, André Borrmann
- Tags: agent, benchmark, context, conversation, long-term, retrieval
- Categories: KDD.org/2026/Workshop/Agentic_AI_Evaluation_and_Trustworthiness/-/Submission
- URL: https://openreview.net/forum?id=v4j9bz4wRS

## One-Sentence Summary
Long-term memory is becoming a core capability of LLM-based agents, but existing evaluations largely test conversational recall in open-domain or persona-grounded settings.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `Agentic AI Evaluation and Trustworthiness KDD2026` 这个 venue 相关。

从摘要来看，作者主要关注的是：Long-term memory is becoming a core capability of LLM-based agents, but existing evaluations largely test conversational recall in open-domain or persona-grounded settings.

进一步看，论文的核心做法或实验重点可以概括为：We argue that a stronger test is whether an agent can reuse information from prior sessions while acting over a live, structured, domain-specific environment.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：Agentic AI Evaluation and Trustworthiness KDD2026
- 高亮主题命中：agent, benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：KDD.org/2026/Workshop/Agentic_AI_Evaluation_and_Trustworthiness/-/Submission

## Abstract Snapshot
Long-term memory is becoming a core capability of LLM-based agents, but existing evaluations largely test conversational recall in open-domain or persona-grounded settings. We argue that a stronger test is whether an agent can reuse information from prior sessions while acting over a live, structured, domain-specific environment. We study this problem in Building Information Modelling (BIM), a professional engineering workflow where agents must query large IFC models while also relying on project specifications, client decisions, and engineering conventions that are often discussed in conversation but absent from the model. We introduce IFCMemoryBench, a human-validated benchmark for evaluating long-term memory in LLM-based BIM information retrieval. IFCMemoryBench contains 143 multi-session tasks across 19 projects and 4,016 prior sessions, derived from incomplete-information questions in IFC-Bench v2. Each task seeds missing project context across earlier conversations and later asks a probe question that can be answered only by combining remembered context with live IFC queries. Our evaluation framework decomposes memory performance into ingestion, retrieval, and utilization, and measures both answer quality and memory quality with expert-validated LLM judges. We evaluate representative vector-, graph-, and file-based memory systems. The strongest system achieves only 32.4\% answer accuracy under a deployment-realistic ingestion scope, and remains below 60\% under oracle-filtered ingestion or a stronger probe agent. Analysis shows that current general-purpose memory systems often retrieve topically relevant context but store project knowledge as incomplete or fragmented facts. These results reveal a domain-transfer gap in agent memory and suggest that reliable professional agents require domain-aware memory representations linking conversations, project knowledge, and structured model entities.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
