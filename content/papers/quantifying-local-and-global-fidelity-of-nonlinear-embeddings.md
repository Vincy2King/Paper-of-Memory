# Quantifying Local and Global Fidelity of Nonlinear Embeddings

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.00290v1
- Published: 2026-10-30
- Updated: 2026-10-30
- Authors: Henry Han
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.00290v1

## One-Sentence Summary
Dimension reduction methods are chosen by a common claim: t-SNE and UMAP preserve local structure, and PCA preserves global structure.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Dimension reduction methods are chosen by a common claim: t-SNE and UMAP preserve local structure, and PCA preserves global structure.

进一步看，论文的核心做法或实验重点可以概括为：Checking it on given data takes local and global scores on one scale and a test that compares two maps.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Dimension reduction methods are chosen by a common claim: t-SNE and UMAP preserve local structure, and PCA preserves global structure. Checking it on given data takes local and global scores on one scale and a test that compares two maps. Both scores come from one curve. The locality profile is the chance-corrected share of each point's k nearest neighbors that a map keeps, over all neighborhood sizes. Its value at k = 10 is the local fidelity L, and its mean over 30 to 50 percent of the data is the global fidelity G. We prove that at the midpoint the profile is the agreement on which half of the data is near each point, a rank correlation of the distances. Because L and G are one statistic, two maps can be tested against each other. The LG reversal test applies to any two dimension reduction methods. It decides, with a block-jackknife p-value, whether one map is more local and the other more global, and returns the scale at which to change maps. On 156 maps of twelve datasets with up to 1.38 million points, G agrees with established global scores at 0.89 and 0.96, and 2,000 points estimate it. The test confirms the usual claim on seven datasets. On both retail datasets and both rolled-up manifolds, it finds the neighbor embeddings more global. In an agent memory of one million passages, the two maps cross at 150,000 passages (p = 2.6e-5). Applications span pathology, single cells, supply chains and AI agent memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
