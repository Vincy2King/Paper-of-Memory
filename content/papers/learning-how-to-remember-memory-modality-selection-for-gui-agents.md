# Learning How to Remember: Memory Modality Selection for GUI Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.17928v1
- Published: 2026-10-13
- Updated: 2026-10-13
- Authors: Taeyun Roh, Suhyeong Park, Gijin Kim, Wonjune Jang, Jaewoo Kang
- Tags: agent, benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.17928v1

## One-Sentence Summary
Recent advances in vision-language models (VLMs) have substantially improved the capabilities of GUI agents, while memory augmentation has emerged as a promising approach for...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recent advances in vision-language models (VLMs) have substantially improved the capabilities of GUI agents, while memory augmentation has emerged as a promising approach for reusing knowledge from past interactions.

进一步看，论文的核心做法或实验重点可以概括为：However, existing memory augmented GUI agents typically adopt a fixed representation strategy, providing retrieved experience as a static modality.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Recent advances in vision-language models (VLMs) have substantially improved the capabilities of GUI agents, while memory augmentation has emerged as a promising approach for reusing knowledge from past interactions. However, existing memory augmented GUI agents typically adopt a fixed representation strategy, providing retrieved experience as a static modality. It remains unclear whether a single memory modality is consistently optimal, or how modality preference changes across interaction steps. In this work, we conduct a systematic study of memory modality in VLM based GUI agents. Across GUI benchmarks, we find that the preferred memory representation is strongly step dependent. Motivated by the finding, we introduce \textbf{SwitchMem}, a routing framework that dynamically selects between textual and visual memory representations at each step. Across three GUI benchmarks, SwitchMem outperforms memory augmented baselines that rely on static memory representations. Our findings validate our claim that memory modality is a step dependent decision rather than a fixed design choice. Code and project resources are available at https://txxnrd.github.io/switchmem

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
