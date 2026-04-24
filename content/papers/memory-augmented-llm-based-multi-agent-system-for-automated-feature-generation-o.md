# Memory-Augmented LLM-based Multi-Agent System for Automated Feature Generation on Tabular Data

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.20261v1
- Published: 2026-04-22
- Updated: 2026-04-22
- Authors: Fengxian Dong, Zhi Zheng, Xiao Han, Wei Chen, Jingqing Ruan, Tong Xu, Yong Chen, Enhong Chen
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2604.20261v1

## One-Sentence Summary
Automated feature generation extracts informative features from raw tabular data without manual intervention and is crucial for accurate, generalizable machine learning.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Automated feature generation extracts informative features from raw tabular data without manual intervention and is crucial for accurate, generalizable machine learning.

进一步看，论文的核心做法或实验重点可以概括为：Traditional methods rely on predefined operator libraries and cannot leverage task semantics, limiting their ability to produce diverse, high-value features for complex tasks.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Automated feature generation extracts informative features from raw tabular data without manual intervention and is crucial for accurate, generalizable machine learning. Traditional methods rely on predefined operator libraries and cannot leverage task semantics, limiting their ability to produce diverse, high-value features for complex tasks. Recent Large Language Model (LLM)-based approaches introduce richer semantic signals, but still suffer from a restricted feature space due to fixed generation patterns and from the absence of feedback from the learning objective. To address these challenges, we propose a Memory-Augmented LLM-based Multi-Agent System (\textbf{MALMAS}) for automated feature generation. MALMAS decomposes the generation process into agents with distinct responsibilities, and a Router Agent activates an appropriate subset of agents per iteration, further broadening exploration of the feature space. We further integrate a memory module comprising procedural memory, feedback memory, and conceptual memory, enabling iterative refinement that adaptively guides subsequent feature generation and improves feature quality and diversity. Extensive experiments on multiple public datasets against state-of-the-art baselines demonstrate the effectiveness of our approach. The code is available at https://github.com/fxdong24/MALMAS

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
