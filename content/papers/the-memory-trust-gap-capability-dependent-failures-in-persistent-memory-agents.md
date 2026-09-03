# The Memory Trust Gap: Capability-Dependent Failures in Persistent-Memory Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.01852v1
- Published: 2026-09-01
- Updated: 2026-09-01
- Authors: Jundong Hu, Shekar Ramachandran
- Tags: agent, benchmark
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2609.01852v1

## One-Sentence Summary
Persistent memory supports personalized agents, but a stale stored fact can override current authoritative evidence without warning.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent memory supports personalized agents, but a stale stored fact can override current authoritative evidence without warning.

进一步看，论文的核心做法或实验重点可以概括为：We study when this harm begins as model capability changes.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Persistent memory supports personalized agents, but a stale stored fact can override current authoritative evidence without warning. We study when this harm begins as model capability changes. We evaluate a frozen, closed-set, action-scored benchmark with 2 suites that represent 2 different meanings of "no memory" (a Benefit suite, unsolvable without the stored fact, and a Safety suite, in which an authoritative tool always holds the correct value), on a same-family model-size series (Qwen3 0.6/1.7/4/8B). The Memory Trust Gap reflects over-trust rather than confusion. In the Benefit suite, models answer with the stale value 0.92-1.00 of the time at every scale. In the Safety suite, harm below the no-memory baseline under the trap conditions ($Δ_{\mathrm{mem}}$) is capability-gated, with the larger models collapsing most once a stale note is made to look current. In a $2\times2\times2\times2$ factorial, which feature triggers over-trust depends on both the feature and model scale. Removing a label amplifies over-trust at every size, and a recency feature (stale dated newer) fools the larger models harder. Source authority is weak and scale-flat, and position changes from positive to negative across the Qwen3 model-size series. We confirm these scale interactions with direct cross-size contrast tests rather than overlapping per-model intervals. Mitigation is likewise capability-dependent: exposing metadata improves accuracy for the capable models, but only pre-resolving the conflict restores accuracy for the 2 smaller checkpoints. The same pattern appears on the capable models in an independent Llama-Instruct model-size series and on 2 external datasets (RGB, MisBench). A framing control finds no consistent advantage for the memory label: at the 3 smaller scales, models trust a stale document more than a stale memory; at 8B, the difference is not significant.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
