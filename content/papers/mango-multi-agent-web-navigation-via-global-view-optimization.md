# Mango: Multi-Agent Web Navigation via Global-View Optimization

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.18779v1
- Published: 2026-04-20
- Updated: 2026-04-20
- Authors: Weixi Tong, Yifeng Di, Tianyi Zhang
- Tags: agent, episodic
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2604.18779v1

## One-Sentence Summary
Existing web agents typically initiate exploration from the root URL, which is inefficient for complex websites with deep hierarchical structures.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Existing web agents typically initiate exploration from the root URL, which is inefficient for complex websites with deep hierarchical structures.

进一步看，论文的核心做法或实验重点可以概括为：Without a global view of the website's structure, agents frequently fall into navigation traps, explore irrelevant branches, or fail to reach target information within a limited budget.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Existing web agents typically initiate exploration from the root URL, which is inefficient for complex websites with deep hierarchical structures. Without a global view of the website's structure, agents frequently fall into navigation traps, explore irrelevant branches, or fail to reach target information within a limited budget. We propose Mango, a multi-agent web navigation method that leverages the website structure to dynamically determine optimal starting points. We formulate URL selection as a multi-armed bandit problem and employ Thompson Sampling to adaptively allocate the navigation budget across candidate URLs. Furthermore, we introduce an episodic memory component to store navigation history, enabling the agent to learn from previous attempts. Experiments on WebVoyager demonstrate that Mango achieves a success rate of 63.6% when using GPT-5-mini, outperforming the best baseline by 7.3%. Furthermore, on WebWalkerQA, Mango attains a 52.5% success rate, surpassing the best baseline by 26.8%. We also demonstrate the generalizability of Mango using both open-source and closed-source models as backbones. Our data and code are open-source and available at https://github.com/VichyTong/Mango.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
