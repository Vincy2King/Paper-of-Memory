# PsyMemBehav: Psychology-Informed and Memory-Grounded Two-Level Identity-to-Action Reasoning for Social-Media Behavior Simulation

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.14570v1
- Published: 2026-10-10
- Updated: 2026-10-10
- Authors: Wenji Zhang, Xilong Cheng, Yunxiao Qin, Mai Tu, Tongye Zhu, Yuhao Zhou, JingBo Ji, Yuting Tan, Duoyin Li, Hongjiang Xiao, Yuan Zhang
- Tags: benchmark
- Categories: cs.AI, cs.SI
- URL: http://arxiv.org/abs/2610.14570v1

## One-Sentence Summary
Large language models (LLMs) support social simulation, but faithfully reproducing real users requires grounding both structured platform decisions and language in sparse, noisy...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models (LLMs) support social simulation, but faithfully reproducing real users requires grounding both structured platform decisions and language in sparse, noisy behavioral evidence.

进一步看，论文的核心做法或实验重点可以概括为：We introduce PsyMemBehav, which maps psychology-informed profiles and retrieved memories to target-first platform behavior through two-level identity-to-action reasoning.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.AI, cs.SI

## Abstract Snapshot
Large language models (LLMs) support social simulation, but faithfully reproducing real users requires grounding both structured platform decisions and language in sparse, noisy behavioral evidence. We introduce PsyMemBehav, which maps psychology-informed profiles and retrieved memories to target-first platform behavior through two-level identity-to-action reasoning. To support this approach with comprehensive behavioral traces, we construct a dataset PsyMemBehav-bench from 5.57M observed behaviors of 5,862 real users (approximately 950 per user) across Reddit, Bluesky, and Twitter. Each recorded engagement is modeled as target selection followed by Comment, Like, or Repost and optional response generation. PsyMemBehav combines 41-dimensional user descriptors, top-5 BM25 memories, reverse-CoT supervision, and rubric-guided DPO over complete reasoning-action trajectories. Experiments show that PsyMemBehav 27B ranks first in 11 of 12 reported individual-level metrics, improving average response quality over GPT-5.4 from 54.28 to 59.68 (9.95% relative), and obtains the lowest group-level MAE (0.081) and MSE (0.009) among simulated systems. These results support evidence-grounded user modeling for observed-thread continuation; the benchmark remains conditional on recorded engagement and does not model no-action decisions.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
