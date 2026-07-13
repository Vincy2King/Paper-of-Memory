# LongMedBench: Benchmarking Medical Agents for Long-Horizon Clinical Decision-Making

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.09322v1
- Published: 2026-07-10
- Updated: 2026-07-10
- Authors: Yanzhen Chen, Zihan Xu, Xiaocheng Zhang, Zhiting Fan, Weiqi Zhai, Hongxia Xu, Zuozhu Liu
- Tags: agent, benchmark, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.09322v1

## One-Sentence Summary
In this work, we introduce LongMedBench, a real-world EHR-based benchmark for long-horizon clinical decision-making.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：In this work, we introduce LongMedBench, a real-world EHR-based benchmark for long-horizon clinical decision-making.

进一步看，论文的核心做法或实验重点可以概括为：Prior evaluations of LLM-based medical agents have largely emphasized short-context knowledge QA and tool use.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：agent memory, context memory
- 来源分类信息：cs.AI

## Abstract Snapshot
In this work, we introduce LongMedBench, a real-world EHR-based benchmark for long-horizon clinical decision-making. Prior evaluations of LLM-based medical agents have largely emphasized short-context knowledge QA and tool use. However, real-world medical care is inherently longitudinal, and clinicians must aggregate evidence across repeated visits, tests, and evolving treatments. Therefore, long-horizon interaction is essential for realistic assessment. LongMedBench is constructed via a reproducible pipeline that integrates MIMIC-IV admission records and clinical notes into time-series event streams and long-context memory datasets, enabling long-horizon, multi-session interactions between agents and a clinical environment. It comprises 335 patients, with 19.72 inpatient visits per patient on average and 44.91 medical events per visit. Guided by the long-horizon decision process, we propose an evaluation taxonomy with three suites: fact-based QA, temporal reasoning, and long-horizon decision-making. This taxonomy measures how agents understand and leverage historical patient information over extended horizons. Our experiments show that while recent LLMs can make good use of explicit timestamps, they have challenges in implicit time inference; The RAG and agent memory system can improve the performance of information retrieval tasks, but the performance of decision-making tasks is highly dependent on the model's immediate context.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
