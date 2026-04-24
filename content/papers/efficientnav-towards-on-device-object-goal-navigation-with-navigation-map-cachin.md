# EfficientNav: Towards On-Device Object-Goal Navigation with Navigation Map Caching and Retrieval

- Source: OpenReview
- Venue: NeurIPS 2025 poster
- Paper ID: openreview:qMm7tC1zvj
- Published: 2025-09-18
- Updated: 2026-04-21
- Authors: Zebin Yang, Sunjian Zheng, Tong Xie, Tianshi Xu, Bo Yu, Fan Wang, Jie Tang, Shaoshan Liu, Meng Li
- Tags: agent, benchmark, retrieval
- Categories: NeurIPS.cc/2025/Conference/-/Submission
- URL: https://openreview.net/forum?id=qMm7tC1zvj

## One-Sentence Summary
Object-goal navigation (ObjNav) tasks an agent with navigating to the location of a specific object in an unseen environment.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `NeurIPS 2025 poster` 这个 venue 相关。

从摘要来看，作者主要关注的是：Object-goal navigation (ObjNav) tasks an agent with navigating to the location of a specific object in an unseen environment.

进一步看，论文的核心做法或实验重点可以概括为：Embodied agents equipped with large language models (LLMs) and online constructed navigation maps can perform ObjNav in a zero-shot manner.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：NeurIPS 2025 poster
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：NeurIPS.cc/2025/Conference/-/Submission

## Abstract Snapshot
Object-goal navigation (ObjNav) tasks an agent with navigating to the location of a specific object in an unseen environment. Embodied agents equipped with large language models (LLMs) and online constructed navigation maps can perform ObjNav in a zero-shot manner. However, existing agents heavily rely on giant LLMs on the cloud, e.g., GPT-4, while directly switching to small LLMs, e.g., LLaMA3.2-11b, suffer from significant success rate drops due to limited model capacity for understanding complex navigation maps, which prevents deploying ObjNav on local devices. At the same time, the long prompt introduced by the navigation map description will cause high planning latency on local devices. In this paper, we propose EfficientNav to enable on-device efficient LLM-based zero-shot ObjNav. To help the smaller LLMs better understand the environment, we propose semantics-aware memory retrieval to prune redundant information in navigation maps. To reduce planning latency, we propose discrete memory caching and attention-based memory clustering to efficiently save and re-use the KV cache. Extensive experimental results demonstrate that EfficientNav achieves 11.1\% improvement in success rate on HM3D benchmark over GPT-4-based baselines, and demonstrates 6.7$\times$ real-time latency reduction and 4.7$\times$ end-to-end latency reduction over GPT-4 planner. Our code is available on https://github.com/PKU-SEC-Lab/EfficientNav.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
