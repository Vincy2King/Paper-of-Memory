# Remembering Through Change: Provenance-Preserving Hypergraph Memory for Multimodal Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.29995v1
- Published: 2026-10-21
- Updated: 2026-10-21
- Authors: Jielong Tang, Ling-An Zeng, Xujie Yuan, Xiao Dong, Zhiqian Xia, Qingfeng Li, Shixiong Kai, Kaichao Liang, Rong Yao, Jian Yin
- Tags: agent, benchmark, long-term
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.29995v1

## One-Sentence Summary
Long-term memory for multimodal agents remains challenging, as it must preserve fine-grained visual evidence while tracking entity evolution across sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory for multimodal agents remains challenging, as it must preserve fine-grained visual evidence while tracking entity evolution across sessions.

进一步看，论文的核心做法或实验重点可以概括为：Existing abstraction-based memories compress images into text, often discarding visually discriminative details, whereas pixel-preserving memories retain raw observations but struggle to reliably associate diverse...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term
- 检索关键词命中：long-term memory, memory compression
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-term memory for multimodal agents remains challenging, as it must preserve fine-grained visual evidence while tracking entity evolution across sessions. Existing abstraction-based memories compress images into text, often discarding visually discriminative details, whereas pixel-preserving memories retain raw observations but struggle to reliably associate diverse observations with persistent entity identities and track their evolving states. To address these limitations, we propose MHG-Mem, a multimodal hypergraph memory that jointly organizes entity identity, state evolution, and provenance to visual evidence. Specifically, MHG-Mem represents distinct entity mentions and their observed facts as individual nodes, grouping identity-consistent mentions and facts through occurrence hyperedges. It then synthesizes aspect-specific evolution states from these grouped observations and links them to supporting entities, facts, and source evidence through evolutionary and evidential hyperedges. To navigate this structured memory, we introduce hypergraph-based agentic search, which adaptively selects an entry layer, traverses typed hyperedges across memory levels, and inspects source observations when fine-grained verification is required. These designs support both detailed visual verification and reasoning over cross-session state changes. Extensive experiments across three benchmarks demonstrate the effectiveness of MHG-Mem, improving performance by 8.20-9.98% over the strongest baseline.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
