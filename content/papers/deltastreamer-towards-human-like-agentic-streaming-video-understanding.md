# DeltaStreamer: Towards Human-Like Agentic Streaming Video Understanding

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.19849v1
- Published: 2026-10-14
- Updated: 2026-10-14
- Authors: Boyuan Sun, Deshui Miao, Wenzhao Gao, Shaoyong Jia, Shaohui Jiao, Chi Liu, Yan Shu, Derek Li, Bryan Dai, Shengsheng Qian, Qibin Hou
- Tags: agent, retrieval
- Categories: cs.CV, cs.AI, cs.HC
- URL: http://arxiv.org/abs/2610.19849v1

## One-Sentence Summary
We propose DeltaStreamer, a novel agentic framework for streaming video understanding inspired by how humans observe, remember, and investigate.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We propose DeltaStreamer, a novel agentic framework for streaming video understanding inspired by how humans observe, remember, and investigate.

进一步看，论文的核心做法或实验重点可以概括为：Streaming video understanding requires a system to retain evidence before knowing which details future queries will need.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.CV, cs.AI, cs.HC

## Abstract Snapshot
We propose DeltaStreamer, a novel agentic framework for streaming video understanding inspired by how humans observe, remember, and investigate. Streaming video understanding requires a system to retain evidence before knowing which details future queries will need. Existing approaches often obscure event transitions and omit relevant details when compressing video history, and cannot recover missing visual evidence. DeltaStreamer addresses these limitations by combining change-aware memory with query-driven planning and targeted evidence gathering with replay. Before a query arrives, it continuously observes the stream and explicitly records visual changes in structured memory, preserving how events unfold rather than only what is present. When a query arrives, a query-driven planner identifies the required evidence and guides memory retrieval and targeted replay. By revisiting historical frames, the agent can recover visual details omitted during observation and ground its answer in evidence beyond the retained descriptions. This connects continuous observation with active investigation tailored to each question. Experiments on OVO-Bench and StreamingBench demonstrate improvements over representative streaming video understanding methods, with overall scores of 66.07% and 59.53%, respectively. Project page: https://bbbbchan.github.io/DeltaStreamer/

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
