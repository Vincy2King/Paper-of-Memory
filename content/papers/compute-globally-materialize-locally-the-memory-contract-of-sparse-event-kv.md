# Compute Globally, Materialize Locally: The Memory Contract of Sparse Event-KV

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.23693v1
- Published: 2026-07-26
- Updated: 2026-07-26
- Authors: Zefeng Cai, Zerui Cai
- Tags: agent, episodic, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.23693v1

## One-Sentence Summary
Long-horizon agents increasingly reuse their KV cache as memory: a serving system keeps a subset of cached entries and drops the rest.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, episodic, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon agents increasingly reuse their KV cache as memory: a serving system keeps a subset of cached entries and drops the rest.

进一步看，论文的核心做法或实验重点可以概括为：Eviction and episodic-memory schemes therefore rest on a premise rarely tested directly, that a retained event is still informative once the observations that produced it are gone.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, episodic, long-term
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-horizon agents increasingly reuse their KV cache as memory: a serving system keeps a subset of cached entries and drops the rest. Eviction and episodic-memory schemes therefore rest on a premise rarely tested directly, that a retained event is still informative once the observations that produced it are gone. We test it by omitting one earlier observation from what is served, across otherwise identical agent histories. Among items sensitive to that observation, the answer overwhelmingly follows the omitted value, though no served span says which value is correct. We call this semantic materialization: a downstream event's cached rows act as an independently servable view of computation whose inputs are gone. It can also be written on purpose. A deliberately phrased, answer-free event raises donor-aligned recovery from 6% to 51% on Qwen3-8B without ever naming the value, whereas passively harvesting natural mentions from long-term dialog yields no detected advantage. What such a row carries is specific and bounded. Compact state survives, larger payloads decay toward chance, and whether a construction writes at all turns on phrasing rather than on meaning alone, so two phrasings the model comprehends equally well can diverge sharply. The result is a memory contract for sparse event-KV serving: what to write, where it lands, and what survives once the source is gone. For anyone who evicts the corollary is that dropping a source event and observing no accuracy loss does not show the source was unnecessary.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
