# MUON-RT Reusing the Teacher's Trajectory for Momentum-Free Muon for LLM Self-Distillation

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.41104v1
- Published: 2026-10-30
- Updated: 2026-10-30
- Authors: Aryan Das, Vinay Kumar Verma, Aakansha Mishra
- Tags: persistent memory
- Categories: cs.LG, cs.AI, cs.CL, stat.ML
- URL: http://arxiv.org/abs/2610.41104v1

## One-Sentence Summary
Self-distillation methods for large language models with an exponential moving average (EMA) teacher already retain a history of student updates.

## Introduction
这篇论文被纳入仓库，是因为它和 `persistent memory` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Self-distillation methods for large language models with an exponential moving average (EMA) teacher already retain a history of student updates.

进一步看，论文的核心做法或实验重点可以概括为：Muon nevertheless stores a separate momentum buffer, increasing persistent training memory.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：persistent memory
- 检索关键词命中：persistent memory
- 来源分类信息：cs.LG, cs.AI, cs.CL, stat.ML

## Abstract Snapshot
Self-distillation methods for large language models with an exponential moving average (EMA) teacher already retain a history of student updates. Muon nevertheless stores a separate momentum buffer, increasing persistent training memory. We propose Muon with Reused Teacher (Muon-RT), which reuses the teacher-student displacement to eliminate momentum buffers for hidden weight matrices. We show that this displacement encodes an exponentially weighted history of applied updates and smooths temporally uncorrelated noise under a local model. Muon-RT removes its radial component, normalizes it spectrally, and mixes it with the current gradient after Newton-Schulz (NS) orthogonalization. Under explicit regularity and alignment assumptions, we establish linear contraction of an expected objective-gap bound toward a residual error level. With Self-Distillation Fine-Tuning (SDFT) on Qwen2.5-7B-Instruct, Muon-RT improves average accuracy over AdamW by 2.6 points with 42% less persistent memory, and over momentum Muon by 5.4 points with 27% less persistent memory. With Self-Distillation Policy Optimization (SDPO) on Olmo-3-7B-Instruct, it improves average accuracy over AdamW by 2.0 points.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
