# When Evidence Changes: Evaluating Memory Repair and Re-reading in Language-Model Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.03902v1
- Published: 2026-10-02
- Updated: 2026-10-02
- Authors: Wenhui Chu
- Tags: agent, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.03902v1

## One-Sentence Summary
When documents supporting an agent's derived facts are revoked or replaced, should it repair memory or re-read current evidence?

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：When documents supporting an agent's derived facts are revoked or replaced, should it repair memory or re-read current evidence?

进一步看，论文的核心做法或实验重点可以概括为：We introduce an evidence-revision evaluation on medication- and problem-list tasks from public ICU records.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
When documents supporting an agent's derived facts are revoked or replaced, should it repair memory or re-read current evidence? We introduce an evidence-revision evaluation on medication- and problem-list tasks from public ICU records. Under revocation, replacement and control events, we compare full and source-filtered re-reading with caching, rebuilding and graph-local repair across two 7B models. Memory is supplied in full without retrieval, and costs include ingest, revision and every use. On short records, local repair uses 5-10$\times$ fewer revision tokens than rebuilding, yet every memory pipeline costs at least twice full re-reading in held-out conditions. In a small pre-specified development sweep, adding task-ineligible documents extended records to about 10,000 tokens; at that length, memory's mean cumulative cost fell below full re-reading's after 2-14 uses, partly through truncated extraction, while source-filtered re-reading remained cheapest. In the replacement study, none of the four primary confirmatory tests reached statistical significance. These results show why the cost of agent memory after evidence revision must be assessed against source-filtered re-reading over the full pipeline.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
