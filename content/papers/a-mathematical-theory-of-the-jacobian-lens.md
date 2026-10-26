# A Mathematical Theory of the Jacobian Lens

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.31955v1
- Published: 2026-10-22
- Updated: 2026-10-22
- Authors: Mitchell Ostrow, Daoyuan Qian, Toni Liu, Ila Fiete
- Tags: context
- Categories: cs.LG, cs.AI, q-bio.NC
- URL: http://arxiv.org/abs/2610.31955v1

## One-Sentence Summary
Recent work from Anthropic introduced a new interpretability tool, called the Jacobian lens (J-lens, Gurnee et al., 2026).

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recent work from Anthropic introduced a new interpretability tool, called the Jacobian lens (J-lens, Gurnee et al., 2026).

进一步看，论文的核心做法或实验重点可以概括为：This method identified linear directions in the hidden states of frontier language models that had properties reminiscent of working memory-like representations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：working memory
- 来源分类信息：cs.LG, cs.AI, q-bio.NC

## Abstract Snapshot
Recent work from Anthropic introduced a new interpretability tool, called the Jacobian lens (J-lens, Gurnee et al., 2026). This method identified linear directions in the hidden states of frontier language models that had properties reminiscent of working memory-like representations. However, it is unclear what mechanistic properties of such features make them detectable to the J-lens. To this end, we introduce a mathematical theory of the J-lens, and show that it preferentially identifies coherent features -- directions that act like leading, spatially coherent Lyapunov modes. Small perturbations along these directions amplify across layers, remain roughly constant across token positions, and are consistent across different contexts. While we are agnostic to whether these properties are necessarily associated with a ``Global Workspace'', the analytically derived preferences of the J-lens nevertheless explain prior empirical applied to both model classes. We validate our analysis on a Bayes filter and a toy transformer, each optimally predicting next tokens emitted from a Hidden Markov Model (HMM). We show how modulating task parameters that change the coherence of features in the Bayes filter correspondingly and predictively modulates the response of the J-lens . We also introduce of a family of J-lenses built to emphasize different temporal scales of information processing in LLMs, which we call $ω$-J-lenses.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
