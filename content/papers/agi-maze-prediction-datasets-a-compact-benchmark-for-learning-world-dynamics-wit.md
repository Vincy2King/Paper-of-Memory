# AGI Maze Prediction Datasets: A Compact Benchmark for Learning World Dynamics with Transformers

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.02339v1
- Published: 2026-09-02
- Updated: 2026-09-02
- Authors: Alexey Potapov
- Tags: benchmark
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2609.02339v1

## One-Sentence Summary
World modeling requires a predictive model to maintain and update an internal state adequate for reasoning about the consequences of actions.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：World modeling requires a predictive model to maintain and update an internal state adequate for reasoning about the consequences of actions.

进一步看，论文的核心做法或实验重点可以概括为：We introduce the AGI Maze Prediction Datasets and Benchmark, a lightweight controlled testbed for studying this capability in Transformers and other predictive models.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：memory augmented, memory-augmented, working memory
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
World modeling requires a predictive model to maintain and update an internal state adequate for reasoning about the consequences of actions. We introduce the AGI Maze Prediction Datasets and Benchmark, a lightweight controlled testbed for studying this capability in Transformers and other predictive models. Derived from procedurally generated, stateful grid worlds, the benchmark comprises per-step transition prediction, fixed-horizon state prediction, and sequential textual-observation prediction. Source-maze-disjoint training and validation splits, together with greedy exact-match evaluation, distinguish learning transferable action-conditioned dynamics from memorizing transitions in familiar layouts. We establish from-scratch byte-level Transformer baselines and compare them with two working-memory-augmented architectures. A generic auxiliary latent-memory Transformer can fit some training sets perfectly but does not consistently improve held-out performance. In contrast, a pseudo-video spatial-memory Transformer initializes a two-dimensional latent workspace from the input map and updates it from action history without receiving intermediate maps, positions, or state labels. Under the same data, objectives, and evaluation protocol, this model reaches perfect validation accuracy on selected fixed-horizon tasks where the byte and unstructured-memory baselines do not, and substantially improves sequential text-trace prediction. These results suggest that structured, task-aligned working memory can be more useful than additional latent capacity alone. More broadly, we argue that language grounding is mediated by persistent data structures and computations over them; the benchmark offers a compact setting for testing architectures that couple textual interfaces to learned structured state.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
