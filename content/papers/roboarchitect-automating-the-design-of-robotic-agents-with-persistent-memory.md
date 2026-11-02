# RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.42141v1
- Published: 2026-10-30
- Updated: 2026-10-30
- Authors: Shengguang Wu, Suning Huang, Cherie Ho, Ria Doshi, Hao Zhu, Serena Yeung-Levy
- Tags: agent, benchmark
- Categories: cs.RO, cs.AI, cs.CV
- URL: http://arxiv.org/abs/2610.42141v1

## One-Sentence Summary
Recent work shows that a frozen robot policy performs far better inside an agent harness, where control code decides when to query the policy, consult vision tools, or command...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recent work shows that a frozen robot policy performs far better inside an agent harness, where control code decides when to query the policy, consult vision tools, or command the arm directly.

进一步看，论文的核心做法或实验重点可以概括为：Yet today these harnesses are built by hand and redesigned for each new robot or benchmark.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：cs.RO, cs.AI, cs.CV

## Abstract Snapshot
Recent work shows that a frozen robot policy performs far better inside an agent harness, where control code decides when to query the policy, consult vision tools, or command the arm directly. Yet today these harnesses are built by hand and redesigned for each new robot or benchmark. We show that harness design can be automated, offering a strong alternative to finetuning on a novel setup. In RoboArchitect, a coding model observes a robot's rollouts, diagnoses failures, and iteratively revises the harness around the frozen policy. The harness evolves on a set of episodes for its optimization and is evaluated on held-out scenes and tasks. Without updating any model weights, RoboArchitect raises average success from 9.7% to 43.3% on unseen scenes (4.5x) and from 12.7% to 40.2% on unseen tasks (3.2x), across multiple benchmarks and policies. The gains are largest where the benchmark is far from the policy's training data: wrapping a general-purpose policy, the evolved harness yields a specialist that often outperforms even the finetuned version. Intuitive control strategies are automatically designed, such as lifting a jammed arm clear or reaching in horizontally when an obstacle blocks the way from above. The harness also evolves its own persistent memory, carrying learned experience, such as effective grasp depths, into later decisions. These results suggest that substantial headroom in robotic manipulation lies in the agent harness, and its design can be effectively automated and optimized without weight updates.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
