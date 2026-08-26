# Does Episodic Memory Help Close the Lexical Frequency Gap in Sensitivity to Syntactic Contrasts? A Test Using Retrieval-Augmented Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.23851v1
- Published: 2026-08-24
- Updated: 2026-08-24
- Authors: Jing Liu, Najoung Kim
- Tags: episodic, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.23851v1

## One-Sentence Summary
Grammatical knowledge and how it is empirically tested are typically considered robust to the frequency of the lexical items in the expressions.

## Introduction
这篇论文被纳入仓库，是因为它和 `episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Grammatical knowledge and how it is empirically tested are typically considered robust to the frequency of the lexical items in the expressions.

进一步看，论文的核心做法或实验重点可以概括为：However, neural network-based models of grammaticality exhibit high sensitivity to lexical frequency.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：episodic, retrieval
- 检索关键词命中：episodic memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Grammatical knowledge and how it is empirically tested are typically considered robust to the frequency of the lexical items in the expressions. However, neural network-based models of grammaticality exhibit high sensitivity to lexical frequency. We draw upon Complementary Learning Systems theory to test the hypothesis that robustness to lexical frequency can arise via a hippocampal episodic memory mechanism, which enables rapid encoding and retrieval of specific experiences and allows learners to leverage them when processing rare patterns. We use retrieval-augmented language models as an instantiation of such an episodic memory mechanism (specifically, $k$-nearest-neighbor language models that augment parametric models with explicit instance storage), and test whether this augmentation helps close the lexical frequency gap that vanilla language models exhibit in syntactic contrast tests. Using syntactic contrasts with frequency-stratified test items, we find that retrieval augmentation narrows the performance gap between high- and low-frequency items, consistent with episodic memory compensating for weak parametric representations. This benefit is consistent across different syntactic phenomena and across models pretrained on child-realistic and large-scale data. Additionally, we show that structural information is critical for effective retrieval, whereas semantic similarity alone provides little benefit. While these are promising proof-of-concept results supporting our hypothesis, the frequency gap is narrowed rather than fully closed. Based on our analyses, we propose preferential reweighting of retrieved instances, better representations and retrieval strategies for structural information, and flexible configurations of storage and retrieval as promising future directions for improving the implementation of episodic memory in language models.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
