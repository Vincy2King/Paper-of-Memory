# When Memory Becomes Authority: Benchmarking Authority Collapse at the Memory Consolidation Boundary

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.01679v1
- Published: 2026-08-03
- Updated: 2026-08-03
- Authors: Qiuyang Zhan, Rui Zhang, Sheng Guo, Lepeng Zhao, Zhuotao Liu
- Tags: agent, benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.01679v1

## One-Sentence Summary
Persistent memory allows (self-evolving) LLM agents to adapt across tasks by consolidating heterogeneous interaction histories into reusable facts, preferences, observations,...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent memory allows (self-evolving) LLM agents to adapt across tasks by consolidating heterogeneous interaction histories into reusable facts, preferences, observations, and rules.

进一步看，论文的核心做法或实验重点可以概括为：Yet consolidation also imposes an implicit authorization boundary: it determines whether stored information may later be consumed as a user fact, an attested observation, or a standing instruction.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：agent memory, persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Persistent memory allows (self-evolving) LLM agents to adapt across tasks by consolidating heterogeneous interaction histories into reusable facts, preferences, observations, and rules. Yet consolidation also imposes an implicit authorization boundary: it determines whether stored information may later be consumed as a user fact, an attested observation, or a standing instruction. We identify authority collapse, in which consolidation preserves a claim while erasing the source constraints governing its authorized use, causing the stored memory to imply greater authority than its source permits. We introduce AuthMem-Bench, a controlled paired benchmark that holds the focal claim and downstream task fixed while varying only source authority. It evaluates write-time collapse, downstream authorization errors, and automatic authority preservation. Across seven consolidators based on widely used agent-memory systems and seven LLM backbones, we observe authority collapse in 48 of 49 evaluated configurations. In a controlled action-grounded evaluation, collapsed memories without authority metadata yield a mean unauthorized-action rate of 50.3%. In an end-to-end evaluation, automatically predicted and persisted authority labels reduce the observed unauthorized-action rate from 16.9% to 0.0%, while benign task success remains essentially unchanged. These findings show that memory-driven adaptation must preserve not only what was learned, but also the authority under which it may be reused.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
