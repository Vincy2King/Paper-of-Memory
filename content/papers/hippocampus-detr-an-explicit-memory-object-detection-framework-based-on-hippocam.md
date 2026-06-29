# Hippocampus-DETR: An Explicit Memory Object Detection Framework Based on Hippocampus Modeling

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.27831v1
- Published: 2026-06-26
- Updated: 2026-06-26
- Authors: Zhaoning Shi, Bo Ma, Hao Xu, Zepeng Yang, Bo Liang
- Tags: retrieval
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2606.27831v1

## One-Sentence Summary
This paper addresses the lack of explicit memory mechanisms in current object detection models and proposes Hippocampus-DETR, a novel detection framework based on biological...

## Introduction
这篇论文被纳入仓库，是因为它和 `retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：This paper addresses the lack of explicit memory mechanisms in current object detection models and proposes Hippocampus-DETR, a novel detection framework based on biological hippocampal memory modeling.

进一步看，论文的核心做法或实验重点可以概括为：This framework integrates a hippocampal memory network module, HipNet, into the DETR architecture and systematically simulates the anatomical structure and functional organization of hippocampal subregions, including...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
This paper addresses the lack of explicit memory mechanisms in current object detection models and proposes Hippocampus-DETR, a novel detection framework based on biological hippocampal memory modeling. This framework integrates a hippocampal memory network module, HipNet, into the DETR architecture and systematically simulates the anatomical structure and functional organization of hippocampal subregions, including the entorhinal cortex, dentate gyrus, CA3, CA1, and subiculum. Through this design, Hippocampus-DETR realizes pattern separation, pattern completion, importance filtering, and information integration of visual encoding features. During training, different memory submodules are optimized using a layer-wise training strategy, ultimately forming a memory system with memory retrieval and completion capabilities. Experimental results demonstrate that Hippocampus-DETR achieves higher detection accuracy than current mainstream models. More importantly, models equipped with this framework also exhibit excellent generalization ability and data efficiency in tasks such as few-shot image classification, multimodal feature construction, and image restoration. Subsequent experiments further validate the functional necessity and internal interpretability of each memory submodule. This study not only provides a novel object detection framework, but also offers a feasible technical pathway for integrating neurocognitive mechanisms with deep learning models, highlighting its significant value in improving model learning efficiency and task robustness. The project is available at https://github.com/2186cloud/hipnet.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
