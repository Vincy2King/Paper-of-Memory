# Memory as the Backbone: A Dual-Store Associative Memory Architecture for Visual Recognition

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.33475v1
- Published: 2026-11-24
- Updated: 2026-11-24
- Authors: Ruizhi Wang, Xiangtao Wang, Bayar Menzat, Jianfeng Wang, Thomas Lukasiewicz
- Tags: context, long-term
- Categories: cs.CV, cs.LG
- URL: http://arxiv.org/abs/2611.33475v1

## One-Sentence Summary
We investigate whether explicit memory can serve as the organizing principle of a general-purpose visual backbone.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We investigate whether explicit memory can serve as the organizing principle of a general-purpose visual backbone.

进一步看，论文的核心做法或实验重点可以概括为：Inspired by the interaction between working and long-term memory in human cognition, we introduce DuSAM (Dual-Store Associative Memory), a hierarchical memory-native visual backbone coupling image-local working memory...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, long-term
- 检索关键词命中：long-term memory, working memory
- 来源分类信息：cs.CV, cs.LG

## Abstract Snapshot
We investigate whether explicit memory can serve as the organizing principle of a general-purpose visual backbone. Inspired by the interaction between working and long-term memory in human cognition, we introduce DuSAM (Dual-Store Associative Memory), a hierarchical memory-native visual backbone coupling image-local working memory (WM) with a fixed-capacity persistent semantic memory (PM). WM organizes local visual evidence into compact, spatially anchored states that are updated and transported across stages, then read back to refine dense features. PM consolidates semantic evidence from training images and annotated regions into prototypes, whose retrieved content enriches the same working states. With these memory operations in place of self-attention or state-space blocks, DuSAM achieves competitive performance relative to representative, similarly sized backbones on ImageNet-1K classification, ADE20K semantic segmentation, and COCO object detection and instance segmentation. Ablations show contributions from both stores, with PM particularly benefiting class groups with fewer annotated training pixels. At $2048\times2048$, the complete DuSAM-based UPerNet segmentor achieves $2.36\times$ the throughput of the evaluated DeiT-S/16 counterpart while using $59.5\%$ less GPU memory, and $1.24\times$ the throughput of the linear-complexity VMamba-T. Memory analyses reveal spatially selective WM access and semantic associations between retrieved prototypes and training regions. Class-targeted removal and restoration further demonstrate that category-specific experience can be replenished through state updates without changing network parameters. These results establish explicit memory as a viable organizing principle for visual backbones and provide a foundation for jointly designing contextual computation and addressable semantic memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
