# Share-Borne AI Virus: Memory-Hopping Attacks Across LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.35576v1
- Published: 2026-09-28
- Updated: 2026-09-28
- Authors: Sidharth Pulipaka, Ansh Sharma, Stanislau Hlebik, Leonidas Raghav, Vyas Raina, Ivaxi Sheth, Mario Fritz
- Tags: agent
- Categories: cs.AI, cs.CL, cs.CR, cs.LG
- URL: http://arxiv.org/abs/2609.35576v1

## One-Sentence Summary
Large language models are increasingly deployed as stateful assistants that retain information across interactions and use tools to read, modify, and create persistent artifacts.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models are increasingly deployed as stateful assistants that retain information across interactions and use tools to read, modify, and create persistent artifacts.

进一步看，论文的核心做法或实验重点可以概括为：As these artifacts are shared between users, they form an indirect communication channel between otherwise independent assistants.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI, cs.CL, cs.CR, cs.LG

## Abstract Snapshot
Large language models are increasingly deployed as stateful assistants that retain information across interactions and use tools to read, modify, and create persistent artifacts. As these artifacts are shared between users, they form an indirect communication channel between otherwise independent assistants. We study a failure mode in which this channel enables self-propagating attacks. We introduce artifact-mediated propagation, where adversarial content introduced through an artifact (e.g. a report), is stored in an assistant's persistent memory, reproduced in a subsequently created artifact, and acquired by another assistant that later reads it. We evaluate this process in temporal human-agent universes that model artifact exchange between independently operated assistants over time, measuring whether an attack survives successive hand-offs, how many hops it reaches, and how broadly it spreads. We find that attacks can propagate across multiple independent assistants and persist over extended interaction sequences. In larger simulated environments, even GPT-5.6 Luna exhibits substantial spread, reaching 60-80% of agents with propagation chains extending to eight hops. These results show that persistent artifacts can act as durable carriers of adversarial state, allowing attacks to outlive individual interactions and spread across isolated assistants.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
