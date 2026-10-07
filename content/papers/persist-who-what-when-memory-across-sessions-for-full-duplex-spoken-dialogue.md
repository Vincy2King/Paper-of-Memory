# PERSIST: Who-What-When Memory Across Sessions for Full-Duplex Spoken Dialogue

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.07725v1
- Published: 2026-10-06
- Updated: 2026-10-06
- Authors: Achira Lin, Siyuan Hou, Wenyi Yu, Xinnian Zhao, Haoyu Niu, Wang Geng, Longshuai Xiao, Shihai Xiao, Mangsuo Zhao, Chao Zhang
- Tags: benchmark, conversation, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.07725v1

## One-Sentence Summary
Modern voice assistants may be shared by multiple users and should be able to answer questions about earlier conversations such as "When did I originally plan to leave?" or...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Modern voice assistants may be shared by multiple users and should be able to answer questions about earlier conversations such as "When did I originally plan to leave?" or adapt their behavior to individual users...

进一步看，论文的核心做法或实验重点可以概括为：This requires more than retrieving a topically similar passage: the assistant must identify the current speaker, recover the relevant past state, and distinguish it from later revisions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, conversation, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Modern voice assistants may be shared by multiple users and should be able to answer questions about earlier conversations such as "When did I originally plan to leave?" or adapt their behavior to individual users based on past interactions. This requires more than retrieving a topically similar passage: the assistant must identify the current speaker, recover the relevant past state, and distinguish it from later revisions. We present PERSIST, a persistent memory system for multi-session, multi-speaker spoken dialogue that explicitly models Who, What, and When. PERSIST structures cross-session histories into readable event records and retrieves them with a 3W joint scoring mechanism that combines semantic content, acoustic speaker identity, and temporal state. For real-time full-duplex interaction, PERSIST further reuses intermediate representations from the dialogue backbone, avoiding query-audio re-encoding and reducing retrieval latency from 578.42 ms to 7.03 ms. We also introduce SpokenTrace, a diagnostic benchmark that factorizes evaluation along memory tasks and speaker-query types, exposing failures in recall, speaker attribution, and temporal-state tracking. On SpokenTrace, PERSIST achieves 85.08% end-to-end task accuracy and improves all-support EM@3 from 49.01% with BGE-large to 82.10%.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
