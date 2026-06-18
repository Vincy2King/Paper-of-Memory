# RTSGameBench: An RTS Benchmark for Strategic Reasoning by Vision-Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.18950v1
- Published: 2026-06-17
- Updated: 2026-06-17
- Authors: San Kim, Daechul Ahn, Reokyoung Kim, Hyeonbeom Choi, Seungyeon Jwa, Jonghyun Choi
- Tags: agent, benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.18950v1

## One-Sentence Summary
Modern Vision-Language Models (VLMs) often struggle with strategic reasoning, i.e., anticipating and influencing other agents' actions, under uncertainty in competitive and...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Modern Vision-Language Models (VLMs) often struggle with strategic reasoning, i.e., anticipating and influencing other agents' actions, under uncertainty in competitive and cooperative settings.

进一步看，论文的核心做法或实验重点可以概括为：Real-time strategy (RTS) games can be a natural testbed for diagnosing this limitation, as they demand coordination with allies, adaptation to opponents' strategy, and long-horizon planning under partial observability.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Modern Vision-Language Models (VLMs) often struggle with strategic reasoning, i.e., anticipating and influencing other agents' actions, under uncertainty in competitive and cooperative settings. Real-time strategy (RTS) games can be a natural testbed for diagnosing this limitation, as they demand coordination with allies, adaptation to opponents' strategy, and long-horizon planning under partial observability. However, existing RTS benchmarks offer limited evaluation scope, lack systematic competency diagnosis, and remain fixed in the pre-designed scenario coverage. To address these limitations, we present RTSGameBench, which is built on Beyond All Reason, a large-scale RTS game with an expanded battlefield that demands broader strategy diversity than the existing testbeds. The proposed benchmark provides evaluations through diverse gameplay across various matchup structures, diagnostic assessment via mini-games, each targeting an individual strategic competency, and extensible coverage via a self-evolving generation framework that converts free-form queries into new mini-games, improving over successive cycles. Additionally, for VLMs to operate in large-scale RTS games, we provide RTSGameAgent that manages units by an FSM with agentic memory. We empirically validate that multiple state-of-the-art VLMs do not perform well when matchups demand tighter coordination, multiagent coordination and when task scale increases.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
