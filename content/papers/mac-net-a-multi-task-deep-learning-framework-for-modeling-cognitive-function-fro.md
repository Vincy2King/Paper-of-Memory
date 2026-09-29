# MAC-Net: A Multi-Task Deep Learning Framework for Modeling Cognitive Function From Task-Based fMRI

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.33440v1
- Published: 2026-09-27
- Updated: 2026-09-27
- Authors: Md. Tanvir Rahman, Nabil Anan Orka, Asaduzzaman Khan, Mohammad Ali Moni
- Tags: benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.33440v1

## One-Sentence Summary
Objective cognitive assessment from neural signals supports neurorehabilitation, but individual-level prediction from task-based fMRI (tfMRI) remains difficult because neural...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Objective cognitive assessment from neural signals supports neurorehabilitation, but individual-level prediction from task-based fMRI (tfMRI) remains difficult because neural features coexist with substantial...

进一步看，论文的核心做法或实验重点可以概括为：We present the Multi-task Activation and Contrast Network (MAC-Net), a covariate-aware deep learning framework for modeling individual cognitive function from regional tfMRI.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：working memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Objective cognitive assessment from neural signals supports neurorehabilitation, but individual-level prediction from task-based fMRI (tfMRI) remains difficult because neural features coexist with substantial demographic and scanner-related variation. We present the Multi-task Activation and Contrast Network (MAC-Net), a covariate-aware deep learning framework for modeling individual cognitive function from regional tfMRI. By isolating tfMRI features into a dedicated neural pathway and restricting participant variables to a terminal late-fusion pathway, MAC-Net prevents dominant covariates from suppressing high-dimensional clinical representations during feature learning. Evaluating baseline data from 6,500 Adolescent Brain Cognitive Development Study participants under family-aware cross-validation, MAC-Net was benchmarked against linear models, random forests, and alternative deep architectures. The N-back plus Monetary Incentive Delay configuration achieved $R^{2}$ values of 0.174, 0.238, and 0.277 for fluid, crystallized, and total cognition, outperforming covariate-only baselines (0.178) and alternative deep models (0.217). N-back was the most informative paradigm, whereas incorporating the Stop Signal Task marginally degraded performance. Feature attributions via Integrated Gradients, DeepLIFT, and Input Gradient were highly concordant, localizing working-memory-related frontal, parietal, and cingulate regions. These findings demonstrate that covariate-aware multi-task modeling yields reproducible cognitive-function estimations, establishing a robust neural engineering framework for clinical translation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
