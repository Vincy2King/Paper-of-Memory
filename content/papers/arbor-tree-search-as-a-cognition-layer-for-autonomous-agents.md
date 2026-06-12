# Arbor: Tree Search as a Cognition Layer for Autonomous Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.12563v1
- Published: 2026-06-10
- Updated: 2026-06-10
- Authors: Neha Prakriya, Chaojun Hou, Zheng Gong, Huasha Zhao, Xi Zhao, Mou Li, Zhenyu Gu, Emad Barsoum
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.12563v1

## One-Sentence Summary
Arbor is a multi-agent framework that introduces structured tree search as a cognition layer for autonomous agents operating in large, stateful action spaces.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Arbor is a multi-agent framework that introduces structured tree search as a cognition layer for autonomous agents operating in large, stateful action spaces.

进一步看，论文的核心做法或实验重点可以概括为：Prior autonomous optimization systems operate on isolated targets with stateless evaluation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：working memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Arbor is a multi-agent framework that introduces structured tree search as a cognition layer for autonomous agents operating in large, stateful action spaces. Prior autonomous optimization systems operate on isolated targets with stateless evaluation. Arbor instead maintains an explicit search tree of scored hypotheses that serves as the shared working memory across agents, evolving with every measurement, treating failures as diagnostic signal that reshapes subsequent exploration, and expanding as prior successes shift the bottleneck distribution. We validate Arbor on full-stack LLM inference optimization, a domain where achieving peak performance has historically required coordinated effort from engineering teams across the application, framework, compiler, kernel, and hardware stack. Arbor pairs an Orchestrator agent, which drives optimization by delegating to Domain Specialists across the inference stack, with a Critic agent that safeguards stability through root-cause analysis, introspection, and measurement validation -- a checks-and-balances architecture where neither agent can unilaterally drive the system. Agent capabilities are decomposed into hard skills (domain expertise) and soft skills (coordination protocols that determine how contributions compose), enabling fully autonomous multi-day campaigns. Arbor achieves up to 193% inference throughput-latency Pareto improvement over vendor-optimized baselines, while a single agent without the harness plateaus at +33% throughput improvement and crashes irrecoverably within hours. Arbor generalizes to multiple generations of hardware platform, and run-to-run variance is within 2 percentage points demonstrating that the method is hardware-agnostic and reproducible.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
