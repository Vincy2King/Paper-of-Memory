# Long-Horizon Autonomous Architecture Research with a Language-Model Agent: A Behavioural Case Study

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.01995v1
- Published: 2026-08-03
- Updated: 2026-08-03
- Authors: Aon Safdar, Mohamed Saadeldin
- Tags: agent, benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.01995v1

## One-Sentence Summary
We study what happens when a single general-purpose large language model acts as the sole researcher on a long-horizon neural architecture design problem.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We study what happens when a single general-purpose large language model acts as the sole researcher on a long-horizon neural architecture design problem.

进一步看，论文的核心做法或实验重点可以概括为：The agent receives a scientific question, an initial hypothesis and motivation, a compute budget, and research affordances (source and experiment management, experiment tracking, literature access, and persistent...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
We study what happens when a single general-purpose large language model acts as the sole researcher on a long-horizon neural architecture design problem. The agent receives a scientific question, an initial hypothesis and motivation, a compute budget, and research affordances (source and experiment management, experiment tracking, literature access, and persistent memory), then autonomously proposes, implements, evaluates, and records experiments over an extended period. The study comprises three phases, separated by human-declared transitions, that progressively expand the agent's tool surface or problem scale. Across approximately 100 sequential experiments, the agent improves a non-standard Vision Transformer from a weak baseline to a stronger, efficient model on small benchmarks and a usable but sub-SOTA model on ImageNet-1K, while producing a dense behavioural trace. We report four findings.(i)Productivity exhibits a clear phase structure: rapid early gains, a multi-dozen-hypothesis saturation wall, and recovery, with recovery triggered by expanding the action surface rather than changing the underlying model.(ii)A single early hypothesis contributes more to accuracy gain, with later improvements long-tailed.(iii)The preference for greedy, incremental hypotheses is largely workflow-induced: a commit-or-discard evaluation rule is isomorphic to greedy hill-climbing; the remainder reflects risk aversion after bold failures and anchoring on familiar literature. (iv)The agent independently rediscovers established results and, in the unfamiliar regime of pure channel attention, overturns a standard design choice. We conclude that workflow design was at least as influential as agent capability in this study and propose diversified search, budgeted moonshot hypotheses, explicit forks, and regime-aware re-validation as testable directions for future autonomous research.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
