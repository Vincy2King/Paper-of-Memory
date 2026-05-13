# MedMemoryBench: Benchmarking Agent Memory in Personalized Healthcare

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.11814v1
- Published: 2026-05-12
- Updated: 2026-05-12
- Authors: Yihao Wang, Haoran Xu, Renjie Gu, Yixuan Ye, Xinyi Chen, Xinyu Mu, Yuan Gao, Chunxiao Guo, Peng Wei, Jinjie Gu, Huan Li, Ke Chen, Lidan Shou
- Tags: agent, benchmark, conversation, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.11814v1

## One-Sentence Summary
The large-scale deployment of personalized healthcare agents demands memory mechanisms that are exceptionally precise, safe, and capable of long-term clinical tracking.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：The large-scale deployment of personalized healthcare agents demands memory mechanisms that are exceptionally precise, safe, and capable of long-term clinical tracking.

进一步看，论文的核心做法或实验重点可以概括为：However, existing benchmarks primarily focus on daily open-domain conversations, failing to capture the high-stakes complexity of real-world medical applications.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, long-term, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
The large-scale deployment of personalized healthcare agents demands memory mechanisms that are exceptionally precise, safe, and capable of long-term clinical tracking. However, existing benchmarks primarily focus on daily open-domain conversations, failing to capture the high-stakes complexity of real-world medical applications. Motivated by the stringent production requirements of an industry-leading health management agent serving tens of millions of active users, we introduce MedMemoryBench. We develop a human-agent collaborative pipeline to synthesize highly realistic, long-horizon medical trajectories based on clinically grounded, synthetic patient archetypes. This process yields a massive, expertly validated dataset comprising approximately 2,000 sessions and 16,000 interaction turns. Crucially, MedMemoryBench departs from traditional static evaluations by pioneering an "evaluate-while-constructing" streaming assessment protocol, which precisely mirrors dynamic memory accumulation in production environments. Furthermore, we formalize and systematically investigate the critical phenomenon of memory saturation, where sustained information influx actively degrades retrieval and reasoning robustness. Comprehensive benchmarking reveals severe bottlenecks in mainstream architectures, particularly concerning complex medical reasoning and noise resilience. By exposing these fundamental flaws, MedMemoryBench establishes a vital foundation for developing robust, production-ready medical agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
