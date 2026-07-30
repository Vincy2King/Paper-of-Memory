# Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.26637v1
- Published: 2026-07-29
- Updated: 2026-07-29
- Authors: Sizhe Zhou, Sheldon Yu, Hui Wei, Junda Wu, Siru Ouyang, Yizhu Jiao, Shijia Pan, Julian McAuley, Yu Zhang, Tong Yu, Jiawei Han
- Tags: agent, benchmark, conversation, long-term, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2607.26637v1

## One-Sentence Summary
Deployed LLM agents increasingly keep their long-term memory as a filesystem: a directory tree of markdown files that the agent itself reads, writes, and reorganizes through...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Deployed LLM agents increasingly keep their long-term memory as a filesystem: a directory tree of markdown files that the agent itself reads, writes, and reorganizes through generic file tools.

进一步看，论文的核心做法或实验重点可以概括为：Yet research has largely passed over this medium: prior systems design bespoke memory representations and study retrieval over them, leaving the default's two working assumptions untested: that an agent can keep a...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Deployed LLM agents increasingly keep their long-term memory as a filesystem: a directory tree of markdown files that the agent itself reads, writes, and reorganizes through generic file tools. Yet research has largely passed over this medium: prior systems design bespoke memory representations and study retrieval over them, leaving the default's two working assumptions untested: that an agent can keep a growing store organized as memories accumulate, conflict, and go stale, and that this organization pays. We present the first systematic exploration of filesystem-based memory for LLM agents. We formalize the setting as three roles around one memory filesystem: a management agent integrates and organizes incoming content, a search agent answers queries with cited sources, and an execution agent supplies task trajectories that are distilled into skills, unifying declarative memory and skills in a single store. Across long-conversation benchmarks and embodied tasks, we vary memory shape (agent-organized hierarchy, verbatim dump, chunk retrieval), stream scale, tool harness (sandboxed shell, memory-tool-style functions, varied search tooling), and the strengths of the management and search agents, tracking answer quality, cost, and store health as memory grows. What organization reliably buys is search economy: organized stores roughly halve retrieval cost where material is large. Today's agents, however, fall short of the default's promise: in our growth study, organization erodes for all but the strongest management agent, and no agent we measure converts organization itself into better answers. And the model is not the only lever over a store's shape: changing the tool set alone reshapes the store as strongly as swapping the model. The study turns the filesystem default from an assumption into a design space for agent memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
