# Step-Level Preference Learning for Generative Agents in Social Simulations

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.14485v1
- Published: 2026-07-16
- Updated: 2026-07-16
- Authors: Wenchang Gao, Pingyue Sheng, Lanlan Qiu, Yunfei Ma, Jian Zhao, Baicheng Chen, Kangda Wang, Yuyang Tian, Shunqiang Mao, Tianxing He
- Tags: agent, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.14485v1

## One-Sentence Summary
Large language model (LLM)-based generative agents simulate human behavior through long-horizon decision-making processes that comprise intermediate steps such as planning,...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM)-based generative agents simulate human behavior through long-horizon decision-making processes that comprise intermediate steps such as planning, memory retrieval, reflection, and action...

进一步看，论文的核心做法或实验重点可以概括为：However, fine-grained human annotations of these intermediate steps remain scarce, and existing agents are not grounded in human preferences over such intermediate decisions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language model (LLM)-based generative agents simulate human behavior through long-horizon decision-making processes that comprise intermediate steps such as planning, memory retrieval, reflection, and action selection. However, fine-grained human annotations of these intermediate steps remain scarce, and existing agents are not grounded in human preferences over such intermediate decisions. To address this gap, we introduce \method, an interactive simulation interface that enables us to collect step-level human preference supervision over agent decision trajectories, leading to a dataset of 57K fine-grained annotations. We conduct step-level preference learning on open-weight language models using supervised finetuning and direct preference optimization on this data, consistently improving simulation fidelity, coordination, and interaction quality, and inducing more socially effective agent behavior. Our results show that step-level human supervision is an effective training signal for improving both local decision quality and long-horizon agent behavior.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
