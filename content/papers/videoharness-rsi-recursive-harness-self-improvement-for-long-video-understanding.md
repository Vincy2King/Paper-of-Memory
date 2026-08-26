# VideoHarness-RSI: Recursive Harness Self-Improvement for Long-Video Understanding with Frozen Vision-Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.24302v1
- Published: 2026-08-25
- Updated: 2026-08-25
- Authors: Guoyang Xu, Hao Chen
- Tags: agent, benchmark, compression, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.24302v1

## One-Sentence Summary
Long-video understanding depends critically on how a limited model context is constructed from a much longer video.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-video understanding depends critically on how a limited model context is constructed from a much longer video.

进一步看，论文的核心做法或实验重点可以概括为：Existing approaches improve this process through compression, retrieval, memory, and agentic evidence acquisition, but these mechanisms are typically introduced as part of a manually designed inference system or...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, context, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-video understanding depends critically on how a limited model context is constructed from a much longer video. Existing approaches improve this process through compression, retrieval, memory, and agentic evidence acquisition, but these mechanisms are typically introduced as part of a manually designed inference system or optimized together with other components. This makes it difficult to isolate a simpler question: how much can be gained by improving the executable context-construction program alone? We study this question through VIDEOHARNESS-RSI, a controlled baseline for recursively searching executable context constructors around a frozen vision-language model (VLM). An outer-loop proposer uses prior programs, evaluation outcomes, and execution traces to generate candidate harnesses, which are executed and evaluated end to end before successful variants are retained for further search. This makes long-video understanding a controlled instance of automated harness design: the searchable object is executable program structure, while the answering model and interface remain fixed. Starting from uniform sampling, recursive harness search consistently finds room for improvement and surpasses several weaker hand-crafted baselines. Starting instead from a stronger hand-crafted baseline, the same RSI process yields a further improvement. The selected harness also transfers to additional long-video benchmarks without further search. Together, these results establish executable context construction as a distinct optimization layer and provide a reproducible baseline for studying harness discovery and transfer around frozen VLMs.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
