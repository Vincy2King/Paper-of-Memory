# REM: What to Store, When to Recall, What to Forget in Experience Memory for Coding Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.27377v1
- Published: 2026-10-19
- Updated: 2026-10-19
- Authors: Xinyi Lisa Chen, Pedro Herrero-Vidal, Xiaohan Chen, Xiaojing Yu, Cris Liu, Bingqing Song, Bin Xu, Suleiman A. Khan, You-Lin Chen
- Tags: agent, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.27377v1

## One-Sentence Summary
Large language model (LLM) agents now autonomously complete long-horizon tasks, such as repository-level coding, through hundreds of think-act steps, yet the experience each run...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents now autonomously complete long-horizon tasks, such as repository-level coding, through hundreds of think-act steps, yet the experience each run produces is rarely reused on the next.

进一步看，论文的核心做法或实验重点可以概括为：Prior memory systems concentrate on retrieval, finding the most relevant past trajectory.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language model (LLM) agents now autonomously complete long-horizon tasks, such as repository-level coding, through hundreds of think-act steps, yet the experience each run produces is rarely reused on the next. Prior memory systems concentrate on retrieval, finding the most relevant past trajectory. Retrieval cannot observe the running agent, so it cannot decide whether the agent needs an experience, at which point, or for how long. We introduce REM (Reusable Experience Memory), a framework that manages the memory lifecycle from inside the agent's think-act loop through three explicit decisions. What to store: each completed trajectory is consolidated into a phase-structured document, two orders of magnitude smaller than the trajectory. When to recall: the document is injected at the start of the task; the costlier implementation record is withheld until an in-loop gate detects the agent struggling. What to forget: the record is evicted after a single exposure. On repository-level bug fixing (SWE-ContextBench Lite), REM retrieves the related trajectory more accurately than every state-of-the-art memory system (68.7% vs. 55.6% match@1) and improves, in every replicate, end-task resolution (27.6% vs. 24.9%) at 17% lower cost. Injecting the same experience as a summary or raw trajectory, even when oracle-retrieved, does not. Ablating any of the three decisions reduces resolution. Altogether, these results demonstrate that the bottleneck in experience reuse is not retrieval fidelity but how experience is stored and governed across its lifecycle, opening a control-theoretic perspective on agent memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
