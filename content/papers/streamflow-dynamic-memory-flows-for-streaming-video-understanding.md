# StreamFlow: Dynamic Memory Flows for Streaming Video Understanding

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.10949v1
- Published: 2026-08-11
- Updated: 2026-08-11
- Authors: Muxin Fu, Yifan Zhang, Wentao Zhang, Fangming Guo, Qian Chen, Guibin Zhang, Shuicheng Yan, Bo An
- Tags: benchmark, long-term, retrieval
- Categories: cs.CV, cs.CL
- URL: http://arxiv.org/abs/2608.10949v1

## One-Sentence Summary
Streaming video understanding requires multimodal large language models (MLLMs) to preserve relevant evidence from continuously evolving streams under strict causality and...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Streaming video understanding requires multimodal large language models (MLLMs) to preserve relevant evidence from continuously evolving streams under strict causality and bounded memory.

进一步看，论文的核心做法或实验重点可以概括为：Yet existing paradigms remain limited: model-based methods require intrusive backbone updates, while memory-based methods expend substantial visual-encoding computation on temporally redundant content and rely on...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CV, cs.CL

## Abstract Snapshot
Streaming video understanding requires multimodal large language models (MLLMs) to preserve relevant evidence from continuously evolving streams under strict causality and bounded memory. Yet existing paradigms remain limited: model-based methods require intrusive backbone updates, while memory-based methods expend substantial visual-encoding computation on temporally redundant content and rely on rigid access to visual history. To address these limitations, we introduce StreamFlow, an efficient visual memory framework that enables dynamic, on-demand access to historical visual information. StreamFlow combines a lightweight, dynamics-aware mid-term memory that filters temporal redundancy before visual encoding with a latent long-term memory that consolidates historical video content into visual latents accessible to subsequent reasoning. During generation, an attention-guided retrieval mechanism injects relevant visual latents when the model's reliance on visual evidence weakens. StreamFlow achieves state-of-the-art streaming video understanding performance, reaching 67.73% overall accuracy on StreamingBench, while also delivering strong performance on offline long-video benchmarks. Relative to the vanilla setting, it improves the visual attention score (VAS) by 59.1% while reducing end-to-end latency and peak memory by 50.4% and 21.1%, respectively, enabling more visually grounded and efficient reasoning.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
