# What Must Generalist Agents Remember?

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.18746v1
- Published: 2026-06-17
- Updated: 2026-06-17
- Authors: Khurram Yamin, Namrata Deka, Maitreyi Swaroop, Albert Ting, Jeff Schneider, Bryan Wilder
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.18746v1

## One-Sentence Summary
This paper develops a formal account of what generalist agents must store in memory in order to act near-optimally across multiple environments and goals.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：This paper develops a formal account of what generalist agents must store in memory in order to act near-optimally across multiple environments and goals.

进一步看，论文的核心做法或实验重点可以概括为：It shows that when two domains share an observational bottleneck but require incompatible optimal actions, any uniformly near-optimal policy must induce distinct memory distributions at that bottleneck.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
This paper develops a formal account of what generalist agents must store in memory in order to act near-optimally across multiple environments and goals. It shows that when two domains share an observational bottleneck but require incompatible optimal actions, any uniformly near-optimal policy must induce distinct memory distributions at that bottleneck. The result yields a separation theorem: sufficiently successful agents cannot rely only on current state observations, but must preserve domain-relevant information in memory. The paper further shows that if an agent's memory contains enough information to estimate values for related goals, then that memory can be used to approximately reconstruct the agent's local transition dynamics. Together, these results characterize memory as the substrate that supports domain disambiguation, transition-model reconstruction, and planning for generalist agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
