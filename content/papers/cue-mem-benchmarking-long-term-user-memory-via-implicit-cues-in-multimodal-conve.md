# CUE-Mem: Benchmarking Long-Term User Memory via Implicit Cues in Multimodal Conversations

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.32574v1
- Published: 2026-09-26
- Updated: 2026-09-26
- Authors: Yulin Hu, Yanyan Zhao, Zimo Long, Xing Fu, Mengtong Ji, Weixiang Zhao, Yutai Hou, Qianchao Wang, Dandan Tu
- Tags: agent, benchmark, conversation, long-term, retrieval
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2609.32574v1

## One-Sentence Summary
Long-term memory is essential for multimodal agents that interact with users across sustained conversations.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory is essential for multimodal agents that interact with users across sustained conversations.

进一步看，论文的核心做法或实验重点可以概括为：However, user memories are not always explicitly stated: they may also be implied by recurring background objects in images, ambient sounds in audio, or other peripheral multimodal cues.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Long-term memory is essential for multimodal agents that interact with users across sustained conversations. However, user memories are not always explicitly stated: they may also be implied by recurring background objects in images, ambient sounds in audio, or other peripheral multimodal cues. Existing benchmarks largely focus on text-only memory or explicit multimodal evidence, leaving implicit multimodal cues underexplored. We introduce CUE-Mem, a text-image-audio benchmark for evaluating long-term user memory from implicit cues. CUE-Mem contains 2,674 questions across explicit and implicit evidence settings and covers four tasks: Entity Recall, Long Pattern, Personalized Recommendation, and Answer Refusal. Across textualized memory systems, implicit performance remains far below oracle evidence, locating the main bottleneck in preserving and retrieving subtle cues rather than question answerability. Increasing caption detail recovers more of this evidence, but brings uneven gains and rapidly growing token costs, motivating native multimodal access. Yet native access does not uniformly resolve the bottleneck: evidence use depends strongly on the backbone, while multimodal indexing introduces substantial retrieval noise. CUE-Mem provides a testbed for memory systems that selectively retain, retrieve, and use subtle multimodal evidence.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
