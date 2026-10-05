# Harnessing LLMs as Agents: What Does It Cost?

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.02488v1
- Published: 2026-10-01
- Updated: 2026-10-01
- Authors: Zelin Zhao, Xinyu Guo, Jingyuan Zhang, Yuxuan Zhang, Yongxin Chen
- Tags: agent, context
- Categories: cs.LG
- URL: http://arxiv.org/abs/2610.02488v1

## One-Sentence Summary
Language-model agents increasingly rely on harnesses that manage bounded context, persistent memory, tools, verification, and repeated execution, yet existing notions of model...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Language-model agents increasingly rely on harnesses that manage bounded context, persistent memory, tools, verification, and repeated execution, yet existing notions of model capability do not quantify the...

进一步看，论文的核心做法或实验重点可以概括为：We introduce the Language Model Agent Machine (LAM), a resource-bounded abstraction that fixes the underlying semantic model while explicitly charging harness-level resources.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：context memory, persistent memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Language-model agents increasingly rely on harnesses that manage bounded context, persistent memory, tools, verification, and repeated execution, yet existing notions of model capability do not quantify the computational resources these mechanisms consume. We introduce the Language Model Agent Machine (LAM), a resource-bounded abstraction that fixes the underlying semantic model while explicitly charging harness-level resources. We establish four classes of results. Communication: LAM execution is instancewise equivalent to red--blue pebbling under simultaneous call--transfer budgets, transferring classical I/O lower bounds to context--memory traffic. Access: memory interfaces induce asymptotic separations, including a $Θ(n)$ gap between random and non-speculative sequential access on pointer chasing. Recomputation: bit-reversal DAGs require $Θ(n^2/(C+S)+n)$ model calls with context capacity $C$ and persistent-memory capacity $S$, quantifying when stored intermediate state avoids repeated semantic computation. Reliability: we derive tight stage-local sampling bounds, exact imperfect-verification costs, and a Young--Daly-type checkpoint law with a closed-form optimal verification interval. Controlled and held-out experiments on GPT-6 Astra test communication and reliability predictions, including checkpoint optima, policy selection under programmatic checking, and tradeoffs among call granularity, logical input traffic, and reliability on chained MATH tasks. Together, these results provide a resource theory for the computational cost of language-model agent harnesses.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
