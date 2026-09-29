# Using LMs to Model the Effects of Context and Coreference during Sentence Comprehension

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.32119v1
- Published: 2026-09-26
- Updated: 2026-09-26
- Authors: Kohei Kajikawa, Lin Ai, Tatsuki Kuribayashi, Ethan Gotlieb Wilcox
- Tags: context
- Categories: cs.CL
- URL: http://arxiv.org/abs/2609.32119v1

## One-Sentence Summary
Language models (LMs) are often used as a tool to model human language processing.

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Language models (LMs) are often used as a tool to model human language processing.

进一步看，论文的核心做法或实验重点可以概括为：Recent studies suggest that severely restricting LMs' context window improves their fit to human psycholinguistic data by simulating human working memory constraints.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：working memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Language models (LMs) are often used as a tool to model human language processing. Recent studies suggest that severely restricting LMs' context window improves their fit to human psycholinguistic data by simulating human working memory constraints. However, it is possible that this strict memory-decay approach overlooks humans' reliance on long-range structural representations, such as discourse structre. In this work, we systematically vary the context window size of GPT-2 across four large-scale naturalistic English reading-time datasets and observe a U-shaped relationship: Although restricted contexts (< 20 tokens) successfully capture local memory limitations, expanded contexts (500--1,000 tokens) ultimately yield the highest overall psycholinguistic fit. To investigate the mechanism driving this benefit, we conduct a counterfactual inference-time experiment that disrupts cross-sentential entity chains by pronominalizing repeated discourse entities. Obscuring these structural linkages significantly degrades the predictive power of larger context windows by 20% to 40%. Our experiments demonstrate that tracking long-range coreference relations is one important factor for the alignment between LM surprisal and human reading behavior, and approximate the extent to which human comprehenders use global discourse relations during language processing.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
