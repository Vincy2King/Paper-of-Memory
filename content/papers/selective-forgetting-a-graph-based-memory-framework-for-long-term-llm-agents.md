# Selective Forgetting: A Graph-Based Memory Framework for Long-Term LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.28978v1
- Published: 2026-08-29
- Updated: 2026-08-29
- Authors: Theo Rusu, Sourena Khanzadeh, Manar Alalfi
- Tags: agent, benchmark, conversation, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.28978v1

## One-Sentence Summary
Knowledge graphs have been proposed as a structured alternative to flat retrieval-augmented generation for long-term agent memory, on the assumption that representing...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Knowledge graphs have been proposed as a structured alternative to flat retrieval-augmented generation for long-term agent memory, on the assumption that representing conversations as entities and relations improves...

进一步看，论文的核心做法或实验重点可以概括为：We evaluate that assumption directly.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, long-term, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Knowledge graphs have been proposed as a structured alternative to flat retrieval-augmented generation for long-term agent memory, on the assumption that representing conversations as entities and relations improves recall. We evaluate that assumption directly. Our framework extracts each conversational turn into typed nodes and attributed edges, answers questions from a two-hop subgraph, and periodically prunes nodes that score low on a weighted combination of recency, access frequency, degree centrality, and age. On LongMemEval, the graph does not outperform a flat vector baseline at a matched candidate-generation budget of five retrieval roots: token F1 is $0.417$ against $0.468$, and a paired bootstrap over 500 questions gives $Δ= -0.050$ (95\% CI $[-0.085, -0.016]$). The gap is widest on questions that require recalling a specific prior assistant turn, where judged correctness falls from $0.911$ to $0.607$, suggesting that decomposing a turn into entities discards the surface form these questions depend on. The forgetting module is more successful. Applied once to a persistent 27{,}021-node graph, it removes 9.8\% of nodes and 9.5\% of stored bytes; token F1 is unchanged ($+0.001$, 95\% CI $[-0.015, +0.016]$) and judged correctness falls by $1.6$ points, with the 95\% interval bounding any loss at $3.8$ points ($[-0.038, +0.006]$). Because our extractor is a single small model evaluated on one benchmark, these results characterise this extraction-based pipeline rather than graph-structured memory in general. Code: https://github.com/skhanzad/Selective-Amnesia

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
