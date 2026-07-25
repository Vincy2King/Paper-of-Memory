# LMEB: Long-horizon Memory Embedding Benchmark

- Source: OpenReview
- Venue: CoRR 2026
- Paper ID: openreview:Pfk4lGFaxA
- Published: 2026-12-31
- Updated: 2026-07-25
- Authors: {'fullname': 'Xinping Zhao', 'username': ''}, {'fullname': 'Xinshuo Hu', 'username': ''}, {'fullname': 'Jiaxin Xu', 'username': ''}, {'fullname': 'Danyu Tang', 'username': ''}, {'fullname': 'Xin Zhang', 'username': ''}, {'fullname': 'Mengjia Zhou', 'username': ''}, {'fullname': 'Yan Zhong', 'username': ''}, {'fullname': 'Yao Zhou', 'username': ''}, {'fullname': 'Zifei Shan', 'username': ''}, {'fullname': 'Meishan Zhang', 'username': ''}, {'fullname': 'Baotian Hu', 'username': ''}, {'fullname': 'Min Zhang', 'username': ''}
- Tags: benchmark, context, episodic, long-term, retrieval
- Categories: OpenReview.net/Public_Article/DBLP.org/-/Record
- URL: https://openreview.net/forum?id=Pfk4lGFaxA

## One-Sentence Summary
Memory embeddings are crucial for memory-augmented systems, such as OpenClaw, but their evaluation is underexplored in current text embedding benchmarks, which narrowly focus on...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, episodic, long-term` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `CoRR 2026` 这个 venue 相关。

从摘要来看，作者主要关注的是：Memory embeddings are crucial for memory-augmented systems, such as OpenClaw, but their evaluation is underexplored in current text embedding benchmarks, which narrowly focus on traditional passage retrieval and fail...

进一步看，论文的核心做法或实验重点可以概括为：To address this gap, we introduce the Long-horizon Memory Embedding Benchmark (LMEB), a comprehensive framework for evaluating embedding models on complex, long-horizon memory retrieval.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：CoRR 2026
- 高亮主题命中：benchmark, context, episodic, long-term, retrieval
- 检索关键词命中：memory retrieval, memory-augmented
- 来源分类信息：OpenReview.net/Public_Article/DBLP.org/-/Record

## Abstract Snapshot
Memory embeddings are crucial for memory-augmented systems, such as OpenClaw, but their evaluation is underexplored in current text embedding benchmarks, which narrowly focus on traditional passage retrieval and fail to assess models' ability to handle long-horizon memory retrieval tasks involving fragmented, context-dependent, and temporally distant information. To address this gap, we introduce the Long-horizon Memory Embedding Benchmark (LMEB), a comprehensive framework for evaluating embedding models on complex, long-horizon memory retrieval. LMEB comprises 22 datasets and 193 zero-shot retrieval tasks spanning four memory types: episodic, dialogue, semantic, and procedural. These memory types differ in terms of level of abstraction and temporal dependency, capturing distinct aspects of memory retrieval that reflect the diverse challenges of the real world. We evaluate 15 widely used embedding models, ranging from hundreds of millions to ten billion parameters. The results reveal that (1) LMEB provides a reasonable level of difficulty; (2) Larger models do not always perform better; (3) LMEB and MTEB measure orthogonal capabilities. This suggests that the field has yet to converge on a universal model capable of excelling across all memory retrieval tasks, and that strong performance on traditional passage retrieval does not necessarily transfer to long-horizon memory retrieval. LMEB provides a standardized and reproducible framework that fills a key gap in memory embedding evaluation and supports future advances in long-term, context-dependent retrieval.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
