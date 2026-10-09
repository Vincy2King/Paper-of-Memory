# Memory Type Varies: Empowering LLM Agents for Long-Term Memory with Diverse Strategies

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.11573v1
- Published: 2026-10-08
- Updated: 2026-10-08
- Authors: Yi Wen, Derong Xu, Pengyue Jia, Yichao Wang, Yingyi Zhang, Maolin Wang, Junyi Li, Wenlin Zhang, Xiaopeng Li, Yong Liu, Xiangyu Zhao
- Tags: agent, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.11573v1

## One-Sentence Summary
The memory capabilities of Large Language Models (LLMs) have garnered increasing attention recently.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：The memory capabilities of Large Language Models (LLMs) have garnered increasing attention recently.

进一步看，论文的核心做法或实验重点可以概括为：Despite great success achieved, existing retrieval-based memory approaches typically overlook the differences between memories and employ a unified strategy to process all memories, leading to suboptimal performance.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
The memory capabilities of Large Language Models (LLMs) have garnered increasing attention recently. Despite great success achieved, existing retrieval-based memory approaches typically overlook the differences between memories and employ a unified strategy to process all memories, leading to suboptimal performance. Thus, an intuitive question arises: can we categorize memory into different types and select appropriate strategies? However, given the topic-rich, scenario-complex, and boundary-blurred nature of memory scenarios, achieving precise classification of memories is not easy. To address this challenge, we propose a memory multi-class dataset in this paper, termed TriMEM, which provides precise annotations for memory types across diverse scenarios. Building upon this foundation, we propose a novel memory framework, named MemoType, which can adaptively recognize each memory and query type with the learned router model. With the memory and query routing, MemoType can retrieve the memory with corresponding query types and design tailored retrieval strategies, thereby enhancing the retrieval performance. Moreover, we theoretically prove that any single retrieval strategy is subject to a fundamental upper bound on its expected retrieval precision in multi-class corpora, leading to systematic precision degradation. Extensive experiments on three datasets demonstrate that MemoType consistently outperforms existing methods, achieving up to 16.18% improvement in Recall@1.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
