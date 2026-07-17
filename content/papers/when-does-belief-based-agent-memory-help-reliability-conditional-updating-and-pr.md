# When Does Belief-Based Agent Memory Help? Reliability-Conditional Updating and Provenance-Capped Poisoning Defense

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.22030v2
- Published: 2026-06-20
- Updated: 2026-07-16
- Authors: Pranav Singh
- Tags: agent, benchmark, conversation, long-term, retrieval
- Categories: cs.AI, cs.CL, cs.IR, cs.LG
- URL: http://arxiv.org/abs/2606.22030v2

## One-Sentence Summary
We investigate when belief-based memory actually improves large language model (LLM) agents.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We investigate when belief-based memory actually improves large language model (LLM) agents.

进一步看，论文的核心做法或实验重点可以概括为：Our vehicle is Nous, a long-term memory architecture that represents each entity-attribute pair as a categorical probability distribution updated through closed-form Bayesian inference, with information-theoretic...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, long-term, retrieval
- 检索关键词命中：conversational memory, long-term memory, memory benchmark, memory benchmarks, memory retrieval
- 来源分类信息：cs.AI, cs.CL, cs.IR, cs.LG

## Abstract Snapshot
We investigate when belief-based memory actually improves large language model (LLM) agents. Our vehicle is Nous, a long-term memory architecture that represents each entity-attribute pair as a categorical probability distribution updated through closed-form Bayesian inference, with information-theoretic surprise driving belief revision and entropy-based forgetting. A controlled ablation on the LoCoMo benchmark shows that Bayesian belief updating alone provides little benefit over naive last-write-wins because existing conversational memory benchmarks rarely contain contradictory or differently reliable evidence. We then introduce reliability-conditioned updating, estimating per-observation reliability from epistemic language, and show on a controlled contradiction benchmark that belief updating substantially outperforms last-write-wins and raw-memory retrieval when observations differ in trustworthiness. Because content-derived reliability is itself vulnerable to manipulation, we further propose provenance-capped belief updating, where trust is bounded by source provenance rather than textual confidence. Under controlled memory-poisoning experiments, this approach resists volumetric poisoning attacks while revealing the utility costs and implementation requirements of provenance-aware memory. Finally, we quantify a 27.5-point discrepancy between strict token-F1 and LLM-as-judge evaluation on identical outputs, highlighting important reproducibility concerns for long-term memory benchmarks. Our results suggest that probabilistic belief-based memory is most beneficial in environments requiring reasoning over conflicting and differently trustworthy evidence, rather than conventional conversational recall alone.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
