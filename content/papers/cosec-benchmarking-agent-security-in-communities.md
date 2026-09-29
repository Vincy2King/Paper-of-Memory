# CoSec: Benchmarking Agent Security in Communities

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.34790v1
- Published: 2026-09-28
- Updated: 2026-09-28
- Authors: Hao Chen, Wenhui Dong, Ye Chen, Jiezhi Yao, Chenbo Xia, Yuwen Qu, Renxiang Wang, Fudong Yuan, Camil Hamami, Chenglong Pan, Xinquan Yue, Ziyu Wang, Fengyu Ye, Chenyang Si, Caifeng Shan
- Tags: agent, benchmark
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2609.34790v1

## One-Sentence Summary
LLM agents operate in persistent collaborative environments involving multiple users, communities, memories, files, and tools.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM agents operate in persistent collaborative environments involving multiple users, communities, memories, files, and tools.

进一步看，论文的核心做法或实验重点可以概括为：Community boundaries may remain fixed or evolve with changes in membership, roles, composition, and relationships.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
LLM agents operate in persistent collaborative environments involving multiple users, communities, memories, files, and tools. Community boundaries may remain fixed or evolve with changes in membership, roles, composition, and relationships. Agents must complete legitimate tasks and prevent unauthorized disclosure of protected information. Existing evaluations do not fully examine these risks in agent systems. We introduce \textbf{CoSec}, an executable benchmark for evaluating privacy and authorization enforcement in LLM agent systems operating within and across communities. CoSec contains 208 canonical scenarios spanning fixed and evolving boundaries, protected information belonging to the agent owner or other participants, and attacks through dialogue, environmental content, persistent memory, and composed workflows. CoSec executes complete agent systems with persistent sessions, memory, files and tools. It verifies information flows against the active authorization state using execution traces and artifacts. Across harness and model configurations, agents frequently complete benign tasks but violate privacy and authorization boundaries. Privacy behavior varies across harnesses, attack surfaces, and community states, revealing how memory, files, tools, and workflows can carry protected information beyond its authorized scope. These findings show that task utility does not imply privacy or authorization compliance and that authorization in community settings remains an unresolved security challenge for persistent LLM agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
