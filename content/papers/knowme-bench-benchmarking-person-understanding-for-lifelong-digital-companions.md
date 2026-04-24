# KnowMe-Bench: Benchmarking Person Understanding for Lifelong Digital Companions

- Source: arXiv
- Venue: N/A
- Paper ID: 2601.04745v2
- Published: 2026-01-08
- Updated: 2026-04-19
- Authors: Tingyu Wu, Zhisheng Chen, Ziyan Weng, Shuhe Wang, Chenglong Li, Shuo Zhang, Sen Hu, Silin Wu, Qizhen Lan, Huacan Wang, Ronghao Chen
- Tags: benchmark, context, retrieval
- Categories: cs.AI, cs.IR
- URL: http://arxiv.org/abs/2601.04745v2

## One-Sentence Summary
Existing long-horizon memory benchmarks mostly use multi-turn dialogues or synthetic user histories, which makes retrieval performance an imperfect proxy for person understanding.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Existing long-horizon memory benchmarks mostly use multi-turn dialogues or synthetic user histories, which makes retrieval performance an imperfect proxy for person understanding.

进一步看，论文的核心做法或实验重点可以概括为：We present \BenchName, a publicly releasable benchmark built from long-form autobiographical narratives, where actions, context, and inner thoughts provide dense evidence for inferring stable motivations and decision...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, retrieval
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：cs.AI, cs.IR

## Abstract Snapshot
Existing long-horizon memory benchmarks mostly use multi-turn dialogues or synthetic user histories, which makes retrieval performance an imperfect proxy for person understanding. We present \BenchName, a publicly releasable benchmark built from long-form autobiographical narratives, where actions, context, and inner thoughts provide dense evidence for inferring stable motivations and decision principles. \BenchName~reconstructs each narrative into a flashback-aware, time-anchored stream and evaluates models with evidence-linked questions spanning factual recall, subjective state attribution, and principle-level reasoning. Across diverse narrative sources, retrieval-augmented systems mainly improve factual accuracy, while errors persist on temporally grounded explanations and higher-level inferences, highlighting the need for memory mechanisms beyond retrieval. Our data is in \href{KnowMeBench}{https://github.com/QuantaAlpha/KnowMeBench}.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
