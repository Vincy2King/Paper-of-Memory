# H-Mem: A Novel Memory Mechanism for Evolving and Retrieving Agent Memory via a Hybrid Structure

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.15701v1
- Published: 2026-05-15
- Updated: 2026-05-15
- Authors: Jiawei Yu, Yixiang Fang, Xilin Liu, Yuchi Ma
- Tags: agent, benchmark, long-term, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2605.15701v1

## One-Sentence Summary
Memory data are ubiquitous in Large Language Model (LLM)-based agents (e.g., OpenClaw and Manus).

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory data are ubiquitous in Large Language Model (LLM)-based agents (e.g., OpenClaw and Manus).

进一步看，论文的核心做法或实验重点可以概括为：A few recent works have attempted to exploit agents'memory for improving their performance on the question-answering (QA) task, but they lack a principled mechanism for effectively modeling how memory data evolves...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory, memory benchmark, memory benchmarks, memory retrieval, retrieval memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Memory data are ubiquitous in Large Language Model (LLM)-based agents (e.g., OpenClaw and Manus). A few recent works have attempted to exploit agents'memory for improving their performance on the question-answering (QA) task, but they lack a principled mechanism for effectively modeling how memory data evolves over time and retrieving memory data effectively, leading to poor performance in memory utilization. To fill this gap, we present H-Mem, a novel memory mechanism via a hybrid structure that can not only effectively model the evolution of agent memory over a long period of time, but also provide an efficient memory retrieval approach. Particularly, H-Mem builds a temporal and semantic tree structure that allows the short-term memory data to evolve progressively into long-term memory data, where the latter provides summarized information about the former, while simultaneously constructing a knowledge graph to capture the relationships between entities in memory. Moreover, it offers an effective memory retrieval approach by exploiting the hybrid structure of the tree and graph structures. Extensive experiments on three agent memory benchmarks show that H-Mem achieves state-of-the-art performance on the QA task.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
