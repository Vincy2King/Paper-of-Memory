# When Does Experience Memory Help Closed-Loop LLM Driving Agents? A Controlled Evaluation with Resampled Warmup Pools, Token-Matched Fillers, and Audited Baselines

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.27714v1
- Published: 2026-10-20
- Updated: 2026-10-20
- Authors: Yingxin Jia, Xuanyi Li
- Tags: agent, episodic, retrieval
- Categories: cs.AI, cs.CL, cs.CV, cs.LG, cs.RO
- URL: http://arxiv.org/abs/2610.27714v1

## One-Sentence Summary
When does experience memory help a closed-loop LLM driving agent?

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：When does experience memory help a closed-loop LLM driving agent?

进一步看，论文的核心做法或实验重点可以概括为：Published gains cannot say, because the two factors we find to matter most, which warmup experiences the pool contains and what any injected tokens do to the prompt, are controlled in none of them.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, episodic, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.AI, cs.CL, cs.CV, cs.LG

## Abstract Snapshot
When does experience memory help a closed-loop LLM driving agent? Published gains cannot say, because the two factors we find to matter most, which warmup experiences the pool contains and what any injected tokens do to the prompt, are controlled in none of them. We answer with a controlled evaluation on one audited HighwayEnv testbed (1Hz, gpt-4o-mini for the decisive contrasts). We treat the warmup pool as a resampled random factor (ten disjoint pools) and add token-matched irrelevant-filler controls, oracle-certified diagnostics, caution-pricing metrics, and quantified audits of the baseline ports. The probe suite spans flat-text retrieval (a DiLu port), a single-frame grid port (RESPOND-inspired), our episodic temporal-graph memory, a retrieval-free consolidated rulebook, and a flat K-step observation-history baseline. Four findings follow, each a property of this testbed. (1) Headline memory gains belong to the warmup draw. The reported pool is the best of ten for both retrieval memories, which beat No-Memory in only one pool of ten (sign test p=0.011), and even the rulebook's apparent pool-immunity collapsed on five fresh draws. (2) No retrieval design tested exceeds token-matched filler. The collision-only merge ceiling is reached by a single 15-token caution instruction, and metrics that price caution erase the rulebook's lead. (3) Representational sophistication is nowhere robustly operative. (4) Baseline port quality silently inverts conclusions. On this testbed, a single-pool comparison without filler controls would have reported memory gains that these controls reverse. We release the testbed, audited ports, seeds, and caches.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
