# OpsMem: Dual-Memory Reasoning with Cross-Memory Resonance for Failure Diagnosis

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.11357v1
- Published: 2026-07-13
- Updated: 2026-07-13
- Authors: Yongqian Sun, Rongchen Gao, Yu Luo, Wenwei Gu, Shenglin Zhang, Qingyi Guo, Qiuai Fu, Yaoliang Wu, Dan Pei
- Tags: agent, long-term
- Categories: cs.AI, cs.SE
- URL: http://arxiv.org/abs/2607.11357v1

## One-Sentence Summary
Failure diagnosis in modern software systems requires iterative evidence acquisition and hypothesis reasoning guided by operational experience.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Failure diagnosis in modern software systems requires iterative evidence acquisition and hypothesis reasoning guided by operational experience.

进一步看，论文的核心做法或实验重点可以概括为：Existing LLM-based methods improve diagnosis through agentic reasoning or knowledge augmentation, but they often lack a mechanism to coordinate the evolving diagnostic state with operational experience during...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term
- 检索关键词命中：long-term memory, memory reasoning
- 来源分类信息：cs.AI, cs.SE

## Abstract Snapshot
Failure diagnosis in modern software systems requires iterative evidence acquisition and hypothesis reasoning guided by operational experience. Existing LLM-based methods improve diagnosis through agentic reasoning or knowledge augmentation, but they often lack a mechanism to coordinate the evolving diagnostic state with operational experience during iterative diagnosis. We propose OpsMem, a dual-memory framework that maintains a short-term memory for the current diagnostic state and a long-term memory for reusable operational experience. OpsMem uses cross-memory resonance to activate state-relevant long-term memory, conditions multi-agent diagnosis on the short-term and activated long-term memories, and consolidates reusable experience from solved incidents back into long-term memory. Experiments on a real-world Huawei microservice failure diagnosis dataset show that OpsMem outperforms representative agentic-reasoning and knowledge-augmented baselines, improving Match and Relevant by up to 46.88% and 18.39% over the strongest baseline, respectively.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
