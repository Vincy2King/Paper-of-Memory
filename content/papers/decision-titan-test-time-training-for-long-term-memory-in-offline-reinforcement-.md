# Decision Titan: Test-Time Training for Long-Term Memory in Offline Reinforcement Learning

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.01513v1
- Published: 2026-10-01
- Updated: 2026-10-01
- Authors: Jude Waide, Robert Lieck
- Tags: context, episodic, long-term
- Categories: cs.AI, cs.LG
- URL: http://arxiv.org/abs/2610.01513v1

## One-Sentence Summary
Long-term dependencies remain a major challenge for sequential decision-making in the field of AI: RNNs suffer from vanishing gradients and the limited expressivity of vector-...

## Introduction
这篇论文被纳入仓库，是因为它和 `context, episodic, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term dependencies remain a major challenge for sequential decision-making in the field of AI: RNNs suffer from vanishing gradients and the limited expressivity of vector-based hidden states, whilst Transformer-...

进一步看，论文的核心做法或实验重点可以概括为：Recent work has proposed tackling this problem with the Test-Time Training (TTT) framework, which stores episodic memories in the parameters of a neural network through gradient descent at both train and test-time.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, episodic, long-term
- 检索关键词命中：episodic memory, long-term memory
- 来源分类信息：cs.AI, cs.LG

## Abstract Snapshot
Long-term dependencies remain a major challenge for sequential decision-making in the field of AI: RNNs suffer from vanishing gradients and the limited expressivity of vector-based hidden states, whilst Transformer-based models are limited by the quadratic scaling of attention. Recent work has proposed tackling this problem with the Test-Time Training (TTT) framework, which stores episodic memories in the parameters of a neural network through gradient descent at both train and test-time. This approach has seen success in the domain of Natural Language Processing, however, to the best of our knowledge it has not yet been applied to the domain of Reinforcement Learning (RL), nor has there been a study analysing how this memory practically functions. In this paper, we study the potential of the TTT framework for offline RL by augmenting a Decision Transformer with TTT layers, dubbed the Decision Titan. We analyse performance and properties of the model in the X-Maze environment, an extension of T-Maze designed to test sequential memory, and investigate how the memory mechanism learns by visualising gate values over time. Our key findings are that Decision Titan can learn long-term dependencies with ranges 20x longer than the context window, generalises to lengths 1.7x the training data, but crucially temporal generalisation depends on the time embeddings used, and the ability to learn long-term dependencies depends on how the relevant information is encoded.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
