# MemQ: Integrating Q-Learning into Self-Evolving Memory Agents over Provenance DAGs

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.08374v1
- Published: 2026-05-08
- Updated: 2026-05-08
- Authors: Junwei Liao, Haoting Shi, Ruiwen Zhou, Jiaqian Wang, Shengtao Zhang, Wei Zhang, Weinan Zhang, Ying Wen, Zhiyu Li, Feiyu Xiong, Bo Tang, Muning Wen
- Tags: agent, benchmark, context, episodic, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.08374v1

## One-Sentence Summary
Episodic memory allows LLM agents to accumulate and retrieve experience, but current methods treat each memory independently, i.e., evaluating retrieval quality in isolation...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Episodic memory allows LLM agents to accumulate and retrieve experience, but current methods treat each memory independently, i.e., evaluating retrieval quality in isolation without accounting for the dependency...

进一步看，论文的核心做法或实验重点可以概括为：We introduce MemQ, which applies TD($λ$) eligibility traces to memory Q-values, propagating credit backward through a provenance DAG that records which memories were retrieved when each new memory was created.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, episodic, retrieval
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Episodic memory allows LLM agents to accumulate and retrieve experience, but current methods treat each memory independently, i.e., evaluating retrieval quality in isolation without accounting for the dependency chains through which memories enable the creation of future memories. We introduce MemQ, which applies TD($λ$) eligibility traces to memory Q-values, propagating credit backward through a provenance DAG that records which memories were retrieved when each new memory was created. Credit weight decays as $(γλ)^d$ with DAG depth $d$, replacing temporal distance with structural proximity. We formalize the setting as an Exogenous-Context MDP, whose factored transition decouples the exogenous task stream from the endogenous memory store. Across six benchmarks, spanning OS interaction, function calling, code generation, multimodal reasoning, embodied reasoning, and expert-level QA, MemQ achieves the highest success rate on all six in generalization evaluation and runtime learning, with gains largest on multi-step tasks that produce deep and relevant provenance chains (up to +5.7~pp) and smallest on single-step classification (+0.77~pp) where single-step updates already suffice. We further study how $γ$ and $λ$ interact with the EC-MDP structure, providing principled guidance for parameter selection and future research. Code will be available soon.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
