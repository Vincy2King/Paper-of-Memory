# MACE: Memory-Augmented Crop-Disease Evaluation of Frozen Vision-Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.28573v1
- Published: 2026-11-21
- Updated: 2026-11-21
- Authors: Tirtho Roy, Shreyan Ganguly, Muhammad Arbab Arshad, Nikhil Bhattacharya, Soumik Sarkar
- Tags: memory-augmented
- Categories: cs.MA, cs.AI, cs.CV
- URL: http://arxiv.org/abs/2611.28573v1

## One-Sentence Summary
In plant phenotyping, crop disease diagnosis has traditionally relied on expert assessment of visible symptoms and on models tailored to specific crops or diseases, and both are...

## Introduction
这篇论文被纳入仓库，是因为它和 `memory-augmented` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：In plant phenotyping, crop disease diagnosis has traditionally relied on expert assessment of visible symptoms and on models tailored to specific crops or diseases, and both are difficult to scale across field...

进一步看，论文的核心做法或实验重点可以概括为：Recent methods provide frozen vision-language models with source-grounded knowledge bases that summarize the typical symptoms of each disease but describe little of how symptoms vary across individual cases.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：memory-augmented
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.MA, cs.AI, cs.CV

## Abstract Snapshot
In plant phenotyping, crop disease diagnosis has traditionally relied on expert assessment of visible symptoms and on models tailored to specific crops or diseases, and both are difficult to scale across field conditions. Recent methods provide frozen vision-language models with source-grounded knowledge bases that summarize the typical symptoms of each disease but describe little of how symptoms vary across individual cases. We introduce MACE (Memory-Augmented Crop-Disease Evaluation), a training-free method that supplements the knowledge base with a memory of symptom descriptions paired with known disease labels. MACE matches a description of the query image against this memory and retrieves only text descriptions and disease labels, so the query is the only image that the diagnosis model sees. Across ten crops, MACE with Claude Sonnet 5.5 improved accuracy over the knowledge-base baseline from 42.8% to 62.2% in distribution and from 50.7% to 57.0% on held-out image collections. Retrieved disease labels accounted for most of the gain, and adding the corresponding text descriptions improved in-distribution accuracy by about six percentage points.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
