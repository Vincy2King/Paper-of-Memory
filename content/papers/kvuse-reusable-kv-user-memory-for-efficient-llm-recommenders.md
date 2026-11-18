# KVUse: Reusable-KV User Memory for Efficient LLM Recommenders

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.21920v1
- Published: 2026-11-16
- Updated: 2026-11-16
- Authors: Xin Guo, Qiang Zhang, Xiang Zhou, Arushi Rai, Siyu Lin, Yifan Wu, Xiang Shen, Lei Huang, Qunshu Zhang, Xiangjun Fan, Lizhu Zhang
- Tags: context
- Categories: cs.LG
- URL: http://arxiv.org/abs/2611.21920v1

## One-Sentence Summary
Memory-augmented recommenders built on large language models (LLMs) maintain a natural-language profile of each user.

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-augmented recommenders built on large language models (LLMs) maintain a natural-language profile of each user.

进一步看，论文的核心做法或实验重点可以概括为：These profiles are updated by a user profile update path that revises the profile as new interactions arrive and are consumed by downstream task paths like ranking.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.LG

## Abstract Snapshot
Memory-augmented recommenders built on large language models (LLMs) maintain a natural-language profile of each user. These profiles are updated by a user profile update path that revises the profile as new interactions arrive and are consumed by downstream task paths like ranking. Because these user profiles are stored as text in the user memory, every ranking LLM call that consumes them must splice them in the prompt and calculate the KV cache of them during the prefill phase. Given these ranking LLM calls are prefill heavy (long prompt but short decoded output) and repeatedly called, these repeated prefill of user profile text dominates the serving. Prefix caching cannot remove it, because these user profiles are preceded by different text in different calls. We present KVUse, which stores the user profiles as reusable key-value (KV) caches instead of text. KVUse trains lightweight LoRA writers by self-distillation, so that the user profile update call produces the reusable KV of the user profile while decoding it, and the LLM can read these reusable KV at new positions and behind new context without recomputation. KVUse also has a customized KV scheduler that uploads the stored reusable KV of the next batch while the current batch is computed, hiding the KV transfer from host memory behind GPU computation. On four InstructRec datasets with Llama-3.1-8B-Instruct, KVUse shows no statistically significant difference in ranking quality from full prefill over continuous memory update rounds. Under saturated load, KVUse raises the throughput of the downstream scoring path by 4.0x-4.5x and of the profile update path by 1.4x-1.9x.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
