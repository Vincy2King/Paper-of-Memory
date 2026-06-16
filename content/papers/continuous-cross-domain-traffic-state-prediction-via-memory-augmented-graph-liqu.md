# Continuous Cross-Domain Traffic State Prediction via Memory-Augmented Graph Liquid Time-Constant Networks

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.15807v1
- Published: 2026-06-14
- Updated: 2026-06-14
- Authors: Jinrong Xiang, Ming Xu
- Tags: memory-augmented
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2606.15807v1

## One-Sentence Summary
Traffic state prediction is a fundamental task in intelligent transportation systems.

## Introduction
这篇论文被纳入仓库，是因为它和 `memory-augmented` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Traffic state prediction is a fundamental task in intelligent transportation systems.

进一步看，论文的核心做法或实验重点可以概括为：In practical applications, some regions suffer from limited traffic observations due to insufficient sensing infrastructure, making cross-domain knowledge transfer an important solution for data-scarce traffic...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：memory-augmented
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Traffic state prediction is a fundamental task in intelligent transportation systems. In practical applications, some regions suffer from limited traffic observations due to insufficient sensing infrastructure, making cross-domain knowledge transfer an important solution for data-scarce traffic prediction. However, existing cross-domain traffic prediction methods still face several limitations, including coarse-grained source-target adaptation, limited capability in handling unseen target-domain patterns, and insufficient modeling of continuous traffic dynamics under irregular or heterogeneous temporal conditions. To address these issues, this paper proposes a continuous cross-domain traffic prediction framework, termed Memory-Augmented Graph Liquid Time-Constant Network (MA-GLTC). Specifically, we first construct spatio-temporal units (STUs) to decompose traffic networks into transferable local units, enabling fine-grained knowledge alignment across domains. Then, a graph liquid time-constant network (GLTC) is developed to model graph-coupled traffic evolution in continuous time. Different from generic graph neural ODE-based models, GLTC introduces graph-coupled recurrent conductance into liquid time-constant dynamics, allowing node states to evolve with leakage, adaptive time constants, and neighborhood-aware feedback. Furthermore, a Memory-based Transfer Storage (MTS) mechanism is designed to preserve source-domain knowledge, retrieve matched traffic patterns, and update reliable target-domain patterns when unseen states emerge. Experiments on five public traffic datasets demonstrate that MA-GLTC consistently outperforms representative innerdomain and cross-domain baselines in both short-term and longterm prediction tasks. Compared with the second-best method, MA-GLTC reduces the average prediction errors by 3.02%, 0.33%, 8.92%, 10.09%, and 2.11%, respectively.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
