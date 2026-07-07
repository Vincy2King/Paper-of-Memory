# EvoAgentBench: Benchmarking Agent Self-Evolution via Ability Transfer

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.05202v1
- Published: 2026-07-06
- Updated: 2026-07-06
- Authors: Xingze Gao, Chuanrui Hu, Hongda Chen, Pengfei Yao, Zhao Wang, Yi Bai, Zhengwei Wu, Yunyun Han, Xiaofeng Cong, Jie Gui, Yafeng Deng, Teng Li
- Tags: agent, benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.05202v1

## One-Sentence Summary
Agent self-evolution in long-horizon LLM systems is largely procedural: useful experience is not merely stored information, but reusable procedures for searching, debugging, and...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agent self-evolution in long-horizon LLM systems is largely procedural: useful experience is not merely stored information, but reusable procedures for searching, debugging, and verification.

进一步看，论文的核心做法或实验重点可以概括为：Yet current evaluations do not isolate this form of transfer.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：cs.AI

## Abstract Snapshot
Agent self-evolution in long-horizon LLM systems is largely procedural: useful experience is not merely stored information, but reusable procedures for searching, debugging, and verification. Yet current evaluations do not isolate this form of transfer. Agent benchmarks test single-episode task solving; memory benchmarks target information retention rather than procedural reuse. We introduce EvoAgentBench, a benchmark for agent self-evolution via Ability-guided transfer across four agentic domains: web research, algorithmic reasoning, software engineering, and knowledge work. EvoAgentBench extracts trace-grounded Abilities from agent executions, canonicalizes them into operational units, and builds domain-specific Ability Graphs linking tasks that share procedural overlap. By design, every test task is backed by verified training-side Ability support. Across a 528/267 train/test split, two scaffolds, and three backbones, curated Ability content transfers reliably across model families, but no current automatic method sustains positive gain in all settings. EvoAgentBench shifts self-evolution evaluation from aggregate accuracy comparison to fine-grained diagnosis of experience encoding, routing, and uptake. The benchmark is publicly available at https://huggingface.co/datasets/EverMind-AI/EvoAgentBench.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
