# UpliftMem: Learning Set-Level Uplift for Agent Memory Retrieval

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.36805v1
- Published: 2026-09-29
- Updated: 2026-09-29
- Authors: Mengkun Liang, Haoran Qiang, Guannan Liu, Junjie Wu
- Tags: agent, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.36805v1

## One-Sentence Summary
Large language model (LLM) agents reuse external memory to guide new tasks, but effective retrieval requires learning which memory sets improve execution.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents reuse external memory to guide new tasks, but effective retrieval requires learning which memory sets improve execution.

进一步看，论文的核心做法或实验重点可以概括为：Such learning relies on costly outcome feedback: ordinary retrieval observes only executed sets, while evaluating alternatives requires additional rollouts.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory, memory retrieval
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language model (LLM) agents reuse external memory to guide new tasks, but effective retrieval requires learning which memory sets improve execution. Such learning relies on costly outcome feedback: ordinary retrieval observes only executed sets, while evaluating alternatives requires additional rollouts. We introduce \textsc{UpliftMem}, which learns memory retrieval from set-level execution uplift relative to the same executor without memory. A theoretical analysis of how retrieval preferences restrict feedback coverage motivates targeted probing of alternative memory sets. Probe selection follows an expected value of sample information (EVSI) criterion, derived in closed form under a correlated Gaussian model, to allocate limited training rollouts according to their expected improvement in local retrieval decisions. The shared scorer is trained with a frozen executor and selects memory sets without test-time probes. Across ALFWorld, WebShop, and BigCodeBench, \textsc{UpliftMem} achieves the best success rates among evaluated baselines on the main evaluation sets. Controlled fixed-store and matched probe budget evaluations further demonstrate improved memory-use decisions and more effective use of execution feedback.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
