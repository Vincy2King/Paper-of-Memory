# Autonomous heterogeneous catalyst discovery with a self-evolving multi-agent digital twin

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.05050v1
- Published: 2026-06-03
- Updated: 2026-06-03
- Authors: Zhilong Song, Zongmin Zhang, Lixue Cheng
- Tags: agent, benchmark
- Categories: cond-mat.mtrl-sci, cs.AI, physics.chem-ph
- URL: http://arxiv.org/abs/2606.05050v1

## One-Sentence Summary
Theoretical heterogeneous catalysis promises rapid catalyst discovery, yet computational and machine-learning predictions often deviate from experiment and stay confined to...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Theoretical heterogeneous catalysis promises rapid catalyst discovery, yet computational and machine-learning predictions often deviate from experiment and stay confined to narrow material families, for want of a...

进一步看，论文的核心做法或实验重点可以概括为：We present CatDT (Catalysis Digital Twin), a self-evolving multi-agent system that builds an autonomous digital twin of a working catalyst, unifying gas-solid and liquid-solid modeling.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：memory augmented, memory-augmented, persistent memory
- 来源分类信息：cond-mat.mtrl-sci, cs.AI, physics.chem-ph

## Abstract Snapshot
Theoretical heterogeneous catalysis promises rapid catalyst discovery, yet computational and machine-learning predictions often deviate from experiment and stay confined to narrow material families, for want of a faithful, condition-aware catalytic simulator. We present CatDT (Catalysis Digital Twin), a self-evolving multi-agent system that builds an autonomous digital twin of a working catalyst, unifying gas-solid and liquid-solid modeling. From only a bulk crystal and a natural-language reaction description, eight specialized agents and 27 scientific tools predict stable facets, reconstruct working surfaces, enumerate and rank reaction pathways, locate transition states, and compute kinetics in 5-30 min on a single GPU. Two innovations address the hardest steps: UniMech finds dominant pathways for novel materials at over $10^3\times$ lower cost than exhaustive enumeration by fusing agent-guided proposals with energy-cached graph search, and a memory-augmented reinforcement loop raises barrier-calculation success from 41\% to 84\% across 600 catalytic surfaces. Across seven gas-solid benchmarks -- stepped metals, single-atom catalysts, ordered intermetallics, vacancy-rich 2D sulfides and carbides, and a strong-metal--support-interaction (SMSI) interface -- every CatDT prediction lies within 0.5-2 times experiment over four orders of magnitude. For propane dehydrogenation, CatDT independently discovers non-precious candidates rivaling the Pt-based industrial benchmark, with a proposed Ni@ZrO$_2$ SMSI overlayer reaching a simulated TOF of $1.63~\text{s}^{-1}$ at $\sim$100\% selectivity. More broadly, the decisive factor for a faithful catalyst digital twin -- or any multi-stage scientific simulator -- is not raw LLM capability but the engineered harness around it: deterministic tools, persistent memory, and verified self-improvement that compound across models, tools, and runs.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
