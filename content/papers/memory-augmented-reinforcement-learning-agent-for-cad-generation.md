# Memory-Augmented Reinforcement Learning Agent for CAD Generation

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.19748v1
- Published: 2026-05-19
- Updated: 2026-05-19
- Authors: Yin Xiaolong, Liu Yu, Shen Jiahang, Lu Xingyu, Ni Jingzhe, Fan Fengxiao, Sang Fan
- Tags: agent, retrieval
- Categories: cs.AI, cs.MA
- URL: http://arxiv.org/abs/2605.19748v1

## One-Sentence Summary
Automatic generation of computer-aided design (CAD) models is a core technology for enabling intelligence in advanced manufacturing.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Automatic generation of computer-aided design (CAD) models is a core technology for enabling intelligence in advanced manufacturing.

进一步看，论文的核心做法或实验重点可以概括为：Existing generation methods based on large language models (LLMs) often fall short when handling complex CAD models characterized by long operation sequences, diverse operation types, and strong geometric constraints,...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI, cs.MA

## Abstract Snapshot
Automatic generation of computer-aided design (CAD) models is a core technology for enabling intelligence in advanced manufacturing. Existing generation methods based on large language models (LLMs) often fall short when handling complex CAD models characterized by long operation sequences, diverse operation types, and strong geometric constraints, primarily because reasoning chains break and effective error-correction mechanisms are lacking. To address this problem, this paper proposes a memory-augmented reinforcement learning framework for CAD generation agents. The framework encapsulates the underlying geometric kernel into a structured toolchain callable by the agent and builds a closed-loop mechanism of design intent understanding, global planning, execution, and multi-dimensional verification. It also designs a dual-track memory module consisting of a case library and a skill library, and proposes a dynamic utility retrieval algorithm. By introducing reinforcement learning into retrieval and policy optimization, the agent can effectively avoid retrieval traps in which examples are semantically similar but geometrically infeasible, enabling online self-correction and continual evolution without additional large-scale annotated data. Experiments show that the proposed method significantly improves both the success rate and geometric consistency on complex CAD model generation tasks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
