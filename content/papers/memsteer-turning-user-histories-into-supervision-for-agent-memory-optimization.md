# MemSteer: Turning User Histories into Supervision for Agent Memory Optimization

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.39276v1
- Published: 2026-10-29
- Updated: 2026-10-29
- Authors: Jie Huang, Cuiling Lan, Qize Yu, Xiulian Peng, Yan Lu
- Tags: agent, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.39276v1

## One-Sentence Summary
An effective agent memory system should adapt to a user's history and task requirements.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：An effective agent memory system should adapt to a user's history and task requirements.

进一步看，论文的核心做法或实验重点可以概括为：Human-annotated supervision can guide this adaptation by providing feedback for evaluating and improving memory designs.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
An effective agent memory system should adapt to a user's history and task requirements. Human-annotated supervision can guide this adaptation by providing feedback for evaluating and improving memory designs. Yet suitable labels are rarely available for new user histories, and manually constructing QA pairs and supporting evidence is costly. We introduce MemSteer, which turns unlabeled user histories into question-answer (QA) supervision with supporting evidence for memory-design optimization. MemSteer constructs an evidence-grounded answer plan that specifies how facts across related records jointly support a reference answer. The plan guides question generation, while source-grounded auditing and blind answer recovery check the resulting annotations. To study the utility of this supervision, we develop MemSteer-Opt, which combines QA-based design evaluation with evidence-guided failure diagnosis to revise memory store, retrieval, and context construction without updating model parameters. Experiments on ATM-Bench and RHELM show that this supervision is competitive with official-QA-guided optimization. Relative to Base-BM25, MemSteer-Opt improves ATM-Bench Question Score by 13.4 points and RHELM accuracy by 4.1 and 6.6 points without and with external data, respectively. The supervision also benefits two existing optimizers on ATM-Bench, while new-user experiments demonstrate continued design optimization using supervision generated from the target histories.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
