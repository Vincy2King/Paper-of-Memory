# A single inference process underlies the behavior and neural circuits of working memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.22054v1
- Published: 2026-11-17
- Updated: 2026-11-17
- Authors: Dongyu Gong, Mario Belledonne, Ilker Yildirim
- Tags: working memory
- Categories: q-bio.NC, cs.LG
- URL: http://arxiv.org/abs/2611.22054v1

## One-Sentence Summary
Working memory holds past inputs online for future behavior.

## Introduction
这篇论文被纳入仓库，是因为它和 `working memory` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Working memory holds past inputs online for future behavior.

进一步看，论文的核心做法或实验重点可以概括为：Despite decades of research, accounts of working memory remain divided across levels of analysis, with long-standing debates on whether its capacity reflects discrete slots or continuous resources, how attention...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：working memory
- 检索关键词命中：working memory
- 来源分类信息：q-bio.NC, cs.LG

## Abstract Snapshot
Working memory holds past inputs online for future behavior. Despite decades of research, accounts of working memory remain divided across levels of analysis, with long-standing debates on whether its capacity reflects discrete slots or continuous resources, how attention improves recall, and whether its representations rely on persistent neural firing or activity-silent states. Here we show that MemGP, a theory that is specified at the computational, algorithmic, and circuit levels of analysis simultaneously, can explain diverse behavioral and neural phenomena in working memory. At the computational level, MemGP casts working memory as probabilistic inference over a continuous function on feature space, with a variational objective that balances memory strength against a Gaussian-process prior. At the algorithmic level, writing, storing, and reading of memories correspond to approximating this posterior with a finite set of inducing points, the resource that all items share. In simulations, MemGP reproduces load-dependent precision loss, attentional benefits during maintenance, and inter-item attraction and repulsion, in each case revealing multiple complex computational dependencies. At the circuit level, the algorithm analytically (without training) maps onto a recurrent circuit, including its architecture and dynamics. Beyond reproducing neural phenomena such as delay-dependent drift, this analytical map deduces center--surround connectivity, a property long assumed in attractor models, and a structured combination of persistent activity and synaptic weights to hold memories. Thus, a single inference objective not only jointly predicts the behavioral and neural signatures of working memory, but also addresses, across several instances and different levels of analysis, existing competing explanations.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
