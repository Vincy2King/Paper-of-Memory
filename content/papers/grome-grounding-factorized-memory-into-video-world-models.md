# GROME: GROunding Factorized MEmory into Video World Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.39812v1
- Published: 2026-10-29
- Updated: 2026-10-29
- Authors: Fang Yu, Xiaoxue Wu, Haiyu Zhang, Yangfu Li, Botong Zhao, Yu Qiao, Tianfan Xue, Yue Lu, Xinyuan Chen
- Tags: context, retrieval
- Categories: cs.CV, cs.LG
- URL: http://arxiv.org/abs/2610.39812v1

## One-Sentence Summary
Long-horizon consistency is essential for video world models, yet it becomes difficult to maintain once observed content falls outside the context window.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon consistency is essential for video world models, yet it becomes difficult to maintain once observed content falls outside the context window.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory mechanisms either retrieve history as implicit context, which remains constrained by context capacity and entangles static and dynamic information or consolidate history into explicit global...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.CV, cs.LG

## Abstract Snapshot
Long-horizon consistency is essential for video world models, yet it becomes difficult to maintain once observed content falls outside the context window. Existing memory mechanisms either retrieve history as implicit context, which remains constrained by context capacity and entangles static and dynamic information or consolidate history into explicit global representations, which struggle to model evolving dynamics and accumulate geometric errors. To overcome these limitations, we introduce \textbf{GROME}, a novel factorized memory framework that augments video world models for long-horizon coherence across both static scenes and dynamic entities. GROME operates via three synergistic components: 1)~\emph{Static-Dynamic Factorization} decouples historical evidence into static and dynamic components, preserving static scene geometry and dynamic entity states separately; 2)~\emph{Local Memory Retrieval} selects spatially aligned static history to eliminate geometric drift alongside the latest dynamic entity states to ensure temporal continuity; 3)~\emph{Training-Free Memory Injection} seamlessly grounds the factorized memory into video world models via their native conditioning pathways. Experiments on long-horizon revisit scenarios demonstrate that GROME substantially enhances scene persistence and dynamic entity fidelity over existing methods, all while preserving the visual quality and controllability of the frozen backbone without additional training. Beyond self-rollouts, GROME readily accommodates external observations as plug-and-play memory, unlocking flexible and controllable video continuation and scene exploration.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
