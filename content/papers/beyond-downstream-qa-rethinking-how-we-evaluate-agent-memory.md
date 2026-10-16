# Beyond Downstream QA: Rethinking How We Evaluate Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.22209v1
- Published: 2026-10-15
- Updated: 2026-10-15
- Authors: Sebastian-Antonio Toma, Jean de Kernier, Mike Ply, Oliviu Matei
- Tags: agent, benchmark, conversation, retrieval
- Categories: cs.CL, cs.AI, cs.LG
- URL: http://arxiv.org/abs/2610.22209v1

## One-Sentence Summary
Agent memory benchmarks evaluate whether an agent's responses reflect correct knowledge, measuring downstream question-answering accuracy as a proxy for memory quality.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agent memory benchmarks evaluate whether an agent's responses reflect correct knowledge, measuring downstream question-answering accuracy as a proxy for memory quality.

进一步看，论文的核心做法或实验重点可以概括为：We show this evaluation paradigm is incomplete: it conflates memory correctness with retrieval and generation quality, producing both false positives where correct responses mask broken memory and false negatives...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, retrieval
- 检索关键词命中：agent memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.CL, cs.AI, cs.LG

## Abstract Snapshot
Agent memory benchmarks evaluate whether an agent's responses reflect correct knowledge, measuring downstream question-answering accuracy as a proxy for memory quality. We show this evaluation paradigm is incomplete: it conflates memory correctness with retrieval and generation quality, producing both false positives where correct responses mask broken memory and false negatives where incorrect responses blame correct memory for retrieval failures. We introduce FEB-30, a benchmark of 30 fact-evolution trajectories spanning 6 diagnostic categories and 3 difficulty levels, constructed via paradigm inversion: documents are generated from known fact trajectories, yielding deterministic ground truth without human annotation. Each trajectory defines how a fact should evolve across multi-author artifacts (documents, emails, conversations), enabling direct inspection of the memory store after each ingestion step. Applying FEB-30 to a representative memory system, we demonstrate that intrinsic and extrinsic evaluation diverge by an average of 16 percentage points, with 44% of trajectories exceeding meaningful divergence thresholds. Diagnostic decomposition reveals that the system correctly classifies memory operations (create, update, reinforce, supersede) only 20% of the time, a failure entirely invisible to extrinsic evaluation, and that failure modes differ systematically by category and difficulty. We release the benchmark, document generation pipeline, and scoring framework to support reproducible evaluation of agent memory systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
