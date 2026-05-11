# Graph-Structured Hyperdimensional Computing for Data-Efficient and Explainable Process-Structure-Property Prediction

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.07999v1
- Published: 2026-05-08
- Updated: 2026-05-08
- Authors: Jingzhan Ge, Ajeeth Vellore, Ajinkya Palwe, Ahsan Khan, David Gorsich, Matthew P. Castanier, SeungYeon Kang, Farhad Imani
- Tags: retrieval
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2605.07999v1

## One-Sentence Summary
Multiphoton photoreduction enables high-fidelity fabrication of complex 3D microstructures, yet reliable process-structure-property (PSP) prediction remains difficult because...

## Introduction
这篇论文被纳入仓库，是因为它和 `retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multiphoton photoreduction enables high-fidelity fabrication of complex 3D microstructures, yet reliable process-structure-property (PSP) prediction remains difficult because the available data are sparse,...

进一步看，论文的核心做法或实验重点可以概括为：In this regime, conventional feature-vector models are statistically underdetermined, making them prone to spurious correlations, poor regime transfer, and unstable post hoc explanations, whereas mechanistic pipelines...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Multiphoton photoreduction enables high-fidelity fabrication of complex 3D microstructures, yet reliable process-structure-property (PSP) prediction remains difficult because the available data are sparse, heterogeneous, and interaction-dominated. In this regime, conventional feature-vector models are statistically underdetermined, making them prone to spurious correlations, poor regime transfer, and unstable post hoc explanations, whereas mechanistic pipelines depend on calibrated submodels that are rarely available during early process development. We present PSP-HDC, a graph-structured hyperdimensional computing framework that encodes a directed PSP graph as an internal prior for representation, inference, and explanation. A trainable scalar-to-hypervector encoder learns parameter-specific embeddings on a fixed hyperdimensional basis to accommodate heterogeneous scales and noise. Sample representations are then composed through graph-aligned binding and bundling along directed PSP dependencies, and prediction is performed by associative-memory retrieval against class prototypes. Because the same prototype memories support both decision making and attribution, PSP-HDC provides intrinsic explanations at the parameter, group, and within-group levels, while memory alignment and separation quantify prototype formation during training. On sheet-resistance regime prediction for the 3D platform, PSP-HDC achieves an accuracy of 0.910 +/- 0.077 over 1000 random splits and 0.896 under process-fold generalization, outperforming strong baselines.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
