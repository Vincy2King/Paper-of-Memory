# Interpreting Quantum Learning Models via Stochastic Processes

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.17327v1
- Published: 2026-07-19
- Updated: 2026-07-19
- Authors: Johannes Fankhauser, Lukas J. Fiderer, Hans J. Briegel
- Tags: episodic
- Categories: quant-ph, cs.LG
- URL: http://arxiv.org/abs/2607.17327v1

## One-Sentence Summary
Quantum machine learning models define probabilistic input--output maps through coherent quantum evolution and measurement.

## Introduction
这篇论文被纳入仓库，是因为它和 `episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Quantum machine learning models define probabilistic input--output maps through coherent quantum evolution and measurement.

进一步看，论文的核心做法或实验重点可以概括为：While such models can exhibit computational advantages, their internal functioning and decision making generally resists interpretation in terms of stochastic trajectories through intermediate configurations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：episodic
- 检索关键词命中：episodic memory
- 来源分类信息：quant-ph, cs.LG

## Abstract Snapshot
Quantum machine learning models define probabilistic input--output maps through coherent quantum evolution and measurement. While such models can exhibit computational advantages, their internal functioning and decision making generally resists interpretation in terms of stochastic trajectories through intermediate configurations. In contrast to classical (Markovian) stochastic processes, quantum dynamics generically violates the Chapman--Kolmogorov divisibility condition, preventing a decomposition into probabilistically meaningful intermediate transitions. We develop a probabilistic framework for representing quantum learning models as stochastic processes over configuration spaces where the dynamics are modeled as linear maps on probability distributions. Starting from a fixed POVM, arbitrary quantum channels induce transition kernels on the associated probability representation. For informationally complete POVMs, and in particular SIC-POVMs, these kernels are Markovian but generally quasi-stochastic, with non-classicality appearing as negativity. By contrast, projective spaces admit positive stochastic kernels but generally require non-Markovian dynamics due to the failure of Chapman--Kolmogorov divisibility. This yields a trade-off between negativity and dependence on past configurations, i.e. quantum dynamics can be represented either by Markovian quasi-stochastic maps or by positive stochastic processes with higher Markov order. We discuss how such representations of quantum dynamics can be interpreted as stochastic walks through a memory space in the spirit of Projective Simulation, a model of learning and agency in which decisions arise from random walks over an episodic memory network. We further outline how finite-order stochastic kernels can approximate such quantum deliberation processes and show in what regimes the classical machine learning model is recovered.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
