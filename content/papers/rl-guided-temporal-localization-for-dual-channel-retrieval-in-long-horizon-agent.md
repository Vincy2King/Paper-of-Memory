# RL-Guided Temporal Localization for Dual-Channel Retrieval in Long-Horizon Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.23598v1
- Published: 2026-10-16
- Updated: 2026-10-16
- Authors: Dabin Sheng, Zhe Wu, Jinming Zhao, Junliang Xing, Yuanchun Shi
- Tags: agent, benchmark, episodic, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.23598v1

## One-Sentence Summary
Time-aware retrieval is crucial for long-horizon LLM agents to effectively leverage ever-growing long-term memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, episodic, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Time-aware retrieval is crucial for long-horizon LLM agents to effectively leverage ever-growing long-term memory.

进一步看，论文的核心做法或实验重点可以概括为：Existing methods focus on lexical or semantic similarity, leading to target memories being crowded out by temporally mismatched yet semantically similar candidates.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, episodic, long-term, retrieval
- 检索关键词命中：agent memory, episodic memory, long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.AI

## Abstract Snapshot
Time-aware retrieval is crucial for long-horizon LLM agents to effectively leverage ever-growing long-term memory. Existing methods focus on lexical or semantic similarity, leading to target memories being crowded out by temporally mismatched yet semantically similar candidates. Even time-aware approaches inject temporal cues only during memory organization or answer generation, overlooking temporal constraints at the retrieval stage, where candidate selection occurs - the root cause of the displacement. Inspired by the temporal contiguity effect in human episodic memory, we propose TIDER (Temporal Interval-driven Dual-channel Evidence Retrieval), a time-aware agentic retrieval framework. Central to TIDER is a reinforcement learning (RL)-trained temporal interval locator that infers the temporal windows in which the evidence lies. RL optimizes window localization as a discrete, non-differentiable retrieval decision, using composite rewards to convert sparse answer supervision into fine-grained retrieval feedback. These temporal windows first define the temporal retrieval channel; the retrieved candidates are then merged with results from the semantic channel and reranked by proximity to the windows. This temporal grounding enables TIDER to retrieve temporally aligned evidence that would otherwise be drowned out by the volume of semantically similar yet temporally mismatched memories. With a lightweight 1.7B locator, TIDER achieves state-of-the-art accuracy on both long-horizon memory benchmarks - 61.52% on LifeBench (+8.82%) and 78.96% on LoCoMo (+3.66%) - which indicates that temporal cues are crucial for pinpointing target evidence amid a vast pool of semantically similar historical events in long-term daily-life memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
