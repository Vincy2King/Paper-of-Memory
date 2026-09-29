# CoMemBench: Benchmarking Collaborative Memory Boundaries across Multi-Agent Workflow Topologies

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.32192v1
- Published: 2026-09-26
- Updated: 2026-09-26
- Authors: Sen Zhao, Ruiqi Kong, Zuyu Zhang, Lifeng Shen, Xinyu He, Ding Zou, Xu Zhang, Qinghua Zhang
- Tags: agent, benchmark, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.32192v1

## One-Sentence Summary
Multi-agent workflows require task-relevant information to be shared across agents, while irrelevant, stale, unverified, or incompatible information must remain isolated.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multi-agent workflows require task-relevant information to be shared across agents, while irrelevant, stale, unverified, or incompatible information must remain isolated.

进一步看，论文的核心做法或实验重点可以概括为：We call this task-conditioned scope of information a collaborative memory boundary.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：cs.AI

## Abstract Snapshot
Multi-agent workflows require task-relevant information to be shared across agents, while irrelevant, stale, unverified, or incompatible information must remain isolated. We call this task-conditioned scope of information a collaborative memory boundary. Workflow topology determines which intermediate artifacts are applicable to which downstream workers and when they cease to be valid, thereby providing a structural stress dimension for sharing and isolation. Existing memory benchmarks primarily evaluate retention and retrieval, whereas multi-agent benchmarks emphasize coordination and end-to-end completion, leaving topology-conditioned memory boundaries largely unmeasured. We introduce CoMemBench, an execution-grounded benchmark for collaborative memory sharing and isolation across multi-agent workflow topologies. It constructs 800 composite workflows across four domains from source-grounded dependency graphs, with node-local specifications, verifiable artifact handoffs, native evaluators, and matched isolation challenges. CoMemBench measures workflow completion, verified node progress, required-handoff reliability, isolation robustness, and token cost. Experiments reveal a sharing-isolation trade-off: broader context improves information availability but can weaken isolation, while system rankings shift across topologies and artifact violations.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
