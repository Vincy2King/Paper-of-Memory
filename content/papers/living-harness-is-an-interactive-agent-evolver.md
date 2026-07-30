# Living-Harness Is an Interactive-Agent Evolver

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.26598v1
- Published: 2026-07-29
- Updated: 2026-07-29
- Authors: Yuetian Du, Yucheng Wang, He Xu, Jiexu Xu, Shanwen Tan, Bing Zhao, Boyu Yang, Zhijie Xu, Ming Kong, Hu Wei, Jie Liu, Qiang Zhu
- Tags: agent, context, episodic, retrieval
- Categories: cs.MA, cs.AI, cs.CL
- URL: http://arxiv.org/abs/2607.26598v1

## One-Sentence Summary
Large language model (LLM) agents may recover from a failure within an episode or after a retry, yet the same execution failure can recur in later tasks because post-episode...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents may recover from a failure within an episode or after a retry, yet the same execution failure can recur in later tasks because post-episode feedback rarely revises the persistent...

进一步看，论文的核心做法或实验重点可以概括为：Static harnesses improve reliability through fixed tools, context, memory, and workflow structures, but remain unchanged after deployment.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, episodic, retrieval
- 检索关键词命中：context memory, episodic memory
- 来源分类信息：cs.MA, cs.AI, cs.CL

## Abstract Snapshot
Large language model (LLM) agents may recover from a failure within an episode or after a retry, yet the same execution failure can recur in later tasks because post-episode feedback rarely revises the persistent harness that guides future interactions. Static harnesses improve reliability through fixed tools, context, memory, and workflow structures, but remain unchanged after deployment. We propose $\textbf{Living-Harness}$, a self-evolving agent harness that converts each completed trajectory and its evaluator signals into posterior evidence for bounded harness updates. Guided by a domain-level $\textbf{Evolution-SOP}$ ($\textbf{S}$tandard $\textbf{O}$perating $\textbf{P}$rocedure), Living-Harness extracts an episode abstraction and structured update evidence, and writes two complementary forms of procedural knowledge: episodic memory that records trigger conditions, failure patterns, and recovery actions, and a state graph that records state nodes, repair edges, and transition rules. The updated harness state is retrieved to guide future interactions, while tools and base context remain frozen, allowing procedural repairs to accumulate across evolution cycles. On eight interactive environments derived from $τ^2$-Bench and MultiWOZ-2.4, Living-Harness improves average Pass@1 over the strongest interactive baseline by 10.07 and 9.91 percentage points, respectively, and supports retrieval-only reuse of the evolved harness state across model backbones.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
