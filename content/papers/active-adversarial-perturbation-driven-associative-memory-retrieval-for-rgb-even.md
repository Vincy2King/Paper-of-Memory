# Active Adversarial Perturbation-driven Associative Memory Retrieval for RGB-Event Visual Object Tracking

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.26455v1
- Published: 2026-06-24
- Updated: 2026-06-24
- Authors: Xiao Wang, Xufeng Lou, Zikang Yan, Lan Chen, Sibao Chen, Yaowei Wang, Yonghong Tian, Jin Tang
- Tags: retrieval
- Categories: cs.CV, cs.AI, cs.LG
- URL: http://arxiv.org/abs/2606.26455v1

## One-Sentence Summary
RGB-Event tracking improves localization robustness by fusing RGB appearance textures and dense temporal motion cues from event sensors.

## Introduction
这篇论文被纳入仓库，是因为它和 `retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：RGB-Event tracking improves localization robustness by fusing RGB appearance textures and dense temporal motion cues from event sensors.

进一步看，论文的核心做法或实验重点可以概括为：While this multi-modal scheme broadens tracking applicability, real-world scenes suffer diverse structured signal degradations that hinder traditional multi-modal fusion.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.CV, cs.AI, cs.LG

## Abstract Snapshot
RGB-Event tracking improves localization robustness by fusing RGB appearance textures and dense temporal motion cues from event sensors. While this multi-modal scheme broadens tracking applicability, real-world scenes suffer diverse structured signal degradations that hinder traditional multi-modal fusion. In harsh environments, either modality can lose reliability drastically, and targets frequently appear incomplete due to occlusion, edge truncation and foreground clutter.To tackle the above challenges, we present a hierarchical perturbation and retrieval framework tailored for RGB-Event tracking with robustness against partial target missing and modal degradation, termed APRTrack. To mimic real-world signal corruption, APRTrack constructs structured degradation via two adversarial perturbation branches at the modality and spatial levels, which separately simulate full-modal failure and localized target region absence. A hierarchical routing mechanism is designed to disentangle the training pipelines of the two perturbation types, effectively eliminating feature collapse induced by superimposed degradation constraints. Furthermore, we devise Footprint-guided Channel-calibrated Hopfield Retrieval (FCHR) for reliable historical information compensation. This module evaluates retrieval confidence based on association footprints between queries and memory banks, and calibrates the retrieval metric space prior to Hopfield matching, realizing controllable historical feature compensation bounded to target regions. Extensive experiments on FE108, COESOT, VisEvent, and FELT datasets demonstrate the effectiveness of our proposed strategies for the RGB-Event visual object tracking. The source code and pre-trained models will be released on https://github.com/Event-AHU/OpenEvTracking

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
