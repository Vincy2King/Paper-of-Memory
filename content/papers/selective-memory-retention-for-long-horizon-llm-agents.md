# Selective Memory Retention for Long-Horizon LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.29178v1
- Published: 2026-06-28
- Updated: 2026-06-28
- Authors: Pranath Reddy
- Tags: agent, benchmark
- Categories: cs.AI, cs.CL, cs.LG
- URL: http://arxiv.org/abs/2606.29178v1

## One-Sentence Summary
When does retention matter for memory-augmented LLM agents?

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：When does retention matter for memory-augmented LLM agents?

进一步看，论文的核心做法或实验重点可以概括为：We study this with TraceRetain, a lightweight framework for bounded external memory in frozen LLM agents that scores entries by interpretable features (success, age, access frequency, redundancy, specificity,...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI, cs.CL, cs.LG

## Abstract Snapshot
When does retention matter for memory-augmented LLM agents? We study this with TraceRetain, a lightweight framework for bounded external memory in frozen LLM agents that scores entries by interpretable features (success, age, access frequency, redundancy, specificity, similarity, downstream utility) and evicts the lowest-scoring ones at capacity. On clean ALFWorld with gpt-5-mini, external memory robustly improves over no memory across two seeds, but differences among bounded retention policies fall within Wilson 95% CIs: clean ALFWorld at T=100 to T=200 does not naturally exhibit the memory pollution retention is designed to address. Under a controlled noisy-write stress (75% synthetic distractors), unbounded memory and FIFO-K50 degrade on Precision@5 (20.2% to 12.4% and 15.8% to 3.8%) while TraceRetain-CEM is essentially unchanged (16.9% to 16.6%) and preserves 97/100 task success. The mechanism: unbounded memory has the highest mean similarity (0.87) but lowest precision, indicating failed distractors close to the query in embedding space. Held-out in-distribution evaluation shows memory-augmented policies solving 47 to 49 of 50 tasks vs. 39/50 for no memory. Bounded retention buys memory and step efficiency on saturated clean benchmarks at no task-success cost, and only differentiates from cache heuristics when streams contain noise.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
