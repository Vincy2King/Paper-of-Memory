# MemCo: Memory-Centric Collaboration for Generalizing LLM Agents to Unseen Environments

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.07376v1
- Published: 2026-10-05
- Updated: 2026-10-05
- Authors: Xinting Liao, Siyan Liu, Rabab K. Ward, Holger R. Roth, Xiaoxiao Li
- Tags: agent, benchmark, episodic
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.07376v1

## One-Sentence Summary
Large language model (LLM) agents increasingly operate in interactive environments, where they need to make sequential decisions through observation, action, and feedback.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents increasingly operate in interactive environments, where they need to make sequential decisions through observation, action, and feedback.

进一步看，论文的核心做法或实验重点可以概括为：Although memory can help agents reuse experience, existing work designs memory in isolation, where collecting enough trajectories to populate it is expensive.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, episodic
- 检索关键词命中：episodic memory, retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language model (LLM) agents increasingly operate in interactive environments, where they need to make sequential decisions through observation, action, and feedback. Although memory can help agents reuse experience, existing work designs memory in isolation, where collecting enough trajectories to populate it is expensive. Existing shared-memory approaches mitigate isolated experience by pooling episodic memories across tasks and environments. However, retrieving shared memory is challenged by the granularity, where retrieved memories can be either too specific to preserve current grounding or too coarse to support the next action. In this work, we propose MemCo, a memory-centric collaboration framework for generalizing LLM agents to unseen interactive environments. It maintains complementary local and global memory spaces, preserving environment-specific details locally while promoting transferable workflows induced from local trajectories to global memory. During online interaction, MemCo routes relevant local and global memories in terms of the agent's current state and decision phase, enabling agents to reuse the experience of other agents without blindly transferring environment-specific details. Experiments on interactive decision-making benchmarks show that MemCo improves task success and reduces redundant exploration compared with isolate-memory and shared-memory baselines. Our code is available at https://github.com/SYannL/nvdamas.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
