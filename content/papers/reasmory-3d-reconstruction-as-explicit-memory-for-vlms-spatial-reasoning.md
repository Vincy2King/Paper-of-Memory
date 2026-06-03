# Reasmory: 3D Reconstruction as Explicit Memory for VLMs Spatial Reasoning

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.00963v1
- Published: 2026-05-31
- Updated: 2026-05-31
- Authors: Jixuan He, Xueting Li, Chieh Hubert Lin, Ming-Hsuan Yang
- Tags: benchmark
- Categories: cs.CV, cs.CL
- URL: http://arxiv.org/abs/2606.00963v1

## One-Sentence Summary
Vision-Language Models (VLMs) exhibit emerging spatial reasoning capabilities, yet they remain unreliable on tasks requiring precise spatial understanding, such as viewpoint...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Vision-Language Models (VLMs) exhibit emerging spatial reasoning capabilities, yet they remain unreliable on tasks requiring precise spatial understanding, such as viewpoint reasoning, directional comparison, and...

进一步看，论文的核心做法或实验重点可以概括为：In multi-view images and monocular videos, relevant spatial cues are often sparse and distributed across redundant observations, making them difficult to organize and exploit.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CV, cs.CL

## Abstract Snapshot
Vision-Language Models (VLMs) exhibit emerging spatial reasoning capabilities, yet they remain unreliable on tasks requiring precise spatial understanding, such as viewpoint reasoning, directional comparison, and distance estimation. In multi-view images and monocular videos, relevant spatial cues are often sparse and distributed across redundant observations, making them difficult to organize and exploit. Reconstruction-based Vision Foundation Models (VFMs) offer a natural way to aggregate such observations into explicit spatial memory, such as point clouds. However, simply exposing reconstruction models as free-form tools is brittle, VLMs may invoke tools incorrectly, skip required spatial transformations, or misuse intermediate results. We propose \textbf{Reasmory}, a framework that formulates spatial reasoning as structured program execution over reconstructed spatial memory. Reasmory constructs explicit 3D memory, augments it with semantically grounded 3D object instances, and introduces a lightweight Domain-Specific Language (DSL) that constrains how VLMs query objects and cameras, transform viewpoints, and render observations during reasoning. Generated programs are parsed and validated before execution, enabling more reliable interaction with spatial memory than unconstrained tool use. Experiments on multi-view image and video spatial reasoning benchmarks show consistent gains of 6--18\% over strong baselines, including GPT-5-mini and Gemini-3-flash, indicating that explicit 3D memory is most useful when accessed through constrained, validated operations rather than free-form tool calls.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
