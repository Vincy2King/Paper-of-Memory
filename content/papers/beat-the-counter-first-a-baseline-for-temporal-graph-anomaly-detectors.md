# Beat the Counter First: A Baseline for Temporal-Graph Anomaly Detectors

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.15965v1
- Published: 2026-08-16
- Updated: 2026-08-16
- Authors: Omair Shafi Ahmed, Zohair Shafi
- Tags: memory-augmented
- Categories: cs.LG
- URL: http://arxiv.org/abs/2608.15965v1

## One-Sentence Summary
Progress in streaming, edge-level graph anomaly detection (GAD) has been marked by increasingly elaborate architectures, from count-min-sketch chi square tests to memory-...

## Introduction
这篇论文被纳入仓库，是因为它和 `memory-augmented` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Progress in streaming, edge-level graph anomaly detection (GAD) has been marked by increasingly elaborate architectures, from count-min-sketch chi square tests to memory-augmented attention networks.

进一步看，论文的核心做法或实验重点可以概括为：Yet the empirical gains attributable to this added complexity have not been systematically evaluated.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：memory-augmented
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.LG

## Abstract Snapshot
Progress in streaming, edge-level graph anomaly detection (GAD) has been marked by increasingly elaborate architectures, from count-min-sketch chi square tests to memory-augmented attention networks. Yet the empirical gains attributable to this added complexity have not been systematically evaluated. We propose SimpleCount, a reference with no parameter fitting that selects one scalar feature per dataset from a fixed pool of counts, recencies, first-occurrence indicators, and count-derived transforms. We compare SimpleCount with two temporal-graph detector models and an IsoForest control fitted to the complete feature vector across five public datasets and one synthetic dataset. SimpleCount matches or exceeds SLADE on three of six datasets and exceeds IsoForest on all six. We report paired statistical tests and five-seed SLADE evaluations. SLADE requires 23 to 133x more wall-clock time than SimpleCount. On Synth-Triangle and an additional Synth-Quad probe, pre-event structural scores recover the planted signal at AUC up to 0.955, while all evaluated detector models remain near random. The benefit of complexity is dataset-dependent, and every claimed gain should be reported against a strong one-feature reference together with its compute cost.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
