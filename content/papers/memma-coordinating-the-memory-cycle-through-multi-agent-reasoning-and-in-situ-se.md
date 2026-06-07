# MemMA: Coordinating the Memory Cycle through Multi-Agent Reasoning and In-Situ Self-Evolution

- Source: OpenReview
- Venue: ACL ARR 2026 March Submission
- Paper ID: openreview:yG3Xv083je
- Published: 2026-06-07
- Updated: 2026-06-07
- Authors: Unknown
- Tags: agent, retrieval
- Categories: aclweb.org/ACL/ARR/2026/March/-/Submission
- URL: https://openreview.net/forum?id=yG3Xv083je

## One-Sentence Summary
Memory-augmented LLM agents maintain external memory banks to support long-horizon interaction, yet most existing systems treat construction, retrieval, and utilization as...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 March Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Memory-augmented LLM agents maintain external memory banks to support long-horizon interaction, yet most existing systems treat construction, retrieval, and utilization as isolated subroutines.

进一步看，论文的核心做法或实验重点可以概括为：This creates two coupled challenges: strategic blindness on the forward path of the memory cycle, where construction and retrieval are driven by local heuristics rather than explicit strategic reasoning, and sparse,...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 March Submission
- 高亮主题命中：agent, retrieval
- 检索关键词命中：memory-augmented
- 来源分类信息：aclweb.org/ACL/ARR/2026/March/-/Submission

## Abstract Snapshot
Memory-augmented LLM agents maintain external memory banks to support long-horizon interaction, yet most existing systems treat construction, retrieval, and utilization as isolated subroutines. This creates two coupled challenges: strategic blindness on the forward path of the memory cycle, where construction and retrieval are driven by local heuristics rather than explicit strategic reasoning, and sparse, delayed supervision on the backward path, where downstream failures rarely translate into direct repairs of the memory bank. To address these challenges, we propose MemMA, a plug-and-play multi-agent framework that coordinates the memory cycle along both the forward and backward paths. On the forward path, a Meta-Thinker produces structured guidance that steers a Memory Manager during construction and directs a Query Reasoner during iterative retrieval. On the backward path, MemMA introduces in-situ self-evolving memory construction, which synthesizes probe QA pairs, verifies the current memory, and converts failures into repair actions before the memory is finalized. Extensive experiments on LoCoMo show that MemMA consistently outperforms existing baselines across multiple LLM backbones and improves three different storage backends in a plug-and-play manner. Our code is publicly available at https://anonymous.4open.science/r/memma-588C.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
