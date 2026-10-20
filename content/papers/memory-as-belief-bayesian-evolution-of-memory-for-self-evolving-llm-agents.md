# Memory as Belief: Bayesian Evolution of Memory for Self-Evolving LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.25119v1
- Published: 2026-10-18
- Updated: 2026-10-18
- Authors: Yiming Xu, Qian Yang, Zihan Chen, Yuefei Wu, Wenhan Zeng, Bin Shi, Bo Dong
- Tags: agent, benchmark, context, retrieval
- Categories: cs.LG
- URL: http://arxiv.org/abs/2610.25119v1

## One-Sentence Summary
Large language model (LLM) agents increasingly rely on external memory to accumulate past experiences for continual adaptation.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents increasingly rely on external memory to accumulate past experiences for continual adaptation.

进一步看，论文的核心做法或实验重点可以概括为：However, effectively reusing memory requires accurately assessing its value, as retrieved experiences may become unreliable when transferred across task contexts.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Large language model (LLM) agents increasingly rely on external memory to accumulate past experiences for continual adaptation. However, effectively reusing memory requires accurately assessing its value, as retrieved experiences may become unreliable when transferred across task contexts. Despite its importance, memory valuation remains largely underexplored, with existing methods relying on historical retrieval success rates that overlook the context dependency of memory usefulness and the varying reliability of estimates under different amounts of evidence. Inspired by the Bayesian brain hypothesis, we propose BEAM (Bayesian-style Evolutionary Agentic Memory), a framework that reformulates memory value evaluation as a parameterized cognitive inference process, where memory value is represented as a context-conditioned dynamic belief rather than a passive historical statistic. Specifically, BEAM infers memory value beliefs from current task contexts and continuously calibrates them using execution feedback as empirical evidence, transforming memory from passive storage into an adaptive cognitive mechanism for continual self-evolution. Extensive experiments across reasoning and code generation benchmarks demonstrate that BEAM consistently improves memory utilization and enables continual self-evolution of LLM agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
