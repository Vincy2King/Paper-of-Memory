# ReMMD: Realistic Multilingual Multi-Image Agentic Verification for Multimodal Misinformation Detection

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.24112v1
- Published: 2026-06-23
- Updated: 2026-06-23
- Authors: Chenhao Dang, Dantong Zhu, Jun Yang, Conghui He, Weijia Li
- Tags: agent, benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.24112v1

## One-Sentence Summary
Multimodal misinformation detection is increasingly important because viral posts now combine long multilingual narratives, several images, mixed provenance, and subtle text--...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multimodal misinformation detection is increasingly important because viral posts now combine long multilingual narratives, several images, mixed provenance, and subtle text--image framing errors.

进一步看，论文的核心做法或实验重点可以概括为：Existing benchmarks and methods remain poorly matched to this setting: they usually isolate short captions, single images, binary labels, or one manipulation source, while agentic verification remains costly under...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Multimodal misinformation detection is increasingly important because viral posts now combine long multilingual narratives, several images, mixed provenance, and subtle text--image framing errors. Existing benchmarks and methods remain poorly matched to this setting: they usually isolate short captions, single images, binary labels, or one manipulation source, while agentic verification remains costly under realistic evidence search. We present ReMMD, a realistic multilingual multi-image agentic verification framework for multimodal misinformation detection. ReMMD includes ReMMDBench, a real-world multimodal misinformation detection benchmark with 500 samples, 2,756 images, five monolingual languages, two cross-lingual settings, three text-length tiers, multi-image posts, five-way veracity labels, eight distortion labels, evidence provenance, and rationales. It also includes ReMMD-Agent, a persistent-memory verifier that decomposes posts into atomic points, builds a reusable evidence set, and predicts structured L1/L2/L3 outputs. Across proprietary systems, open LVLMs, MMD-Agent, and T2-Agent, ReMMD-Agent obtains the best five-way veracity performance, with 41.80% accuracy and 39.12% macro-F1 using GPT-5.2, while reducing cost by 17.5% relative to MMD-Agent and 79.9% relative to T2-Agent. The project is available at https://dang-ai.github.io/ReMMD.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
