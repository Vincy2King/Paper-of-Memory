# On Memory Construction and Retrieval for Personalized Conversational Agents

- Source: OpenReview
- Venue: CoRR 2025
- Paper ID: openreview:oGFeYwuB2l
- Published: 2025-01-01
- Updated: 2026-08-24
- Authors: Zhuoshi Pan, Qianhui Wu, Huiqiang Jiang, Xufang Luo, Hao Cheng, Dongsheng Li, Yuqing Yang, Chin-Yew Lin, H. Vicky Zhao, Lili Qiu, Jianfeng Gao
- Tags: agent, benchmark, compression, conversation, long-term, retrieval
- Categories: DBLP.org/-/Record
- URL: https://openreview.net/forum?id=oGFeYwuB2l

## One-Sentence Summary
To deliver coherent and personalized experiences in long-term conversations, existing approaches typically perform retrieval augmented response generation by constructing memory...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, conversation` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `CoRR 2025` 这个 venue 相关。

从摘要来看，作者主要关注的是：To deliver coherent and personalized experiences in long-term conversations, existing approaches typically perform retrieval augmented response generation by constructing memory banks from conversation history at...

进一步看，论文的核心做法或实验重点可以概括为：Building on these insights, we propose SeCom, a method that constructs the memory bank at segment level by introducing a conversation segmentation model that partitions long-term conversations into topically coherent...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：CoRR 2025
- 高亮主题命中：agent, benchmark, compression, conversation, long-term, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：DBLP.org/-/Record

## Abstract Snapshot
To deliver coherent and personalized experiences in long-term conversations, existing approaches typically perform retrieval augmented response generation by constructing memory banks from conversation history at either the turn-level, session-level, or through summarization techniques.In this paper, we present two key findings: (1) The granularity of memory unit matters: turn-level, session-level, and summarization-based methods each exhibit limitations in both memory retrieval accuracy and the semantic quality of the retrieved content. (2) Prompt compression methods, such as LLMLingua-2, can effectively serve as a denoising mechanism, enhancing memory retrieval accuracy across different granularities. Building on these insights, we propose SeCom, a method that constructs the memory bank at segment level by introducing a conversation segmentation model that partitions long-term conversations into topically coherent segments, while applying compression based denoising on memory units to enhance memory retrieval. Experimental results show that SeCom exhibits a significant performance advantage over baselines on long-term conversation benchmarks LOCOMO and Long-MT-Bench+. Additionally, the proposed conversation segmentation method demonstrates superior performance on dialogue segmentation datasets such as DialSeg711, TIAGE, and SuperDialSeg.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
