# Metis: Memory Foundation Model

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.26760v1
- Published: 2026-07-29
- Updated: 2026-07-29
- Authors: Zeyu Zhang, Ziliang Guo, Yihang Sun, Xichong Zhang, Xixuan Hao, Zehao Lin, Yang Zhang, Xiaoyan Zhao, Tong Shen, Bo Tang, Zhi-Qin John Xu, Junchi Yan, Haofen Wang, Xu Chen, Feiyu Xiong, Zhiyu Li, Tat-Seng Chua
- Tags: agent
- Categories: cs.CL, cs.LG
- URL: http://arxiv.org/abs/2607.26760v1

## One-Sentence Summary
Recent advances in AI agents have increasingly internalized native capabilities into their underlying foundation models, giving rise to multimodal foundation models and large...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recent advances in AI agents have increasingly internalized native capabilities into their underlying foundation models, giving rise to multimodal foundation models and large reasoning models.

进一步看，论文的核心做法或实验重点可以概括为：However, agent memory is still primarily implemented through external modules, leaving the native memory capability largely unexplored.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL, cs.LG

## Abstract Snapshot
Recent advances in AI agents have increasingly internalized native capabilities into their underlying foundation models, giving rise to multimodal foundation models and large reasoning models. However, agent memory is still primarily implemented through external modules, leaving the native memory capability largely unexplored. In this paper, we take a first step toward this direction by introducing memory foundation models, which empower foundation models with native memory capabilities. We formalize native memory from two perspectives: a persistent and dynamically evolving memory state within the backbone, and native memory procedures that autonomously store and utilize information through model computation. We show that native memory offers advantages in architecture, end-to-end optimization, and efficiency. Based on this formulation, we propose Metis, the first prototype of memory foundation models. Metis introduces a new architecture that equips a foundation model with a native memory state, allowing historical information to be compressed into the model and accessed through memory attention. We construct large-scale memory-specific training data and introduce multiple optimization objectives to acquire these native memory procedures through mid-training. The online memory maintenance of Metis is gradient-free, and the memory update requires only a forward pass. At inference time, all learned model weights remain frozen, while the native memory states are autonomously transformed through standard forward computation. Through extensive experiments, we show that Metis exhibits native memory capabilities and further provide a detailed analysis of its strengths, limitations, and behaviors. To facilitate future research on memory foundation models, we release our project and model checkpoints.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
