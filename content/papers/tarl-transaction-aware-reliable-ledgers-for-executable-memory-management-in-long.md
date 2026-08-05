# TARL: Transaction-Aware Reliable Ledgers for Executable Memory Management in Long-Term Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.03699v1
- Published: 2026-08-04
- Updated: 2026-08-04
- Authors: Han Xiao, Hongjun Xu, Xin Zhang, Yidong Chen, Xiaodong Shi
- Tags: agent, benchmark, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.03699v1

## One-Sentence Summary
Persistent memory helps long-term agents retain knowledge, yet a single update error can repeatedly distort future retrieval and reasoning.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent memory helps long-term agents retain knowledge, yet a single update error can repeatedly distort future retrieval and reasoning.

进一步看，论文的核心做法或实验重点可以概括为：Most existing systems reduce memory updating to a binary Write/Hold decision, which cannot distinguish whether new information should be added, ignored, used to revise an outdated belief, rejected as unreliable, or...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Persistent memory helps long-term agents retain knowledge, yet a single update error can repeatedly distort future retrieval and reasoning. Most existing systems reduce memory updating to a binary Write/Hold decision, which cannot distinguish whether new information should be added, ignored, used to revise an outdated belief, rejected as unreliable, or deferred for verification. These choices may share the same binary label while producing fundamentally different memory states. We introduce TARL, a memory state update framework that maps each statement to one of five executable actions. TARL identifies the affected memory, resolves its temporal scope, compares source reliability, and updates accepted, pending, and rejected ledgers. It is further trained by comparing the memory states produced by alternative update operations, encouraging the model to select the operation that leads to the correct result. We also introduce TARL-Mem, a benchmark with fine-grained action labels and next-state targets. Across in-domain, cross-source, temporal, counterfactual, and sequential evaluations, TARL improves action prediction and state recovery, reduces memory pollution, preserves conflicting evidence, and limits cumulative corruption. The complete model implementation is provided in the supplementary material.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
