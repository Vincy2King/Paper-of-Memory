# PIA: A Personal Intelligence Agent Turning Health Conversations into Records and Records into Understanding

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.31255v1
- Published: 2026-09-25
- Updated: 2026-09-25
- Authors: Jeonghun Yoon, Dongchan Kim, Hongyeon Yu, Young-Bum Kim, Jaegul Choo
- Tags: agent, context, conversation, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2609.31255v1

## One-Sentence Summary
General-purpose agent memory summarizes conversations: it extracts salient snippets, embeds them, and retrieves the top-k into the prompt.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：General-purpose agent memory summarizes conversations: it extracts salient snippets, embeds them, and retrieves the top-k into the prompt.

进一步看，论文的核心做法或实验重点可以概括为：A health agent cannot run on summaries: a dose becomes a sentence, "since last week" is resolved at the model's discretion, and a three-month glucose trend cannot be answered by text similarity.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, retrieval
- 检索关键词命中：agent memory, memory retrieval
- 来源分类信息：cs.CL

## Abstract Snapshot
General-purpose agent memory summarizes conversations: it extracts salient snippets, embeds them, and retrieves the top-k into the prompt. A health agent cannot run on summaries: a dose becomes a sentence, "since last week" is resolved at the model's discretion, and a three-month glucose trend cannot be answered by text similarity. We present PIA, a personal intelligence agent deployed alongside a consumer health agent. PIA receives the agent's natural-language requests, decides for itself whether and how to write or read, and turns conversations into typed clinical records and records into a synthesized understanding of the user. Its memory harness consists of four controls -- extraction, memory, retrieval, and understanding -- each a domain-agnostic mechanism with a pluggable health module: schema, medical alias dictionary, knowledge graph, and temporal rules. We show how the same query receives a different answer as the memory injected into the response context deepens from one-dimensional recall, to a two-dimensional health snapshot, to a three-dimensional trajectory with causality, and report lessons from operation: self-reported health data are missing not at random, question phrasing governs the quality of synthesized understanding, and nearly a third of candidate causal links are structural noise that rules alone remove.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
