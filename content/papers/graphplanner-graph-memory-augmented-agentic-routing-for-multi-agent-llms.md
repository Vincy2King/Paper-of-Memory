# GraphPlanner: Graph Memory-Augmented Agentic Routing for Multi-Agent LLMs

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.23626v1
- Published: 2026-04-26
- Updated: 2026-04-26
- Authors: Tao Feng, Haozhen Zhang, Zijie Lei, Peixuan Han, Jiaxuan You
- Tags: agent
- Categories: cs.CL
- URL: http://arxiv.org/abs/2604.23626v1

## One-Sentence Summary
LLM routing has achieved promising results in integrating the strengths of diverse models while balancing efficiency and performance.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM routing has achieved promising results in integrating the strengths of diverse models while balancing efficiency and performance.

进一步看，论文的核心做法或实验重点可以概括为：However, to support more realistic and challenging applications, routing must extend into agentic LLM settings, where task planning, multi-round cooperation among heterogeneous agents, and memory utilization are...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CL

## Abstract Snapshot
LLM routing has achieved promising results in integrating the strengths of diverse models while balancing efficiency and performance. However, to support more realistic and challenging applications, routing must extend into agentic LLM settings, where task planning, multi-round cooperation among heterogeneous agents, and memory utilization are indispensable. To address this gap, we propose GraphPlanner, a heterogeneous graph memory-augmented agentic router for multi-agent LLMs that generates routing workflows for each query and supports both inductive and transductive inference. GraphPlanner formulates workflow generation as a Markov Decision Process (MDP), where at each step it selects both the LLM backbone and the agent role, including Planner, Executor, and Summarizer. By leveraging a heterogeneous graph, denoted as GARNet, to capture interaction memories among queries, agents, and responses, GraphPlanner integrates historical memory and workflow memory into richer state representations. The entire pipeline is optimized with reinforcement learning, jointly improving task-specific performance and computational efficiency. We evaluate GraphPlanner across 14 diverse LLM tasks and demonstrate that: (1) GraphPlanner outperforms strong single-round and multi-round routers, improving accuracy by up to 9.3% while reducing GPU cost from 186.26 GiB to 1.04 GiB; (2) GraphPlanner generalizes robustly to unseen tasks and LLMs, exhibiting strong zero-shot capabilities; and (3) GraphPlanner effectively leverages historical memories, supporting both inductive and transductive inference for more adaptive routing. Our code for GraphPlanner is released at https://github.com/ulab-uiuc/GraphPlanner.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
