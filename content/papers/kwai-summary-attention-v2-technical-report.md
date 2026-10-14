# Kwai Summary Attention V2 Technical Report

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.18654v1
- Published: 2026-10-13
- Updated: 2026-10-13
- Authors: OneRec Team, Chenglong Chu, Guohong Mu, Guowang Zhang, Hao Peng, Hui Wang, Jian Liang, Jiangxia Cao, Jiao Ou, Jiaxin Deng, Lu Ren, Muhao Wei, Ruiming Tang, Tianle Xu, Wenwu Ou, Xingmei Wang, Zhixin Ling, Zhiyuan Liang, Ziqi Wang, Chaoyi Ma, Haixiao Gao, Kuo Cai, Renpu Liu, Ruochen Yang, Wenlong Xu, Xinqi Jin, Yan Sun, Yifan Wang, Yingzhi He, Yiyu Wang, Yusen Huo, Zhaojie Liu, Zihan Zhou
- Tags: compression, context
- Categories: cs.LG, cs.AI, cs.IR
- URL: http://arxiv.org/abs/2610.18654v1

## One-Sentence Summary
Summary-token architectures such as Kwai Summary Attention (KSA) compress distant context into learnable Summary token per chunk, and hybrid variants interleave these layers...

## Introduction
这篇论文被纳入仓库，是因为它和 `compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Summary-token architectures such as Kwai Summary Attention (KSA) compress distant context into learnable Summary token per chunk, and hybrid variants interleave these layers with full attention to retain exact access...

进一步看，论文的核心做法或实验重点可以概括为：In such hybrid KSA-Full architecture, the interleaving inserted summary tokens are served as a streaming flow role across different layers.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression, context
- 检索关键词命中：memory compression
- 来源分类信息：cs.LG, cs.AI, cs.IR

## Abstract Snapshot
Summary-token architectures such as Kwai Summary Attention (KSA) compress distant context into learnable Summary token per chunk, and hybrid variants interleave these layers with full attention to retain exact access to the original text. In such hybrid KSA-Full architecture, the interleaving inserted summary tokens are served as a streaming flow role across different layers. Although effective, however, it also introduce some bottlenecks: (1) the different layers summary compression chunk must be same, therefore hard to reach a flexible KV Cache compression, e.g., different layer set different summary compression chunk window. (2) in the full-attention layers, the summary token introduced additional computation cost, but such layer ignore them and still pay quadratic prefilling, therefore unfriendly to the computation side. Motivated by them, we developed the KSA V2, which not only achieves a more flexible KV cache memory compression but also reduces the computation cost in Full attention layer. Specifically, we found that the summary tokens can serve two roles: the KV memory and sparse indexer.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
