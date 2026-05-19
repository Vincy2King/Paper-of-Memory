# CommitDistill: A Lightweight Knowledge-Centric Memory Layer for Software Repositories

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.18284v1
- Published: 2026-05-18
- Updated: 2026-05-18
- Authors: Divya Chukkapalli, Thejesh Avula, Aditya Aggarwal, Harsimran Singh, Amith Tallanki
- Tags: agent, benchmark, retrieval
- Categories: cs.SE, cs.AI
- URL: http://arxiv.org/abs/2605.18284v1

## One-Sentence Summary
Software repositories accumulate large amounts of unstructured knowledge in commit messages, pull-request discussions, and issue threads, but developers and AI coding assistants...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Software repositories accumulate large amounts of unstructured knowledge in commit messages, pull-request discussions, and issue threads, but developers and AI coding assistants rarely reuse this history effectively.

进一步看，论文的核心做法或实验重点可以概括为：Recent work on typed-memory architectures for LLM agents (MemGPT, generative agents, and the PlugMem module of Yang et al.) argues that agent memory should be distilled, typed knowledge rather than raw interaction text.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.SE, cs.AI

## Abstract Snapshot
Software repositories accumulate large amounts of unstructured knowledge in commit messages, pull-request discussions, and issue threads, but developers and AI coding assistants rarely reuse this history effectively. Recent work on typed-memory architectures for LLM agents (MemGPT, generative agents, and the PlugMem module of Yang et al.) argues that agent memory should be distilled, typed knowledge rather than raw interaction text. We adapt that stance to a software repository's own git history under a constrained regime: deterministic, dependency-free, local-only, no embeddings. We present CommitDistill, an open-source Python prototype that mines a local git history into typed knowledge units (Facts, Skills, Patterns) using deterministic regex and surfaces them through a TF-IDF retriever with a calibrated silence threshold (theta = 2.5) that abstains on out-of-distribution queries. The artefact is a trust-instrumented memory substrate: deterministic, no external service, inspectable plain-JSON store, tunable abstention. A case study on five public repositories spanning Python, JavaScript, C, and Java (25,000 commits, 1,167 extracted units) reports useful-precision 0.525 at Cohen's kappa = 0.633 on 40 dual-annotated Python units. The decisive finding is budget-constrained retrieval: at a 256-character per-query budget, CommitDistill reaches 0.750 hit-rate on a 12-query benchmark against BM25's 0.333 and git log --grep's 0.083. On a four-arm paired LLM-as-judge evaluation (n=200 time-travel bug-fixes, two judges) covering control, CommitDistill, a body-budget-matched CD-Hybrid, and BM25, no condition produces a statistically detectable lift over control on the headline mean and CD-Hybrid is indistinguishable from BM25 head-to-head. Extraction over 10,000 commits completes in under 4 seconds on a laptop. Source, annotations, baselines, and a reproducibility script accompany this paper.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
