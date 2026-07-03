# MMIR-TCM: Memory-Integrated Multimodal Inference and Retrieval for TCM Clinical Decision Support

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.01814v1
- Published: 2026-07-02
- Updated: 2026-07-02
- Authors: Lihui Luo, Joongwon Chae, Ziyan Chen, Yang Liu, Siyi Cheng, Weihan Gao, Zelin Zeng, Xiaoming Yin, Samaneh Beheshti Kashi, Dongmei Yu, Lian Zhang, Jing Sui, Zeming Liang, Jiansong Ji, Peter E. Lobie, Peiwu Qin
- Tags: retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.01814v1

## One-Sentence Summary
Traditional Chinese Medicine (TCM) diagnosis, particularly through tongue inspection, faces persistent challenges in subjectivity and reproducibility.

## Introduction
这篇论文被纳入仓库，是因为它和 `retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Traditional Chinese Medicine (TCM) diagnosis, particularly through tongue inspection, faces persistent challenges in subjectivity and reproducibility.

进一步看，论文的核心做法或实验重点可以概括为：The application of multimodal artificial intelligence to TCM clinical tasks, such as syndrome differentiation and prescription generation, is significantly hampered by the semantic gap between visual tongue features...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Traditional Chinese Medicine (TCM) diagnosis, particularly through tongue inspection, faces persistent challenges in subjectivity and reproducibility. The application of multimodal artificial intelligence to TCM clinical tasks, such as syndrome differentiation and prescription generation, is significantly hampered by the semantic gap between visual tongue features and textual reasoning, as well as the lack of large-scale, standardized datasets. To address these challenges, we introduce MMIR-TCM, a novel framework that emulates the diagnostic process of TCM experts by integrating multimodal large language model(MLLM) with memory-augmented segmentation and retrieval-augmented generation (RAG). Employing a three-stage architecture, MMIR-TCM integrates a training-free Memory-SAM module for robust tongue extraction, a fine-tuned Qwen3-VL model for structured tongue diagnosis generation, and a Qwen3-based RAG component for evidence-grounded clinical decision support generation. The framework was developed and validated using MedTCM, a new large-scale multimodal dataset that we introduce specifically for advanced TCM research. To properly evaluate our framework's clinical accuracy, which existing metrics fail to capture, we also developed TDEU, a domain-specific evaluation metric incorporating semantic understanding and diagnostic importance. Our comprehensive experiments demonstrate that MMIR-TCM significantly outperforms leading models, including GPT-4o and Gemini 2.5 Flash.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
