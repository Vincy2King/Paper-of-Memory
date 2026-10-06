# ReMAP: Restoring the Perceptual Cycle with Reasoning-Time Latent Visual Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.05097v1
- Published: 2026-10-04
- Updated: 2026-10-04
- Authors: Hao Jiang, Zhanyu Guo, Chenwei Wu, Yichen Guo, Qizhe Zhang, Junchi Yao, Jixian Wu, Jinhao You, Kai Tang, Jiajun Cao, Tinghao Wang, Mengyu Wang, Leo Anthony Celi, Shanghang Zhang
- Tags: benchmark, context, retrieval
- Categories: cs.CV, cs.AI, cs.CL
- URL: http://arxiv.org/abs/2610.05097v1

## One-Sentence Summary
As multimodal large language models (MLLMs) reason for longer, attention to the initial visual input diminishes, weakening visual grounding.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：As multimodal large language models (MLLMs) reason for longer, attention to the initial visual input diminishes, weakening visual grounding.

进一步看，论文的核心做法或实验重点可以概括为：Visual memory reintroduces visual evidence during reasoning.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CV, cs.AI, cs.CL

## Abstract Snapshot
As multimodal large language models (MLLMs) reason for longer, attention to the initial visual input diminishes, weakening visual grounding. Visual memory reintroduces visual evidence during reasoning. We conduct a controlled analysis of visual memory along three axes: curation, organization, and access. We find that local evidence benefits from global context, compact latent representations balance accuracy and visual-context cost, and the utility of memory access depends on the reasoning state. Guided by these findings, we propose ReMAP (Reasoning-Time Memory-Augmented Perception), which couples two complementary latent memories: a static, question-conditioned Global memory that preserves scene and cross-image context, and a dynamic Local memory that uses this context as an anchor while selecting and re-encoding region-level evidence according to the current reasoning state. Both memories return compact latent tokens inserted into the reasoning sequence, and a reinforcement-learning access policy trained with branched rollouts decides when to continue reasoning or invoke Global or Local memory. On ten benchmark families, ReMAP outperforms prior visual-memory methods on all four multi-image benchmarks, exceeding the strongest prior results on MuirBench and MIMIC by 8.38 and 14.84 percentage points. Across four backbone families, enabling memory access improves over the same trained model with memory disabled, and on shared V*Bench, CV-Bench-2D, and MuirBench questions ReMAP reduces the visual tokens entering the reasoning sequence by 51.0-76.8% relative to the native-resolution backbone. Further analyses show that Global and Local memory form distinct yet complementary latent representations. Together, these components restore the perceptual cycle by letting the reasoning state trigger targeted visual retrieval, with the retrieved evidence guiding subsequent reasoning.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
