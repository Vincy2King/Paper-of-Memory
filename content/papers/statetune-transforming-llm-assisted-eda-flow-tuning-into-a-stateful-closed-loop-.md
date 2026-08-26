# StateTune: Transforming LLM-Assisted EDA Flow Tuning into a Stateful, Closed-Loop Process

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.23601v1
- Published: 2026-08-19
- Updated: 2026-08-19
- Authors: Kunlong Li, Shangshang Yao, Su Zheng, Lingli Wang
- Tags: benchmark, context, retrieval
- Categories: cs.AR, cs.LG, cs.MA
- URL: http://arxiv.org/abs/2608.23601v1

## One-Sentence Summary
EDA flow parameter tuning is critical for quality-of-results~(QoR), yet the parameter space is large, tightly coupled, and full evaluations are prohibitively expensive.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：EDA flow parameter tuning is critical for quality-of-results~(QoR), yet the parameter space is large, tightly coupled, and full evaluations are prohibitively expensive.

进一步看，论文的核心做法或实验重点可以概括为：Prior LLM-assisted tuners mainly use the LLM as an external proposer with transient working context; we instead present \textbf{StateTune}, which reformulates LLM-assisted EDA tuning as a closed-loop, state-carrying...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AR, cs.LG, cs.MA

## Abstract Snapshot
EDA flow parameter tuning is critical for quality-of-results~(QoR), yet the parameter space is large, tightly coupled, and full evaluations are prohibitively expensive. Prior LLM-assisted tuners mainly use the LLM as an external proposer with transient working context; we instead present \textbf{StateTune}, which reformulates LLM-assisted EDA tuning as a closed-loop, state-carrying process. Its optimizer state is a typed, evidence-gated \emph{persistent optimization memory} that is updated by every evaluation and shared between candidate generation and budget allocation. On top of this optimizer state, an expected hypervolume improvement (EHVI)-guided, runtime-aware promotion policy ranks quick-stage candidates by expected Pareto frontier gain per unit of runtime cost. Evaluated on a Cadence industrial flow across six benchmark blocks (two technology nodes \(\times\) three designs), against five baselines including LLM+retrieval-augmented generation (RAG) and preference-based Bayesian optimization (BO) tuners, StateTune achieves the strongest final hypervolume on all six benchmark blocks, showing a stable improvement in frontier quality across the full matrix; it also matches or surpasses the strongest baselines on worst negative slack (WNS), area, and power across the same set. Ablation shows persistent memory is the largest contributor: removing it costs 58.5\% of the hypervolume. Dedicated analyses of evidence-gating sensitivity, memory poisoning, cross-design transfer, and three-seed reproducibility (CV\,\(<\)\,7\% on five of six blocks) further validate the memory design.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
