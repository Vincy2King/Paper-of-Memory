# State Contamination in Memory-Augmented LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.16746v1
- Published: 2026-05-16
- Updated: 2026-05-16
- Authors: Yian Wang, Agam Goyal, Yuen Chen, Hari Sundaram
- Tags: agent, context
- Categories: cs.AI, cs.LG
- URL: http://arxiv.org/abs/2605.16746v1

## One-Sentence Summary
LLM agents increasingly rely on persistent state, including transcripts, summaries, retrieved context, and memory buffers, to support long-horizon interaction.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM agents increasingly rely on persistent state, including transcripts, summaries, retrieved context, and memory buffers, to support long-horizon interaction.

进一步看，论文的核心做法或实验重点可以概括为：This makes safety depend not only on individual model outputs, but also on what an agent stores and later reuses.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：memory augmented, memory-augmented, persistent memory
- 来源分类信息：cs.AI, cs.LG

## Abstract Snapshot
LLM agents increasingly rely on persistent state, including transcripts, summaries, retrieved context, and memory buffers, to support long-horizon interaction. This makes safety depend not only on individual model outputs, but also on what an agent stores and later reuses. We study a failure mode we call memory laundering: toxic or adversarial context can be compressed into memory summaries that no longer appear toxic under standard detectors, while still preserving hostile framing or conflict structure that influences future generations. Using paired counterfactual multi-agent rollouts, we show that toxic-origin memory summaries can remain below common toxicity thresholds while nevertheless increasing downstream toxicity relative to matched neutral baselines. To measure this hidden influence, we introduce the sub-threshold propagation gap (SPG), which quantifies downstream behavioral differences conditioned on memory states that a deployed monitor would classify as safe. Our experiments show that toxicity propagates through distinct state channels: raw transcript reuse drives overt downstream toxicity, while compressed memory carries hidden sub-threshold influence. We further find that mitigation depends critically on intervention placement. Sanitizing toxic state before summarization substantially reduces the hidden propagation gap, whereas cleaning only the completed summary can leave laundered influence intact. These results suggest that safety in memory-augmented agents should be treated as a state-control problem over evolving context, with sanitization applied before unsafe information is compressed into persistent memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
