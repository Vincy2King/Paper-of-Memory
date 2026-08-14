# $\varepsilon$-MemEvo: Adaptive Cross-Task Memory Transfer for LLM Program Evolution

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.12522v1
- Published: 2026-08-12
- Updated: 2026-08-12
- Authors: Aofan Liu, Shiyuan Song, Yiyan Qi
- Tags: benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.12522v1

## One-Sentence Summary
LLM-based program evolution systems such as FunSearch and AlphaEvolve have shown strong ability to discover novel algorithms, but typically optimize each task in isolation,...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM-based program evolution systems such as FunSearch and AlphaEvolve have shown strong ability to discover novel algorithms, but typically optimize each task in isolation, discarding search experience after completion.

进一步看，论文的核心做法或实验重点可以概括为：We introduce $\varepsilon$-MemEvo, a framework for cross-task knowledge transfer in LLM program evolution. $\varepsilon$-MemEvo stores prior experience as task-agnostic tactic memories: compact natural-language...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
LLM-based program evolution systems such as FunSearch and AlphaEvolve have shown strong ability to discover novel algorithms, but typically optimize each task in isolation, discarding search experience after completion. We introduce $\varepsilon$-MemEvo, a framework for cross-task knowledge transfer in LLM program evolution. $\varepsilon$-MemEvo stores prior experience as task-agnostic tactic memories: compact natural-language summaries of successful algorithmic strategies rather than raw code, enabling transfer across tasks with different APIs and evaluators. To avoid negative transfer from semantically mismatched memories, $\varepsilon$-MemEvo uses an adaptive injection gate that decides whether retrieved memories should be injected, and at what intensity. We evaluate $\varepsilon$-MemEvo on 8 diverse optimization benchmarks spanning mathematical optimization and systems engineering, using a content-level Leave-One-Out protocol that excludes target-task memory entries. On the primary GPT-5 backbone, $\varepsilon$-MemEvo improves AUCC over AdaEvolve on all 8 tasks, with a mean relative gain of +8.7%, and improves early-stage convergence by +9.4% on average. Ablations show that naive memory injection can fail catastrophically, while adaptive gating remains safe across all five ablation tasks. The data-updated posterior is interpretable in observed states: it favors skip during improving search and shifts from skip to hint across early and late plateaus. These gains incur less than 1% computational overhead.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
