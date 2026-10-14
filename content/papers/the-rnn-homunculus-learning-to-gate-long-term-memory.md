# The RNN Homunculus: Learning to Gate Long-Term Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.14279v1
- Published: 2026-10-09
- Updated: 2026-10-09
- Authors: Zeyu Fan, Alexandru-Dragos Manolache, Jan van Gemert
- Tags: long-term
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2610.14279v1

## One-Sentence Summary
Learning long-range dependencies with recurrent neural networks (RNNs) is difficult because of the vanishing gradient problem.

## Introduction
这篇论文被纳入仓库，是因为它和 `long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Learning long-range dependencies with recurrent neural networks (RNNs) is difficult because of the vanishing gradient problem.

进一步看，论文的核心做法或实验重点可以概括为：Gated recurrent neural networks like GRUs and LSTMs address this problem and are commonly explained by their ability to create additive copy paths through time.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Learning long-range dependencies with recurrent neural networks (RNNs) is difficult because of the vanishing gradient problem. Gated recurrent neural networks like GRUs and LSTMs address this problem and are commonly explained by their ability to create additive copy paths through time. This explanation is correct, but incomplete: useful RNN gate values must themselves be learned, which is typically done with another RNN. We study this gate-learning problem through carefully controlled sequence classification tasks. Our analysis shows that gated architectures struggle when all training samples require long-range memory and thus equally suffer from the vanishing gradient problem. We intervene by adding short-dependency samples which let gated models learn solutions that capture long-dependency samples, but also generalize across different class labels. When properly learned, gated RNNs match or even exceed the test accuracy of modern architectures like Mamba and xLSTM. Overall, our results highlight gate learning as a central part of learning long-range memory and show how training data can support this process by exposing the same task over shorter dependencies.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
