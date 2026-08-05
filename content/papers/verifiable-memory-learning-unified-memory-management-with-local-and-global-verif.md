# Verifiable Memory: Learning Unified Memory Management with Local and Global Verifiers for Large Language Model Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.03137v1
- Published: 2026-08-04
- Updated: 2026-08-04
- Authors: Xiaolong Sun, Qichao Wang, Hangyu Li, Liang Chen
- Tags: agent, benchmark, context, episodic, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.03137v1

## One-Sentence Summary
Large language model (LLM) agents must retain reusable information, control a bounded active context, and recover earlier evidence during long-horizon interaction.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents must retain reusable information, control a bounded active context, and recover earlier evidence during long-horizon interaction.

进一步看，论文的核心做法或实验重点可以概括为：Existing methods commonly optimize long-term memory (LTM) and short-term memory (STM) separately, while unified policies are often trained primarily with trajectory-level feedback, which provides weak credit for...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, episodic, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language model (LLM) agents must retain reusable information, control a bounded active context, and recover earlier evidence during long-horizon interaction. Existing methods commonly optimize long-term memory (LTM) and short-term memory (STM) separately, while unified policies are often trained primarily with trajectory-level feedback, which provides weak credit for individual memory decisions. We present Verifiable Memory (VerMem), a framework that represents LTM, active context, and episodic history as distinct states and controls them with one memory operation policy. Seven atomic operations let the policy add, revise, or soft-delete LTM entries; retrieve LTM into the active context; filter or summarize the active context; and restore selected episodic fragments. VerMem is initialized by supervised fine-tuning and trained with a three-stage reinforcement-learning curriculum. The local verifier scores executable memory transitions, and a global verifier assesses evidence coherence and terminal-memory consistency after task completion. These scores are combined with programmatically computed task, evidence-recall, efficiency, and constraint signals through hierarchical credit assignment. The verifiers are used only during training. Across five benchmarks and two LLM backbones, VerMem achieves the best result on the vast majority of reported metrics and consistently outperforms strong memory baselines. Under controlled online-token budgets on three interactive benchmarks, it also achieves the strongest efficiency--performance frontier among the compared methods. Code is available at https://github.com/Sun-SYSU-24/VerMem.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
