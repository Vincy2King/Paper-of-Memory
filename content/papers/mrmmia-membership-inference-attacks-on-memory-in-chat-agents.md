# MRMMIA: Membership Inference Attacks on Memory in Chat Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.27825v1
- Published: 2026-05-27
- Updated: 2026-05-27
- Authors: Kai Chen, Yan Pang, Tianhao Wang
- Tags: agent, retrieval
- Categories: cs.CR, cs.LG
- URL: http://arxiv.org/abs/2605.27825v1

## One-Sentence Summary
Membership inference attacks (MIAs) test whether a target data record belongs to a system's private data, and have become a standard tool to measure privacy leakage in machine...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Membership inference attacks (MIAs) test whether a target data record belongs to a system's private data, and have become a standard tool to measure privacy leakage in machine learning systems.

进一步看，论文的核心做法或实验重点可以概括为：Prior work has primarily focused on training corpora or retrieval databases.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CR, cs.LG

## Abstract Snapshot
Membership inference attacks (MIAs) test whether a target data record belongs to a system's private data, and have become a standard tool to measure privacy leakage in machine learning systems. Prior work has primarily focused on training corpora or retrieval databases. However, MIAs against agent memory have received less attention, even though such memory can contain sensitive user-agent interactions, retrieved facts, and user preferences. Therefore, in this work, we focus on chat agent memory MIAs, where an adversary infers whether a candidate memory unit belongs to the chat agent's memory store. We propose Multi-Recall Memory MIA (MRMMIA), a unified attack that utilizes multiple recall probes to the agent to extract the membership signal across black-box, gray-box, and white-box settings. Our experiments demonstrate that MRMMIA consistently outperforms baselines. Our results expose the privacy risk in agents and provide an initial evaluation framework for membership leakage in chat-agent memory systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
