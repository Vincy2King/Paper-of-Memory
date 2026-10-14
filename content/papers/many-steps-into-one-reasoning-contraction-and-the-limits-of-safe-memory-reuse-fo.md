# Many Steps into One: Reasoning Contraction and the Limits of Safe Memory Reuse for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.17544v1
- Published: 2026-10-13
- Updated: 2026-10-13
- Authors: Jianghong Zhou, Hao Rong, Chen Lin, Daoan Zhang
- Tags: agent
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2610.17544v1

## One-Sentence Summary
Thought templates, skill libraries, agent memories and caches turn many reasoning steps into one.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Thought templates, skill libraries, agent memories and caches turn many reasoning steps into one.

进一步看，论文的核心做法或实验重点可以概括为：We call this reasoning contraction.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Thought templates, skill libraries, agent memories and caches turn many reasoning steps into one. We call this reasoning contraction. A contracted memory saves reasoning steps and errors until its facts change, then quietly answers wrong. Most systems trust memories by counting successes and failures. We prove that such counters are badly tuned change detectors: a symmetric counter notices a partial change only after a power of its false-alarm horizon, and an unclipped one may never notice it. On five LLMs answering multi-hop questions over edited facts, ExpeL- and ACE-style counters serve 7.0-13.5x more stale answers than certified memories given the same information, and on code tasks with an exact verifier 35-73x more. Safety also has a price. When facts change and each memory is judged only by its own verified outcomes, one number, the certification load, sets how much reasoning any safe memory can skip, and under Zipf demand it yields a scaling law. Our recipe weighs each memory's failures by its own likelihood ratio, certifies its utility against live reasoning, and restarts the certificate when facts change, with the likelihood-ratio detector as the safety net for unannounced changes; for large edits it also invalidates the memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
