# Myocardial Strain Drift Correction in Deep Learning Based Ultrasound Tracking

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.09577v1
- Published: 2026-09-09
- Updated: 2026-09-09
- Authors: Thierry Judge, Nicolas Duchateau, Andreas Østvik, Havard Dalen, Bjørnar Grenne, Pierre-Yves Courand, Lasse Lovstakken, Pierre-Marc Jodoin, Olivier Bernard
- Tags: persistent memory
- Categories: eess.IV, cs.AI, cs.CV
- URL: http://arxiv.org/abs/2609.09577v1

## One-Sentence Summary
Myocardial strain from echocardiography is a key biomarker for cardiac function.

## Introduction
这篇论文被纳入仓库，是因为它和 `persistent memory` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Myocardial strain from echocardiography is a key biomarker for cardiac function.

进一步看，论文的核心做法或实验重点可以概括为：Recent deep learning methods show strong performance for myocardial motion tracking but often lack physiological constraints, leading to temporal drift across the cardiac cycle.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：persistent memory
- 检索关键词命中：persistent memory
- 来源分类信息：eess.IV, cs.AI, cs.CV

## Abstract Snapshot
Myocardial strain from echocardiography is a key biomarker for cardiac function. Recent deep learning methods show strong performance for myocardial motion tracking but often lack physiological constraints, leading to temporal drift across the cardiac cycle. Consequently, tracked points may not return to their relative initial positions at the end of each cardiac cycle, producing inaccurate strain estimates and even divergence in some cases. We propose a deep learning framework that compensates for drift during myocardial tracking. We extend a state-of-the-art echocardiographic tracking method (TAS-Net) with persistent memory tokens that share information across sliding windows over full cardiac cycles. A teacher-student fine-tuning strategy on real echocardiographic data then enforces physiologically consistent cyclic motion while preserving tracking accuracy. Experiments show reduced global and regional strain drift, improved agreement with clinical references, and better test-retest reproducibility, supporting more reliable myocardial strain estimation in clinical practice.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
