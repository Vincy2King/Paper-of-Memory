# Long-Horizon Embodied Decision-Making via Multimodal Memory Compression

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.01456v1
- Published: 2026-08-02
- Updated: 2026-08-02
- Authors: Bingxuan Li, Rui Yang, Cheng Qian, Jiateng Liu, Jeonghwan Kim, Zhenhailong Wang, Manling Li, Tong Zhang, Heng Ji
- Tags: agent, benchmark, compression
- Categories: cs.CV, cs.CL
- URL: http://arxiv.org/abs/2608.01456v1

## One-Sentence Summary
Agents are increasingly expected to act not only as task executors, but also as decision-makers on behalf of human users.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agents are increasingly expected to act not only as task executors, but also as decision-makers on behalf of human users.

进一步看，论文的核心做法或实验重点可以概括为：This shift requires agents to accumulate evidence over long horizons, interpret implicit user preferences, and compare multiple candidates under partial observations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression
- 检索关键词命中：memory compression
- 来源分类信息：cs.CV, cs.CL

## Abstract Snapshot
Agents are increasingly expected to act not only as task executors, but also as decision-makers on behalf of human users. This shift requires agents to accumulate evidence over long horizons, interpret implicit user preferences, and compare multiple candidates under partial observations. In this work, we propose DunphyBench, a new benchmark for evaluating agents on long-horizon human-centered embodied decision-making, where the agent must navigate through multiple embodied housing environments and make decisions that align with multi-dimensional human preferences. Unlike standard embodied reasoning tasks that often focus on procedural planning or immediate goal completion, our setting requires agents to integrate multimodal, multi-source input into coherent knowledge that supports complex reasoning across long horizon. The evaluation results reveal that there is a substantial gap between current agents and human performance. Furthermore, our diagnosis of state-of-the-art VLM-driven agents reveals that memory management is one of the bottlenecks, where raw multimodal history introduces noise that hinders decision quality. Motivated by this finding, we design MeMento, a preference-conditioned multimodal memory compressor that selectively compresses decision-relevant information from long-horizon history based on user preferences with a fixed set of memory tokens. Experiments show that MeMento helps VLM-driven agents improve accuracy by 7.18%, while reducing memory usage by 85.38% compared to the strongest baseline.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
