# Recall What Is Missing: Composing Evidence from Long-Term Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.15642v1
- Published: 2026-10-11
- Updated: 2026-10-11
- Authors: Qi Feng, Jicong Fan
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.15642v1

## One-Sentence Summary
Under a limited context budget, a long-term agent must recall not merely memories that are individually relevant, but evidence that is collectively sufficient for the current...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Under a limited context budget, a long-term agent must recall not merely memories that are individually relevant, but evidence that is collectively sufficient for the current query.

进一步看，论文的核心做法或实验重点可以概括为：Conventional memory access retrieves, scores, and truncates memories, often spending multiple context slots on redundant facts while leaving complementary evidence behind.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Under a limited context budget, a long-term agent must recall not merely memories that are individually relevant, but evidence that is collectively sufficient for the current query. Conventional memory access retrieves, scores, and truncates memories, often spending multiple context slots on redundant facts while leaving complementary evidence behind. We cast the read phase of long-term memory as query-conditioned evidence composition: each memory is valued by what it adds beyond the evidence already selected. We instantiate this operation with MemPursuit, a training-free mechanism that uses the residual of a sparse convex query reconstruction as a representation-space proxy for what the current memory set is missing. By reusing the query and candidate embeddings already available from retrieval, MemPursuit progressively composes nested evidence contexts without invoking a language model or cross-encoder to score each query--memory pair. The effectiveness of our method is verified on 3 popular benchmarks in comparison to strong baselines. In fixed-budget LoCoMo experiments, MemPursuit improves end-to-end accuracy by 7.2 percentage points at Top-10 and 5.5 percentage points at Top-20, with consistent gains across multiple memory frameworks, while achieving a 32.9$\times$ speedup in median reranking latency over fully batched BGE-v2-m3. Our implementation is available at https://github.com/FengQi-HITSZ/MemPursuit.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
