# When Memory Lies: An Empirical Study of Spatial Memory Staleness in VLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.04574v1
- Published: 2026-08-05
- Updated: 2026-08-05
- Authors: Yushi Sun, Yanjie Zhang
- Tags: agent
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.04574v1

## One-Sentence Summary
Memory-augmented VLM agents act on persistent spatial knowledge, yet that knowledge silently goes stale as the environment changes.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-augmented VLM agents act on persistent spatial knowledge, yet that knowledge silently goes stale as the environment changes.

进一步看，论文的核心做法或实验重点可以概括为：We ask what happens when an agent must reconcile a confident memory claim with a contradicting observation, and whether current models can catch the conflict before it becomes a safety-relevant mistake.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CL

## Abstract Snapshot
Memory-augmented VLM agents act on persistent spatial knowledge, yet that knowledge silently goes stale as the environment changes. We ask what happens when an agent must reconcile a confident memory claim with a contradicting observation, and whether current models can catch the conflict before it becomes a safety-relevant mistake. Using a dynamic FrozenLake testbed, we pair a staleness-detection task with a downstream navigation task across three closed-source models and three open-weight VLMs under both text and image inputs (1,800 detection runs, and 12,000 text-mode navigation episodes over four LLM navigators at a shared 50-seed scale). Three findings emerge. First, text solvability does not imply visual grounding: models that flag stale entries reliably from text nonetheless span vision F1 from 0.887 down to 0.067 on the identical grids, and the weakest keeps making fluent, confident decisions that ignore the image. Second, consuming stale memory without an audit is a safety liability: in our primary GPT-4o setting, an agent that trusts raw memory dies more than twice as often as the same agent given no memory at all. Third, auditing helps but does not close the gap: a transparent read-time filter removes much of the safety cost in text mode, yet even oracle stale labels bring no further significant gain on the current grid size, and when visual auditing is unreliable, filtering yields no consistent benefit. Together these results frame spatial-memory staleness as a safety failure mode and isolate reliable visual grounding and action selection under memory--observation conflict as the central open challenges for memory-augmented agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
