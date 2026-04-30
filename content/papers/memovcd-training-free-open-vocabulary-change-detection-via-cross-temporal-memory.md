# MemOVCD: Training-Free Open-Vocabulary Change Detection via Cross-Temporal Memory Reasoning and Global-Local Adaptive Rectification

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.26774v1
- Published: 2026-04-29
- Updated: 2026-04-29
- Authors: Zuzheng Kuang, Honghao Chang, Boqiang Liang, Haoqian Wang, Lijun He, Fan Li, Haixia Bi
- Tags: benchmark
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2604.26774v1

## One-Sentence Summary
Open-vocabulary change detection aims to identify semantic changes in bi-temporal remote sensing images without predefined categories.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Open-vocabulary change detection aims to identify semantic changes in bi-temporal remote sensing images without predefined categories.

进一步看，论文的核心做法或实验重点可以概括为：Recent methods combine foundation models such as SAM, DINO and CLIP, but typically process each timestamp independently or interact only at the final comparison stage.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：memory reasoning
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Open-vocabulary change detection aims to identify semantic changes in bi-temporal remote sensing images without predefined categories. Recent methods combine foundation models such as SAM, DINO and CLIP, but typically process each timestamp independently or interact only at the final comparison stage. Such paradigms suffer from insufficient temporal coupling during semantic reasoning, which limits their ability to distinguish genuine semantic changes from non-semantic appearance discrepancies. In addition, patch-dominant inference on high-resolution images often weakens global semantic continuity and produces fragmented change regions. To address these issues, we propose MemOVCD, a training-free open-vocabulary change detection framework based on cross-temporal memory reasoning and global-local adaptive rectification. Specifically, we reformulate bi-temporal change detection as a two-frame tracking problem and introduce weighted bidirectional propagation to aggregate semantic evidence from both temporal directions. To stabilize memory propagation across large temporal gaps, we construct histogram-aligned transition frames to smooth abrupt appearance changes. Moreover, a global-local adaptive rectification strategy adaptively fuses local and global-view predictions, improving spatial consistency while preserving fine-grained details. Experiments on five benchmarks demonstrate that MemOVCD achieves favorable performance on two change detection tasks, validating its effectiveness and generalization under diverse open-vocabulary settings.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
