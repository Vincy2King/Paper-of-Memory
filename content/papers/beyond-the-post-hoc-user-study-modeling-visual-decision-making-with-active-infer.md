# Beyond the Post Hoc User Study: Modeling Visual Decision-Making with Active Inference

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.25131v1
- Published: 2026-07-27
- Updated: 2026-07-27
- Authors: Harrison J. Goldwyn, Graham Johnson, Christopher Ibarra, Lace Padilla, Kenny Gruchalla
- Tags: agent
- Categories: cs.HC, q-bio.NC
- URL: http://arxiv.org/abs/2607.25131v1

## One-Sentence Summary
Empirical user studies are essential for evaluating visual encodings and can reveal perceptual and cognitive mechanisms, but they do not by themselves provide causal, predictive...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Empirical user studies are essential for evaluating visual encodings and can reveal perceptual and cognitive mechanisms, but they do not by themselves provide causal, predictive accounts of interpretation errors.

进一步看，论文的核心做法或实验重点可以概括为：Evaluations are therefore often post hoc: they measure performance after a design has been specified rather than predicting how attention, uncertainty, memory, and bias may produce accurate or erroneous judgments.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：working memory
- 来源分类信息：cs.HC, q-bio.NC

## Abstract Snapshot
Empirical user studies are essential for evaluating visual encodings and can reveal perceptual and cognitive mechanisms, but they do not by themselves provide causal, predictive accounts of interpretation errors. Evaluations are therefore often post hoc: they measure performance after a design has been specified rather than predicting how attention, uncertainty, memory, and bias may produce accurate or erroneous judgments. To address this mechanistic gap, we translate a cognitive theory of visualization interpretation into executable simulation using Active Inference, a probabilistic framework for perception, learning, and action. We model chart reading as dynamic visual search in which agents update beliefs and choose actions that balance uncertainty reduction against cognitive effort. As a proof of concept, we implement Fast, heuristic (Type 1) and Slow, analytic (Type 2) agents for a bar-chart average-estimation task. The Fast agent is vulnerable to tick-salience bias, whereas the Slow agent is more vulnerable to working-memory decay. Both produce inspectable cognitive traces, including evolving belief uncertainty and fixation sequences. By expressing these hypothesized failure mechanisms as interpretable parameters, the architecture provides a framework for formalizing and testing mechanistic hypotheses about visualization interpretation. Empirical studies can then parameterize, refine, or falsify these simulations, supporting earlier and more predictive in silico evaluation of visualization efficacy.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
