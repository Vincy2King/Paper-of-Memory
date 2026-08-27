# Learning What to Share and What to Personalize: Hierarchical Strategy Co-Evolution for Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.25329v1
- Published: 2026-08-26
- Updated: 2026-08-26
- Authors: Yupeng Han, Shuochen Liu, Kai Zhang, Ze Liu, Zhihong Pan, Xianquan Wang
- Tags: agent, conversation
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2608.25329v1

## One-Sentence Summary
Memory-augmented agents maintain compact user profiles throughout extended conversations, enabling personalized and consistent responses without the need to process the entire...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-augmented agents maintain compact user profiles throughout extended conversations, enabling personalized and consistent responses without the need to process the entire dialogue history.

进一步看，论文的核心做法或实验重点可以概括为：The quality of these user profiles relies on the underlying memory management strategy: at each step, the agent must determine what to retain, compress, or discard.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation
- 检索关键词命中：agent memory, memory augmented, memory-augmented
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Memory-augmented agents maintain compact user profiles throughout extended conversations, enabling personalized and consistent responses without the need to process the entire dialogue history. The quality of these user profiles relies on the underlying memory management strategy: at each step, the agent must determine what to retain, compress, or discard. However, existing methods typically employ a static, one-size-fits-all strategy established before training. In practice, the optimal memory decision is inherently user-specific and dynamically evolves alongside policy optimization. To address this, we propose \textbf{HiPS} (\textbf{Hi}erarchical \textbf{P}ersonalized \textbf{S}trategy), a framework that decouples memory management into a globally shared foundation and a user-specific adaptive tier. Specifically, HiPS employs \textbf{Universal Strategy} to extract shared principles from cross-persona trajectories, alongside \textbf{Persona Delta Distillation} to generate tailored rules for users whose behaviors diverge from general patterns. \textbf{Cross-Level Rule Flow} dynamically calibrates their boundary by promoting broadly validated personal rules and demoting contradicted global ones. The architecture establishes a co-evolution loop where a mechanism guarantees that all strategy refinements are anchored to task outcomes. Extensive experiments demonstrate consistent improvements over memory-augmented baselines.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
