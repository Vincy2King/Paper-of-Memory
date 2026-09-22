# MADrive: Memory-Augmented Driving Scene Modeling

- Source: OpenReview
- Venue: CVPR 2026 Findings
- Paper ID: openreview:uXQUhpd83Q
- Published: 2026-09-21
- Updated: 2026-09-21
- Authors: Polina Karpikova, Daniil Selikhanovych, Kirill Struminsky, Ruslan Musaev, Maria Golitsyna, Dmitry Baranchuk
- Tags: retrieval
- Categories: thecvf.com/CVPR/2026/Conference/-/Submission
- URL: https://openreview.net/forum?id=uXQUhpd83Q

## One-Sentence Summary
Recent advances in scene reconstruction have pushed toward highly realistic modeling of autonomous driving (AD) environments using 3D Gaussian splatting.

## Introduction
这篇论文被纳入仓库，是因为它和 `retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `CVPR 2026 Findings` 这个 venue 相关。

从摘要来看，作者主要关注的是：Recent advances in scene reconstruction have pushed toward highly realistic modeling of autonomous driving (AD) environments using 3D Gaussian splatting.

进一步看，论文的核心做法或实验重点可以概括为：However, the resulting reconstructions remain closely tied to the original observations and struggle to support photorealistic synthesis of significantly altered or novel driving scenarios.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：CVPR 2026 Findings
- 高亮主题命中：retrieval
- 检索关键词命中：memory-augmented
- 来源分类信息：thecvf.com/CVPR/2026/Conference/-/Submission

## Abstract Snapshot
Recent advances in scene reconstruction have pushed toward highly realistic modeling of autonomous driving (AD) environments using 3D Gaussian splatting. However, the resulting reconstructions remain closely tied to the original observations and struggle to support photorealistic synthesis of significantly altered or novel driving scenarios. This work introduces MADrive, a memory-augmented reconstruction framework designed to extend the capabilities of existing scene reconstruction methods by replacing observed vehicles with visually similar 3D assets retrieved from a large-scale external memory bank. Specifically, we release MADrive, a curated dataset of ~70K 360° car videos captured in the wild and present a retrieval module that finds the most similar car instances in the memory bank, reconstructs the corresponding 3D assets from video, and integrates them into the target scene through orientation alignment and relighting. The resulting replacements provide complete multi-view representations of vehicles in the scene, enabling photorealistic synthesis of substantially altered configurations, as demonstrated in our experiments.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
