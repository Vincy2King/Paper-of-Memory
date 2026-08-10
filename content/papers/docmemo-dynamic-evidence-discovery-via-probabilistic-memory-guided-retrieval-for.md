# DocMemo: Dynamic Evidence Discovery via Probabilistic Memory-Guided Retrieval for Multi-Modal Document Understanding

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.07067v1
- Published: 2026-08-07
- Updated: 2026-08-07
- Authors: Hanshu Yao, Janfeng Zhong, Niu Lian, Jinpeng Wang
- Tags: benchmark, episodic, retrieval
- Categories: cs.AI, cs.CL, cs.IR, cs.MM
- URL: http://arxiv.org/abs/2608.07067v1

## One-Sentence Summary
Long-document understanding requires locating sparse and heterogeneous evidence across hundreds of pages, yet existing systems remain limited by static retrieval and fragile...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-document understanding requires locating sparse and heterogeneous evidence across hundreds of pages, yet existing systems remain limited by static retrieval and fragile cross-round memory.

进一步看，论文的核心做法或实验重点可以概括为：Mainstream single-round methods commit to a fixed top-$k$ page set at the outset and struggle to recover from early retrieval errors; recent iterative approaches allow multi-round evidence acquisition, but they do not...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, episodic, retrieval
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI, cs.CL, cs.IR, cs.MM

## Abstract Snapshot
Long-document understanding requires locating sparse and heterogeneous evidence across hundreds of pages, yet existing systems remain limited by static retrieval and fragile cross-round memory. Mainstream single-round methods commit to a fixed top-$k$ page set at the outset and struggle to recover from early retrieval errors; recent iterative approaches allow multi-round evidence acquisition, but they do not investigate the propagation mechanism of cross-round states, making it difficult to track the dynamic changes in page relevance. To address these limitations, we propose DocMemo, a memory-guided framework that formulates long-document reasoning as dynamic evidence exploration. DocMemo maintains a tri-level retrieval state consisting of Document Schema Memory, Page Belief Memory, and Question Episodic Memory, which respectively capture structural priors, dynamic relevance estimation, and query-specific reasoning trajectories. During reasoning, DocMemo continuously refines cross-round page selection through Bayesian page belief updating with Thompson sampling, spatial proximity propagation, and structure-aware adaptive-granularity evidence access, while supplementing page-level evidence with fine-grained visual regions. Experiments on 3 benchmarks show that DocMemo achieves state-of-the-art performance and validate the efficacy of structured memory and dynamic page belief updating. Code is available at https://github.com/Harrygof/DocMemo.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
