# MemLife: Curating and Reasoning over Long-Term Egocentric Video Memories

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.40195v1
- Published: 2026-09-30
- Updated: 2026-09-30
- Authors: Guangzhi Xiong, Xinyuan Zhang, Xiao Yang, Hyokun Yun, Kai Zhang, Shiun-Zu Kuo, Hyeonjeong Ha, Xilun Chen, Kai Sun, Lucas Liang, Guangqiang Dong, Ejaz Ahmed, Ahmed A Aly, Anuj Kumar, Raffay Hamid, Aidong Zhang, Xin Luna Dong
- Tags: agent, benchmark, long-term, retrieval
- Categories: cs.CV, cs.AI, cs.CL
- URL: http://arxiv.org/abs/2609.40195v1

## One-Sentence Summary
Long-term egocentric video enables personalized AI assistants to reason about daily life.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term egocentric video enables personalized AI assistants to reason about daily life.

进一步看，论文的核心做法或实验重点可以概括为：However, as video histories grow to hundreds of hours spanning months or years, reprocessing raw clips for every query becomes computationally prohibitive.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.CV, cs.AI, cs.CL

## Abstract Snapshot
Long-term egocentric video enables personalized AI assistants to reason about daily life. However, as video histories grow to hundreds of hours spanning months or years, reprocessing raw clips for every query becomes computationally prohibitive. Memory systems offer a scalable alternative by compacting videos into text representations, but often fail on practical benchmarks: either the memory does not preserve key evidence, or the retriever fails to locate relevant entries due to retrieval competition in growing search spaces. To address these challenges, we introduce MemLife, a multimodal memory system that constructs entity-grounded, first-person text episodes and retrieves them via a time-indexed agentic reader. Without training or query-time video access, MemLife improves over the strongest training-free baseline by 4.6--12.0% across four long-horizon benchmarks. To further improve memory quality, we propose MemOpt, a reinforcement learning framework that optimizes the memory writer to produce faithful, informative, and retrievable memories. MemOpt consistently improves MemLife by 2.7--5.0% across different video and question distributions, with gains that generalize across writer and reader backbones and memory systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
