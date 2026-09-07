# Compact-Memory LLM Agents via Online Max-Member Clustering and Atom-Aware Packing

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.04915v1
- Published: 2026-09-04
- Updated: 2026-09-04
- Authors: Jiahe Geng, Jinpeng Wang, Kun Yuan
- Tags: agent, benchmark, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.04915v1

## One-Sentence Summary
Many long-horizon LLM deployments face tight prompt budgets: latency, cost, and context limits make full-context prompting impractical as interaction length grows.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Many long-horizon LLM deployments face tight prompt budgets: latency, cost, and context limits make full-context prompting impractical as interaction length grows.

进一步看，论文的核心做法或实验重点可以概括为：The key question is then not raw recall alone, but which memory design gives the best quality--token trade-off in the compact-memory regime.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：agent memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.AI

## Abstract Snapshot
Many long-horizon LLM deployments face tight prompt budgets: latency, cost, and context limits make full-context prompting impractical as interaction length grows. The key question is then not raw recall alone, but which memory design gives the best quality--token trade-off in the compact-memory regime. We present \textbf{RSM-full}, an online clustered-memory pipeline designed for a strong quality--token Pareto point. RSM-full combines two design choices: a cosine-gated \emph{max-member merge} write rule and an atom-aware grouped context packer. On AMA-Bench, our primary compact-memory benchmark, it reaches $83%$ of Full-Context quality at $32%$ of the token cost at a $4$k budget; under four-seed averaging it beats the closest streaming-clustered baseline (Online K-Means) by $+3.5$--$6.0$,pp ($p{<}.001$) across the whole ${\sim}2.6$k--${\sim}5$k regime. Three-seed ablations show most of this gain comes from the merge rule ($+5.7$,pp over Online K-Means and matched-$τ$ DP-means) and the grouped packer ($+5.0$,pp over flat concatenation). The pattern reproduces on RealMem, an independent long-horizon persona-memory benchmark: RSM-full improves on Budget-RAG ($+0.69$,pp, $p{=}.006$), is on par with BM25-RAG (paired $Δ{=}{+}0.27$,pp, $p{=}.47$; we do \emph{not} claim BM25 equivalence in the equivalence-test sense), and significantly outperforms Streaming-Proto ($+2.97$,pp) and the closest reproduced 2025 agentic-memory baseline A-MEM ($+1.65$,pp, $p{<}.001$). Across benchmarks the message is consistent: under tight budgets, compact-memory performance is driven mainly by how streaming memories are merged and how retrieved content is assembled. Overall, RSM-full is most useful when answeroughly $2k$--$5k$ prompt tokens, where itdefines a strong compact-memory Pareto point; higher-token baselines remain stronger outside this regime.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
