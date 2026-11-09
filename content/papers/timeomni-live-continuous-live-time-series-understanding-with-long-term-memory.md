# TimeOmni-Live: Continuous & Live Time Series Understanding with Long-Term Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.09502v1
- Published: 2026-11-06
- Updated: 2026-11-06
- Authors: Tong Guan, Alexander Chemeris, Yiqing Guo, Warren Jin, Zhao Li, Shirui Pan, Ming Jin
- Tags: context, long-term
- Categories: cs.LG
- URL: http://arxiv.org/abs/2611.09502v1

## One-Sentence Summary
Existing time series language models predominantly follow an offline, one-shot paradigm: they process fixed-length inputs independently and do not retain past states.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Existing time series language models predominantly follow an offline, one-shot paradigm: they process fixed-length inputs independently and do not retain past states.

进一步看，论文的核心做法或实验重点可以概括为：This static approach fundamentally misaligns with the continuous nature of real-world streaming applications and fails to maintain the historical context necessary for cross-window reasoning.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Existing time series language models predominantly follow an offline, one-shot paradigm: they process fixed-length inputs independently and do not retain past states. This static approach fundamentally misaligns with the continuous nature of real-world streaming applications and fails to maintain the historical context necessary for cross-window reasoning. To bridge this gap, we introduce Continuous & Live Time Series Understanding (CL-TSU), a novel paradigm that shifts the focus toward maintaining a persistent, stateful understanding over open-ended data streams. To systematically evaluate this paradigm, we present LiveTS-Suite, the first comprehensive data suite tailored for CL-TSU, supporting data generation, model training, and systematic evaluation across 18 tasks spanning six core capabilities. It comprises over 5K streams totaling 2.2B timesteps, annotated with 15K specific response events. We further design an evaluation protocol that jointly assesses response timeliness, content accuracy, and computational efficiency. Building on this foundation, we propose TimeOmni-Live, the first live time series understanding model. It integrates a hybrid time series encoding for natively temporal input, a stream-persistent hybrid memory mechanism to effectively preserve exact historical evidence and long-term task states, and an elastic stream-inference synchronization strategy to reduce processing lag. Evaluations show that TimeOmni-Live establishes a strong baseline for CL-TSU, outperforming frontier LLMs (90.0 vs. 79.3 for Opus 5) with only 4B parameters and achieving 206$\times$ lower p95 latency than its backbone. Deployment on a Jetson edge device further shows its ability to support real-time continuous temporal understanding locally at the edge.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
