# MemFolder: Structure-Guided Memory Folding for Efficient Agent Memory Management

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.26427v1
- Published: 2026-11-19
- Updated: 2026-11-19
- Authors: Xuyang Liu, Chenwen Lu, Junxi Wang, Siyu Ren, Xinying Lin, Siteng Huang, Hongli Sun, Linfeng Zhang, Honggang Chen
- Tags: agent, benchmark, compression, context, long-term, retrieval
- Categories: cs.CL, cs.CV
- URL: http://arxiv.org/abs/2611.26427v1

## One-Sentence Summary
Long-term agents accumulate large external memory stores as interactions unfold, increasing the costs of storage, retrieval, and response generation.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term agents accumulate large external memory stores as interactions unfold, increasing the costs of storage, retrieval, and response generation.

进一步看，论文的核心做法或实验重点可以概括为：Efficiency is constrained by two coupled factors: a growing record count increases retrieval overhead, while longer retrieved contexts increase prefill computation and decoding-time attention costs.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, context, long-term, retrieval
- 检索关键词命中：agent memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.CL, cs.CV

## Abstract Snapshot
Long-term agents accumulate large external memory stores as interactions unfold, increasing the costs of storage, retrieval, and response generation. Efficiency is constrained by two coupled factors: a growing record count increases retrieval overhead, while longer retrieved contexts increase prefill computation and decoding-time attention costs. Existing methods prune or consolidate records, but pruning can discard useful evidence, whereas consolidation may produce fewer yet longer retrieval units. We introduce MemFolder, a structure-guided memory folding framework that sequentially reduces record count and context length. The framework comprises two core components that share memory groups, using cross-record structure to guide both evidence consolidation and compact representation. RecordFolder grounds entity mentions, progressively selects representative yet complementary anchors, and combines semantic and entity affinity with temporal chaining to consolidate compatible records into fewer retrieval units. ContextFolder encodes the original records within these groups into compact text and uses verification feedback to revise encodings when key facts cannot be recovered. Experiments on the three text-based memory benchmarks LoCoMo, PersonaMem, and LongMemEval and the two multimodal benchmarks M3-Bench-web and M3-Bench-robot demonstrate the strong performance of our methods. Notably, on Mem0, RecordFolder retains 99.0% of the original average performance across the three text-based benchmarks with 50% fewer records, exceeding the strongest baseline by 1.9 percentage points in performance retention. Combined with ContextFolder, existing record compression methods further shorten their output records while retaining most of their performance.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
