# JOVE ICE: Intent Guided Cloud Edge Device Collaboration for AI Glasses

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.33735v1
- Published: 2026-11-25
- Updated: 2026-11-25
- Authors: Yuyang Jin, Bingfeng Pi, Jiamei Sun, Wei Jin, Dongyang Wang, Yunpeng Li, Yan Bai, Lei Zuo
- Tags: agent, benchmark, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.33735v1

## One-Sentence Summary
Recent advances in large language models (LLMs) and LLM based agents have expanded the capabilities of AI glasses, enabling egocentric visual question answering, memory...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recent advances in large language models (LLMs) and LLM based agents have expanded the capabilities of AI glasses, enabling egocentric visual question answering, memory retrieval, and proactive assistance.

进一步看，论文的核心做法或实验重点可以概括为：These applications involve diverse inputs, including speech, images, and video, and range from simple device control to complex visual reasoning, posing challenges for efficient computation and communication.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.AI

## Abstract Snapshot
Recent advances in large language models (LLMs) and LLM based agents have expanded the capabilities of AI glasses, enabling egocentric visual question answering, memory retrieval, and proactive assistance. These applications involve diverse inputs, including speech, images, and video, and range from simple device control to complex visual reasoning, posing challenges for efficient computation and communication. While video centric capabilities have received considerable attention, simple text based and device executable tasks remain underexplored despite their prevalence in daily interactions. Efficiently supporting diverse workloads within a unified assistant remains an open challenge. We propose JOVE ICE, an intent guided cloud, edge, and device collaborative framework that routes requests among AI glasses, a paired smartphone, and cloud servers according to user intent. JOVE ICE integrates hierarchical intent classification with dynamic subagent orchestration to select efficient execution paths and flexibly incorporate new applications through specialized subagents. Analysis of real world AI glasses requests reveals that simple device control tasks account for over 30% of interactions, which JOVE ICE handles directly on device to avoid unnecessary cloud computation and costs. Evaluations on three public benchmarks demonstrate that JOVE ICE reduces time to first token by approximately 13% and token usage by over 11% compared with conventional device and cloud architectures, while maintaining task quality. These results demonstrate the potential of intent guided collaboration to improve the efficiency and scalability of AI glasses.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
