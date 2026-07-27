# Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.21962v1
- Published: 2026-07-24
- Updated: 2026-07-24
- Authors: Quentin Spencer
- Tags: agent, benchmark, conversation
- Categories: cs.CL
- URL: http://arxiv.org/abs/2607.21962v1

## One-Sentence Summary
Benchmarks for LLM-agent memory typically generate conversations first and extract answer keys afterwards -- with documented label-error and contamination problems -- and they...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Benchmarks for LLM-agent memory typically generate conversations first and extract answer keys afterwards -- with documented label-error and contamination problems -- and they overwhelmingly measure short interaction...

进一步看，论文的核心做法或实验重点可以概括为：We invert the pipeline: a seeded life-script sampler emits facts with validity intervals, volatility classes, and source channels before any text exists; an LLM renderer writes chat and email from per-event fact...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Benchmarks for LLM-agent memory typically generate conversations first and extract answer keys afterwards -- with documented label-error and contamination problems -- and they overwhelmingly measure short interaction histories. We invert the pipeline: a seeded life-script sampler emits facts with validity intervals, volatility classes, and source channels before any text exists; an LLM renderer writes chat and email from per-event fact manifests; a fidelity verifier confirms every planted fact; and questions are instantiated mechanically from the script, so gold answers are script-valid by construction and separately validated for answerability. The synthetic, fictionalized corpus (~380 questions, 15 types) embeds features absent from the benchmarks we survey: per-fact validity intervals, sent/received trust distinctions, injection probes in a benign harness, and as-of-date question sets. Benchmarking five memory architectures against a no-memory control (fixed answerer, versioned LLM judge, three replicates, two horizons), we find backend rankings invert with history length: the budgeted curated-map memory that leads at three weeks loses recall of evicted content by nine weeks (96% to 72%) while a provenance-typed graph rises to 90%; the inversion is positive for all six users under complete cross-family re-judging (exact p=0.031). A full-rendered-history baseline ties or exceeds the best memory system at the short horizon but shows no judge-independent advantage at nine weeks, at about twice the read cost. Write-stage quality strongly correlates with downstream quality (weakly-written facts fail 24% vs 2%), and injection resistance tracked whether provenance boundaries survive representation. A layered architecture performs best among the memory systems in both regimes (96.8% short-horizon) and is released as Veracium, an open-source library, with the corpus generator and harness.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
