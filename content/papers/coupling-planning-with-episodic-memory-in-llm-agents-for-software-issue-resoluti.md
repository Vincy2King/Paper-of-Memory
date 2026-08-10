# Coupling Planning with Episodic Memory in LLM Agents for Software Issue Resolution

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.06811v1
- Published: 2026-08-07
- Updated: 2026-08-07
- Authors: Jiahao Zhang, Yifan Zhang, Yu Huang
- Tags: agent, context, episodic, retrieval
- Categories: cs.SE, cs.AI
- URL: http://arxiv.org/abs/2608.06811v1

## One-Sentence Summary
Resolving a real software issue with a large language model (LLM) agent is a long repair episode, often tens to hundreds of steps spanning exploration, hypothesis,...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Resolving a real software issue with a large language model (LLM) agent is a long repair episode, often tens to hundreds of steps spanning exploration, hypothesis, implementation, and verification.

进一步看，论文的核心做法或实验重点可以概括为：Success depends on both the base model's local reasoning and the agent's ability to maintain an evolving plan and remember observations across phases.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, episodic, retrieval
- 检索关键词命中：episodic memory, memory retrieval
- 来源分类信息：cs.SE, cs.AI

## Abstract Snapshot
Resolving a real software issue with a large language model (LLM) agent is a long repair episode, often tens to hundreds of steps spanning exploration, hypothesis, implementation, and verification. Success depends on both the base model's local reasoning and the agent's ability to maintain an evolving plan and remember observations across phases. Existing repository-level agents typically strengthen planning or memory in isolation, leaving long trajectories vulnerable to stale evidence, repeated failed edits, and verification inferred from the agent's own claims instead of execution evidence. We present PMCoder, an issue-resolution agent that couples a hierarchical phase planner with episodic memory. The coupling is bidirectional: the current plan phase conditions memory retrieval, while memory-derived trajectory statistics inform stuck detection and replanning. When available, issue-reproduction verdicts ground verification progress in execution evidence rather than self-reported completion. On SWE-bench Verified, PMCoder resolves an average of $25$ more cases ($+5.0$pp) than a harness-matched baseline, with gains persisting even where the reproduction gate never fires. Further Verified-500 evaluations show the same positive direction across Claude Haiku 4.5, DeepSeek-V4-Flash, and an OpenHands port, with at least $14$ additional resolved cases ($+2.8$pp). Separately, evaluation on TerminalWorld's official sample suggests that the plan-memory substrate transfers beyond issue reports. Ablation and trajectory analyses show where the gains come from: coupling planning and memory outperforms either component alone and reduces repeated failed actions, empty-patch exits, and context-window exhaustion.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
