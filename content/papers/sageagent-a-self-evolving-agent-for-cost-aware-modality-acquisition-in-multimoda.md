# SAGEAgent: A Self-Evolving Agent for Cost-Aware Modality Acquisition in Multimodal Survival Prediction

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.09521v1
- Published: 2026-07-10
- Updated: 2026-07-10
- Authors: Chongyu Qu, Can Cui, Zhengyi Lu, Junchao Zhu, Tianyuan Yao, Junlin Guo, Juming Xiong, Yanfan Zhu, Yuechen Yang, Bennett A. Landman, Yuankai Huo
- Tags: agent, episodic
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.09521v1

## One-Sentence Summary
Does every cancer patient truly need a complete diagnostic workup for accurate survival prediction?

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Does every cancer patient truly need a complete diagnostic workup for accurate survival prediction?

进一步看，论文的核心做法或实验重点可以概括为：In multimodal clinical oncology, diagnostic modalities follow a clinically mandated order of escalating burden -- from demographics collected at intake to genomic profiling requiring specialized tissue analysis.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Does every cancer patient truly need a complete diagnostic workup for accurate survival prediction? In multimodal clinical oncology, diagnostic modalities follow a clinically mandated order of escalating burden -- from demographics collected at intake to genomic profiling requiring specialized tissue analysis. Current multimodal survival methods either assume all modalities are available or passively handle missing data, but none actively reason about whether acquiring the next modality is justified for a given patient along this ordered workflow. We formulate this as a sequential decision problem and propose SAGEAgent (Sequential Acquisition Guided by Experience), a self-evolving LLM-based clinical agent that decides which diagnostic modalities to acquire for each patient, balancing predictive accuracy against clinical invasiveness. SAGEAgent reasons about each patient's evolving diagnostic state through clinical tools that translate numerical predictions into text, an episodic memory that retrieves similar past cases, and a semantic memory that accumulates reusable decision patterns from experience. Experiments on a glioma cohort combining TCGA-LGG, TCGA-GBM, and BraTS with four diagnostic modalities demonstrate that SAGEAgent achieves competitive survival prediction accuracy while reducing average acquisition burden by 55%.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
