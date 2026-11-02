# RAMA: Retrieval-Augmented Multi-Agent Routing with Episodic Memory for LEO Satellite Networks

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.42068v1
- Published: 2026-10-30
- Updated: 2026-10-30
- Authors: Xin Ming Li, Peng Hu
- Tags: agent, episodic, retrieval
- Categories: cs.NI, cs.LG
- URL: http://arxiv.org/abs/2610.42068v1

## One-Sentence Summary
Low-Earth orbit (LEO) satellite networks present a challenging routing environment due to rapidly changing topology, traffic, and link conditions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Low-Earth orbit (LEO) satellite networks present a challenging routing environment due to rapidly changing topology, traffic, and link conditions.

进一步看，论文的核心做法或实验重点可以概括为：Existing deep reinforcement learning (DRL) routing methods typically rely on current observations and information encoded in network weights, limiting their ability to exploit successful past experiences.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, episodic, retrieval
- 检索关键词命中：episodic memory, memory retrieval
- 来源分类信息：cs.NI, cs.LG

## Abstract Snapshot
Low-Earth orbit (LEO) satellite networks present a challenging routing environment due to rapidly changing topology, traffic, and link conditions. Existing deep reinforcement learning (DRL) routing methods typically rely on current observations and information encoded in network weights, limiting their ability to exploit successful past experiences. We propose RAMA, a retrieval-augmented multi-agent DRL framework with Approximate Information State (AIS), in which each satellite combines its local observation, recent routing history, neighboring state information, and retrieved entries from a per-satellite episodic memory. Retrieved experiences are integrated through a Transformer-based decision network trained with AIS-based auxiliary objectives. With weights frozen in a 140-satellite Kepler constellation, RAMA reduces mean end-to-end latency by 13.4% and 99th-percentile latency by 66.7% relative to the state-of-theart double deep Q-network (DDQN) routing method, mainly by avoiding long detours. Updated online, RAMA remains stable while DDQN degrades. On the 1,584-satellite Starlink shell 1, the reduction in mean latency grows to 93.2%, and updating RAMA online lowers its mean latency by a further 25.5%. These results demonstrate the effectiveness of retrieval-augmented memory for scalable decentralized routing in LEO satellite networks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
