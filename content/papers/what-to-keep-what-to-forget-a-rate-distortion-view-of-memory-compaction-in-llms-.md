# What to Keep, What to Forget: A Rate--Distortion View of Memory Compaction in LLMs and Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.08032v1
- Published: 2026-07-09
- Updated: 2026-07-09
- Authors: Ashwin Gerard Colaco, Nada Lahjouji
- Tags: agent, benchmark, compression, context, long-term
- Categories: cs.LG
- URL: http://arxiv.org/abs/2607.08032v1

## One-Sentence Summary
Large language models, and the agents built on them, spend an ever-growing share of their compute and memory on remembering: caching attention keys and values, carrying long...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models, and the agents built on them, spend an ever-growing share of their compute and memory on remembering: caching attention keys and values, carrying long prompts, maintaining recurrent state, and...

进一步看，论文的核心做法或实验重点可以概括为：Because none of this memory is free, four largely separate research communities have each learned to compact it.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, context, long-term
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Large language models, and the agents built on them, spend an ever-growing share of their compute and memory on remembering: caching attention keys and values, carrying long prompts, maintaining recurrent state, and storing what happened in previous turns and sessions. Because none of this memory is free, four largely separate research communities have each learned to compact it. They evict or quantize the KV cache, prune or distill prompts, bound architectural state, and consolidate agent memory. We argue that these are instances of one problem: a rate--distortion decision about what context-derived information to retain versus discard, at what fidelity, under a resource budget, so as to preserve downstream task utility. We make this lens precise with a single compaction objective and a layer-agnostic lower bound, use it to build a seven-axis taxonomy that classifies methods from across the stack uniformly, and use it to transfer mechanisms between layers that have never been connected, from serving-stack KV management to agent long-term memory. Two patterns hold across the survey. At every layer the signal that decides what to keep is attention magnitude or recency, and it fails in the same way everywhere, by discarding, before the query is known and with no way to undo it, information the query later needs. And while compression is measured carefully on single-turn long context, the repeated compaction that agents actually perform is almost never measured, and no benchmark holds one budget axis across all the layers at once. We turn both observations into a benchmark proposal, a small reference experiment, and a set of compaction-aware design principles, and we map the open problems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
