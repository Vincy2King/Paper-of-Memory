# MOSAIC: An Omni-Modal Benchmark for Long-Term Memory and Cross-Modal Reasoning in Conversational Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.29249v1
- Published: 2026-10-21
- Updated: 2026-10-21
- Authors: Hong Ting Tsang, Boyi Zhang, Haoyu Huang, Jiaxin Bai, Yufei Li, Yisen Gao, Zhongwei Xie, Hongyu Luo, Jeff Z. Pan, Yangqiu Song
- Tags: agent, benchmark, conversation, long-term, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2610.29249v1

## One-Sentence Summary
Omni-modal assistants must remember not only what users say, but also what they show and convey.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Omni-modal assistants must remember not only what users say, but also what they show and convey.

进一步看，论文的核心做法或实验重点可以概括为：Existing long-term memory benchmarks are mostly text-and-image or report a single end-to-end score, so they cannot locate whether evidence is lost when it is represented, retrieved, delivered, or read.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, long-term, retrieval
- 检索关键词命中：long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Omni-modal assistants must remember not only what users say, but also what they show and convey. Existing long-term memory benchmarks are mostly text-and-image or report a single end-to-end score, so they cannot locate whether evidence is lost when it is represented, retrieved, delivered, or read. We introduce MOSAIC, a benchmark of 923 questions over persona-grounded histories of 11-24 sessions spanning text, image, video, and audio. MOSAIC constructs targeted spatial, temporal, and prosodic signals rather than decorative media, with the strongest causal validation for spatial information and selector-level validation for annotated prosody, and pairs them with a matched diagnostic protocol that freezes the question, reader, prompt, and budget while intervening on representation, retrieval, and delivery. Matched decomposition shows that representation loss is modality-dependent, residual reading dominates even under gold evidence, and abstention remains weak on these controls: strong answerable scores coexist with failures to refuse. MOSAIC thus turns omni-modal memory evaluation from a leaderboard into a diagnosis of write, retrieve, deliver, and read failures.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
