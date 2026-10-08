# Stale, Misattributed, or Late: Where Personal Memory Fails Before Generation

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.10265v1
- Published: 2026-10-07
- Updated: 2026-10-07
- Authors: Haonan Deng, Park Sinchaisri
- Tags: agent, benchmark, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.10265v1

## One-Sentence Summary
Personal memory for language agents is usually judged by whether the final an- swer is correct.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Personal memory for language agents is usually judged by whether the final an- swer is correct.

进一步看，论文的核心做法或实验重点可以概括为：That score hides errors that arise before generation: the memory block may contain an obsolete value, a fact about the wrong person, or no use- ful fact before the serving deadline.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Personal memory for language agents is usually judged by whether the final an- swer is correct. That score hides errors that arise before generation: the memory block may contain an obsolete value, a fact about the wrong person, or no use- ful fact before the serving deadline. We measure these failures directly. Using Personal Fact Memory (PFM) as a reference layer, we find that temporal validity is primarily a property of memory construction in our setting. On a controlled revision benchmark, serving only the active value of each correctly keyed slot eliminates observed stale exposure; without update resolution, 70.3% of prompts expose a superseded value. Once retrievers share the same active store and par- ticipant information, participant-aware BM25 is equivalent to the reference ranker within a prespecified 0.02 margin. The harder problem is assigning revisions to the right slot. Missed merges leave stale values active, whereas false merges silently remove current values; four LLM key assigners achieve higher key re- call than a rule extractor yet produce lower clean-retrieval rates, and open-domain merge recall on LongMemEval never exceeds 0.062. Misattribution survives va- lidity filtering: an entity posterior reduces same-name exposure on controlled data but cannot distinguish identically named speakers in LoCoMo. Two frozen lan- guage models reproduce prompt errors in generated text. Retrieval latency varies across rankers, but prompt prefill dominates turn-level latency on our hardware. These results argue for evaluating agent memory before generation, separating stored-state validity, identity resolution, abstention, and serving latency.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
